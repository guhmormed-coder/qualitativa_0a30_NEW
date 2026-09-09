# Regras de Limpeza — V3 em Camadas (Regex + Substituições + Densidade)

V3 (2026-09): regras recalibradas com evidências de 2026. O vocabulário é pontuado por **densidade por parágrafo**, não excluído por palavra. Travessões têm **teto**, não são banidos. Ritmo forçado é um indício, não uma correção. Veja o SKILL.md para a filosofia dos níveis e `tier-rationale.md` §V3 para as evidências.

## Conteúdo

- Pontuação por densidade (como cada regra de vocabulário é aplicada)
- NÍVEL: FORENSIC (sempre ativo)
- NÍVEL: STRICT (ativo por padrão)
- NÍVEL: AESTHETIC (apenas opcional)
- Passo 2 - Restauração de ritmo (todos os níveis)
- Passo 3 - Inserções proibidas (marcadores de sinceridade, hedges)
- Detecção de abertura / fechamento clichê (nível strict)
- Preserve isto (voz do usuário, não limpe)
- Limpeza de resposta a comentário (ao responder comentaristas no seu próprio post)
- Limpeza de abertura de anúncio (nível strict)

---

## Pontuação por densidade (como cada regra de vocabulário é aplicada)

O princípio do agrupamento: leitores especializados identificam texto de IA por agrupamentos de marcadores, não por uma única palavra. Um "notably" em um parágrafo é inglês comum. "Notably", "comprehensive" e uma nominalização no mesmo parágrafo é uma assinatura.

```python
def score_paragraph(paragraph: str, markers: dict) -> dict:
    """Count marker hits per paragraph across all STRICT vocabulary, grammar,
    and LinkedIn-layer lists. Returns hits and the action to take."""
    hits = []
    for name, pattern in markers.items():
        for m in re.finditer(pattern, paragraph, flags=re.I):
            hits.append((name, m.group(0)))
    n = len(hits)
    always = [h for h in hits if h[0] in ("reveal_bridge", "neg_parallel", "sincerity_marker")]
    if n >= 3:
        action = "REWRITE_PARAGRAPH"     # 3+ markers = signal. Rewrite the whole paragraph, not word-by-word.
    elif always:
        action = "REPLACE"               # a reveal bridge / negative parallelism / sincerity marker is always scrubbed,
                                         # even when paired with one ordinary marker (checked BEFORE the density branch)
    elif n == 2:
        action = "REPLACE_WEAKEST"       # 2 ordinary markers = borderline. Replace the one doing least work, leave the other.
    else:
        action = "LEAVE"                 # a single common word is not a verdict
    return {"hits": hits, "count": n, "action": action}
```

Regras de aplicação:
- Pontue os marcadores forenses separadamente: uma ocorrência = exclui, sem limiar de densidade.
- Contagens no nível do post também importam para dois padrões: tríades (3+ por post = reduzir para uma) e fragmentos isolados (3+ por post = fundir de volta, veja o Passo 2).
- Nunca substitua uma palavra por um sinônimo da mesma lista. "Leverage" por "harness" não é uma correção.
- Ao reescrever um parágrafo, reescreva no registro do autor (confira `voice-fingerprint.md`), não em registro "neutro". Neutralidade em temperatura uniforme é, em si, uma assinatura.

---

## NÍVEL: FORENSIC (sempre ativo)

Vazamento real de modelo. Nenhum escritor humano jamais produz isso. Todo detector concorda. Não existe defesa.

### Marcadores de ferramenta de IA (excluir por completo + sinalizar)

```python
FORENSIC_MARKERS = [
    r"\boaicite\b",                          # ChatGPT internal citation token
    r"\bcontentReference\b",                 # ChatGPT artifact
    r"\bturn\d+search\d+\b",                 # OpenAI tool call leakage (turn0search0 etc)
    r"\battached_file\b",                    # Claude/GPT file ref
    r"\bgrok_card\b",                        # Grok artifact
    r"\boai_citation\b",                     # OpenAI citation marker
    r"\bcontentReference\[\^\d+\]",          # numbered citation refs
]
```

### Avisos de corte de conhecimento (excluir a frase)

```python
CUTOFF_DISCLAIMERS = [
    r"As of my (last update|knowledge cutoff|training cutoff)[^.]*\.",
    r"As of (January|June|October|November) 202\d[^.]*\.",
    r"Based on (information|data) (available|up to) [^.]*\.",
    r"My (knowledge|training data) (cuts off|extends to) [^.]*\.",
    r"I cannot provide (real-time|current|up-to-date) [^.]*\.",
]
```

### Templates fraseológicos (sinalizar para o usuário preencher, NÃO preencher automaticamente)

```python
PHRASAL_TEMPLATES = [
    r"\[Your Name\]",
    r"\[Your Company\]",
    r"\[Describe [^]]+\]",
    r"\[Insert [^]]+\]",
    r"202\d-XX-XX",                          # date placeholder
    r"\[NAME\]|\[DATE\]|\[TOPIC\]",
    r"Mad[\- ]Libs",                         # any literal mention
]
```

### DENSIDADE de travessão (teto: cerca de 1 a cada 100 palavras)

O caractere não é um indício. O GPT-5.4 emite 1,43 travessões a cada 1.000 palavras, abaixo da referência humana de 3,23; 29% das legendas humanas do Instagram e 23% dos posts de top creators no LinkedIn no nosso corpus usam um (razão relativa ao autor de 1,09, ou seja, não é um indício confiável no LinkedIn). Zero travessões em um post que pedia um é o indício de alguém tentando parecer humano. O que ainda é forense é o antigo hábito de "cola" do GPT-4: 3+ em um post curto.

```python
def em_dash_excess(text: str) -> int:
    """Return how many em dashes exceed the cap (~1 per 100 words, floor 1, ceiling 2 per post).
    0 = leave every em dash alone."""
    words = len(text.split())
    em = text.count("—")
    cap = max(1, min(2, round(words / 100)))
    return max(0, em - cap)

# Replacement order for the EXCESS ones (keep the one doing the most work, usually the first):
#   1. comma            if the dash joins a clause to the main sentence
#   2. colon            if the dash introduces a reveal, a list, or a consequence
#   3. parentheses      if the dash pair wraps an aside
#   4. rewrite          if none of the above reads naturally
# NEVER a period. "X. Y." from a split dash creates fragment stacking, which is a worse tell than the dash.
```

### Fechamentos em fórmula de outline (sinalizar)

```python
OUTLINE_CLOSERS = [
    r"Despite (its|the) [^,]+, faces (challenges|obstacles)[^.]*\.",
    r"Looking ahead, [^.]+ (will|must|should)[^.]*\.",
    r"In conclusion, [^.]+\.",
    r"To summarize,[^.]+\.",
    r"In summary,[^.]+\.",
]
```

---

## NÍVEL: STRICT (ativo por padrão)

O que leitores humanos especializados citam quando identificam texto de IA (vocabulário 53%, estrutura de frase 36%) e o que o filtro de slop do LinkedIn percebe. Todas as listas de vocabulário e gramática abaixo passam por `score_paragraph()`; pontes de revelação e paralelismo negativo são removidos em uma única ocorrência.

### Pontuação

```python
STRICT_PUNCT = [
    (r"“|”", '"'),                # curly quotes → straight
    (r"‘|’", "'"),                # curly apostrophes → straight (preserve apostrophe-in-contractions: don't / it's / you're)
    (r"\s*--\s*", ", "),          # double dash → comma (or rewrite). Not a period: a period here stacks fragments.
    (r"\s*–\s*", ", "),           # en dash between clauses → comma (number ranges stay literal e.g. 7-9)
]
# Em dashes are NOT in this list. They are handled by em_dash_excess() above: only the excess over
# ~1 per 100 words is replaced, and the replacement is comma / colon / parentheses / rewrite, never a period.
```

### Vocabulário: marcadores duráveis de 2026 (pontuados por densidade)

A lista de 2023-24 (delve, tapestry, realm) está em queda porque os humanos agora evitam essas palavras. Os marcadores duráveis são palavras comuns que os LLMs selecionam em excesso a uma taxa 2-5x maior que a humana entre GPT-5.5, Claude 4.8 e Gemini 3.1 (Kobak Sci Adv 2025; Wu et al 2026). São inglês comum, então um por parágrafo está bem. Três em um parágrafo é uma assinatura.

```python
STRICT_VOCAB_2026 = {
    # word / stem      : preferred replacement when the paragraph is over threshold
    "significant":      "<a number>",         # "significant growth" → "31% growth". Ask if no number exists.
    "crucial":          "<delete or 'the'>",  # "the crucial point is" → "the point is"
    "notably":          "",                   # delete + comma
    "particularly":     "",                   # delete
    "comprehensive":    "full",
    "insights?":        "<what was learned>", # "key insights" → say the thing
    "robust":           "solid",              # keep if it is a term of art (statistics, engineering)
    "leverag(e|es|ed|ing)": "use",
    "foster(s|ed|ing)?": "build",
    "landscape":        "field",
    "nuanced":          "specific",
    "multifaceted":     "<delete>",
    "holistic":         "full",
    "streamlin(e|es|ed|ing)": "simplify",
    "elevat(e|es|ed|ing)":    "improve",
    "empower(s|ed|ing)?":     "let",
    # older corporate verbs still worth counting (weaker signal, but readers still cite them)
    "utiliz(e|es|ed|ing)":    "use",
    "facilitat(e|es|ed|ing)": "help",
    "harness(es|ed|ing)?":    "use",
    "unlock(s|ed|ing)?":      "find",
    "navigat(e|es|ed|ing)":   "handle",
    "seamless":               "smooth",
    "ecosystem":              "space",
}

STRICT_ADVERB_FILLER = {
    # counted as markers; delete whole word + surrounding comma when the paragraph is over threshold
    "fundamentally", "essentially", "ultimately", "crucially", "notably",
    "arguably", "certainly", "definitely", "undoubtedly", "particularly",
}
```

### Marcadores gramaticais (pontuados por densidade; a assinatura estrutural de 2026)

```python
GRAMMAR_MARKERS = {
    # Present-participial clause openers: 5.3x human rate (PNAS 2025).
    # "Leveraging our data, we..." / "Building on this, ..." / "Recognizing that X, ..."
    "ing_opener": r"(?m)^[\s>*\-]*[A-Z][a-z]+ing\b[^.]{0,60},",
    # Nominalisations: verb-turned-noun that hides the actor.
    # "the implementation of" / "the utilization of" / "the optimization of"
    "nominalisation": r"\bthe (\w+(?:tion|sion|ment|ance|ence|ization|isation)) of\b",
    # Stacked abstract nouns
    "abstract_stack": r"\b(alignment|transformation|optimization|innovation|efficiency|scalability|synergy)\b.{0,40}\b(alignment|transformation|optimization|innovation|efficiency|scalability|synergy)\b",
}
# Fix for ing_opener: put the actor first. "Leveraging our data, we cut churn" → "We cut churn with our data."
# Fix for nominalisation: use the verb. "the implementation of the new flow" → "when we implemented the new flow"
```

### Camada 2026 do LinkedIn (pontuada por densidade)

Palavras e frases que eram gíria humana de LinkedIn em 2024 e são gíria de modelo em 2026. Cada uma conta como um marcador; as frases no segundo bloco são removidas em uma única ocorrência porque também são negativas para alcance.

```python
LINKEDIN_LAYER_2026 = [
    r"\bquietly\b",                          # "quietly shipped", "quietly became"
    r"\b\w+ matters\b\.?",                   # "distribution matters." as a sentence
    r"\bcompound(s|ing)?\b",                 # "small wins compound"
    r"\ba signal\b|\bthe signal\b",
    r"\bthe work\b",                         # "do the work", "the work is the work"
    r"\bbuilt different\b",
    r"\bload-bearing\b",
    r"\bdoing the heavy lifting\b",
    r"\blet that sink in\b",
    r"\bthat's the real story\b",
]
```

### Pontes de revelação (uma ocorrência = substituir; medidas como negativas para alcance no LinkedIn)

```python
REVEAL_BRIDGES = [
    (r"(?m)^The (result|outcome|answer|lesson|catch|kicker|truth)\?\s*", ""),   # "The result?" -4.8% reach
    (r"(?i)\bit'?s not \w[^,.]{0,40}, it'?s \b", None),                          # "It's not X, it's Y" -4.9%; rewrite as paired declaratives
    (r"(?i)^stop \w[^,.]{0,40}\. start \b|^stop \w[^,.]{0,40}, start \b", None),  # "Stop X, start Y" -6.7%
    (r"(?im)^here'?s (what|how|why|the thing)\b[^:.\n]{0,40}[:.]\s*", ""),      # "Here's what/how" -4.3%
    (r"(?im)^(plot twist|spoiler|the twist)[:?]\s*", ""),
]
# Vendor data (single platform, 2026). Confidence: vendor. The direction is consistent with reader-tell reports.
# Fix: delete the bridge and let the next sentence stand. It was the point anyway.
```

### Paralelismo negativo (cobertura total conforme banimento de 2026-04-27; agora também -4,9% de alcance)

```python
NEG_PARALLEL_PATTERNS = [
    # All forms must be rewritten as paired declaratives
    r"It's not just (\w+(?:\s+\w+){0,5}), it's (\w+(?:\s+\w+){0,5})",
    r"(\w+(?:\s+\w+){0,3}) isn't (\w+(?:\s+\w+){0,5}), it's (\w+(?:\s+\w+){0,5})",
    r"Not (\w+(?:\s+\w+){0,5}), but (\w+(?:\s+\w+){0,5})",
    r"It's not about (\w+(?:\s+\w+){0,5}), it's about (\w+(?:\s+\w+){0,5})",
    r"The question isn't (\w+(?:\s+\w+){0,5}), it's (\w+(?:\s+\w+){0,5})",
    r"This isn't (\w+(?:\s+\w+){0,5})\. This is (\w+(?:\s+\w+){0,5})",
    r"The real (\w+) isn't (\w+(?:\s+\w+){0,5}), it's (\w+(?:\s+\w+){0,5})",
]

# Replacement strategy: rewrite as paired declaratives, NOT as auto-substitution.
# Example:
#   "the bet isn't unit economics, it's owning distribution"
#   → "nobody's playing for unit economics. they're playing to own distribution."
# Always flag for user review since meaning preservation needs human judgment.
```

### Regra do três (strict em densidade; uma tríade natural é permitida)

Sequências de tricolon ocorrem a 2x a densidade de especialistas humanos entre os modelos de fronteira de 2026 (arXiv 2604.19768). O indício é a tríade empilhada ou perfeitamente paralela e a repetição, não a forma: 26% dos top tweets humanos contêm exatamente uma.

```python
def detect_triads(text: str) -> list:
    patterns = [
        r"(\w+), (\w+),? and (\w+)",                       # word triplets
        r"(\w+ \w+), (\w+ \w+),? and (\w+ \w+)",           # short-phrase triplets
        r"(?m)^(\w+)\. (\w+)\. (\w+)\.$",                  # "Simple. Effective. Easy." (also a Pass 2 staccato hit)
        r"\b(no \w+)[,.] (no \w+)[,.] (just|only) \w+",    # "No X. No Y. Just Z." (also a Pass 2 hit)
    ]
    return [m for p in patterns for m in re.finditer(p, text, flags=re.I)]

def triad_action(triads: list, text: str) -> list:
    """STRICT: scrub any triad whose three items are interchangeable or perfectly parallel
    (same part of speech, same length, no receipts), and every triad beyond the second in a post.
    Leave ONE natural triad with concrete, non-interchangeable items.
    AESTHETIC: scrub the last remaining one too."""
    actions = []
    for i, t in enumerate(triads):
        items = t.groups()
        parallel = len(set(len(x.split()) for x in items)) == 1
        hollow = all(x.lower() in HOLLOW_ADJECTIVES for x in items) if len(items) == 3 else False
        if parallel or hollow or i >= 2:
            actions.append((t, "REWRITE_AS_TWO_OR_FOUR"))   # 2 items, or 4 with one that breaks the pattern
        else:
            actions.append((t, "LEAVE"))
    return actions

HOLLOW_ADJECTIVES = {"dynamic", "vibrant", "innovative", "faster", "cheaper", "better", "simple",
                     "effective", "easy", "bold", "clear", "focused", "scalable", "powerful"}
```

### Limpeza no nível de frase

```python
STRICT_PHRASES = [
    (r"\bIn today's fast-paced world[,.]?\s*", ""),
    (r"\bin the age of AI[,.]?\s*", ""),
    (r"\bat the end of the day[,.]?\s*", ""),
    (r"\bgame-changer\b", "unusual"),
    (r"\bdeep dive\b", "look"),
    (r"\bneedle-moving\b", "real"),
    (r"\bmove the needle\b", "change the numbers"),
    (r"\bparadigm shift\b", "real shift"),
    (r"\bpivotal moment\b", "the moment"),
    (r"\btestament to\b", "shows"),
    (r"\btapestry of\b", "set of"),
    (r"\bin a world where\b", "when"),
    (r"\bthe (harsh|hard|uncomfortable) (truth|reality) is\b[:,]?\s*", ""),
]
```

---

## NÍVEL: AESTHETIC (apenas opcional)

Padrões que a IA usa mas que humanos também usam legitimamente, mais o vocabulário de 2023-24 que hoje está em queda e é majoritariamente inofensivo. Aplicar apenas quando o público exigir. Vai achatar escrita literária e vai disparar a proteção do Passo 4.

### Vocabulário aesthetic (conjunto em queda de 2023-24 + inglês normal defensável)

```python
AESTHETIC_VOCAB_REPLACE = {
    # Decaying 2023-24 markers. Humans now avoid them, so a single instance reads as human-ish.
    # Still counted as ONE marker each in score_paragraph() at strict; replaced outright only at aesthetic.
    "delve":       "look",
    "delving":     "looking",
    "tapestry":    "set",
    "realm":       "area",
    "intricate":   "complex",
    "intricacies": "details",
    "journey":     "<the actual thing: the year, the project, the 14 months>",
    "paradigm":    "approach",
    # Defendable normal English. Every epidemiologist, scientist, novelist uses these.
    "cultivate":   "grow",
    "vibrant":     "alive",                  # Toni Morrison Nobel lecture
    "garner":      "get",
    "showcase":    "show",
    "underscore":  "show",
    "highlight":   "show",                   # only when used as filler verb, not noun
    "bolster":     "back",
    "bolstered":   "backed",
    "meticulous":  "careful",
    "valuable":    "useful",
}
```

### Travessões (aesthetic: remove o último também)

```python
# Strict leaves ~1 per 100 words. Aesthetic removes the remaining one(s) for audiences that
# treat any dash as suspicious (some academic forums). Even here: comma / colon / parentheses,
# never a period. Know that zero dashes in a 300-word post is itself below the human baseline.
AESTHETIC_PUNCT_STRIP = [
    (r"\s*—\s*", ", "),
    (r"–", "-"),
]
```

### Regra do três (a última natural)

```python
# Strict leaves one natural triad per post. Aesthetic breaks it into 2 or 4 items.
# Defense: Lincoln, Caesar, Churchill. Apply only when the audience hunts for tells.
```

### Voz passiva

```python
# Defense: scientific writing, news leads, legal writing all require passive.
# Watson & Crick 1953 paper opens passive: "It has not escaped our notice..."
# Joan Didion: "The center was not holding."
PASSIVE_TARGETS = [
    r"was (\w+ed) by",
    r"is being (\w+ed)",
    r"has been (\w+ed)",
    r"will be (\w+ed)",
]
```

---

## Passo 2 — Restauração de ritmo (todos os níveis)

Substitui o `enforce_burstiness()` da V2. Detectores não pontuam burstiness (o GPTZero abandonou isso em 2023). No LinkedIn, a variância de comprimento de frase não é uma alavanca de engajamento em nenhum dos dois sentidos: nosso corpus normalizado por autor (palavra-chave n=205 + top creators n=192, 2026-09) mostra razões dentro do mesmo criador de 0,96 / 0,80 / 0,92 entre faixas de comprimento, Spearman -0,06, e uma leve vantagem de ritmo uniforme para posts de uma-ideia-por-linha entre 112-204 palavras. A descoberta anterior de X/Threads ("burstiness vence em posts longos") era um fator de confusão de autor e não se transfere. O que os leitores de fato percebem é a uniformidade mecânica (estrutura = 36% dos julgamentos de especialistas) e, pior, a variância encenada: alternância mecânica de longo/curto é uma assinatura reconhecível de humanizador (DAMAGE 2025). Então: corrija o ritmo apenas onde soar mecanicamente achatado, remova variância fabricada em todo lugar, nunca adicione variância como tática.

```python
STACCATO_TELLS = [
    r"(?m)^\w+\.$",                                              # one-word paragraph: "Still." "Mostly." "Exactly."
    r"(?m)^(\w+\. ){2,}\w+\.$",                                  # "Short. Punchy. Done." / "Simple. Effective. Easy."
    r"(?i)\bno \w+\. no \w+\. (just|only) \w+",                  # "No X. No Y. Just Z."
    r"(?i)\ball (of )?the \w+\. none of the \w+",                # "All the X. None of the Y."
    r"(?m)^The (result|outcome|answer|lesson|catch|kicker|truth)\?",  # "The result?" reveal (also strict reveal bridge)
    r"(?i)\b(why|how|what happened)\? (because|simple|easy)\b",  # pseudo-Socratic Q&A
    r"(?i)\b(that's it|that's all|that's the post|full stop|period)\.$",
]

def restore_rhythm(text: str) -> str:
    """V3. Remove staged variance; un-flatten only what reads machine-flat. Never manufacture variance."""
    paragraphs = split_paragraphs(text)
    fragments_seen = 0

    for i, p in enumerate(paragraphs):
        # 1. Kill staged rhythm first. Merge staccato runs into one full sentence with a real clause.
        for pat in STACCATO_TELLS:
            if re.search(pat, p):
                p = merge_into_sentence(p, pat)     # "No meetings. No decks. Just code." → "We skipped the meetings and the decks and shipped code."

        sents = split_sentences(p)
        lengths = [len(s.split()) for s in sents]

        # 2. Cap standalone fragments (<4 words) at 2 per POST, not per paragraph.
        for j, n in enumerate(lengths):
            if n < 4:
                fragments_seen += 1
                if fragments_seen > 2:
                    sents[j] = attach_to_neighbor(sents, j)   # fold into the previous sentence with a comma or colon

        # 3. Un-flatten ONLY a machine-flat paragraph: 4+ sentences, every one within ±3 words of the
        #    mean, no subordinate clause anywhere. Then extend the ONE sentence that carries the most
        #    content by joining it to its natural neighbour with a clause that does work (because / which /
        #    when / after), not a comma splice. Once per paragraph, and only if the result reads like the
        #    author. A paragraph with one long and one short sentence is already fine. Two or three
        #    mid-length sentences in a row are fine. This is not a reach tactic: on LinkedIn sentence-length
        #    variance is null-to-slightly-negative for engagement; the only goal is to not read machine-flat.
        if len(sents) >= 4 and all(abs(n - mean(lengths)) <= 3 for n in lengths) and not any(has_working_clause(s) for s in sents):
            k = argmax(lengths)
            sents[k] = join_with_clause(sents[k], sents[k + 1] if k + 1 < len(sents) else sents[k - 1])

        # 4. Never long/short/long/short across the post. If the paragraph now alternates, fold the
        #    second short sentence back in. The seesaw is the humanizer fingerprint.

        # 5. One-idea-per-line posts (112-204 words, each paragraph one sentence): leave rhythm alone entirely.
        #    Uniform rhythm has a mild advantage in that format on LinkedIn.

        paragraphs[i] = " ".join(sents)

    return "\n\n".join(paragraphs)
```

Layout vs ritmo: parágrafos de 1-2 frases com linhas em branco entre eles são o layout nativo para mobile do LinkedIn e **não** são tocados por este passo. Um parágrafo que é uma única frase completa de 22 palavras é layout. Um parágrafo que é "Ainda." é fragmento por dramaticidade. O passo edita frases, nunca as linhas em branco.

Nota sobre extensão: no LinkedIn nosso corpus mostra que a variância de comprimento de frase não é uma alavanca de engajamento (de nula a levemente negativa dentro do mesmo criador); a regra de "não force variância" das plataformas de formato curto se aplica em Threads e X curto. Aqui ela se aplica em qualquer extensão.

## Passo 3 — Inserções proibidas (marcadores de sinceridade, hedges)

O Passo 3 adiciona apenas concretude (um número de precisão incomum com referente, uma entidade nomeada, um fato datado e seco). Ele nunca adiciona o que segue, e o Passo 1 strict remove quando o rascunho já os tem como abertura ou pivô:

```python
SINCERITY_MARKERS = [
    r"(?im)^(let me be (honest|real|direct|clear)|i'?ll be (honest|real|direct)|honestly\?|honest (caveat|version|answer)|the honest (version|answer|truth) is|to be (direct|honest|fair|transparent)|real talk|full transparency|can i be (honest|vulnerable)|i'?ll say the quiet part|not gonna lie|ngl|unpopular opinion)[:,.]?\s*",
    r"(?i)\b(i (might|may|could) be wrong,? but|perhaps|it seems (to me )?that|in my humble opinion|i think it'?s fair to say)\b",  # inserted hedges: only scrub if NOT in the author's voice samples
]
# Fix: delete the marker and keep the sentence that follows. If the sentence that follows is not
# a specific fact, the marker was doing the work of vulnerability. Ask the author for the fact.
# Evidence: performed hesitancy 2x more common in LLM than expert human text; confession-cue humanizers
# caught 100% by expert readers; "false vulnerability" is a named 2026 tell (tropes.fyi).
# A flat dated uncomfortable fact with no frame is reach-POSITIVE (+4.6% to +10%, vendor data).
```

## Detecção de abertura / fechamento clichê (nível strict)

```python
OPENER_TELLS = [
    r"^In today's ",
    r"^Have you ever ",
    r"^Most people don't realize ",
    r"^Here's a hard truth",
    r"^Let me tell you about ",
    r"^Here's (what|how|why) ",               # reveal bridge as opener
    r"^(Stop|Quit) \w+ing\b.*\b(start|try)\b", # "Stop X, start Y"
]

CLOSER_TELLS = [
    r"What do you think\?",
    r"Thoughts\?",
    r"Agree or disagree\?",
    r"Let me know in the comments",
    r"Tag someone who needs this",
    r"Smash the like button",
    r"Let that sink in\.?$",
    r"That's the real story\.?$",
    r"(?m)^\w+\.$\Z",                         # one-word closing paragraph
]
```

## Preserve isto (voz do usuário, não limpe)

- Inícios de frase em minúsculas (assinatura do Serge)
- `..` como pausa suave (não travessão)
- Um ou dois fragmentos de frase usados intencionalmente ("Valeu a pena.", "Toda vez.") - o teto é 2 por post, não 0
- Um travessão a cada ~100 palavras. Não force a contagem a zero; zero está abaixo da referência humana
- Uma regra do três natural com itens concretos e não intercambiáveis
- Uma frase genuinamente longa por parágrafo, mesmo que um guia de estilo a dividisse
- Contrações (don't, it's, you're)
- Números específicos com referentes e entidades nomeadas (adicione MAIS, nunca remova)
- Detalhes sensoriais em primeira pessoa
- As reações e opiniões do autor, incluindo uma direta. Tom achatado ao longo de todo o post é uma assinatura de humanizador
- Um único marcador de palavra comum em um parágrafo ("notably", "robust" como termo técnico). Um não é um veredito

## Limpeza de resposta a comentário (ao responder comentaristas no seu próprio post)

**Respostas de autor proibidas** (sinalizam baixa qualidade, rebaixam a thread):

- "Ótimo ponto!"
- "Obrigado!"
- "100%"
- "Bem dito."
- "🙌"
- "Isso mesmo."

**Obrigatório:** toda resposta do autor deve conter ao menos um dos seguintes:
- Um novo detalhe concreto que não estava no post original
- Um nome específico (pessoa, empresa, ferramenta)
- Uma pergunta de acompanhamento que convide profundidade na thread

## Limpeza de abertura de anúncio (nível strict)

Substitua estes padrões pelo momento concreto que motivou o post:

- "Estou animado para anunciar" → descreva o que realmente aconteceu, em ordem
- "Estou empolgado para compartilhar" → apenas compartilhe, sem preâmbulo
- "Honrado por ser mencionado" → o que você fez para merecer a menção?
- "Encantado por ser destacado" → comece pelo insight, não pelo destaque
- "Deixa eu ser honesto" / "Vou ser real" → exclua o anúncio; declare o fato datado que vem depois, de forma seca
