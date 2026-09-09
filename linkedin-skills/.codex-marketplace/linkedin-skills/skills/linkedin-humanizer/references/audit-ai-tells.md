# Indícios de IA — Lista Negra Completa (V3, 2026-09)

Pontuado da forma como os leitores leem: por densidade por parágrafo, não por palavra. Um marcador em um parágrafo é apenas inglês (ou português) comum. Três é uma assinatura. As exceções que falham em uma única ocorrência estão listadas como tal.

## Conteúdo

- Pontuação (regex)
- Marcadores de vocabulário (pontuados por densidade)
- Lista negra de frases (ocorrência única)
- Indícios de linha de abertura
- Indícios de linha de fechamento
- Indícios estruturais
- Bloqueios de dos-and-donts de 2026 (falha automática)
- Orçamento de atenção
- Padrões regex (para implementação de auditoria)

## Pontuação (regex)

| Padrão | Motivo | Correção |
|---|---|---|
| `—` (travessão `—`) acima de ~1 a cada 100 palavras (1-2 por post) | Indício de densidade, não de caractere. O GPT-5.4 usa menos que humanos; 23% dos posts de top creators no LinkedIn no nosso corpus contêm um (razão relativa ao autor de 1,09, não é um indício). 3+ em um post curto é o antigo hábito de "cola" do GPT-4 | Substitua apenas o excesso: `,` ou `:` ou `( )` ou uma reescrita. Nunca `.` (empilhar fragmentos é pior) |
| `—` em zero ao longo de um post de 300+ palavras que soa como se quisesse um | Abaixo da referência humana; soa como autocensura do travessão | Deixe um |
| `–` (meia-risca `–`) entre orações | Mesma família | Substitua por `,`; intervalos numéricos permanecem |
| `--` | Mesma família | Substitua por `,` ou reescreva |
| `“”` (aspas curvas) | Artefato de copiar e colar | Converta para `"` |

## Marcadores de vocabulário (pontuados por densidade)

Conte por parágrafo. **3+ = reescreva o parágrafo. 2 = substitua o mais fraco. 1 = deixe.** O vocabulário de IA é o único marcador consistentemente negativo para alcance no LinkedIn no nosso próprio corpus (0,74-0,84 relativo ao autor), então esse passo permanece mesmo com a lista de palavras tendo mudado.

**Conjunto durável de 2026 (palavras comuns, taxa 2-5x humana entre GPT-5.5 / Claude 4.8 / Gemini 3.1):** significant, crucial, notably, particularly, comprehensive, insights, robust, leverage, foster, landscape, nuanced, multifaceted, holistic, streamline, elevate, empower

**Verbos corporativos mais antigos (sinal mais fraco, mas ainda citados pelos leitores):** utilize, facilitate, harness, unlock, navigate, seamless, ecosystem

**Advérbios de preenchimento:** fundamentally, essentially, ultimately, crucially, notably, particularly

**Marcadores gramaticais:** oração de abertura em "-ing" ("Leveraging our data, we..."), nominalização ("the implementation of"), substantivos abstratos empilhados (alignment / transformation / optimization / synergy)

**Camada 2026 do LinkedIn:** quietly, "X matters." como frase, compound(s), "a signal", "the work", "built different", load-bearing, "doing the heavy lifting", "let that sink in", "that's the real story"

**Conjunto em queda de 2023-24 (conte como um marcador cada, mas não persiga isoladamente):** delve, tapestry, realm, intricate, journey, paradigm, cultivate

## Lista negra de frases (uma ocorrência = corrigir)

Pontes de revelação e paralelismo negativo são removidos em uma única ocorrência porque são negativos para alcance no LinkedIn (dados de fornecedor, 2026):

- "The result?" / "The catch?" / "The kicker?" (-4,8%)
- "It's not just X, it's Y" e todas as 6 formas de paralelismo negativo (-4,9%)
- "Stop X, start Y" (-6,7%)
- "Here's what / Here's how / Here's the thing" (-4,3%)
- "In today's fast-paced world"
- "Game-changer"
- "Deep dive"
- "Needle-moving"
- "Move the needle"
- "At the end of the day"
- "When it comes to"
- "In the age of AI"
- "Paradigm shift"
- "The hard truth is" / "The uncomfortable reality is"
- Anúncios de sinceridade como abertura ou pivô: "let me be honest", "I'll be real", "honestly?", "to be direct", "the honest version is", "honest caveat", "real talk", "full transparency", "unpopular opinion:"

## Indícios de linha de abertura

- Qualquer frase começando com "In today's..."
- Ganchos de pergunta retórica ("Have you ever wondered...?") — mortos no LinkedIn
- Primeira linha toda em maiúsculas ("THIS CHANGED EVERYTHING.")
- "Most people don't realize..."
- "Here's a hard truth..."

## Indícios de linha de fechamento

- "What do you think?"
- "Thoughts?"
- "Agree or disagree?"
- "Let me know in the comments!"
- "Tag someone who needs this."

## Indícios estruturais

- Toda frase com o mesmo comprimento, mecanicamente achatada (leitores especializados citam estrutura 36% das vezes). Corrija apenas onde soar achatado; no LinkedIn a variância de comprimento de frase não é uma alavanca de alcance em nenhum dos sentidos (nosso corpus, dentro do mesmo criador: de nulo a levemente negativo), então nunca fabrique isso
- Empilhamentos staccato: "Short. Punchy. Done.", "Simple. Effective. Easy.", "No X. No Y. Just Z.", "All the X. None of the Y."
- Parágrafos de uma única palavra ("Still." "Mostly." "Exactly.")
- Mais de 2 fragmentos isolados (<4 palavras) no post
- Vaivém longo/curto/longo/curto ao longo do post inteiro (alternância mecânica é assinatura de humanizador)
- Pseudo-diálogo socrático ("Why? Because...")
- Todo parágrafo com 3 linhas
- Estrutura paralela perfeita em uma lista
- Tríades empilhadas ou perfeitamente paralelas, ou 3+ tríades em um post ("faster, cheaper, better"). Uma tríade natural está tudo bem
- Empilhamentos de hedge: "perhaps", "might", "could potentially", "it seems" (hesitação encenada corre a 2x a taxa humana)
- Confissão emoldurada: uma frase de sinceridade envolvendo um fato ("I'll be honest, this hurt: we lost the client"). O fato sozinho está tudo bem
- Voz passiva >10% das orações
- Tom uniformemente achatado sem reação, sem opinião, sem detalhe concreto (a assinatura da limpeza excessiva)

## Bloqueios de dos-and-donts de 2026 (falha automática)

| Padrão | Motivo | Correção |
|---|---|---|
| Link externo no corpo do post | Penalidade de -40 a -60% no alcance; o LinkedIn suprime tráfego para fora da plataforma | Mova o link para o primeiro comentário, ou resuma o insight no próprio texto |
| "Comment YES if you agree" / "Drop a 🙌" / CTA fabricado | O algoritmo detecta e rebaixa explicitamente isca de engajamento | Faça uma pergunta aberta e específica ligada à tese do post |
| Tom de release de imprensa / polido demais no estilo corporativo | Tem desempenho 3x pior que voz pessoal; suprime sinais de autenticidade | Reescreva em primeira pessoa com um momento concreto |
| Abertura de humble-brag ("honored to announce…") | Fracassos superam humble brags em **8,5x** | Comece pelo que quebrou ou pelo que você aprendeu |
| Edições significativas na primeira hora após publicar | Reseta o teste inicial de distribuição do algoritmo | Corrija apenas erros de digitação nos primeiros 60 min; segure edições estruturais |
| Posts >3x/semana de um mesmo autor | Retornos decrescentes; canibaliza o próprio alcance | Limite a 2-3x/semana, mesmo horário/dias |
| Distribuição apenas via página da empresa | Posts de funcionários têm 6-8x mais alcance que páginas de empresa | Publique pelo perfil pessoal, deixe a empresa republicar |
| Perseguição pura de métrica de vaidade (só curtidas) | Curtidas são o sinal mais fraco; salvamentos > comentários > compartilhamentos > curtidas | Projete para salvamentos: frameworks, templates, dados |
| Aberturas de anúncio ("I'm excited to share") | Soa como assessoria de imprensa; mata a voz | Substitua pelo momento concreto que motivou o post |

## Orçamento de atenção

A atenção média de tela do usuário é de **47 segundos** (caindo de 150 segundos em 2004). Meta de tempo de permanência no post: 31-60 segundos.

Sinalize qualquer rascunho que exija mais de 60s de leitura contínua sem uma quebra visual, lista ou frase fragmentada — ele vai perder a camada de leitura rápida (skim).

## Padrões regex (para implementação de auditoria)

```python
import re

# Verb stems that should match every inflection (-s, -ing, -ed, -es).
# Use a non-capturing inflection suffix so "harnessed", "fostering", "unlocks" all match.
_VERB_STEMS = (
    "leverag", "utiliz", "facilitat", "streamlin", "delv", "navigat",
    "unlock", "harness", "foster", "cultivat", "elevat", "empower",
)
_VERB_GROUP = "|".join(_VERB_STEMS)

# DENSITY-SCORED markers: count hits per paragraph. 3+ = rewrite paragraph, 2 = replace weakest, 1 = leave.
DENSITY_PATTERNS = {
    "vocab_verbs": rf"\b(?:{_VERB_GROUP})(?:e|es|ed|ing|s)?\b",
    "vocab_2026": r"(?i)\b(significant(ly)?|crucial(ly)?|notably|particularly|comprehensive|insights?|robust|landscape|nuanced|multifaceted|holistic|seamless|ecosystem)\b",
    "adverb_filler": r"(?i)\b(fundamentally|essentially|ultimately|arguably|certainly|definitely|undoubtedly)\b",
    "ing_opener": r"(?m)^[\s>*\-]*[A-Z][a-z]+ing\b[^.\n]{0,60},",
    "nominalisation": r"(?i)\bthe \w+(?:tion|sion|ment|ance|ence|ization|isation) of\b",
    "linkedin_2026": r"(?i)\b(quietly|compound(s|ing)?|(a|the) signal|the work|built different|load-bearing|doing the heavy lifting)\b|(?m)^\w+ matters\.$",
    "decaying_2024": r"(?i)\b(delve|delving|tapestry|realm|intricate|journey|paradigm)\b",
}

# SINGLE-HIT patterns: one match = fix.
AI_PATTERNS = {
    "en_dash": r"–",
    "double_dash": r"--",
    # Reveal bridges (reach-negative on LinkedIn).
    "reveal_bridge": r"(?im)^(the (result|outcome|answer|lesson|catch|kicker|truth)\?|here'?s (what|how|why|the thing)\b|stop \w+[^.\n]{0,40}[.,] ?start \b|plot twist:)",
    "inflated_symbolism": r"(?i)not just \w+, it'?s \w+",
    "neg_parallel": r"(?i)\b(isn'?t|not) (about )?[^,.\n]{1,40}, it'?s (about )?\b",
    # Staccato / forced rhythm.
    "staccato_stack": r"(?m)^(\w+\. ){2,}\w+\.$",
    "one_word_paragraph": r"(?m)^\w+\.$",
    "no_no_just": r"(?i)\bno \w+\. no \w+\. (just|only) \w+",
    "all_none": r"(?i)\ball (of )?the \w+\. none of the \w+",
    "pseudo_socratic": r"(?i)\b(why|how)\? (because|simple)\b",
    # Sincerity announcements as opener or pivot.
    "sincerity_marker": r"(?im)^[\s>*\-]*(let me be (honest|real|direct|clear)|i'?ll be (honest|real|direct)|honestly\?|honest (caveat|version|answer)|the honest (version|answer|truth) is|to be (direct|honest|transparent)|real talk|full transparency|can i be (honest|vulnerable)|not gonna lie|ngl|unpopular opinion)\b",
    # Case-insensitive opener match; allow leading whitespace, bullets, or quote marks.
    "opener_filler": r"(?im)^[\s>*\-]*[\"'“]?(In today's|Have you ever|Most people don't realize|Here's a hard truth)",
    # Generic closing-question CTA: matches "What do you think?" / "What are your thoughts?" / "Thoughts?" / "Your take?" etc.
    "closer_filler": r"(?i)(what (do|are) you (think|your? thought)|what(?:'s| is) your (take|thoughts?)|thoughts\?|agree or disagree\?|let me know in the comments|tag someone|let that sink in|that'?s the real story)",
}

def em_dash_excess(text: str) -> int:
    """Em dashes above the cap (~1 per 100 words, floor 1, ceiling 2 per post). 0 = fine."""
    words = len(text.split())
    cap = max(1, min(2, round(words / 100)))
    return max(0, text.count("—") - cap)

def fragment_count(text: str) -> int:
    """Standalone sentences under 4 words. More than 2 per post = forced rhythm."""
    return sum(1 for s in re.split(r"(?<=[.!?])\s+", text) if 0 < len(s.split()) < 4)

def paragraph_density(paragraph: str) -> int:
    return sum(len(re.findall(p, paragraph)) for p in DENSITY_PATTERNS.values())

# Compile-time sanity: catches inflected and conjugated forms.
assert re.search(DENSITY_PATTERNS["vocab_verbs"], "We harnessed cross-functional synergy.")
assert re.search(DENSITY_PATTERNS["vocab_verbs"], "We fostered alignment.")
assert re.search(DENSITY_PATTERNS["vocab_verbs"], "We unlocked 47% gains.")
assert re.search(DENSITY_PATTERNS["ing_opener"], "Leveraging our data, we cut churn.")
assert re.search(AI_PATTERNS["closer_filler"], "What are your thoughts?")
assert re.search(AI_PATTERNS["closer_filler"], "What's your take?")
assert re.search(AI_PATTERNS["reveal_bridge"], "The result? We doubled.")
assert re.search(AI_PATTERNS["no_no_just"], "No meetings. No decks. Just code.")
assert re.search(AI_PATTERNS["sincerity_marker"], "Let me be honest: this one hurt.")
assert em_dash_excess("a — b " * 3 + "word " * 90) == 2
assert em_dash_excess("one — dash in " + "word " * 120) == 0
```
