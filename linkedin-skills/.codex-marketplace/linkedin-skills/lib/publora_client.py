"""Cliente REST Publora enxuto para o projeto LinkedIn Skills.

Encapsula os endpoints da API da Publora. Em 2026-05-11 a Publora expõe:
- POST /create-post              (agendar post multiplataforma)
- POST /linkedin-comments        (comentário de topo ou resposta via parentComment)
- DELETE /linkedin-comments      (remover um comentário que publicamos)
- POST /linkedin-reactions       (reagir a um post ou comentário)
- POST /linkedin-reshare         (reshare/repost de um post, com commentary opcional)

Não há endpoint de leitura no momento (sem GET /posts, sem listagem, sem
delete-scheduled-post). O agendamento de posts é "dispare e esqueça"; o
cancelamento precisa ser feito no painel da Publora.

Cabeçalho de autenticação: x-publora-key: sk_...

Nota de design: este cliente é deliberadamente minimalista. As skills chamam
exatamente um método por ação, depois que o usuário aprovou um rascunho
renderizado via `lib/approval.py`. Todos os métodos de escrita tentam
novamente em 408/429/5xx transitórios via o decorador de retry compartilhado.
"""
from __future__ import annotations
import os
import time
import random
from typing import Any, Optional

import requests

from ._env import load_env


class PubloraError(RuntimeError):
    pass


RETRYABLE_STATUSES = {408, 429, 500, 502, 503, 504}


def _retry(attempts: int = 3, base_delay: float = 0.6):
    """Decorador de retry para métodos HTTP. Ativa em 408/429/5xx e em
    erros transitórios de rede. Backoff exponencial com jitter."""

    def decorator(fn):
        def wrapper(*args, **kwargs):
            last_exc: Optional[Exception] = None
            for attempt in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except PubloraError as e:
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


class PubloraClient:
    BASE_URL = "https://api.publora.com/api/v1"

    def __init__(self, api_key: Optional[str] = None, timeout: float = 30.0):
        load_env()
        self.api_key = api_key or os.getenv("PUBLORA_API_KEY")

        if not self.api_key:
            raise PubloraError(
                "PUBLORA_API_KEY not set. Export it or pass api_key= explicitly."
            )
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update(
            {
                "x-publora-key": self.api_key,
                "Content-Type": "application/json",
            }
        )

    # ---- Comentários do LinkedIn -------------------------------------------

    def create_comment(
        self,
        *,
        post_urn: str,
        message: str,
        platform_id: str,
        parent_comment: Optional[str] = None,
    ) -> dict[str, Any]:
        """Publica um comentário do LinkedIn (de topo) ou uma resposta (com parent_comment definido).

        Args:
            post_urn: urn:li:activity:... | urn:li:ugcPost:... | urn:li:share:...
            message: até 1.250 caracteres; suporta menções @{urn:li:person:ID|Name}
            platform_id: por exemplo, "linkedin-fToLopAkEI"
            parent_comment: urn:li:comment:(POST_URN,COMMENT_ID) para respostas.
                Nota: o LinkedIn achata as respostas em 2 níveis; para responder
                a uma resposta, use aqui a URN do comentário de TOPO, não a URN da resposta.

        Returns:
            Dict de resposta da Publora com `comment.id`, `comment.commentUrn`, etc.
        """
        if len(message) > 1250:
            raise PubloraError("message exceeds 1,250 char LinkedIn limit")
        payload = {
            "postedId": post_urn,
            "message": message,
            "platformId": platform_id,
        }
        if parent_comment:
            payload["parentComment"] = parent_comment
        return self._post("/linkedin-comments", payload)

    def delete_comment(
        self,
        *,
        post_urn: str,
        comment_id: str,
        platform_id: str,
    ) -> dict[str, Any]:
        r = self._session.delete(
            self.BASE_URL + "/linkedin-comments",
            json={
                "postedId": post_urn,
                "commentId": comment_id,
                "platformId": platform_id,
            },
            timeout=self.timeout,
        )
        return self._handle(r)

    # ---- Reações do LinkedIn -----------------------------------------------

    # Tipos de reação válidos segundo a Publora: LIKE, PRAISE, EMPATHY, INTEREST,
    # APPRECIATION, ENTERTAINMENT. (INSIGHTFUL NÃO é válido — mapeie para INTEREST.)
    REACTION_ALIASES = {
        "INSIGHTFUL": "INTEREST",
        "CURIOUS": "INTEREST",
        "FUNNY": "ENTERTAINMENT",
        "LAUGH": "ENTERTAINMENT",
        "LOVE": "APPRECIATION",
        "CELEBRATE": "PRAISE",
    }

    def create_reaction(
        self,
        *,
        post_urn: str,
        platform_id: str,
        reaction_type: str = "LIKE",
    ) -> dict[str, Any]:
        rtype = self.REACTION_ALIASES.get(reaction_type.upper(), reaction_type.upper())
        return self._post(
            "/linkedin-reactions",
            {
                "postedId": post_urn,
                "platformId": platform_id,
                "reactionType": rtype,
            },
        )

    # ---- Posts ----------------------------------------------------------------

    def create_post(
        self,
        *,
        content: str,
        platforms: list,
        scheduled_time: Optional[str] = None,
        media_urls: Optional[list[str]] = None,
    ) -> dict[str, Any]:
        """Cria um post multiplataforma.

        `platforms` é uma lista de STRINGS de ID de conexão de plataforma, por
        exemplo, ["linkedin-xxx"]. O endpoint /create-post da Publora exige IDs
        em string; passar o formato antigo de dict {"platform","platformId"}
        retorna HTTP 400 ("Invalid platform ID format"). Por compatibilidade
        com versões anteriores, entradas em dict são normalizadas aqui para
        seu "platformId". `scheduled_time` é ISO 8601 (UTC); se None, o post
        é criado como rascunho.
        """
        norm_platforms = [
            p if isinstance(p, str) else (p.get("platformId") or p.get("platform"))
            for p in platforms
        ]
        payload: dict[str, Any] = {
            "content": content,
            "platforms": norm_platforms,
        }
        if scheduled_time:
            payload["scheduledTime"] = scheduled_time
        if media_urls:
            payload["mediaUrls"] = media_urls
        return self._post("/create-post", payload)

    # ---- Reshare (repost) ------------------------------------------------------

    def create_reshare(
        self,
        *,
        parent: str,
        platform_id: str,
        commentary: Optional[str] = None,
        visibility: str = "PUBLIC",
    ) -> dict[str, Any]:
        """Refaz o reshare (repost) de um post existente do LinkedIn no feed da conexão.

        `parent` é a URN do post ORIGINAL e deve ser `urn:li:share:<id>` ou
        `urn:li:ugcPost:<id>` (NÃO `urn:li:activity:<id>`, que o endpoint
        rejeita). O `fetch_post` da Apify retorna isso diretamente como
        `shareUrn`; prefira-o em vez de converter um activity id, já que os
        dois números podem divergir.

        `commentary` (<=3000 caracteres) é o texto mostrado acima do reshare
        ("repost com seus comentários"); omita para um reshare simples.
        `visibility` é `PUBLIC` ou `CONNECTIONS`. O endpoint retorna HTTP 201;
        a nova URN de reshare é `result["reshare"]["id"]`.
        """
        payload: dict[str, Any] = {
            "platformId": platform_id,
            "parent": parent,
        }
        if commentary:
            payload["commentary"] = commentary
        if visibility:
            payload["visibility"] = visibility.upper()
        return self._post("/linkedin-reshare", payload)

    # ---- Internos ---------------------------------------------------------

    @_retry()
    def _post(self, path: str, json_body: dict[str, Any]) -> dict[str, Any]:
        r = self._session.post(
            self.BASE_URL + path, json=json_body, timeout=self.timeout
        )
        return self._handle(r)

    @staticmethod
    def _handle(r: requests.Response) -> dict[str, Any]:
        if r.status_code >= 400:
            try:
                body = r.json()
            except Exception:
                body = {"error": r.text[:500]}
            raise PubloraError(f"HTTP {r.status_code}: {body}")
        return r.json()
