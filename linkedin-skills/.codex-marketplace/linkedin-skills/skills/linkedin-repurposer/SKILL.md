---
name: linkedin-repurposer
description: 'Reaproveita conteúdo já existente em um post nativo para o LinkedIn. Pega um tweet, thread, vídeo do YouTube, blog ou newsletter e reconstrói para o LinkedIn: refaz o gancho antes do corte, expande para o ponto ideal de 900 a 1300 caracteres, adiciona espaçamento em branco e um CTA, move links para o primeiro comentário, roda o humanizer, publica via Publora após aprovação. Não é para escrever do zero (use linkedin-post-writer), nem para auditar um rascunho (use linkedin-humanizer --mode audit).'
---

# LinkedIn Repurposer

Transforme algo que você já criou em um post que soa como se tivesse sido escrito para o LinkedIn. Reaproveitar não é copiar e colar. Um tweet que bombou no X vai fracassar se colado direto no LinkedIn: curto demais, sem espaçamento em branco, ritmo errado, e um link no corpo que derruba seu alcance.

Este skill transforma, não gera. Ele lê a sua fonte, mantém a ideia, e reconstrói a entrega para o algoritmo de 2026 do LinkedIn.

## Quando usar

- "Transforme esse tweet / thread em um post do LinkedIn"
- "Reaproveite meu vídeo do YouTube / blog / newsletter para o LinkedIn"
- "Isso funcionou no Threads, adapte para o LinkedIn"
- "Tenho uma ideia bruta em outro formato, torne-a nativa aqui"

Não é para um rascunho em página em branco (use `linkedin-post-writer`) e não é para revisar um rascunho de LinkedIn já pronto (use `linkedin-humanizer --mode audit`).

## Como funciona

**Perfil de voz primeiro (todos os rascunhos).** Se `../../references/voice-profile.md` tiver `filled: yes`, carregue-o e siga a impressão digital de voz do usuário, as regras rígidas, e o estilo de CTA/link ao longo de todo o processo. Se não estiver preenchido, mencione uma vez que `linkedin-humanizer --mode profile` pode aprender a voz do usuário a partir de alguns posts, e então prossiga com as regras de voz genéricas.

1. **Pegue a fonte.** Qualquer formato: um tweet ou thread, um vídeo ou roteiro, um parágrafo de blog, uma legenda, uma transcrição, uma lista com marcadores, um link para leitura. Pergunte pela fonte e pelo objetivo (comentários / compartilhamentos / curtidas / salvamentos) se não for informado.
2. **Extraia a espinha dorsal.** Retire a casca da plataforma de origem e puxe a única afirmação, história ou número que vale a pena manter. O reaproveitamento fracassa quando mantém as palavras em vez do ponto principal.
3. **Refaça o gancho para o LinkedIn.** O gancho precisa aterrissar nos primeiros 210 caracteres, antes do corte "...ver mais". O gancho da fonte raramente sobrevive; escreva uma nova primeira linha usando uma das 16 fórmulas em `../../references/hook-formulas.md`, escolhida de acordo com o objetivo.
4. **Expanda para o comprimento do LinkedIn.** O X comprime; o LinkedIn respira. Faça a espinha dorsal crescer até o ponto ideal de 900 a 1300 caracteres: parágrafos curtos, quebras de linha duplas entre ideias, um detalhe concreto por momento. Um tweet denso vira 4 a 6 parágrafos curtos, não um bloco de texto.
5. **Adicione a forma do LinkedIn.** Espaçamento em branco entre ideias, um momento de risco real ou vulnerabilidade (posts de puro insight não engajam em 2026), e uma pergunta de fechamento clara ou CTA.
6. **Corrija links e artefatos.** Mova qualquer link externo para o primeiro comentário (links no corpo suprimem o alcance). Remova artefatos fora da plataforma: muros de hashtags, "link na bio", "aperte inscrever-se", @-handles do X, introduções do tipo "como eu tuitei". 0 a 2 hashtags no final.
7. **Passagem pelo humanizer.** Rode a limpeza: vocabulário de IA de 2026 por densidade, travessões acima do limite (cerca de um a cada 100 palavras), tríades empilhadas em regra-de-três, aberturas genéricas e pontes de revelação. Mantenha os números reais e as entidades nomeadas do usuário vindos da fonte.
8. **Cartão de aprovação.** Mostre: mapeamento fonte → LinkedIn (o que virou o quê), fórmula usada, contagem de caracteres, janela de publicação sugerida (Ter/Qua/Qui 7:30 às 9:00 da manhã no horário local), a observação sobre link-no-primeiro-comentário.
9. **Após a aprovação.** Publique via `lib.publish(kind="post", draft_text=<approved>, target_url="https://www.linkedin.com/post/new/", platforms=[{"platform":"linkedin","platformId":<id>}], scheduled_time=<iso_or_None>)`. O wrapper cuida do roteamento Publora / manual / diy.

## Regras de adequação nativa (fonte → LinkedIn)

- **Tweet → LinkedIn:** expanda, não cole. Um tweet é um gancho; faça o argumento crescer por baixo dele com espaçamento em branco.
- **Thread do X → LinkedIn:** desenrole em um único post fluido, não em uma lista numerada. Mantenha a melhor linha como o gancho.
- **Vídeo/roteiro do YouTube → LinkedIn:** lidere com a recompensa, depois conte a história de como você chegou lá. Coloque o link do vídeo no primeiro comentário.
- **Blog/newsletter → LinkedIn:** escolha a única afirmação mais citável como o gancho, depois a única história que a comprova. Não resuma a peça inteira.
- **Legenda do Instagram/TikTok → LinkedIn:** remova a densidade de emojis e os blocos de hashtags; adicione o risco profissional que o LinkedIn recompensa.

## Regras rígidas

Regras globais de voz: veja `SKILL.md` §Voice rules na raiz. Regras adicionais específicas deste skill:

- Mantenha a **afirmação e os fatos** da fonte intactos. Reaproveitar muda a entrega, nunca o significado ou os números.
- O gancho precisa aterrissar nos primeiros 210 caracteres, antes do corte.
- Nunca cole a fonte e apenas apare. Reconstrua o gancho, o comprimento e o ritmo a partir da espinha dorsal.
- Nenhum link externo no corpo do post. Ofereça colocá-lo no primeiro comentário.
- Inclua pelo menos um momento de risco real ou vulnerabilidade. Mantenha os números reais e as entidades nomeadas da fonte.
- Não mencione o produto do usuário como autopromoção. No máximo uma menção natural.

## Anti-padrões (o skill vai recusar)

- Copiar e colar a fonte com edições leves (isso não é reaproveitamento).
- Manter os artefatos da plataforma de origem ("link na bio", "aperte inscrever-se", muros de hashtags).
- Publicar um post do tamanho de um tweet sem espaçamento em branco ou expansão.
- Primeira linha toda em maiúsculas ("ISSO MUDOU TUDO").
- Travessões acima do limite (mais de cerca de um a cada 100 palavras), ou um travessão trocado por um ponto final.
- Listas de regra-de-três sem provas.
- "leverage" (alavancar), "fundamentalmente", "revolucionário" (game-changer), "mergulho profundo" (deep dive).
- Links externos no corpo.
- Introduções meta ("originalmente postei isso em...").

## Recursos

- `../../references/hook-formulas.md` - os 16 esqueletos de fórmula para refazer o gancho
- `../../references/algorithm-heuristics.md` - regras de publicação de 2026 (horário, formato, comprimento)

## Skills relacionados

- `linkedin-post-writer` - escreva um post novo do zero
- `linkedin-humanizer` - remova marcas de IA, além de `--mode audit` para revisar o resultado
- `linkedin-hook-extractor` - faça engenharia reversa de um gancho a partir de um post que você admira
