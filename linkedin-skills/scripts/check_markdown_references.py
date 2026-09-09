#!/usr/bin/env python3
"""Verifica as referências Markdown declaradas pelos documentos de skill.

Todo caminho entre crases terminado em ``.md`` no ``SKILL.md`` raiz, na
árvore compartilhada ``references/``, e em tudo sob ``skills/`` deve resolver
seja em relação ao documento que o cita (irmão simples ``post-audit.md``,
local à skill ``references/X.md`` / ``sub-skills/X.md``, aninhado
``../../../references/X.md``) seja em relação à raiz do repositório
(``skills/<skill>/SKILL.md``, ``README.md``).
"""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REFERENCE = re.compile(r"`((?:\.\.?/)*[A-Za-z0-9_.\-]+(?:/[A-Za-z0-9_.\-]+)*\.md)(?:#[^`]*)?`")


def documents() -> list[Path]:
    """SKILL.md raiz, referências compartilhadas da raiz, e tudo sob skills/."""
    found = [ROOT / "SKILL.md"] if (ROOT / "SKILL.md").is_file() else []
    found += sorted((ROOT / "references").rglob("*.md"))
    found += sorted(SKILLS.rglob("*.md"))
    return found


def resolves(document: Path, ref: str) -> bool:
    return (document.parent / ref).resolve().is_file() or (ROOT / ref).resolve().is_file()


def main() -> None:
    broken: list[str] = []

    for document in documents():
        text = document.read_text(encoding="utf-8")
        for match in REFERENCE.finditer(text):
            ref = match.group(1)
            if "://" in ref or ref.startswith("/"):
                continue
            if not resolves(document, ref):
                broken.append(f"{document.relative_to(ROOT)}: {ref}")

    if broken:
        raise SystemExit("Referências Markdown quebradas:\n" + "\n".join(broken))

    print("Todas as referências Markdown resolvem corretamente.")


if __name__ == "__main__":
    main()
