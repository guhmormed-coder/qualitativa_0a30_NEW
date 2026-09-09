"""Auxiliares do portão de aprovação.

Toda skill que publica no LinkedIn DEVE apresentar um rascunho ao usuário e
aguardar aprovação explícita antes de chamar a Publora. Este arquivo é uma
camada fina de convenções, não uma imposição em tempo de execução — as
skills devem chamar `render_approval_card` para formatar o rascunho de
forma consistente e então parar até o usuário dar o sinal verde.
"""
from __future__ import annotations
from typing import Optional


def render_approval_card(
    *,
    kind: str,  # "post" | "comment" | "reply" | "reaction"
    preview_text: str,
    target_url: Optional[str] = None,
    reaction_type: Optional[str] = None,
    char_count: Optional[int] = None,
    extra_context: Optional[dict] = None,
) -> str:
    """Formata um cartão de aprovação padronizado para o usuário revisar.

    O cartão DEVE conter:
    - Qual é a ação (post / comentário / resposta / reação)
    - O texto de prévia completo
    - URL de destino, se aplicável
    - Um prompt claro: "responda SIM para publicar ou sugira edições"
    """
    lines = [f"## Draft ready for approval — {kind}", ""]
    if target_url:
        lines.append(f"**Target:** {target_url}")
    if reaction_type:
        lines.append(f"**Reaction:** `{reaction_type}`")
    if char_count is None:
        char_count = len(preview_text)
    lines.append(f"**Chars:** {char_count}")
    lines.append("")
    lines.append("**Preview:**")
    lines.append("")
    for pl in preview_text.splitlines() or [""]:
        lines.append(f"> {pl}")
    lines.append("")
    if extra_context:
        lines.append("**Context:**")
        for k, v in extra_context.items():
            lines.append(f"- **{k}**: {v}")
        lines.append("")
    lines.append("Reply **post** / **yes** to publish, or suggest edits.")
    return "\n".join(lines)
