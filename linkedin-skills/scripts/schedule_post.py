#!/usr/bin/env python3
"""CLI: agenda um post aprovado do LinkedIn via Publora às 10:00 horário local.

Uso:
    python scripts/schedule_post.py --file draft.txt --angle <slug> [--source URL ...] [--dry-run]
    python scripts/schedule_post.py --selftest

Regra de agendamento: hoje às 10:00 horário local. Se já passou das 10:00,
agora + 5 min (a Publora trata um scheduledTime ausente como "salvar como
rascunho", então não existe uma chamada verdadeira de "publicar
imediatamente"; a alternativa mais próxima é agendar para alguns minutos à frente).

Todo agendamento bem-sucedido acrescenta uma linha JSON a
testing/linkedin-routine-log.jsonl para que a próxima execução possa
alternar para um ângulo diferente. testing/ está no gitignore.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

LOG_PATH = ROOT / "testing" / "linkedin-routine-log.jsonl"
POST_HOUR = 10
LEAD_MINUTES = 5


def slot(now: datetime) -> datetime:
    """O horário de 10:00 de hoje no fuso de `now`, ou now+5min se já tiver passado."""
    ten = now.replace(hour=POST_HOUR, minute=0, second=0, microsecond=0)
    return ten if now < ten else now + timedelta(minutes=LEAD_MINUTES)


def selftest() -> int:
    tz = timezone(timedelta(hours=-6))
    early = datetime(2026, 9, 7, 8, 30, tzinfo=tz)
    assert slot(early) == datetime(2026, 9, 7, 10, 0, tzinfo=tz)
    late = datetime(2026, 9, 7, 14, 20, tzinfo=tz)
    assert slot(late) == datetime(2026, 9, 7, 14, 25, tzinfo=tz)
    # 10:00 em ponto conta como já passado -> empurrado para frente, nunca agendado no passado
    assert slot(datetime(2026, 9, 7, 10, 0, tzinfo=tz)) > datetime(2026, 9, 7, 10, 0, tzinfo=tz)
    assert slot(early).astimezone(timezone.utc).isoformat() == "2026-09-07T16:00:00+00:00"
    print("autoteste OK")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", help="caminho para o texto final do post (UTF-8)")
    ap.add_argument("--angle", default="", help="slug do sub-tópico usado, para o log de rotação")
    ap.add_argument("--source", action="append", default=[], help="URL/título da fonte (repetível)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.file:
        ap.error("--file é obrigatório")

    text = Path(args.file).read_text(encoding="utf-8").strip()
    if not text:
        print("✗ o arquivo de rascunho está vazio", file=sys.stderr)
        return 2
    if len(text) > 3000:
        print(f"✗ o rascunho tem {len(text)} caracteres, o LinkedIn limita posts a 3000", file=sys.stderr)
        return 2

    when = slot(datetime.now().astimezone())
    scheduled_utc = when.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"→ {len(text)} caracteres, agendado para {when.isoformat()} (UTC {scheduled_utc})")

    if args.dry_run:
        print("(dry-run, nada foi agendado)")
        return 0

    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")

    from lib import active_backend, publish

    backend = active_backend()
    if backend != "publora":
        print(f"✗ backend é {backend!r}, esperado 'publora'. Verifique PUBLORA_API_KEY "
              f"e LINKEDIN_PLATFORM_ID no .env", file=sys.stderr)
        return 2

    try:
        resp = publish(
            "post",
            text,
            "https://www.linkedin.com/feed/",
            scheduled_time=scheduled_utc,
        )
    except Exception as e:
        print(f"✗ falha ao agendar na publora: {e}", file=sys.stderr)
        return 1

    r = resp or {}
    post_id = r.get("postGroupId") or r.get("postId") or r.get("id") or json.dumps(r)[:200]
    entry = {
        "date": when.date().isoformat(),
        "angle": args.angle,
        "sources": args.source,
        "scheduled_utc": scheduled_utc,
        "post_id": post_id,
        "chars": len(text),
    }
    LOG_PATH.parent.mkdir(exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"✓ agendado. id do post na publora: {post_id}")
    print(f"  resposta bruta: {json.dumps(resp, ensure_ascii=False)[:400]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
