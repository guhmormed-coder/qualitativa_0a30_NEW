---
name: linkedin-post-writer
description: Cria uma nova publicação do LinkedIn do zero usando uma das 20 fórmulas de hook de 2026 (anáfora, R.I.P., âncora temporal, gap de curiosidade, contrarian, A/B controlado, falso binário, e mais) além de uma biblioteca de ângulos para founders, escolhida pelo objetivo de engajamento (comentários, reposts, curtidas, salvamentos). Executa o passo de humanização e agenda via Publora após a aprovação. Use para escrever uma publicação, encontrar um hook ou formato comprovado, ou obter ângulos específicos para founders. Não serve para revisar rascunhos existentes (use linkedin-humanizer --mode audit).
---

# LinkedIn Post Writer

Publique posts longos no LinkedIn usando fórmulas de hook que realmente performaram em 2025-2026 (multiplicadores de engajamento verificados).

## Quando usar

- O usuário diz "escreva uma publicação do LinkedIn sobre X"
- O usuário tem um tópico + um ângulo aproximado e precisa de um hook + estrutura
- O usuário quer escolher entre formatos comprovadamente vencedores e preencher com sua própria voz
- O usuário quer auditar + agendar em um único fluxo

## Fórmulas que esta skill pode usar

| Código | Fórmula | Engajamento de referência | Melhor para |
|---|---|---|---|
| F1 | Anáfora de Risco de Plataforma | 4.240 | Publicações sobre categoria/plataforma, produto como solução |
| F2 | Obituário R.I.P. | 3.822 | Afirmações de fim de era, mudanças de rumo no setor |
| F3 | Virada Ano a Ano | 494, 3,74x | Mudanças de identidade, reflexão de founder |
| F4 | Confissão com Âncora Temporal | 1.519+ | Vulnerabilidade, reset de voz, re-segmentação de ICP (2026: usar com cautela, ver ressalvas) |
| F5 | Meta Autocomprobatória | 1.082 / 435 comentários | Publicações baseadas em compromisso, testes em público |
| F6 | Isca de Lead via Comentário-Portão | 717-3.008 | Construção de lista (2026: usar com cautela, apenas com entregável real, ver ressalvas) |
| F7 | Livro-Razão de Precisão Ímpar | 1.755, 9,4x | Diário de construção do founder, detalhamento de custos (2026: abertura mais forte, número primeiro) |
| F8 | Reversão Pago-vs-Gratuito | 550, 19,64x | Distribuição gratuita de um framework |
| F9 | Teaser de Gap de Curiosidade | 306, 4,25x | Comportamento emergente, bastidores (2026: usar com cautela, resolver em 2 linhas) |
| F10 | Contrarian + Evidências Históricas | 3.083 | Opiniões contra vacas sagradas, ciclos de IA/tecnologia |
| F11 | Abertura Emocional a Frio | alto alcance* | História real com peso emocional (curtidas) |
| F12 | Autorização para Sentir | rico em comentários* | Encorajamento, reasseguramento (comentários; 2026: usar com cautela, precisa de um fato datado) |
| F13 | Reversão Isca-e-Troca | alto alcance* | Mudança de política/processo que é uma melhoria (curtidas) |
| F14 | Gratidão / Tributo Nominal | rico em reposts* | Agradecer mentores / equipe / colega que está saindo (reposts) |
| F15 | Explicar-para-Crianças | rico em salvamentos* | Desmistificar jargão (salvamentos) |
| F16 | Humildade com Faixa de Status | rico em curtidas* | Voz sênior que quer transmitir calor, não distância (curtidas) |
| F17 | Anedota A/B Controlada | estrutural† | Comparação de uma variável, opiniões sobre delegação/IA (comentários) |
| F18 | Dissolução do Falso Binário | estrutural† | "As duas respostas óbvias falham" em governança/estratégia (comentários/reposts; 2026: é o único contraste da publicação) |
| F19 | Ponte Anedota-Evidência | estrutural† | Observação pessoal + um conjunto de dados (comentários/salvamentos) |
| F20 | Fechamento com Curvas Divergentes | estrutural† | Duas trajetórias que divergem, máxima citável (reposts) |

\* O alcance de F11-F16 é o alcance absoluto do corpus 2026 (muitas vezes impulsionado pela fonte: um reshare ou um autor famoso), NÃO um multiplicador de base como os números de F1-F10. As duas colunas medem coisas diferentes e não são comparáveis: o "256k" de F11 é alcance bruto, o "550, 19,64x" de F8 é um multiplicador de formato. Não classifique fórmulas colocando esses números lado a lado. Veja `../../references/hook-formulas.md` para a referência real e as ressalvas de cada fórmula.

† F17-F20 são **fórmulas estruturais**: moldam a lógica de uma publicação (uma comparação controlada, um falso binário, uma ponte de evidência, duas curvas divergentes) em vez do seu tópico. Não carregam um número de referência e são escolhidas pelo objetivo principal. Foram criadas para a edição de founders e vários ângulos de founder as fixam pelo nome.

Esqueletos completos em `../../references/hook-formulas.md`. F1-F10 são o conjunto de liderança de pensamento em formato longo; F11-F16 (validadas contra um corpus 2026 de posts com desempenho acima da média) tendem a ser mais curtas e emocionais, e cada uma carrega um objetivo de engajamento primário.

### Ressalvas de alcance 2026 (auditoria de set/2026)

Os números de referência acima permanecem inalterados; o que mudou foi como o feed de 2026 trata o *recurso* em que cada fórmula se apoia. Toda fórmula em `../../references/hook-formulas.md` agora carrega uma "nota de alcance 2026"; as que importam na hora de escolher:

- **Nunca abra com uma pergunta.** Pergunta como primeira linha é -34% de curtidas medianas em todas as faixas de seguidores (MagicPost, 1,2M publicações; dados de fornecedor, AI-score proprietário). Mova a pergunta para o fechamento, onde ela é +3%.
- **Prefira número primeiro.** Um número de precisão ímpar na linha 1 é +34% de curtidas medianas (mesma fonte). F7 é a abertura mais forte de 2026; F3, F5, F17 já colocam o número primeiro por construção.
- **F4 Confissão, usar com cautela:** um fato específico, datado e desconfortável, sem enquadramento do tipo "vou ser sincero" / "confissão:"; a substância precisa estar nas primeiras 3 linhas. Franqueza fabricada é o sinal de "falsa vulnerabilidade"; vulnerabilidade genuína é +7 a +10% (dados de fornecedor).
- **F6 Comentário-Portão, usar com cautela:** CTAs de comentário-portão são o alvo nomeado da atualização de autenticidade de março/2026 do LinkedIn, e o botão de denúncia de "AI slop" de julho/2026 corta cerca de 40% das visualizações de publicações sinalizadas. Só usar com um entregável real e nomeado, e nunca com a frase "comente X para receber Y".
- **F9 Gap de Curiosidade, usar com cautela:** frases de teaser ("o que ninguém te conta", "o que a maioria não percebe", "a pergunta real é") estão nas listas de consenso de sinais de IA de 2026. O gap precisa ser específico e ser resolvido em até 2 linhas, antes do corte de "ver mais".
- **F12 Autorização para Sentir e F18 Falso Binário, usar com cautela:** ambas são recursos de enquadramento genérico ("Pare de X, comece Y" -6,7%, "Não é X, é Y" -4,9%, dados de fornecedor). Sobrevivem com um fato datado e sendo o único contraste da publicação.
- **Regra de densidade:** um contraste e uma tríade por publicação, zero pontes de revelação do tipo "O resultado?" / "Reviravolta:" / "Eis o que". 98-100% dos principais criadores humanos ainda usam esses recursos; o sinal de alerta é repetição somada a vazio, não o recurso em si.
- **Ainda eleva o alcance:** linha com número primeiro, pergunta de fechamento, assinatura em P.S. (+7,5%), 1.000+ caracteres (1,18x) e 20+ frases (1,14x, AuthoredUp, 3M publicações), parágrafos de 1-2 frases com linhas em branco (layout recomendado, não é um sinal de IA).

### Escolha primeiro pelo objetivo

Se o usuário já sabe o que quer que a publicação renda, comece aqui e depois refine pelo tópico. Mapeamento canônico: `../../references/hook-formulas.md` → Divisão por objetivo de engajamento.

| Objetivo | Buscar |
|---|---|
| Comentários | F17, F10, F4, F12, F9 (F4/F12/F9 com suas ressalvas de 2026) |
| Reposts | F14, F2, F8 |
| Curtidas | F11, F13, F16 |
| Salvamentos | F15, F7, F8 |

## Passos

**Perfil de voz primeiro (todos os rascunhos).** Se `../../references/voice-profile.md` tiver `filled: yes`, carregue-o e siga a impressão digital de voz do usuário, as regras fixas e o estilo de CTA/link em tudo. Se não estiver preenchido, mencione uma vez que `linkedin-humanizer --mode profile` pode aprender a voz do usuário a partir de alguns posts, e então prossiga com as regras de voz genéricas.

**Modo founder (quando quem escreve é um founder).** Antes de escolher uma fórmula, abra `../../references/founder-topics.md` e ofereça um **ângulo** de founder (A1-A10) que combine com o objetivo dele. O ângulo define o *território* (reprecificar a categoria, a matemática das oportunidades escassas, a linha de delegação, e assim por diante); vários ângulos já fixam a fórmula para você (A9 usa F17, A10 usa F18+F20). Ângulos de founder constroem confiança com um público restrito de investidores, contratações e design partners, em vez de perseguir alcance amplo. Preencha os campos entre colchetes do ângulo com os números reais do founder e então continue a partir do passo 3.

1. **Reúna os insumos.** Tópico, ângulo, ideias de rascunho se o usuário já tiver, público-alvo (founders / operadores / profissionais de marketing), tamanho desejado (curto 300-500 / médio 900-1300 / longo 1500-1900 caracteres).
2. **Escolha a fórmula.** Primeiro pergunte (ou infira) o objetivo: comentários, reposts, curtidas ou salvamentos. Use a tabela "Escolha primeiro pelo objetivo" para pré-selecionar, depois sugira 2-3 fórmulas que também combinem com o tópico e deixe o usuário escolher. Mostre o número de engajamento de referência ao lado de cada uma, mais a ressalva de 2026 da fórmula, se houver. Duas regras de hook valem independentemente da fórmula: **nunca abra com uma pergunta** (-34% de curtidas medianas; a pergunta vai para o fechamento, +3%) e **prefira uma linha com número primeiro** (+34% de curtidas medianas; ambos dados de fornecedor MagicPost, AI-score proprietário). Se o melhor hook que você tem é uma pergunta, inverta-o para o número que a responde.
3. **Redija a publicação.** Preencha o esqueleto da fórmula com a voz do usuário. Respeite as regras do algoritmo de 2026:
   - Hook nos primeiros 210 caracteres (antes do "... ver mais"); a linha 1 é uma afirmação ou um número, nunca uma pergunta, nunca "Eis o que/como", nunca "Pare de X, comece Y"
   - Faixa ideal de 900-1.300 caracteres para publicações em texto; 1.000+ caracteres e 20+ frases carregam um ganho de alcance de 1,18x / 1,14x (AuthoredUp, 3M publicações), então não corte uma publicação substancial abaixo de 1.000 só para acertar a faixa ideal
   - Quebras de linha duplas entre ideias, não simples; parágrafos de 1-2 frases são o layout recomendado
   - No máximo um contraste e uma tríade por publicação; nenhuma ponte de revelação do tipo "O resultado?" / "Reviravolta:" (regra de Densidade em `../../references/hook-formulas.md`)
   - Feche com uma pergunta específica, e adicione um P.S. de uma linha quando houver um desdobramento real (+7,5%)
   - 0-2 hashtags, colocadas no final
   - Nenhum link externo no corpo (mover para o primeiro comentário)
4. **Passo de humanização.** Elimine vocabulário de IA de 2026 por densidade, limite travessões (cerca de um a cada 100 palavras), quebre tríades empilhadas, aberturas genéricas e pontes de revelação. Adicione pelo menos 1 número específico, 1 entidade nomeada, 1 detalhe concreto em primeira pessoa a cada 100 palavras.
5. **Execute a auditoria.** Opcionalmente, invoque `linkedin-humanizer --mode audit` para verificações de algoritmo e voz antes de mostrar ao usuário.
6. **Ilustração opcional.** Se a publicação ficar melhor com um visual (ou o usuário pedir), ofereça um: rascunhe uma imagem e gere-a com `lib.illustrate(prompt, kind="wide")`, puxando o handle/cor da marca do Perfil de Voz e Marca §6 para a sobreposição. Mostre a `url` e o `cost` retornados no cartão de aprovação e anexe-os via `media_urls` na publicação. Para uma **grade de múltiplas imagens** (2-10 imagens em uma publicação) use `lib.illustrate_set([p1, p2, ...], kind="wide", overlay=brand)` e passe cada `url` em `media_urls=[...]`. Fluxo completo: `../linkedin-humanizer/sub-skills/illustration.md`. Sem chave da Pixfaro -> a skill redige o prompt para o usuário gerar manualmente.
7. **Cartão de aprovação.** Mostre: fórmula usada, rascunho completo, contagem de caracteres, janela de publicação sugerida (ter/qua/qui 7h30-9h00 horário local), alvos de reação de prováveis comentaristas, e a ilustração (se houver).
8. **Na aprovação.** Chame `lib.publish(kind="post", draft_text=<approved>, target_url="https://www.linkedin.com/post/new/", platforms=[{"platform":"linkedin","platformId":<id>}], scheduled_time=<iso_or_None>, media_urls=<list_or_None>)`. O wrapper cuida do roteamento Publora / manual / diy.

## Regras fixas (a partir de feedback de usuários)

Regras de voz globais: veja o `SKILL.md` raiz §Regras de voz. Regras adicionais específicas desta skill:

- Nunca enquadre o LinkedIn como inferior em uma publicação do LinkedIn (penalidade do algoritmo).
- Não cite o produto do usuário de um jeito que soe como autopromoção. No máximo uma menção, e apenas quando for a conclusão natural, não o pitch.
- Inclua pelo menos um momento de vulnerabilidade real ou peso concreto. Publicações de puro insight não performam em 2026.
- Ritmo natural, não variância fabricada: uma frase genuinamente longa ao lado de uma curta por parágrafo está ok; nunca alterne longo/curto ao longo de toda a publicação e nunca empilhe fragmentos (no máximo 2 fragmentos isolados por publicação). Só mexa em um parágrafo se toda frase tiver o mesmo comprimento monótono.

## Antipadrões (a skill vai recusar)

- Primeira linha em caixa alta ("ISSO MUDOU TUDO."). Isso vale até para F11 Abertura Emocional a Frio: carregue a intensidade na escolha das palavras, nunca em caixa alta.
- Pergunta como primeira linha ("Já se perguntou por que...?"). Inverta para um número, mova a pergunta para o fechamento.
- "Eis o que / eis como" ou "Pare de X, comece Y" como abertura; "O resultado?" / "Reviravolta:" como ponte de revelação
- Franqueza anunciada ("Vou ser sincero", "Confissão:") sem um fato datado por trás
- Frase de comentário-portão "Comente X para receber Y"
- Travessões acima do limite (mais de cerca de um a cada 100 palavras)
- Aberturas do tipo "No mundo acelerado de hoje"
- Listas de regra-de-três sem provas
- "Game-changer", "mergulho profundo", "alavancar", "fundamentalmente"
- Links externos no corpo
- Fechamentos genéricos de isca de engajamento ("marque alguém que precisa ver isso")

## Recursos

- `../../references/hook-formulas.md` — todos os 20 esqueletos de fórmula com exemplos trabalhados, notas de alcance 2026 por fórmula, "O que ainda eleva o alcance em 2026" e a regra de Densidade
- `../../references/founder-topics.md` — biblioteca de 10 ângulos de founder (A1-A10) da edição para founders, com templates de preenchimento
- `../../references/algorithm-heuristics.md` — regras de publicação de 2026 (timing, formato, extensão)
- `references/humanizer-checklist.md` — a lista completa de limpeza

## Skills relacionadas

- `linkedin-humanizer` — removedor agressivo de sinais de IA, mais `--mode audit` para revisão antes de publicar
- `linkedin-hook-extractor` — faz engenharia reversa de um hook a partir de uma publicação viral que você admira
