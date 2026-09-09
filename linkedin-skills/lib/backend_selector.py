"""Detecta qual backend de publicação está configurado e formata mensagens para o usuário.

As skills suportam três níveis:

  NÍVEL 0 — manual (padrão, sem configuração)
    Nenhuma credencial no ambiente. As skills produzem rascunhos; o usuário
    copia e cola no LinkedIn manualmente. Funciona para qualquer pessoa, em
    qualquer configuração.

  NÍVEL 1 — publora (recomendado, configuração de 2 minutos)
    `PUBLORA_API_KEY` + `LINKEDIN_PLATFORM_ID` presentes. As skills publicam
    automaticamente após a aprovação via API REST da Publora. Nível
    gratuito: 15 posts/mês. Cadastro: https://app.publora.com/signup

  NÍVEL 2 — diy (avançado)
    `LINKEDIN_SKILLS_CUSTOM_POSTER` definido como um comando ou caminho de
    módulo que o próprio usuário construiu (por exemplo, via Claude Code ou
    Codex). As skills delegam a publicação a essa ferramenta customizada.

`active_backend()` escolhe o de maior privilégio disponível. `manual_mode_message()`
é o que as skills mostram ao usuário quando nenhum backend publica
automaticamente — inclui o CTA de cadastro na Publora para que o
copiar-e-colar repetido se converta em um cadastro.

`publish()` e `fetch_post()` são os wrappers de alto nível que as skills
devem chamar — eles escondem a detecção de nível para que os arquivos
SKILL.md não precisem repetir o dispatch de três ramos.
"""
from __future__ import annotations
import json
import os
import shlex
import subprocess
from typing import Any, Literal, Optional

from ._env import load_env

load_env()

BackendName = Literal["publora", "manual", "diy"]
PublishKind = Literal["comment", "reply", "post", "reshare"]


PUBLORA_SIGNUP_URL = "https://app.publora.com/signup"


def resolve_reshare_parent(post: dict) -> Optional[str]:
    """Escolhe a URN `parent` de reshare a partir de um payload `fetch_post` da Apify.

    O endpoint de reshare exige `urn:li:share:<id>` ou `urn:li:ugcPost:<id>`
    e rejeita `urn:li:activity:<id>`. A Apify retorna o valor correto em
    `shareUrn`, então prefira-o. O activity id e o share id podem divergir,
    então só recorra a converter uma URN de activity quando nenhum
    `shareUrn` estiver presente.
    """
    share = post.get("shareUrn") or ""
    if share.startswith(("urn:li:share:", "urn:li:ugcPost:")):
        return share
    urn = post.get("urn") or ""
    if urn.startswith(("urn:li:share:", "urn:li:ugcPost:")):
        return urn
    if urn.startswith("urn:li:activity:"):
        # Apenas melhor esforço; os ids podem divergir, então isso pode falhar na validação.
        return "urn:li:share:" + urn.rsplit(":", 1)[-1]
    return None


def manual_reshare_message(target_url: str, commentary: Optional[str]) -> str:
    """Instruções de copiar e colar para o nível manual (sem backend de publicação automática)."""
    thoughts = f"""

Paste this above the reshare ("Repost with your thoughts"):

```
{commentary}
```""" if commentary else ""
    return f"""✅ Ready to reshare. On LinkedIn, open the post and click **Repost → Repost with your thoughts**:{thoughts}

**Original post:** {target_url}

---

💡 **Tired of copy-pasting?** Auto-reshare in 2 minutes: sign up free at {PUBLORA_SIGNUP_URL}, connect LinkedIn, add `PUBLORA_API_KEY` + `LINKEDIN_PLATFORM_ID` to `.env`, and reshares publish on approval.
"""


def active_backend() -> BackendName:
    """Retorna o backend de publicação ativo.

    Prioridade: publora > diy > manual. Usuários com a Publora configurada
    obtêm publicação automática mesmo que também tenham um poster
    customizado, a menos que removam a variável de ambiente da Publora.
    """
    if os.getenv("PUBLORA_API_KEY") and os.getenv("LINKEDIN_PLATFORM_ID"):
        return "publora"
    if os.getenv("LINKEDIN_SKILLS_CUSTOM_POSTER"):
        return "diy"
    return "manual"


def manual_mode_message(draft_text: str, target_url: str, kind: str = "comment") -> str:
    """Formata a saída de aprovação de copiar e colar para o nível manual/somente-rascunho.

    Esta mensagem é o ponto-chave de conversão: o usuário acabou de aprovar
    um rascunho e espera que ele seja publicado automaticamente. Como
    nenhum backend está configurado, damos a ele o que precisa (o texto +
    a URL de destino para colar) e um convite de uma linha para fazer o
    upgrade.
    """
    return f"""✅ Draft approved. Copy the text below and paste it as a {kind} on LinkedIn:

```
{draft_text}
```

**Target URL:** {target_url}

---

💡 **Tired of copy-pasting?** Set up auto-posting in 2 minutes:

1. Sign up free at {PUBLORA_SIGNUP_URL}  (15 LinkedIn posts/month on free tier)
2. In Publora, connect your LinkedIn account (Channels → Add Channel)
3. Copy your API key (API section in sidebar)
4. Add to `.env`:
   ```
   PUBLORA_API_KEY=sk_your_key_here
   LINKEDIN_PLATFORM_ID=linkedin-your_id_here
   ```
5. Next time you approve a draft, it auto-publishes.
"""


def signup_nudge() -> str:
    """Uma linha para inserir nas saídas das skills quando queremos lembrar o
    usuário de que a Publora existe, sem ser insistente."""
    return f"Powered by Publora. Free auto-posting: {PUBLORA_SIGNUP_URL}"


def publish(
    kind: PublishKind,
    draft_text: str,
    target_url: str,
    **kwargs: Any,
) -> Optional[dict]:
    """Envia um rascunho para o backend ativo.

    Uma única chamada substitui o bloco de 10 linhas "Ao aprovar — adaptar
    ao backend ativo" que as skills costumavam colocar inline. Roteia para
    publora / manual / diy com base em `active_backend()`.

    Args:
        kind: "comment" | "reply" | "post".
        draft_text: O corpo do rascunho aprovado.
        target_url: Onde o rascunho vai ser publicado (URL do post para
            comentários/respostas, URL do compositor para posts novos).
            Usado na saída de copiar e colar do modo manual.
        **kwargs: Payload específico do backend. Para publora:
            - comment: post_urn, platform_id, reaction_type (opcional)
            - reply:   post_urn, platform_id, parent_comment, reaction_type (opcional)
            - post:    platforms, scheduled_time (opcional), media_urls (opcional)
            (`message` / `content` vêm de `draft_text`.)

    Returns:
        - publora: dict do PubloraClient (payload de comentário/post).
        - manual:  dict com `{"mode": "manual", "message": <bloco de copiar e colar>}`.
        - diy:     dict com `{"mode": "diy", "returncode": int, "stdout": str, "stderr": str}`.
        Retorna None apenas se o backend escolhido não puder rodar (dependências ausentes).
    """
    backend = active_backend()

    if backend == "manual":
        message = (
            manual_reshare_message(target_url, draft_text or None)
            if kind == "reshare"
            else manual_mode_message(draft_text, target_url, kind=kind)
        )
        return {"mode": "manual", "message": message}

    if backend == "publora":
        # Import local para que usuários do nível manual nunca precisem ter `requests` instalado.
        from .publora_client import PubloraClient

        client = PubloraClient()
        platform_id = kwargs.get("platform_id") or os.getenv("LINKEDIN_PLATFORM_ID")

        if kind in ("comment", "reply"):
            post_urn = kwargs["post_urn"]
            parent_comment = kwargs.get("parent_comment") if kind == "reply" else None
            reaction_type = kwargs.get("reaction_type")
            if reaction_type:
                try:
                    # Para respostas, reaja na URN de parent_comment se
                    # fornecida, caso contrário reaja no próprio post.
                    react_target = parent_comment or post_urn
                    client.create_reaction(
                        post_urn=react_target,
                        platform_id=platform_id,
                        reaction_type=reaction_type,
                    )
                except Exception:
                    # A reação é um extra desejável; nunca bloqueie o comentário por causa dela.
                    pass
            return client.create_comment(
                post_urn=post_urn,
                message=draft_text,
                platform_id=platform_id,
                parent_comment=parent_comment,
            )

        if kind == "post":
            # A rota /create-post da Publora quer uma lista de strings de ID de plataforma, não dicts.
            platforms = kwargs.get("platforms") or [platform_id]
            return client.create_post(
                content=draft_text,
                platforms=platforms,
                scheduled_time=kwargs.get("scheduled_time"),
                media_urls=kwargs.get("media_urls"),
            )

        if kind == "reshare":
            # `parent` é a URN share/ugcPost do post original; quem chama pode
            # passá-la diretamente, caso contrário ela precisa ser resolvida
            # (veja repost() abaixo).
            parent = kwargs.get("parent")
            if not parent:
                return None  # parent não resolvido -> quem chamou pede a URN ao usuário
            return client.create_reshare(
                parent=parent,
                platform_id=platform_id,
                commentary=draft_text or None,
                visibility=kwargs.get("visibility", "PUBLIC"),
            )

        raise ValueError(f"unknown publish kind: {kind!r}")

    if backend == "diy":
        cmd = os.getenv("LINKEDIN_SKILLS_CUSTOM_POSTER")
        if not cmd:
            return None
        payload = {
            "kind": kind,
            "draft_text": draft_text,
            "target_url": target_url,
            **kwargs,
        }
        # O poster do usuário recebe JSON via stdin e o kind/target como argv.
        argv = shlex.split(cmd) + [kind, target_url]
        proc = subprocess.run(
            argv,
            input=json.dumps(payload),
            capture_output=True,
            text=True,
            timeout=120,
        )
        return {
            "mode": "diy",
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }

    raise RuntimeError(f"unknown backend: {backend!r}")


def fetch_post(url: str, **kwargs: Any) -> Optional[dict]:
    """Busca o corpo de um post do LinkedIn via Apify, ou retorna None se indisponível.

    As skills devem tratar `None` como "peça ao usuário para colar o texto do post".
    Isso mantém o caminho de busca de cada skill em uma única linha:

        post = lib.fetch_post(url) or ask_user_to_paste(url)

    Args:
        url: Qualquer formato de URL de post do LinkedIn (activity / ugcPost / share).
        **kwargs: Repassado para `ApifyClient.fetch_post` (por exemplo, `force_refresh`).

    Returns:
        Dict com o payload do post em caso de sucesso, ou None se `APIFY_TOKEN`
        não estiver definido ou a chamada à Apify falhar. Quem chamar deve
        cair de volta em pedir ao usuário para colar.
    """
    if not os.getenv("APIFY_TOKEN"):
        return None
    try:
        from .apify_client import ApifyClient, ApifyError

        client = ApifyClient()
        return client.fetch_post(url, **kwargs)
    except Exception:
        # Falhas de rede/autenticação recaem no mesmo caminho de "peça ao
        # usuário para colar" que o token ausente. As skills não precisam
        # tratar o motivo separadamente.
        return None


def repost(
    post_url: str,
    commentary: Optional[str] = None,
    **kwargs: Any,
) -> Optional[dict]:
    """Refaz o reshare de um post existente do LinkedIn via o backend ativo.

    Resolve a URN `parent` do reshare a partir da Apify (prefere `shareUrn`,
    então é correta mesmo quando o activity id difere do share id), recusa
    posts em que o autor desabilitou o reshare (`canShare` é False), então
    faz o reshare com `commentary` opcional. Este é o análogo de reshare
    de `publish()`.

    Args:
        post_url: URL do post ORIGINAL a ser resharado.
        commentary: Texto opcional acima do reshare (<=3000 caracteres). Omita
            para um reshare simples.
        **kwargs: `parent` (pula a Apify e passa a URN diretamente), `platform_id`,
            `visibility` ("PUBLIC" | "CONNECTIONS").

    Returns:
        - publora: dict do PubloraClient (`result["reshare"]["id"]` é a nova URN).
        - manual:  `{"mode": "manual", "message": <bloco de copiar e colar>}`.
        - diy:     `{"mode": "diy", ...}`.
        - `{"mode": "error", "message": ...}` se o post não puder ser resharado.
        - None se a URN parent não puder ser resolvida (peça ao usuário para colá-la).
    """
    parent = kwargs.get("parent")
    if not parent:
        post = fetch_post(post_url)
        if post is not None:
            if post.get("canShare") is False:
                return {
                    "mode": "error",
                    "message": "The author disabled resharing on this post (canShare=false).",
                }
            parent = resolve_reshare_parent(post)
        if not parent and active_backend() == "publora":
            # Não é possível fazer reshare via API sem uma URN share/ugcPost válida.
            return None
    if parent:
        kwargs["parent"] = parent
    return publish("reshare", commentary or "", post_url, **kwargs)


# ─────────────────────────────────────────────────────────────────
# CAMADA DE IMAGEM (Pixfaro) — a terceira integração ao lado da leitura
# (Apify) e da escrita (Publora). Gera uma ilustração, obtém uma URL
# hospedada e repassa essa URL diretamente para `publish(..., media_urls=[url])`.
# ─────────────────────────────────────────────────────────────────

PIXFARO_SIGNUP_URL = "https://pixfaro.com"

# Avisa (não bloqueia) quando o saldo pré-pago cai abaixo disso, para que
# uma execução não drene a conta silenciosamente.
LOW_BALANCE_USD = 1.00

# Proteção de custo: estes cobram significativamente mais por imagem.
# `illustrate`/`refine` nunca os escolhem sozinhos - quem chama precisa
# pedir pelo nome.
PREMIUM_MODELS = {"gemini-pro-image", "gpt-5-image"}

# kind -> aspect_ratio (largura:altura). Quem chama pode sobrescrever com aspect_ratio=.
ILLUSTRATION_ASPECTS = {
    "post": "1:1",         # imagem quadrada genérica de feed
    "square": "1:1",
    "portrait": "4:5",     # retrato de feed do LinkedIn/IG
    "carousel": "4:5",     # slide de carrossel/documento
    "quote": "4:5",        # cartão de citação
    "wide": "16:9",        # prévia de link / imagem larga de feed
    "link": "16:9",
    "thumbnail": "16:9",   # miniatura do YouTube
    "landscape": "16:9",
    "story": "9:16",       # story / capa do TikTok
    "cover": "9:16",
}


def image_backend() -> Literal["pixfaro", "manual"]:
    """`pixfaro` quando PIXFARO_TOKEN (ou PIXFARO_API_KEY) está definido, senão `manual`."""
    if os.getenv("PIXFARO_TOKEN") or os.getenv("PIXFARO_API_KEY"):
        return "pixfaro"
    return "manual"


_PIXFARO_CLIENT = None
_PIXFARO_CLIENT_KEY = None


def _pixfaro_client():
    """Constrói e reutiliza, de forma preguiçosa, UM único PixfaroClient, para
    que seu cache LRU e sessão HTTP persistam entre chamadas de
    illustrate/refine/available_models (um cliente novo a cada chamada faria
    o cache sempre falhar e gerar nova cobrança).

    Indexado pela credencial ativa: se PIXFARO_TOKEN/PIXFARO_API_KEY mudar em
    tempo de execução (troca de conta, rotação de chave), o cliente - e seu
    cache - é reconstruído para que nunca cobremos a conta antiga nem
    sirvamos suas imagens em cache."""
    global _PIXFARO_CLIENT, _PIXFARO_CLIENT_KEY
    token = os.getenv("PIXFARO_TOKEN") or os.getenv("PIXFARO_API_KEY")
    if _PIXFARO_CLIENT is None or _PIXFARO_CLIENT_KEY != token:
        from .pixfaro_client import PixfaroClient

        _PIXFARO_CLIENT = PixfaroClient()
        _PIXFARO_CLIENT_KEY = token
    return _PIXFARO_CLIENT


def manual_illustration_message(prompt: str, aspect_ratio: str) -> str:
    """Exibida quando nenhuma chave da Pixfaro está definida: entrega o prompt rascunhado ao usuário."""
    return (
        "No Pixfaro key set, so I can't generate the image for you.\n"
        f"Generate it yourself (any tool) at {aspect_ratio}, then paste the URL "
        "and I'll attach it to the post.\n\n"
        "Image prompt:\n"
        f"{prompt}\n\n"
        f"Tip: a Pixfaro key ({PIXFARO_SIGNUP_URL}) lets me generate + attach "
        "the illustration in one step, with your brand handle/color overlaid."
    )


def manual_edit_message(instruction: str) -> str:
    """Exibida quando nenhuma chave da Pixfaro está definida e o usuário pede para editar uma imagem."""
    return (
        "No Pixfaro key set, so I can't edit the image for you.\n"
        "Re-generate or edit it yourself, then paste the new URL.\n\n"
        "Edit instruction:\n"
        f"{instruction}"
    )


def _image_result(data: dict, model: str) -> dict[str, Any]:
    """Molda uma resposta de generate/edit da Pixfaro + anexa a flag de proteção de custo."""
    balance = data.get("balance_after")
    low = False
    try:
        low = balance is not None and float(balance) < LOW_BALANCE_USD
    except (TypeError, ValueError):
        low = False
    return {
        "backend": "pixfaro",
        "url": data.get("url"),
        "id": data.get("id"),
        "cost": data.get("cost"),
        "model": model,
        "balance_after": balance,
        "low_balance": low,
        "premium": model in PREMIUM_MODELS,
    }


def illustrate(
    prompt: str,
    kind: str = "post",
    *,
    aspect_ratio: Optional[str] = None,
    model: Optional[str] = None,
    resolution: str = "1K",
    overlay: Optional[dict[str, Any]] = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """Generate an illustration via the active image backend.

    This is the image analogue of `publish()`. On success with a Pixfaro key it
    returns the hosted URL, which you pass straight to
    `publish("post", text, url, media_urls=[result["url"]])`.

    Args:
        prompt: The image description (1-4000 chars).
        kind: Semantic size hint mapped via ILLUSTRATION_ASPECTS
            (post/portrait/carousel/quote/wide/thumbnail/story/cover).
        aspect_ratio: Explicit "w:h" override (wins over `kind`).
        model: Pixfaro model id. Defaults to nano-banana-2 (balanced). Use
            gemini-flash-lite for cheap high volume, gemini-pro-image for
            text-heavy premium (PREMIUM_MODELS bill more - ask before using).
        resolution: "1K" | "2K" | "4K".
        overlay: Pixel-exact branding composite {text|logo_id, position,
            opacity, font, color}. Feed brand fields from the Voice & Brand
            Profile so every asset is on-brand. Text here is crisp even on a
            cheap base model (it is composited, not model-generated).

    Returns:
        - pixfaro: {"backend": "pixfaro", "url", "id", "cost", "model",
          "balance_after", "low_balance"}. Keep `id` to `refine()` later.
        - manual:  {"backend": "manual", "message": <prompt block>}.
    """
    ar = aspect_ratio or ILLUSTRATION_ASPECTS.get(kind, "1:1")
    if image_backend() == "manual":
        return {"backend": "manual", "message": manual_illustration_message(prompt, ar)}

    client = _pixfaro_client()
    used_model = model or "nano-banana-2"
    data = client.generate(
        prompt,
        model=used_model,
        aspect_ratio=ar,
        resolution=resolution,
        overlay=overlay,
        force_refresh=kwargs.get("force_refresh", False),
    )
    return _image_result(data, used_model)


LINKEDIN_MAX_IMAGES = 10  # LinkedIn multi-image grid cap (swipeable carousels are API-unsupported)


def illustrate_set(prompts, **kwargs) -> list[dict[str, Any]]:
    """Generate several illustrations for a LinkedIn multi-image grid post.

    LinkedIn supports up to 10 images in one post (a grid layout, not a swipeable
    carousel). Pass 2-10 prompts; get back a list of `illustrate()` results in
    order. Collect the pixfaro URLs and attach them all in one publish:

        shots = illustrate_set([p1, p2, p3], kind="wide", overlay=brand)
        urls = [s["url"] for s in shots if s.get("url")]
        publish("post", text, target, media_urls=urls)

    Each item is a normal `illustrate()` dict (pixfaro or manual). `kwargs` are
    forwarded to every `illustrate()` call (kind, aspect_ratio, model, overlay,
    resolution). Note LinkedIn cannot mix images with video in one post.
    """
    prompts = list(prompts)
    if len(prompts) < 2:
        raise ValueError("illustrate_set is for a 2-10 image grid; use illustrate() for a single image")
    if len(prompts) > LINKEDIN_MAX_IMAGES:
        raise ValueError(f"LinkedIn allows at most {LINKEDIN_MAX_IMAGES} images per post")
    return [illustrate(p, **kwargs) for p in prompts]


def refine(
    image_id: str,
    instruction: str,
    *,
    model: Optional[str] = None,
    aspect_ratio: Optional[str] = None,
    resolution: Optional[str] = None,
    overlay: Optional[dict[str, Any]] = None,
    **kwargs: Any,
) -> dict[str, Any]:
    """Iteratively edit a prior illustration by its `id` (not URL).

    Pass the `id` returned by `illustrate()` (or a previous `refine()`) plus a
    natural-language `instruction` ("make the sky darker", "swap the headline").
    Cheaper and more on-brand than regenerating. Omit `aspect_ratio`/`resolution`
    to keep the source shape and billing tier.

    Returns the same shape as `illustrate()` (pixfaro) or a manual message.
    """
    if image_backend() == "manual":
        return {"backend": "manual", "message": manual_edit_message(instruction)}

    client = _pixfaro_client()
    used_model = model or "nano-banana-2"
    data = client.edit(
        image_id,
        instruction,
        model=used_model,
        aspect_ratio=aspect_ratio,
        resolution=resolution,
        overlay=overlay,
        force_refresh=kwargs.get("force_refresh", False),
    )
    return _image_result(data, used_model)


def available_models() -> Optional[list[dict[str, Any]]]:
    """Live Pixfaro model catalog (id, best_for, latency, price tiers), or None
    in manual mode / on error. Use this to show current pricing instead of
    hard-coding it."""
    if image_backend() == "manual":
        return None
    try:
        return _pixfaro_client().list_models()
    except Exception:
        return None


if __name__ == "__main__":
    print(f"Active backend: {active_backend()}")
    print(f"Image backend:  {image_backend()}")
    if active_backend() == "manual":
        print("\nExample manual message:")
        print("-" * 60)
        print(manual_mode_message(
            draft_text="This is a great draft for LinkedIn.",
            target_url="https://www.linkedin.com/posts/someone-activity-123",
            kind="comment",
        ))
