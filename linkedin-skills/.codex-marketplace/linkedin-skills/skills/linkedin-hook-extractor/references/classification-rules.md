# Regras de Classificação de Fórmulas de Gancho

Características extraídas de um post e como elas mapeiam para as fórmulas.

## Extração de características

### Características do gancho (primeiras 2 linhas)
- `anaphora_count`: número de linhas paralelas no estilo "X pode Y" no topo
- `leads_with_number`: a linha 1 começa com um valor em dinheiro ou estatística?
- `question_hook`: a linha 1 é uma pergunta?
- `confession_phrase`: "Eu parei de", "Eu estava errado", "durante anos eu"
- `obituary_phrase`: "R.I.P.", "morrendo desde", "causa da morte"
- `time_anchor`: "{N} {dias|meses|anos} atrás"
- `year_over_year`: "Em {2024|2025}, eu ... Em {2025|2026}, eu estou"
- `curiosity_gap`: provocação curta e incompleta (<8 palavras, sem substantivo especificado)
- `free_reversal`: "Eu cobro X. Hoje é de graça."
- `public_commitment`: "Nas próximas 24 horas, eu vou"

### Características do corpo
- `has_numbered_list`: 1., 2., 3., ... com ≥4 itens
- `has_dated_receipts`: múltiplas linhas do tipo "{Mês Ano} — {evento}"
- `has_ledger`: valores em dinheiro item a item (não arredondados)
- `has_teardown`: referências ou anotações a capturas de tela
- `has_checklist`: passos nomeados com instruções

### Características do fechamento
- `mirror_question`: "Qual é o seu pivô de {ano anterior→este ano}?"
- `identity_reframe`: "Se você é X, você já perdeu"
- `commitment_close`: "Se eu estiver errado, eu te devo um post"
- `soft_offer`: "Conecte-se + me chame no DM para X"
- `comment_gate`: "Comente PALAVRA-CHAVE abaixo"

## Mapeamento de características → fórmulas

```python
FORMULA_RULES = {
    "F1_anaphora": {
        "required": ["anaphora_count >= 3"],
        "boost": ["has_numbered_list", "metaphor_close"],
    },
    "F2_rip_obituary": {
        "required": ["obituary_phrase"],
        "boost": ["has_numbered_list", "identity_reframe"],
    },
    "F3_year_over_year": {
        "required": ["year_over_year"],
        "boost": ["mirror_question"],
    },
    "F4_time_anchor_confession": {
        "required": ["time_anchor OR confession_phrase"],
        "boost": ["mirror_question"],
    },
    "F5_self_proving_meta": {
        "required": ["public_commitment"],
        "boost": ["commitment_close", "has_numbered_list"],
    },
    "F6_comment_gate": {
        "required": ["comment_gate"],
        "boost": ["has_numbered_list"],
    },
    "F7_odd_precision_money": {
        "required": ["leads_with_number", "has_ledger"],
        "boost": ["identity_reframe"],
    },
    "F8_paid_vs_free_reversal": {
        "required": ["free_reversal"],
        "boost": ["has_checklist", "soft_offer"],
    },
    "F9_curiosity_gap": {
        "required": ["curiosity_gap"],
        "boost": [],
    },
    "F10_contrarian_historical": {
        "required": ["has_dated_receipts"],
        "boost": ["identity_reframe"],
    },
}
```

## Pontuação de confiança

```python
def score_formula(post_features: dict, rules: dict) -> float:
    required_met = sum(1 for r in rules["required"] if eval_feature(post_features, r))
    if required_met < len(rules["required"]):
        return 0.0
    boost = sum(1 for b in rules["boost"] if post_features.get(b))
    return 1.0 + 0.15 * boost  # limite de 1.6
```

Retornar as 2 melhores fórmulas com pontuação > 0.8.

## Casos extremos

- **Ganchos híbridos:** quando um post mistura duas fórmulas (ex.: F4 confissão + F3 ano-a-ano), retornar ambas com a confiança dividida.
- **Posts apenas narrativos:** se nenhum gancho estrutural é disparado, classificar como "narrativa livre" e pular a atribuição de fórmula.
- **Não em inglês:** pular a classificação, retornar apenas o detalhamento estrutural.
