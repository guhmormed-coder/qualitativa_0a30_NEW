# Explicador de Regras do LinkedIn

A base educacional do pacote humanizador. Toda regra em `linkedin-humanizer` veio de algum lugar — a taxonomia "Signs of AI writing" da Wikipedia, as heurísticas da OriginalityAI, a estilometria do GPTZero, ou padrões específicos de LinkedIn de 2026. Algumas são forenses de verdade (um marcador `[oaicite:0]` é indefensável). Algumas são banimentos de jargão corporativo que o usuário quer fora por questão de estilo. Algumas são exagero estético — padrões sobre os quais Lincoln, Dickinson e Didion construíram carreiras, agora sinalizados porque o GPT-4 também os usa.

Esta skill responde a uma pergunta simples: **para qualquer regra dada, o veredito de indício de IA é forensic, strict ou aesthetic — e quão forte é a defesa?**

## Quando usar

- Defender uma escolha estilística que um detector sinalizou ("mas a Emily Dickinson usa travessões")
- Argumentar o post polêmico sobre o exagero das regras de IA
- Auditar a saída do humanizador antes de aplicar uma reescrita
- Ensinar uma equipe quais regras são sinais reais vs. quais são só questão de gosto
- Revisar um falso positivo da OriginalityAI / GPTZero / Pangram

## Entrada

Uma das opções:
- O nome de uma regra específica ("travessões", "regra do três", "robust")
- Um trecho sinalizado por um detector
- Um pedido para percorrer a taxonomia completa

## Saída

Para cada regra:
- **A regra** (o que é sinalizado)
- **Nível** (forensic / strict / aesthetic)
- **Resumo em uma linha** (por que é sinalizada)
- **Escritor humano famoso** que usa esse padrão (com exemplo)
- **Força da defesa** (baixa / média / alta)
- **Citação** (quando disponível)

## Os três níveis

### Forensic — sinais reais de IA, indefensáveis

São vazamento do próprio modelo ou do template de prompt. Nenhum escritor humano os produz por acidente. Se o humanizador sinalizar um, aceite a reescrita.

Exemplos: marcadores `oaicite`, tokens `contentReference`, artefatos `turn0search0`, avisos de corte de conhecimento ("Até minha última atualização em janeiro de 2022..."), lacunas estilo Mad-Libs, templates fraseológicos com placeholders literais `[Your Name]`.

**Força da defesa: zero.** Citação: Wikipedia "Signs of AI writing".

### Strict — jargão corporativo, fácil de banir por questão de gosto

São padrões humanos reais, mas são padrões que o usuário explicitamente quer fora. A regra não é "isso prova que a IA escreveu" — é "eu acho essa voz barata e quero que suma". Defender esses padrões é possível, mas inútil dentro de uma voz de marca que já os rejeitou.

Exemplos: leverage / utilize / harness / delve / foster / cultivate, advérbios de preenchimento (fundamentally, essentially, ultimately), aberturas de preenchimento ("No mundo acelerado de hoje"), fechamentos clichê ("O que você acha?"), paralelismo negativo ("X não é Y, é Z").

**Força da defesa: média** (alguém poderia defender "leverage" como vocabulário de gestão dos anos 1980). **Força na voz de marca: zero** — o usuário os baniu.

### Aesthetic — exagero, defensável

São padrões sinalizados porque LLMs os usam, não porque sinalizam IA. Escritores humanos famosos construíram carreiras sobre eles. Detectores disparam em excesso sobre eles e produzem falsos positivos — veja Stanford HAI / Liang et al. (2023) mostrando que detectores são tendenciosos contra escritores não nativos de inglês, e o processo da Universidade Adelphi sobre uma acusação de falso positivo de IA.

Exemplos: um único travessão (Emily Dickinson, Cormac McCarthy), a regra do três (Lincoln, César, Churchill), voz passiva (Watson & Crick, Joan Didion, toda a escrita científica), a palavra "robust" (um século de epidemiologia e engenharia), aspas curvas (automáticas no Word/Pages, estilo de casa da New Yorker desde 1925).

**Força da defesa: alta.** Estas são as regras sobre as quais o post polêmico do Sergey se apoia.

## Regras inegociáveis

- Não confunda níveis. Um marcador `[oaicite]` e um único travessão não são o mesmo tipo de evidência.
- Ao defender, nomeie o escritor e dê o exemplo. "Lincoln" é mais fraco que "Lincoln, Discurso de Gettysburg, 1863: 'of the people, by the people, for the people'."
- Cite quando disponível. Stanford HAI e o desligamento do classificador da OpenAI são os comprovantes externos mais fortes.
- Não defenda uma regra que o usuário baniu pessoalmente (travessões na própria voz dele, mesmo que Dickinson os tenha usado). A voz de marca tem precedência sobre a defesa estética.

## Exemplo

> **Entrada:** "A OriginalityAI sinalizou meu post por usar 'robust' — devo reescrever?"
>
> **Saída:**
> Nível: aesthetic. A palavra "robust" é usada por epidemiologistas, engenheiros e estatísticos há mais de um século — tem um significado preciso ("insensível a violações de premissas") que nenhum sinônimo carrega. A OriginalityAI a sinaliza porque o GPT-4 a usa em excesso, não porque ela sinaliza IA. Força da defesa: alta.
>
> Recomendação: mantenha "robust" se você estiver descrevendo um modelo estatístico, uma arquitetura de sistema, ou uma resposta imune. Reescreva para "sólido" apenas se estiver usando como elogio genérico — esse é o exagero corporativo que o humanizador está de fato mirando.
>
> Citação: Wikipedia "Signs of AI writing" lista "robust" sob vocabulário de IA; Stanford HAI mostra que detectores disparam em excesso sobre inglês técnico.

## Arquivos

- `../references/rules-explainer.md` — tabela completa de todas as 15 regras organizadas por nível, com exemplos de escritores famosos e citações

## Skills relacionadas

- `linkedin-humanizer` — aplica as regras (esta skill as explica)
- `post-audit.md` (irmã) — sinaliza regras em um rascunho
- `detector-tester.md` (irmã) — roda OriginalityAI / GPTZero / Pangram contra rascunhos
