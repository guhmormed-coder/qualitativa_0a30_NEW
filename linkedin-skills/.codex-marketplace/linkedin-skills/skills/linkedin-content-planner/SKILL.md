---
name: linkedin-content-planner
description: Gera um plano de conteúdo de 7 dias para o LinkedIn a partir de um tema, público e pilares. Produz, por dia, o pilar do post, formato, tipo de gancho, CTA, horário de publicação, metas diárias de comentários, e uma checagem semanal de prontidão para inbound. Use quando o usuário quiser planejar uma semana ou um mês de conteúdo, não redigir um único post.
---

# LinkedIn Content Planner

Produza um plano de 7 dias para o LinkedIn construído em torno da disciplina dos 3 pilares (Autoridade 40-50%, Narrativa Pessoal 30-40%, Comunidade 20-30%). Opcionalmente adiciona um pilar de Produto/Oferta em 10-15%.

## Quando usar

- O usuário pede "planeje minha semana" ou "o que devo postar essa semana"
- O usuário quer sair da publicação ad-hoc e estabelecer um ritmo
- Antes de uma semana de lançamento (o usuário precisa de alinhamento com o pilar de produto)

## Entrada

- **Tema** (opcional): ex.: "agentes de IA em produção", "primeiros 6 meses da Co.Actor"
- **Descrição do público:** ex.: "fundadores B2B, líderes de operações de IA, VPs de marketing"
- **Mix de pilares** (opcional): padrão de 40% Autoridade / 30% Narrativa / 20% Comunidade / 10% Produto
- **Dias de publicação** (opcional): padrão de Ter/Qua/Qui/Sex (4 posts)
- **Amostras de voz** (opcional): caminhos para posts anteriores para calibração de voz

## Saída

Um plano em markdown com:

### Calendário de 7 dias

| Dia | Horário | Pilar | Formato | Fórmula de gancho | Ângulo em 1 linha | Tipo de CTA | Objetivo |
|---|---|---|---|---|---|---|---|
| Seg | — | (dia de comentários) | — | — | — | — | — |
| Ter | 8:00 no horário local | Autoridade | Texto | F7 Odd-Precision Money | "Quanto custam 3 meses de operação de agentes" | Fechamento com pergunta | Salvamentos |
| Qua | 9:30 no horário local | Narrativa | Texto | F4 Time-Anchor Confession | "Por que parei de publicar por 4 semanas" | Pergunta-espelho | Comentários |
| Qui | 8:00 no horário local | Comunidade | Texto | F14 Named Gratitude | "As 3 pessoas que moldaram nosso lançamento" | Marcação + agradecimento | Compartilhamentos |
| Sex | 9:00 no horário local | Narrativa | Texto | F11 Emotional Cold-Open | "A noite em que nosso primeiro deploy falhou" | Fechamento suave | Curtidas |
| Sáb/Dom | — | (sem post) | — | — | — | — | — |

A coluna Objetivo cobre salvamentos / comentários / compartilhamentos / curtidas ao longo dos quatro posts, satisfazendo a checagem de mix de objetivos abaixo.

### Metas diárias de comentários

Para cada dia de publicação:
- **3-5 criadores para engajar** (nomes ou arquétipos: "fundadores pares com 5-20 mil seguidores", "VCs com tese em IA", "CTOs de grandes empresas")
- **Padrão de comentário** a aplicar (primeiro-a-comentar, dados-primeiro, responder-a-pergunta-deles)
- **Meta de quantidade:** 10-20 comentários substantivos por dia

### Checagem semanal de prontidão para inbound

- [ ] Pelo menos 1 post de vulnerabilidade (Narrativa)
- [ ] Pelo menos 1 post de prova/dado (Autoridade)
- [ ] Pelo menos 1 post de oferta suave ou que gere CTA
- [ ] A estratégia de comentários inclui 70% pares, 20% aspiracionais, 10% prospects
- [ ] Nenhum pilar acima de 60% dos posts da semana
- [ ] Nenhuma fórmula duplicada duas vezes na mesma semana
- [ ] Distribuição de objetivos: nem todo post busca a mesma reação (ver Mix de objetivos abaixo)

## Regras

- **Mínimo de 3 pilares, máximo de 5.** Mais de 5 dilui o sinal.
- **3-5 posts por semana.** 6+ por semana dispara sinal de canibalização no 360Brew.
- **10-20 comentários/dia** em outros criadores. Comentários geram mais inbound do que posts.
- **Ter/Qua/Qui** são os melhores para B2B. Evite sexta após as 14h, sábado/domingo (corte de alcance de 30-50% no B2B).
- **Um formato por pilar por semana.** Não empilhe 3 posts de texto para Autoridade — varie.
- **Pilar Produto/Oferta com no máximo 1 post/semana.** O uso excessivo mata a confiança.

## Mapeamento fórmula → pilar

| Pilar | Fórmulas preferidas |
|---|---|
| Autoridade | F7 Odd-Precision Money, F10 Contrarian Historical, F8 Paid-vs-Free, F5 Self-Proving Meta, F15 Explain-to-Kids |
| Narrativa | F4 Time-Anchor Confession, F3 Year-over-Year Pivot, F9 Curiosity-Gap, F11 Emotional Cold-Open, F16 Status-Strip |
| Comunidade | F6 Comment-Gate (usar com moderação), F12 Permission Slip, F14 Named Gratitude, posts de enquete, menções em destaque |
| Produto/Oferta | F2 R.I.P. Obituary (ao pivotar de categoria), F1 Anaphora (ao enquadrar o produto como solução), F13 Bait-and-Switch (anúncios de upgrade) |

## Edição para fundadores (conjunto de pilares alternativo)

Quando o plano inteiro é para um **fundador** construindo confiança com investidores, contratações e parceiros de design, substitua o mix de pilares padrão pelo conjunto de fundadores de `../../references/founder-topics.md`. Ele mapeia cada pilar para **ângulos** de fundador (A1-A10) em vez de tópicos genéricos, e se apoia nas fórmulas estruturais F17-F20.

| Pilar | Participação | Ângulos de fundador | Fórmulas preferidas |
|---|---|---|---|
| **Convicção** (ponto de vista, categoria, filosofia de produto) | 30-40% | A1 Reprice, A7 Designed Serendipity, A8 Evasive-Sentence | F10, F18, F5 |
| **Construindo em público** (o trabalho real, sem glamour) | 30-40% | A5 Unglamorous Bet, A6 Limit of Delegation, A9 Delegation Line | F7, F4, F17 |
| **A matemática** (como um fundador realmente decide) | 15-20% | A4 Scarce-Shots, A10 Learning Gate | F10, F18, F20 |
| **Prova** (relacionamentos e vitórias, contados com moderação) | 10-15% | A2 Content-to-Pipeline, A3 Audience of One | F9, F11, F5 |

As mesmas salvaguardas se aplicam: 3-5 posts/semana, nenhum pilar acima de 60%, nenhuma fórmula repetida dentro de 7 dias, distribuir o objetivo ao longo da semana. Pergunte ao usuário "plano de fundador ou plano geral?" quando o público for um fundador construindo uma empresa, e use este conjunto por padrão se ele disser fundador.

## Mix de objetivos (equilibrar a semana, não só os pilares)

Cada fórmula gera uma reação primária: comentários, compartilhamentos, curtidas ou salvamentos (veja `../../references/hook-formulas.md` "Divisão de objetivo de engajamento"). Uma semana inteira só de isca-de-comentário ou só de isca-de-compartilhamento soa artificial e achata o alcance. Distribua os objetivos ao longo da semana:

| Objetivo | Fórmulas | Meta semanal |
|---|---|---|
| Comentários | F4, F10, F12, F9 | pelo menos 1 |
| Compartilhamentos | F14, F2, F8 | pelo menos 1 |
| Curtidas | F11, F13, F16 | pelo menos 1 |
| Salvamentos | F15, F7, F8 | pelo menos 1 |

## Passos

1. Coletar as entradas. Perguntar ao usuário sobre tema, público, preferências de pilares se não fornecidos.
2. Validar que o mix de pilares soma 100%; avisar se algum pilar passar de 60%.
3. Para cada dia de publicação, escolher:
   - Pilar (girar para corresponder ao mix)
   - Fórmula do banco daquele pilar (não repetir dentro de 7 dias)
   - Formato (alternando texto / carrossel / enquete conforme as regras de cada pilar)
   - Ângulo específico (o usuário fornece ou o skill gera)
   - Horário de publicação (considerando o fuso horário do público)
4. Para cada dia de publicação, adicionar 3-5 alvos de comentário com padrão sugerido.
5. Rodar a checagem de prontidão para inbound; sinalizar o que estiver faltando.
6. Retornar como markdown + JSON opcional para importação no Notion/Airtable.

## Exemplo

Veja `references/example-plan-week.md` para um plano de 7 dias resolvido.

## Arquivos

- `SKILL.md` — este arquivo
- `references/example-plan-week.md` — exemplo resolvido
- `references/pillars-framework.md` — a disciplina dos 3 pilares explicada
- `../../references/founder-topics.md` — biblioteca de ângulos da edição para fundadores (A1-A10) e conjunto de pilares de fundador

## Skills relacionados

- `linkedin-post-writer` — gere o rascunho de cada dia a partir do plano
- `linkedin-comment-drafter` — execute as metas diárias de comentários
- `linkedin-thread-monitor` — acompanhe o inbound gerado pela estratégia de comentários
- `linkedin-engager-analytics` — segmente o público em cada post
