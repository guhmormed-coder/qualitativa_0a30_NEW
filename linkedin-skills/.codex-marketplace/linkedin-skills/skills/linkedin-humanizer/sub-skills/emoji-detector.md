# Detector de Emoji do LinkedIn

Sinaliza o uso de emoji em padrão de IA em rascunhos do LinkedIn antes de irem ao ar. Construído com dados de frequência da MagicPost (fev 2026) mostrando que os emojis de lâmpada, foguete, brilhos e reciclagem aparecem 2-3x mais em posts do LinkedIn gerados por IA do que em posts escritos por humanos.

Dados de padrão da análise de LinkedIn da MagicPost (fev 2026, post viral com 220 de engajamento).

## Quando usar

- Antes de publicar qualquer post ou comentário rascunhado por IA
- Como um passo prévio ao `linkedin-humanizer` (pega um indício que o humanizador não corrige)
- Quando o passo de auditoria sinaliza "parece IA" sem um motivo específico
- Ao auditar um backlog de posts agendados em busca de emojis assinatura de IA

## Entrada

Qualquer texto do LinkedIn (post, comentário, resposta, DM). Opcional: flag de modo (`--strict`, `--lenient`, `--score`).

## Saída

- Escore de densidade de emoji de IA (0-100, quanto maior, mais parecido com IA)
- Lista de emojis sinalizados com frequência vs. referência de IA
- Alternativas sugeridas em padrão humano (ou recomendação de remoção)
- Veredito: "limpo", "limítrofe", "provável IA"

## Os três modos

### Modo 1 — SCAN (padrão)

Percorre o texto, extrai todo emoji, procura cada um na tabela de frequência em `../references/emoji-patterns.md`, e retorna um relatório por emoji.

Para cada emoji de padrão IA detectado:
- Mostra o emoji
- Mostra sua frequência de correlação com IA (ex.: lâmpada = 2,57%)
- Mostra a contagem no rascunho
- Sugere uma alternativa em padrão humano ou recomenda a exclusão

### Modo 2 — SCORE (`--score`)

Retorna um único número (0-100). Sem reescrita, sem sugestões.

Fórmula:
- Cada emoji de padrão IA contribui com `frequency_pct * count * 10`
- Teto de 100
- Bônus de +20 se 3+ emojis distintos de padrão IA estiverem presentes (sinal de agrupamento)
- Bônus de +15 se um único emoji aparecer 2+ vezes (indício de repetição)

Veredictos:
- 0-20: limpo
- 21-50: limítrofe
- 51-100: provável IA

### Modo 3 — SUGGEST

Retorna um conjunto de emoji reescrito. Mantém a contagem de emoji do post aproximadamente igual, mas troca emojis de padrão IA por alternativas menos correlacionadas, ou recomenda a remoção onde não há substituto limpo.

## Strict vs. lenient

### `--strict`

Sinaliza qualquer emoji de padrão IA, não importa quantos. Uma única lâmpada = veredito de provável IA. Use quando o conteúdo vai ao ar sob uma marca pessoal que nunca usou padrões de IA carregados de emoji.

### `--lenient`

Sinaliza apenas se 3+ emojis de padrão IA aparecerem no mesmo post, OU se um único emoji de padrão IA se repetir 2+ vezes. Use para contas em que emoji ocasional está tudo bem e só o padrão de agrupamento importa.

O modo padrão fica entre os dois: sinaliza se o escore for >20.

## Regras inegociáveis

- Nunca reescreva automaticamente sem mostrar o diff primeiro
- Preserve a paridade na contagem de emoji se o usuário quiser emojis (não remova tudo e deixe nada)
- Capitalize todos os nomes nas substituições sugeridas (HubSpot, Claude, etc.)
- Se o post tiver zero emojis, pule a skill inteiramente e retorne "n/a"
- Não invente frequências "humanas" de emoji — as alternativas em padrão humano em `../references/emoji-patterns.md` são emojis com correlação de IA abaixo de 1%, não emojis comprovadamente "mais humanos"

## Exemplo

> **Entrada:**
> "Empolgado para compartilhar nosso novo recurso 🚀 IA revolucionária ✨ Desbloqueie seu potencial 💡 Vamos lá 🔥"
>
> **Saída (modo padrão):**
> Escore: 78 / 100 — provável IA
>
> Sinalizados:
> - 🚀 foguete (3,28% de freq. em IA, 1 uso) → considere 📦 ou remover
> - ✨ brilhos (3,11% de freq. em IA, 1 uso) → remover, sem troca limpa
> - 💡 lâmpada (2,57% de freq. em IA, 1 uso) → 🪛 ou remover
> - 🔥 fogo (1,31% de freq. em IA, 1 uso) → manter ou trocar por 🌶️
>
> Bônus de agrupamento: +20 (4 emojis distintos de padrão IA)
>
> **Reescrita sugerida:**
> "Empolgado para compartilhar nosso novo recurso. Uma IA que realmente funciona. Experimente. 🌶️"

## Arquivos

- `SKILL.md` — este arquivo
- `../references/emoji-patterns.md` — tabela de frequência completa + alternativas em padrão humano

## Skills relacionadas

- `linkedin-humanizer` — roda depois do detector de emoji para limpar vocabulário e ritmo de IA
- `post-audit.md` (irmã) — checagem pré-publicação mais ampla (chama esta internamente)
- `linkedin-post-writer` — gera rascunhos que já evitam emojis de padrão IA
