"""Cliente Pixfaro enxuto para o projeto LinkedIn Skills.

Camada de imagem (geração de ilustração). Fica ao lado da camada de leitura
(`apify_client`) e da camada de escrita (`publora_client`) como a terceira
integração: gera uma ilustração, recebe de volta uma URL hospedada, e
repassa essa URL diretamente para o `media_urls` da Publora ao publicar.

Autenticação: variável de ambiente PIXFARO_TOKEN (ou argumento do
construtor). Formato da chave `pf_live_...`. Sem um token, as skills caem
para o modo "manual": elas rascunham o prompt da imagem e pedem para você
gerá-la você mesmo e colar a URL.

Endpoint (compatível com o SDK da OpenAI):
  POST https://api.pixfaro.com/v1/images/generations
    body: {model, prompt, aspect_ratio "w:h", resolution "1K|2K|4K", overlay}
    overlay: {text|logo_id, position, opacity, font, color}  # composição com
             precisão de pixel, texto NÃO gerado pelo modelo — então um
             modelo base barato mais um overlay renderiza quote-cards /
             miniaturas nítidos a baixo custo.
    resp: {id, url, cost, balance_after}   # URL hospedada, não base64

Modelos (id / latência mediana / $ por imagem):
  gemini-flash-lite  3.0s   $0.041   (alto volume, barato)
  nano-banana-2      10.7s  $0.080   (padrão equilibrado)
  gemini-pro-image   20.8s  $0.164   (premium, com muito texto)
  gpt-5-image        53.0s  $0.238   (qualidade máxima)

Cache: LRU em processo (128 entradas, TTL de 6h). Passe `force_refresh=True`
para ignorá-lo. Novas tentativas em 408/429/5xx transitórios (3 tentativas,
backoff exponencial).
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


class PixfaroError(RuntimeError):
    def __init__(self, message: str, status_code: Optional[int] = None, retryable: bool = False):
        super().__init__(message)
        self.status_code = status_code
        self.retryable = retryable


BASE_URL = "https://api.pixfaro.com/v1"
DEFAULT_MODEL = "nano-banana-2"
KNOWN_MODELS = ("gemini-flash-lite", "nano-banana-2", "gemini-pro-image", "gpt-5-image")

RETRYABLE_STATUSES = {408, 429, 500, 502, 503, 504}
CACHE_MAX_ENTRIES = 128
CACHE_TTL_SECONDS = 6 * 60 * 60


def _retry(attempts: int = 3, base_delay: float = 0.6):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            last_exc: Optional[Exception] = None
            for attempt in range(attempts):
                try:
                    return fn(*args, **kwargs)
                except PixfaroError as e:
                    # Retryable = status HTTP transitório OU falha em nível de
                    # rede (timeout/reset), ambos sinalizados na exceção no momento em que é levantada.
                    if not getattr(e, "retryable", False) or attempt == attempts - 1:
                        raise
                    last_exc = e
                    time.sleep(base_delay * (2 ** attempt) + random.uniform(0, 0.3))
            if last_exc:
                raise last_exc
        return wrapper
    return decorator


class PixfaroClient:
    """Um método que importa: `generate`. Retorna a URL da imagem hospedada."""

    def __init__(self, api_key: Optional[str] = None, timeout: float = 90.0):
        load_env()
        self.api_key = api_key or os.getenv("PIXFARO_TOKEN") or os.getenv("PIXFARO_API_KEY")
        if not self.api_key:
            raise PixfaroError(
                "No Pixfaro API key. Set PIXFARO_TOKEN (pf_live_...) or pass api_key. "
                "Sign up at https://pixfaro.com."
            )
        self.timeout = timeout
        self._session = requests.Session()
        self._cache: "OrderedDict[str, tuple[float, dict]]" = OrderedDict()

    # ---- auxiliares de cache (espelha apify_client) ----
    def _cache_get(self, key: str) -> Optional[dict]:
        hit = self._cache.get(key)
        if not hit:
            return None
        ts, val = hit
        if time.time() - ts > CACHE_TTL_SECONDS:
            self._cache.pop(key, None)
            return None
        self._cache.move_to_end(key)
        return val

    def _cache_put(self, key: str, val: dict) -> None:
        self._cache[key] = (time.time(), val)
        self._cache.move_to_end(key)
        while len(self._cache) > CACHE_MAX_ENTRIES:
            self._cache.popitem(last=False)

    @_retry()
    def generate(
        self,
        prompt: str,
        *,
        model: str = DEFAULT_MODEL,
        aspect_ratio: str = "1:1",
        resolution: str = "1K",
        overlay: Optional[dict[str, Any]] = None,
        force_refresh: bool = False,
    ) -> dict[str, Any]:
        """Gera uma ilustração. Retorna {id, url, cost, balance_after}.

        `overlay` é repassado tal como recebido (por exemplo,
        {"text": "@handle", "position": "bottom-right", "opacity": 0.9,
         "color": "#0A66C2"}). Alimente os campos de marca a partir do
        Perfil de Voz & Marca para que todo asset carregue um
        handle/logo/cor consistente.
        """
        if not prompt or not prompt.strip():
            raise PixfaroError("prompt cannot be empty")
        if len(prompt) > 4000:
            raise PixfaroError("prompt exceeds 4000 characters")

        payload: dict[str, Any] = {
            "model": model,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "resolution": resolution,
        }
        if overlay:
            payload["overlay"] = overlay

        key = json.dumps(payload, sort_keys=True)
        if not force_refresh:
            cached = self._cache_get(key)
            if cached is not None:
                return cached

        data = self._post("/images/generations", payload)
        self._cache_put(key, data)
        return data

    @_retry()
    def edit(
        self,
        image_id: str,
        instruction: str,
        *,
        model: str = DEFAULT_MODEL,
        aspect_ratio: Optional[str] = None,
        resolution: Optional[str] = None,
        overlay: Optional[dict[str, Any]] = None,
        force_refresh: bool = False,
    ) -> dict[str, Any]:
        """Edita iterativamente uma geração anterior. Retorna {id, url, cost, ...}.

        `image_id` deve ser o id `img_...` retornado por uma chamada anterior
        de `generate` (ou `edit`) - URLs hospedadas NÃO são aceitas como
        origem. Omitir `aspect_ratio` mantém o formato de origem; omitir
        `resolution` herda (e cobra) o nível de origem. Mais barato e mais
        consistente do que regenerar do zero quando o usuário quer "deixar o
        céu mais escuro".
        """
        if not image_id or not str(image_id).startswith("img_"):
            raise PixfaroError(
                "edit requires a source image id (img_...) from a prior "
                "generation; hosted URLs are not accepted"
            )
        if not instruction or not instruction.strip():
            raise PixfaroError("instruction cannot be empty")
        if len(instruction) > 4000:
            raise PixfaroError("instruction exceeds 4000 characters")

        payload: dict[str, Any] = {
            "model": model,
            "image": image_id,
            "instruction": instruction,
        }
        if aspect_ratio:
            payload["aspect_ratio"] = aspect_ratio
        if resolution:
            payload["resolution"] = resolution
        if overlay:
            payload["overlay"] = overlay

        key = "edit:" + json.dumps(payload, sort_keys=True)
        if not force_refresh:
            cached = self._cache_get(key)
            if cached is not None:
                return cached

        data = self._post("/images/edits", payload)
        self._cache_put(key, data)
        return data

    @_retry()
    def list_models(self) -> list[dict[str, Any]]:
        """GET /v1/models — catálogo de modelos ao vivo + preços por nível."""
        url = f"{BASE_URL}/models"
        try:
            r = self._session.get(url, headers=self._headers(), timeout=self.timeout)
        except requests.RequestException as e:
            raise PixfaroError(f"request failed: {e}", retryable=True) from e
        out = self._handle(r)
        return out.get("data", out) if isinstance(out, dict) else out

    # ---- internos ----
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _post(self, path: str, json_body: dict[str, Any]) -> dict[str, Any]:
        url = f"{BASE_URL}{path}"
        try:
            r = self._session.post(url, json=json_body, headers=self._headers(), timeout=self.timeout)
        except requests.RequestException as e:
            raise PixfaroError(f"request failed: {e}", retryable=True) from e
        return self._handle(r)

    @staticmethod
    def _handle(r: requests.Response) -> dict[str, Any]:
        if r.status_code >= 400:
            detail = ""
            try:
                detail = json.dumps(r.json())
            except Exception:
                detail = r.text[:300]
            raise PixfaroError(
                f"HTTP {r.status_code}: {detail}",
                status_code=r.status_code,
                retryable=r.status_code in RETRYABLE_STATUSES,
            )
        try:
            return r.json()
        except ValueError as e:
            raise PixfaroError(f"non-JSON response: {r.text[:300]}") from e
