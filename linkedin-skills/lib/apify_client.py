"""Cliente Apify enxuto para o projeto LinkedIn Skills.

Substitui a antiga dependência privada do HarvestAPI. Cada método encapsula
um actor público do Apify e usa o endpoint run-sync-get-dataset-items, de
modo que o chamador recebe os resultados em uma única requisição HTTP (sem
necessidade de polling).

Autenticação: variável de ambiente APIFY_TOKEN (ou argumento do construtor),
enviada como cabeçalho `Authorization: Bearer` (nunca como parâmetro de
query `?token=`, o que vazaria a credencial para logs de proxy e rastros de
erro).

Actors usados (todos sem cookies, públicos, "$1-$5 por 1.000 resultados"):
  - apimaestro/linkedin-post-detail
      Busca o corpo do post, autor, estatísticas e o `share_urn` de reshare
      pela URL do post (chave de entrada `post_urls`, sem cookies). A saída
      é aninhada e normalizada para o contrato plano por `_normalize_post`.
      Use para extração de gancho, contexto pré-comentário e resolução da
      URN pai do reshare. (Substituiu supreme_coder/linkedin-post, que
      passou a retornar resultados vazios.)
  - apimaestro/linkedin-post-comments-replies-engagements-scraper-no-cookies
      Busca comentários + respostas de um post (por ID ou URL do post). Use
      para a estrutura de thread do reply-handler e para evitar capturas de
      comentário duplicadas.
  - apimaestro/linkedin-profile-comments
      Busca os comentários recentes de um usuário pelo username. Use para o
      rastreamento de respostas do autor no engagement-monitor.
  - scraping_solutions/linkedin-posts-engagers-likers-and-commenters-no-cookies
      Busca as pessoas que curtiram ou comentaram um post. Use para
      analytics de engajamento (agrupar por senioridade, empresa, cargo,
      fit com o ICP).

Cache: LRU em processo (256 entradas, TTL de 6h). Passe `force_refresh=True`
em qualquer método para ignorá-lo. Novas tentativas em 408/429/5xx
transitórios (3 tentativas com backoff exponencial + jitter).
"""
from __future__ import annotations
import json
import os
import random
import time
from collections import OrderedDict
from typing import Any, Optional

import requests

from ._env import load_env


class ApifyError(RuntimeError):
    pass


RETRYABLE_STATUSES = {408, 429, 500, 502, 503, 504}
CACHE_MAX_ENTRIES = 256
CACHE_TTL_SECONDS = 6 * 60 * 60


def _retry(attempts: int = 3, base_delay: float = 0.6):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            last_exc: Optional[Exception] = None
            for attempt in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except ApifyError as e:
                    msg = str(e)
                    retryable = any(f"HTTP {s}" in msg for s in RETRYABLE_STATUSES)
                    if not retryable or attempt == attempts - 1:
                        raise
                    last_exc = e
                except (requests.ConnectionError, requests.Timeout) as e:
                    if attempt == attempts - 1:
                        raise
                    last_exc = e
                time.sleep(base_delay * (2**attempt) + random.uniform(0, 0.25))
            assert last_exc is not None
            raise last_exc

        return wrapper

    return decorator


class ApifyClient:
    BASE_URL = "https://api.apify.com/v2"

    POST_ACTOR = "apimaestro~linkedin-post-detail"
    POST_COMMENTS_ACTOR = (
        "apimaestro~linkedin-post-comments-replies-engagements-scraper-no-cookies"
    )
    PROFILE_COMMENTS_ACTOR = "apimaestro~linkedin-profile-comments"
    POST_ENGAGERS_ACTOR = (
        "scraping_solutions~linkedin-posts-engagers-likers-and-commenters-no-cookies"
    )

    def __init__(self, token: Optional[str] = None, timeout: float = 180.0):
        load_env()
        self.token = token or os.getenv("APIFY_TOKEN")

        if not self.token:
            raise ApifyError(
                "APIFY_TOKEN not set. Export it or pass token= explicitly."
            )
        self.timeout = timeout
        self._session = requests.Session()
        self._cache: OrderedDict[str, tuple[float, Any]] = OrderedDict()

    # ---- Corpo do post ------------------------------------------------------

    def fetch_post(
        self, post_url: str, *, force_refresh: bool = False
    ) -> dict[str, Any]:
        """Retorna o corpo do post, autor e estatísticas de engajamento de um post.

        Args:
            post_url: Qualquer um dos três formatos de URL de URN do LinkedIn funciona.
            force_refresh: Se True, ignora o cache e busca novamente na Apify.

        Returns:
            Dict com as chaves: text, authorName, authorProfileUrl, urn, shareUrn,
            canShare, url, numLikes, numComments, numShares, postedAtISO, além de
            metadados extras. `shareUrn` é a URN pai do reshare
            (`urn:li:share:*` / `urn:li:ugcPost:*`).
        """
        items = self._run_sync(
            self.POST_ACTOR, {"post_urls": [post_url]}, force_refresh=force_refresh
        )
        if not items:
            raise ApifyError(f"no post returned for {post_url}")
        post = self._normalize_post(items[0])
        if not post.get("text") and not post.get("authorName"):
            # o apimaestro retorna um shell nulo (job_title "This post cannot be
            # displayed") para posts privados, removidos ou atrás de login. Trate
            # como indisponível para que os chamadores caiam de volta em pedir
            # ao usuário para colar o texto.
            raise ApifyError(
                f"post not retrievable (private, removed, or login-walled): {post_url}"
            )
        return post

    @staticmethod
    def _normalize_post(raw: dict[str, Any]) -> dict[str, Any]:
        """Achata a resposta aninhada do apimaestro/linkedin-post-detail para o
        contrato de post plano que as skills consomem. Mantém o payload bruto em `_raw`."""
        post = raw.get("post") or {}
        author = raw.get("author") or {}
        stats = raw.get("stats") or {}
        urn = post.get("urn") or {}

        def _urn(prefix: str, value: Any) -> Optional[str]:
            return f"{prefix}{value}" if value else None

        share_urn = (
            _urn("urn:li:share:", urn.get("share_urn"))
            or _urn("urn:li:ugcPost:", urn.get("ugcPost_urn"))
        )
        activity_urn = _urn("urn:li:activity:", urn.get("activity_urn"))
        return {
            "text": post.get("text"),
            "urn": activity_urn or share_urn,
            "shareUrn": share_urn,
            # o apimaestro não expõe canShare; deixe None para que o reshare só
            # bloqueie com um False explícito (o LinkedIn ainda rejeita se estiver desabilitado).
            "canShare": None,
            "url": post.get("url"),
            "type": post.get("type"),
            "authorName": author.get("name"),
            "authorHeadline": author.get("headline"),
            "authorProfileUrl": author.get("profile_url"),
            "authorFollowers": author.get("followers"),
            "numLikes": stats.get("total_reactions"),
            "numComments": stats.get("comments"),
            "numShares": stats.get("shares"),
            "reactions": stats.get("reactions"),
            "postedAtISO": post.get("created_at"),
            "isReshare": raw.get("is_reshared"),
            "resharedPost": raw.get("reshared_post"),
            "_raw": raw,
        }

    # ---- Comentários do post --------------------------------------------------

    def fetch_post_comments(
        self,
        *,
        post_id: str,
        max_items: int = 20,
        scrape_replies: bool = False,
        force_refresh: bool = False,
    ) -> list[dict[str, Any]]:
        """Retorna comentários (e opcionalmente respostas) de um post.

        Args:
            post_id: Activity ID, ugcPost ID, ou URL completa do post.
            max_items: Limite máximo de comentários retornados.
            scrape_replies: Se True, a lista `replies` de cada comentário é preenchida.
            force_refresh: Ignora o cache.
        """
        items = self._run_sync(
            self.POST_COMMENTS_ACTOR,
            {
                "postIds": [post_id],
                "maxItems": max_items,
                "scrapeReplies": scrape_replies,
            },
            force_refresh=force_refresh,
        )
        # O actor anexa um objeto de resumo da execução ({"summary": {...}}) junto
        # com os comentários (e o retorna sozinho quando um post tem zero comentários).
        # Descarte-o para que os chamadores só vejam registros de comentário reais.
        return [it for it in items if isinstance(it, dict) and "summary" not in it]

    # ---- Comentários recentes do perfil (usuário) ----------------------------

    def fetch_user_recent_comments(
        self,
        *,
        username: str,
        result_limit: int = 30,
        force_refresh: bool = False,
    ) -> list[dict[str, Any]]:
        """Retorna os comentários mais recentes de um usuário em todo o LinkedIn."""
        return self._run_sync(
            self.PROFILE_COMMENTS_ACTOR,
            {"username": username, "resultLimit": result_limit},
            force_refresh=force_refresh,
        )

    # ---- Engajadores do post (curtidas + comentários) -----------------------

    def fetch_post_engagers(
        self,
        *,
        post_url: str,
        max_items: int = 50,
        force_refresh: bool = False,
    ) -> list[dict[str, Any]]:
        """Retorna as pessoas que curtiram ou comentaram um post."""
        return self._run_sync(
            self.POST_ENGAGERS_ACTOR,
            {"urls": [post_url], "maxItems": max_items},
            force_refresh=force_refresh,
        )

    # ---- Auxiliares de cache -----------------------------------------------

    @staticmethod
    def _cache_key(actor_id: str, payload: dict[str, Any]) -> str:
        return f"{actor_id}::{json.dumps(payload, sort_keys=True, default=str)}"

    def _cache_get(self, key: str) -> Optional[Any]:
        entry = self._cache.get(key)
        if entry is None:
            return None
        ts, value = entry
        if time.time() - ts > CACHE_TTL_SECONDS:
            del self._cache[key]
            return None
        self._cache.move_to_end(key)
        return value

    def _cache_put(self, key: str, value: Any) -> None:
        self._cache[key] = (time.time(), value)
        self._cache.move_to_end(key)
        while len(self._cache) > CACHE_MAX_ENTRIES:
            self._cache.popitem(last=False)

    # ---- Internos -----------------------------------------------------------

    def _run_sync(
        self,
        actor_id: str,
        payload: dict[str, Any],
        *,
        force_refresh: bool = False,
    ) -> list[dict[str, Any]]:
        key = self._cache_key(actor_id, payload)
        if not force_refresh:
            cached = self._cache_get(key)
            if cached is not None:
                return cached
        data = self._do_request(actor_id, payload)
        result = data if isinstance(data, list) else []
        self._cache_put(key, result)
        return result

    @_retry()
    def _do_request(
        self, actor_id: str, payload: dict[str, Any]
    ) -> Any:
        # O token vai no cabeçalho Authorization, nunca na query string.
        # Um token na URL vaza para logs de proxy, histórico do shell, rastros
        # de erro e cabeçalhos Referer; um cabeçalho não.
        url = f"{self.BASE_URL}/acts/{actor_id}/run-sync-get-dataset-items"
        r = self._session.post(
            url,
            json=payload,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            timeout=self.timeout,
        )
        if r.status_code >= 400:
            try:
                body = r.json()
            except Exception:
                body = {"error": r.text[:500]}
            raise ApifyError(f"HTTP {r.status_code}: {body}")
        data = r.json()
        if isinstance(data, dict) and "error" in data:
            raise ApifyError(f"actor failed: {data['error']}")
        return data
