# Justificativa dos Níveis — Por Que Existem Três Modos

A V1 deste humanizador aplicava todas as regras igualmente. Aprendemos que algumas regras pegam saída real de IA e outras pegam boa escrita humana. A V2 as dividiu em 3 níveis para que os usuários pudessem escolher em quais sinais confiar. A V3 (2026-09) reordenou as regras dentro desses níveis com base em evidências de 2026: veja a §recalibração V3 no final.

## Conteúdo

- O insight central
- Nível 1 - FORENSIC (sempre ativo)
- Nível 2 - STRICT (ativo por padrão)
- Nível 3 - AESTHETIC (apenas opcional)
- Padrão recomendado
- O que essa divisão em níveis rejeita
- Recalibração V3 (evidências de 2026, com rótulos de confiança)

## O insight central

As regras de detecção de IA se agrupam em 3 grupos pela sua relação com a geração real de IA:

1. **Vazamento puro** — padrões que nenhum escritor humano jamais produz. Detectá-los é indefensável. (Nível forensic)
2. **Sobreposição com estilo ruim** — padrões que a IA usa pesadamente e que também são má escrita para humanos. Detectá-los é defensável por motivos de estilo mesmo quando a origem não é clara. (Nível strict)
3. **Sobreposição com boa escrita** — padrões que a IA usa pesadamente e que também são normais na escrita humana. Detectá-los cegamente sinaliza Dickinson, Lincoln e todo epidemiologista como IA. (Nível aesthetic)

A maioria das ferramentas de humanização mistura os três em um único livro de regras indiferenciado. É por isso que a saída delas achata a escrita literária mas ainda assim perde vazamento real de IA.

## Nível 1 — FORENSIC (sempre ativo)

Estes são sinais reais de IA. Todo detector concorda. Nenhum escritor humano os produz. Não existe defesa.

### Por que são forensic

- **oaicite / contentReference / turn0search0**: tokens internos de ferramenta do ChatGPT que vazam quando o usuário copia e cola a saída bruta sem limpeza. Nenhum humano escreve isso.
- **"Até minha última atualização em janeiro de 2024"**: aviso interno do modelo sobre o corte de treinamento. Humanos não avisam sobre o corte do próprio conhecimento.
- **`[Your Name]` / `2025-XX-XX` / `[Describe X]`**: texto de placeholder literal de templates de prompt que não foi preenchido.
- **Densidade de travessão acima de ~1 a cada 100 palavras**: o sinal de *frequência*, não o caractere em si. Emily Dickinson tem 1-2 travessões em um poema; o GPT-4 tinha uma média de 4-6 em um post do LinkedIn. O GPT-5.4 caiu para 1,43 a cada 1.000 palavras, abaixo do 3,23 humano, então o caractere sozinho não prova nada (veja §V3). O antigo hábito de "cola" (3+ em um post curto) ainda é de nível vazamento.

### Citações

- Seção de regras forenses da Wikipedia "Signs of AI writing": https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Russell, Karpinska, Iyyer (2025) "People who frequently use ChatGPT are accurate detectors" — confirmação empírica de que usuários frequentes identificam vazamento real com alta precisão.

## Nível 2 — STRICT (ativo por padrão)

Jargão corporativo. Mau estilo de LinkedIn independentemente de quem escreveu. A IA usa isso porque o corpus de treinamento usava. Baní-los melhora o post mesmo que o autor seja humano.

### Por que são strict

- **O vocabulário durável de 2026 (significant, crucial, notably, comprehensive, insights, robust, leverage, foster, landscape, nuanced, streamline, elevate, empower)**: palavras comuns que LLMs selecionam em excesso a uma taxa 2-5x maior que a humana em todo modelo de fronteira de 2026. São inglês comum, o que é exatamente o motivo pelo qual sobrevivem enquanto "delve" desaparece. Pontuadas por densidade: uma por parágrafo é inglês comum, três é uma assinatura.
- **Marcadores gramaticais (nominalizações, aberturas de oração em "-ing")**: "Leveraging our data, we..." ocorre a 5,3x a taxa humana. Os leitores sentem a mudança de registro mesmo quando não conseguem nomeá-la.
- **fundamentally / essentially / ultimately**: advérbios de preenchimento que não acrescentam informação. Strunk & White já sinalizavam isso em 1918. Eram mau estilo antes mesmo da IA existir.
- **"no mundo acelerado de hoje"** e as pontes de revelação ("The result?", "Here's what", "Stop X, start Y"): aberturas e pivôs que o LinkedIn mensuravelmente rebaixa (-4,3% a -6,7% de alcance, dados de fornecedor). Removê-los melhora o alcance independentemente de quem os escreveu.
- **Paralelismo negativo ("X não é Y, é Z")**: conforme o banimento rígido do Sergey em 2026-04-27, agora respaldado por dados de -4,9% de alcance. Usado historicamente por JFK, mas no contexto do LinkedIn em 2026 soa como ChatGPT em 90% dos casos.
- **Tríades empilhadas ou perfeitamente paralelas, e qualquer terceira tríade em um post**: tricolon a 2x a densidade de especialistas humanos em modelos de 2026. A forma é inocente; a densidade e os itens intercambiáveis são o indício. Uma tríade natural permanece.
- **Empilhamentos staccato e pontes de revelação** ("Short. Punchy. Done.", "No X. No Y. Just Z.", parágrafos de uma única palavra): o principal indício citado por leitores em 2026, e a assinatura de todo humanizador no estilo prompt. A V2 costumava adicioná-los. A V3 os remove.

### A defesa (e por que a ignoramos)

Um leitor poderia argumentar que "leverage" aparece em escrita de negócios legítima ou que "notably" aparece em toda revista acadêmica. Verdade, e é exatamente por isso que a V3 pontua densidade em vez de excluir palavras: uma é deixada em paz. Mas um parágrafo com três delas, no LinkedIn, em 2026, com este público, sinaliza corporativo ou IA em mais de 90% dos casos. O custo de reescrever esse parágrafo é quase zero. O custo de deixá-lo é a suposição do leitor de que o post foi rascunhado por IA, e possivelmente uma denúncia de slop. Então o modo strict reescreve por padrão os parágrafos acima do limiar.

### Citações

- Juzek & Ward (2025) "Why Does ChatGPT 'Delve' So Much?": https://arxiv.org/abs/2412.11385
- Kobak et al. (2025) "Excess vocabulary in LLM-assisted biomedical writing", Science Advances 11/27.
- Wu et al. (2026) replicação cross-model do excesso de vocabulário (GPT-5.5, Claude 4.8, Gemini 3.1).
- PNAS (2025) sobre aberturas de oração em particípio presente e taxa de nominalização em prosa de LLM.
- arXiv 2604.19768 (2026) sobre densidade de tricolon entre modelos de fronteira.

## Nível 3 — AESTHETIC (apenas opcional)

Padrões que a IA usa mas que humanos usam legitimamente. Baní-los cegamente identifica Hemingway como IA.

### As 5 regras mais controversas deste nível

#### Travessões (o último abaixo do teto)
- **Defesa**: Emily Dickinson construiu sua poesia sobre travessões. Cormac McCarthy os usa ao longo de *The Road* e *Blood Meridian*. A *New Yorker* usa travessões como estilo de casa desde 1925. E em 2026 os modelos de fronteira usam *menos* que humanos (GPT-5.4: 1,43 a cada 1.000 palavras vs. 3,23 humana). A The Economist chamou isso de "não mais um sinal confiável." 29% das legendas humanas no nosso próprio corpus usam um.
- **O sinal real não é o caractere.** É a frequência acima de ~1 a cada 100 palavras (coberto no nível forensic). Abaixo disso, autocensurar os próprios travessões é, em si, o indício de alguém tentando parecer humano.
- **Quando usar o modo aesthetic**: escrevendo para públicos que ainda tratam qualquer travessão como suspeito. Fora isso, deixe o travessão único em paz, e nunca o substitua por um ponto final (empilhar fragmentos é o indício pior).

#### Regra do três (a última natural)
- **Defesa**: Lincoln "of the people, by the people, for the people." César veni vidi vici. Churchill "blood, toil, tears and sweat." Aristóteles codificou o tricolon em 350 a.C. 26% dos top tweets humanos contêm exatamente uma.
- **Banir o tricolon bane 2.400 anos de escrita de discursos.**
- **O sinal real**: tríades vazias em que os três itens são intercambiáveis ("dynamic, vibrant, and innovative"), tríades perfeitamente paralelas, e 3+ por post (2x a densidade de especialistas humanos em modelos de 2026). A forma é inocente; a densidade e o conteúdo vazio são o indício. O modo strict já remove essas. O modo aesthetic remove a última natural.

#### Voz passiva
- **Defesa**: Watson & Crick (1953): *"It has not escaped our notice..."* Joan Didion *"The center was not holding."* O próprio Orwell usava mais de 20% de passivas em seus próprios ensaios. Escrita científica, jurídica e jornalística exigem a passiva.
- **Banir a passiva sinaliza mais de 60% da *Economist* e da *Nature* como IA.**
- **Quando usar o modo aesthetic**: públicos de escrita de opinião que esperam voz ativa. Nunca aplicar a escrita científica ou jurídica.

#### "Cultivate" / "vibrant" / "delve" / "tapestry" / "journey"
- **Defesa**: *Cultivate* é uma assinatura de George Eliot em Middlemarch. *Vibrant* abre a palestra do Nobel de Toni Morrison. E as palavras-cartaz de 2023-24 (delve, tapestry, realm, journey) agora estão em queda: humanos as evitam, os modelos estão sendo ajustados para se afastar delas, e um único "delve" em 2026 é mais provavelmente uma piada humana do que um vazamento (Geng & Trotta 2025).
- **Banir inglês normal porque LLMs o usam confunde sinal com corpus.** LLMs usam essas palavras porque leram todo livro em língua inglesa publicado desde 1500.
- **O sinal real**: densidade do conjunto durável de palavras comuns ("robust", "foster", "significant", "notably" a 3+ por parágrafo), coberto no nível strict. Note que "robust" e "foster" passaram de aesthetic para strict na V3 porque sobreviveram à mudança de vocabulário de 2025-26; "robust" como termo técnico estatístico continua isento.

#### Aspas curvas / aspas tipográficas
- **Defesa**: Aspas curvas acontecem automaticamente ao digitar no Word, Google Docs, Pages ou Notes. Travessões são produzidos por autocorreção em todo dispositivo Apple. Chamar isso de indício de IA sinaliza qualquer pessoa que escreve em um processador de texto de verdade.
- **O sinal real**: copiar e colar saída bruta de modelo em que a tipografia não foi normalizada. O modo strict já trata essa conversão para aspas retas por padrão.

### Citações

- Stanford HAI / Liang et al. 2023 "AI detectors biased against non-native English writers": https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers
- TechCrunch sobre a OpenAI encerrando seu próprio classificador com 26% de precisão: https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/
- Newby v. Adelphi University (out 2025): https://www.plagiarismtoday.com/2025/10/14/adelphi-university-sued-over-ai-allegation/
- Boston Globe "AI didn't kill the em dash" (mai 2025)
- Algorithmic Bridge / Alberto Romero "In Defense of the Em Dash"

## Padrão recomendado

Para posts e comentários de LinkedIn de fundadores / criadores / escritores sérios em 2026:

```
linkedin-humanizer --mode strict <text>
```

Isso aplica forensic + strict mas deixa os padrões aesthetic em paz. Ele pega vazamento real de IA e jargão corporativo sem achatar a voz do escritor. O modo aesthetic é para o caso raro em que a adequação ao público exige limpeza máxima (por exemplo, contribuir para a Wikipedia, postar em um fórum acadêmico paranoico com detecção de IA).

## O que essa divisão em níveis rejeita

A abordagem anterior de tamanho único fingia que toda regra tinha peso igual. Isso estava errado. Um post com `oaicite[^1]` deixado no texto está genuinamente vazado por IA. Um post usando "robust" para descrever um modelo estatístico não está. Tratá-los como igualmente suspeitos cria dois problemas: falsos positivos em escrita legítima, e falsa confiança de que passar pelo humanizador significa que um post é "humano". Essa divisão em níveis é a versão honesta.

## Recalibração V3 (evidências de 2026, com rótulos de confiança)

Rótulos de confiança: **[strong]** = replicado em 2+ estudos independentes de 2025-2026 ou no nosso próprio corpus com controle de tamanho (X n=445, Threads n=311); **[vendor]** = dataset de uma única plataforma ou fornecedor; **[weak]** = um único estudo ou um relatório de painel de especialistas.

### 1. Detectores não são o alvo

GPTZero, Pangram, Turnitin e Originality são classificadores treinados calibrados na assinatura de estilo do instruction-tuning do RLHF. O GPTZero abandonou perplexidade e burstiness do seu escore em 2023. O Pangram 4 vem com uma cabeça dedicada de humanização. Reescritas no estilo prompt "soar como uma pessoa de verdade" são pegas em 92-95% dos casos (VUB IJEI 2026; Russell 2025) [strong]. Reescrita mecânica leve *aumenta* a detectabilidade (arXiv 2603.17522) [weak]. O GPTZero afirma que sua ferramenta de vocabulário não está conectada ao seu escore. E texto do tamanho do LinkedIn (100-300 palavras) é onde todo detector é menos confiável [strong].

Consequência: a skill não promete mais passar em nenhum detector, e nenhuma regra neste arquivo é justificada por "o detector X pondera isso". Os dois alvos que continuam reais são **leitores humanos especializados** (que citam vocabulário 53% e estrutura de frase 36% das vezes ao identificar texto de IA) [weak: painel de especialistas] e o **filtro de slop do LinkedIn** (botão de denúncia de julho de 2026; posts sinalizados perdem cerca de 40% das visualizações) [vendor].

### 2. Vocabulário: densidade, não exclusão

As palavras evidentes de 2023-24 (delve, tapestry, realm, intricate, journey, paradigm) estão em queda conforme os humanos as evitam (Geng & Trotta 2025) [strong]. Os marcadores duráveis de 2026 são palavras comuns: significant, crucial, notably, particularly, comprehensive, insights, robust, leverage, foster, landscape, nuanced, multifaceted, holistic, streamline, elevate, empower (Kobak Sci Adv 2025; Wu et al 2026 entre GPT-5.5 / Claude 4.8 / Gemini 3.1) [strong]. Mais gramática: nominalizações e aberturas de oração em particípio presente "-ing" a 5,3x a taxa humana (PNAS 2025) [strong]. Mais uma camada específica de LinkedIn em 2026 (quietly, matters, compound, signal, "the work", "built different", load-bearing, "doing the heavy lifting", "let that sink in", "that's the real story") [vendor]. Pontes de revelação são negativas para alcance no LinkedIn: "The result?" -4,8%, "It's not X, it's Y" -4,9%, "Stop X, start Y" -6,7%, "Here's what/how" -4,3% [vendor].

Nosso próprio corpus de LinkedIn concorda no lado do vocabulário: vocabulário de IA é o único marcador consistentemente negativo para alcance dentro do mesmo criador (0,74-0,84 relativo ao autor) [strong], então o passo de vocabulário permanece mesmo com a lista de palavras tendo mudado.

Consequência: o sinal é densidade por parágrafo. 3+ marcadores = reescrever o parágrafo. 1 = deixar, a menos que seja uma ponte de revelação ou paralelismo negativo (limpeza em ocorrência única por causa dos dados de alcance).

### 3. Travessão: com teto, não banido

O GPT-5.4 emite 1,43 travessões a cada 1.000 palavras, abaixo da referência humana de 3,23. A The Economist (2026): "não mais um sinal confiável." Travessões isolados não carregam penalidade de alcance no LinkedIn [vendor]. 29% das legendas humanas do Instagram usam um, e 23% dos posts de top creators no LinkedIn também, a uma razão relativa ao autor de 1,09 (nosso corpus de LinkedIn de 2026-09, n=397) [strong]. Autocensurar os próprios travessões é, em si, o indício de alguém tentando parecer humano.

Consequência: teto de ~1 a cada 100 palavras (1-2 por post). Substitua o excesso por vírgula, dois-pontos, parênteses ou reescrita. Nunca um ponto final, porque um travessão dividido cria empilhamento de fragmentos, o que é um indício pior que o travessão.

### 4. Regra do três: ainda um indício, em densidade

Tricolon ocorre a 2x a densidade de especialistas humanos entre os modelos de fronteira de 2026 (arXiv 2604.19768) [strong]. 26% dos top tweets humanos usam exatamente uma [strong: corpus].

Consequência: remova tríades empilhadas ou perfeitamente paralelas e qualquer terceira tríade em um post. Deixe uma natural com itens concretos e não intercambiáveis.

### 5. Burstiness: restaurar, não forçar

O desvio-padrão de comprimento de frase de LLMs é cerca de metade do humano [strong], mas nenhum detector o pontua, e a alternância mecânica de longo/curto é, ela mesma, uma assinatura reconhecível de humanizador (DAMAGE 2025) [weak]. Os principais indícios citados por leitores em 2026 são exatamente o ritmo forçado: "Short. Punchy. Done.", "No X. No Y. Just Z.", "All the X. None of the Y.", "Simple. Effective. Easy.", revelações do tipo "The result?", parágrafos de uma única palavra ("Still." "Mostly."), pseudo-diálogo socrático "Why? Because." [strong: múltiplas listas de indícios de 2026 + nosso corpus]. No LinkedIn especificamente, a variância de comprimento de frase não é uma alavanca de engajamento em nenhum dos dois sentidos: nosso corpus normalizado por autor (palavra-chave n=205 + 15 top creators n=192, 2026-09) mostra razões de CV dentro do mesmo criador de 0,96 / 0,80 / 0,92 entre faixas de comprimento, Spearman -0,06, sem inversão dependente de tamanho, e uma leve vantagem de ritmo uniforme para posts de uma-ideia-por-linha entre 112-204 palavras [strong]. O resultado anterior de X/Threads ("burstiness vence em posts longos") era um fator de confusão de autor e desaparece após a normalização; aplica-se às plataformas irmãs, não aqui.

Consequência: o Passo 2 é RITMO, não QUEBRA, e o ritmo não é uma tática de alcance. Seu único objetivo positivo é evitar o indício de uniformidade mecânica que leitores especializados percebem (estrutura = 36% dos julgamentos deles): não deixe um parágrafo mecanicamente achatado, mas nunca fabrique variância. Uma frase genuinamente longa ao lado de uma curta está bem; sequências de fragmentos são o indício. Fragmentos limitados a 2 por post. Padrões staccato banidos. O layout tipo "broetry" (parágrafos de 1-2 frases, linhas em branco) está bem e é nativo para mobile; fragmentos por dramaticidade são o indício.

### 6. Marcas de autenticidade: concretude sim, confissão não

Concretude (entidades nomeadas, datas, quanto custou) é uma marca de autenticidade humana sustentada por evidência: texto de LLM tem menor densidade de entidades nomeadas em 3 estudos [strong]. Um número de precisão incomum na primeira linha eleva curtidas em +34% [vendor]. Mas números soltos não são um diferencial; textos de notícias de LLM usam mais números que humanos [strong]. Hedges e confissões inseridos saem pela culatra: "hesitação encenada" é 2x mais comum em texto de LLM do que em texto humano especializado; humanizadores construídos sobre pistas de confissão foram pegos em 100% dos casos por leitores especializados [weak: estudo único, mas a direção é consistente]; anúncios de sinceridade ("deixa eu ser honesto", "vou ser real", "sinceramente?") são um indício nomeado de 2026 (tropes.fyi "falsa vulnerabilidade") [vendor]; inautenticidade descoberta é a queda de confiança mais acentuada (Schilke & Reimann 2025) [strong]. Um fato específico, datado e desconfortável declarado de forma seca é positivo para alcance (+4,6% a +10%) [vendor].

Consequência: o Passo 3 pede um número de precisão incomum COM um referente nomeado, uma entidade nomeada, e um fato datado e desconfortável declarado de forma seca sem frase de introdução. Ele nunca insere hedges ou marcadores de sinceridade, e o Passo 1 os remove quando abrem ou fazem o pivô de um rascunho.

### 7. A correção excessiva é o novo indício

O resultado do humanizador tem sua própria assinatura (DAMAGE 2025; as próprias descobertas da skill slopotron de-slop) [weak]. "Escrever um pouco pior de propósito" agora se lê como um indício. Zero travessões, zero tríades, zero frases longas e um tom uniformemente achatado sem reação juntos se leem como "processado".

Consequência: Passo 4 SELF-CHECK. Edições proporcionais a problemas reais, sem cota fixa. Na dúvida sobre se um padrão é do autor ou do modelo, deixe como está.
