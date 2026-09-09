# Auditoria de Post do LinkedIn

Passa qualquer rascunho de post pelo checklist heurístico de 2026. Pega indícios de IA, problemas de timing/formato, violações de tamanho e fraquezas estruturais antes de publicar.

## Quando usar

- Antes de publicar um post escrito à mão ou rascunhado por IA
- Quando o `linkedin-post-writer` termina um rascunho (invocado automaticamente)
- Quando um post recente não decolou e o usuário quer um post-mortem

## Entrada

- Um rascunho de post (texto simples)
- Opcional: público-alvo, horário agendado, formato (texto / carrossel / vídeo / imagem)

## Saída

- Cabeçalho de **Aprovado/Reprovado**
- **Bloqueios** (precisam ser corrigidos antes de publicar): densidade de travessão acima do teto, parágrafos com 3+ marcadores de IA, pontes de revelação, links externos no corpo
- **Avisos** (arriscados para publicar): empilhamentos staccato, marcadores de sinceridade, números de referência ausentes, fechamento genérico
- **Estimativas de escore:** densidade de indício por parágrafo, ajuste aproximado de alcance na primeira hora. Sem escore de detector: em textos de 100-300 palavras eles são ruído e a skill não promete superá-los
- **Correções sugeridas:** reescritas inline para cada problema
- **Recomendação de timing:** melhor janela dado o público

## Checagens

### Bloqueios (falha automática)
1. Densidade de travessão acima de ~1 a cada 100 palavras (1-2 por post); meia-risca entre orações; travessão duplo. Um único travessão não é um bloqueio
2. Link externo no corpo (não no primeiro comentário)
3. Post excede 3.000 caracteres (limite rígido do LinkedIn)
4. Abre com "No mundo acelerado de hoje...", uma ponte de revelação ("Here's what", "Stop X, start Y"), ou um anúncio de sinceridade ("Deixa eu ser honesto")
5. Termina com "O que você acha?", "Pensamentos?", "Deixe isso te marcar."
6. Qualquer parágrafo com 3+ marcadores de vocabulário / gramática, ou qualquer ponte de revelação de paralelismo negativo / "E o resultado?" (veja `../references/audit-ai-tells.md`)
7. Enquadra o LinkedIn como inferior dentro de um post do LinkedIn (penalidade do algoritmo)

### Avisos (sinalizar com correção sugerida)
8. O gancho não cabe nos primeiros 210 caracteres (corte de "…ver mais" no mobile)
9. Tamanho fora do ponto ideal de 900-1.300 (ou 1.500-1.900 para formato longo com quebras)
10. Um parágrafo que soa mecanicamente achatado (4+ frases todas do mesmo tamanho, nenhuma oração cumprindo função). Sinalize apenas esse parágrafo; variância de comprimento de frase não é uma alavanca de alcance no LinkedIn, então nunca sugira adicionar variância como tática
11. Sem número de precisão incomum com referente nomeado (um número solto não resolve isso)
12. Sem entidade nomeada
13. Sem detalhe sensorial em primeira pessoa
14. Regra do três empilhada ou perfeitamente paralela, ou 3+ tríades no post (uma tríade natural passa)
15. Mais de 2 hashtags
16. O próprio produto do usuário citado mais de uma vez
17. Falta um momento que provoque reação: um fato específico, datado e desconfortável declarado de forma seca, ou uma opinião com risco envolvido. Uma confissão emoldurada ("vou ser honesto, isso doeu") não resolve isso; a moldura é o indício
18. Voz passiva >10%
18a. Empilhamentos staccato ("Curto. Direto. Pronto.", "Nada de X. Nada de Y. Só Z.", "Tudo de X. Nada de Y."), parágrafos de uma única palavra, mais de 2 fragmentos isolados, ou um vaivém longo/curto/longo/curto
18b. Empilhamento de hedge ou marcador de sinceridade no meio do post ("talvez", "parece que", "sinceramente?", "falando sério")
18c. Limpeza excessiva: tom uniformemente achatado, zero travessões e zero tríades em um post longo, nenhuma reação ou opinião em lugar nenhum
19. A primeira linha não é um gancho autônomo completo (precisa da linha 2 para fazer sentido). Corpus de 2026: todo top post carrega um gancho completo antes da dobra.
20. Sem linha em branco depois do gancho / abertura em bloco de texto. Os vencedores usam bastante espaço em branco: uma ideia por linha, linha em branco depois do gancho.
21. Emoji espalhado no meio do texto em um post narrativo, ou mais de 2-3 no total em prosa. Os top posts carregam 1-2 emojis significativos no início; posts sérios/contrarian usam zero. Isento: formatos estruturados de glossário/lista (ex.: F15 Explicar-para-Crianças) em que um emoji ancora cada linha de propósito.
22. Portão de comentário ("comente X e eu te mando DM...") em um post cujo objetivo é liderança de pensamento. Os top performers orgânicos usam zero portões de comentário rígidos; só sinalize claramente quando o objetivo do post for construção de lista (nesse caso o F6 é intencional).
23. Sem objetivo primário claro: o post persegue comentários, republicações, curtidas e salvamentos ao mesmo tempo. Escolha um (veja `../../../references/hook-formulas.md` "Engagement-goal split").

### Info (notas neutras)
24. Horário de publicação sugerido dado o público
25. Recomendação de formato (texto / carrossel / vídeo) dado o tema
26. Detecção de gancho similar: se os primeiros 100 caracteres deste post combinam com um post recente

## Passos

1. Divida o rascunho em frases, parágrafos, gancho dos primeiros 210 caracteres.
2. Rode cada checagem de bloqueio; colete as falhas.
3. Se houver bloqueios, retorne **REPROVADO** com sugestões de correção específicas; opcionalmente ofereça reescrita automática.
4. Se não houver bloqueios, rode os avisos.
5. Reporte a densidade de indício por parágrafo (marcadores por parágrafo, travessões por 100 palavras, contagem de fragmentos, contagem de tríades). Não estime um escore de detector.
6. Retorne o relatório estruturado.

## Exemplo

Veja `../references/audit-examples.md` para exemplos trabalhados.


## Skills relacionadas

- `linkedin-humanizer` — reescrita agressiva se a auditoria falhar
- `linkedin-post-writer` — regenerar rascunho usando uma fórmula comprovada
