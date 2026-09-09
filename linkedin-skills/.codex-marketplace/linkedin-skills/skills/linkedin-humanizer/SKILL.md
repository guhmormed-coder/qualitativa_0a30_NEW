---
name: linkedin-humanizer
description: 'Remove os indícios de IA aos quais leitores humanos e o filtro anti-"AI slop" do LinkedIn reagem em um post ou comentário: vocabulário de 2026 por densidade de parágrafo, pontes de revelação, fragmentos staccato, tríades empilhadas, sinceridade encenada. Reescritor em camadas (forensic / strict / aesthetic / all) além de uma revisão pass-fail em `--mode audit` e um construtor de perfil de voz em `--mode profile`. Não serve para enganar detectores de IA (nenhuma edição faz isso de forma confiável). Palavras-chave: humanizar, de-AI, parece ChatGPT, AI slop, remover indícios de IA, revisar este rascunho, auditar antes de publicar.'
---

# LinkedIn Humanizer V3

Reescreve qualquer texto para remover os indícios de IA que leitores humanos percebem e aos quais o filtro de "AI slop" do LinkedIn reage. Baseado na taxonomia "Signs of AI writing" da Wikipedia, na literatura de estilometria de 2025-2026 e no nosso próprio corpus com controle de tamanho. **V3 (2026-09):** recalibrado com evidências de 2026. O vocabulário agora é pontuado por densidade, os travessões passam a ter um teto em vez de serem banidos, o ritmo forçado agora é um indício em vez de uma correção, e há uma proteção contra correção excessiva.

**O que esta skill não faz:** ela não faz o texto "passar" no GPTZero, Pangram, Turnitin ou Originality. Esses são classificadores treinados calibrados na assinatura de estilo do instruction-tuning; reescritas no estilo "soar como uma pessoa de verdade" são pegas em 92-95% dos casos (VUB IJEI 2026, Russell 2025), e reescritas mecânicas leves aumentam a detectabilidade (arXiv 2603.17522). Nenhuma edição feita depois do fato supera de forma confiável um detector de classe Pangram, e os escores de detector em textos do tamanho do LinkedIn (100-300 palavras) são ruído. O valor real está em outro lugar: leitores humanos experientes citam vocabulário (53%) e estrutura de frase (36%) como o que denuncia texto de IA, e o botão de denúncia de slop do LinkedIn, lançado em julho de 2026, custa a um post sinalizado cerca de 40% de suas visualizações. Esta skill remove o que esses leitores e esse filtro percebem.

## O que mudou na V3

Nível de evidência entre colchetes: [strong] = replicado em 2+ estudos independentes de 2025-2026 ou no nosso próprio corpus com controle de tamanho; [vendor] = dataset de uma única plataforma ou fornecedor; [weak] = um único estudo ou relatório de painel de especialistas.

- **O vocabulário deixou de ser uma lista de exclusão e passou a ser pontuado por densidade.** As palavras de 2023-24 (delve, tapestry, realm, journey) estão em queda porque os humanos passaram a evitá-las [strong: Geng & Trotta 2025]. Os marcadores duráveis de 2026 são palavras comuns (significant, crucial, notably, comprehensive, insights, robust, leverage, foster, landscape, nuanced, streamline, elevate) mais marcadores gramaticais: nominalizações e aberturas de oração em "-ing" a uma taxa 5,3x maior que a humana [strong: Kobak Sci Adv 2025; Wu et al 2026; PNAS 2025]. O vocabulário de IA também é o único marcador consistentemente negativo para alcance no LinkedIn no nosso próprio corpus (0,74-0,84 relativo ao autor) [strong]. Um marcador em um parágrafo não é um veredito. Três ou mais, é.
- **O travessão (em dash) deixou de ser um indício.** O GPT-5.4 emite 1,43 por 1.000 palavras, abaixo da referência humana de 3,23; 29% das legendas humanas e 23% dos posts de top creators no LinkedIn no nosso corpus usam um (razão relativa ao autor de 1,09) [strong]. Zero travessões agora é, por si só, um indício (o autor está tentando parecer humano). Nova regra: teto de cerca de 1 a cada 100 palavras; o excesso é substituído por vírgula, dois-pontos, parênteses ou reescrita. Nunca por um ponto final.
- **O ritmo forçado é o indício nº 1 de 2026, não a correção.** A variância de comprimento de frase de LLMs é metade da humana [strong], mas os detectores não pontuam isso, a alternância mecânica de longo/curto é uma assinatura reconhecível de humanizador [weak: DAMAGE 2025], e no LinkedIn a variância de comprimento de frase não é uma alavanca de engajamento em nenhum dos dois sentidos (nosso corpus, n=397, dentro do mesmo criador: de nulo a levemente negativo) [strong]. "Curto. Direto. Pronto.", "Nada de X. Nada de Y. Só Z.", parágrafos de uma única palavra e revelações do tipo "E o resultado?" são os principais indícios atuais. O Passo 2 agora é RITMO, não QUEBRA: corrigir o ritmo mecanicamente uniforme, nunca fabricar variância.
- **A regra do três continua sendo um indício, em densidade.** Sequências de tricolon aparecem a 2x a taxa de especialistas humanos nos modelos de fronteira de 2026 [strong: arXiv 2604.19768]. Tríades empilhadas, perfeitamente paralelas e 3+ por post são removidas. Uma tríade natural única permanece (26% dos top tweets humanos têm uma).
- **A injeção de "fingerprints" (marcas de autenticidade) estava parcialmente errada.** Entidades nomeadas e concretude são sustentadas por evidência [strong: menor densidade de entidades em texto de LLM em 3 estudos]; um número de precisão incomum com um referente na primeira linha eleva curtidas em 34% [vendor]. Números soltos não são um diferencial, e hedges e confissões inseridos saem pela culatra: hesitação encenada é 2x mais comum em texto de LLM do que em texto humano especializado, e anúncios de sinceridade ("deixa eu ser honesto") são um indício nomeado de 2026 [strong: falsa vulnerabilidade do tropes.fyi; Schilke & Reimann 2025]. O Passo 3 agora pede um fato seco, datado e desconfortável, em vez disso.
- **Proteção contra correção excessiva.** O resultado do humanizador tem sua própria assinatura; "escrever um pouco pior de propósito" agora se lê como um indício [weak: DAMAGE 2025; slopotron]. O Passo 4 verifica se os Passos 1-3 introduziram exatamente os padrões que deveriam remover. As edições são proporcionais a problemas reais. Na dúvida, deixe como está.

Veja `sub-skills/rules-explainer.md` para justificativa por regra, defesas e citações, e `references/tier-rationale.md` §V3 para as evidências.

## Quando usar

- Antes de publicar qualquer post ou comentário rascunhado por IA (modo reescrita)
- Revisão pré-publicação de um rascunho finalizado (modo audit, veja `sub-skills/post-audit.md`)
- Quando um rascunho parece estranho e você não consegue apontar por quê

## Entrada

Qualquer texto (post, comentário, resposta, DM). Opcional: amostras da voz-alvo (posts humanos anteriores do usuário).

## Saída

- Texto reescrito com os indícios de IA removidos
- Diff mostrando o que mudou e por quê
- Densidade de indícios por parágrafo (marcadores por parágrafo; 3+ dispara uma reescrita)
- Confiança de leitura do leitor: "lê como humano", "misto", "lê como IA" (isso é uma estimativa de percepção do leitor, não um escore de detector)
- Nível aplicado (qual modo foi usado)

## Modos

```bash
# Padrão: forensic + strict (recomendado para LinkedIn)
linkedin-humanizer <text>

# Apenas forensic: toque mínimo, só elimina o vazamento
linkedin-humanizer --mode forensic <text>

# Strict: forensic + vocabulário de 2026 pontuado por densidade, pontes de revelação, staccato (a config padrão para LinkedIn)
linkedin-humanizer --mode strict <text>

# Aesthetic: strict + regras de estilo (tríades naturais únicas, voz passiva, vocabulário defensável)
# Use quando o público-alvo são editores da Wikipedia / leitores acadêmicos / caçadores de indícios de IA
linkedin-humanizer --mode aesthetic <text>

# All: todas as regras. Limpeza máxima. Vai achatar escrita literária e disparar a proteção do Passo 4.
linkedin-humanizer --mode all <text>

# Audit: revisão pass-fail apenas de detecção. Sem reescrita.
# Executa o checklist do algoritmo 2026: tamanho, gancho, CTA, estrutura, indícios de IA.
# Retorna Bloqueios + Avisos + correções sugeridas. Veja sub-skills/post-audit.md.
linkedin-humanizer --mode audit <text>

# Profile: constrói/atualiza o Perfil de Voz & Marca do usuário para que toda skill de
# escrita rascunhe na voz real dele. Aprende com 3-6 posts colados (portátil, sem
# token) ou, se APIFY_TOKEN estiver definido, com atividade puxada. Escreve
# ../../references/voice-profile.md. Veja sub-skills/voice-profile.md.
linkedin-humanizer --mode profile
```

## Os quatro passos

### Passo 1: SCRUB (pontuar, depois excluir ou substituir)

O passo de limpeza aplica catálogos em camadas para excluir ou substituir indícios de IA. A unidade de julgamento é o **parágrafo, não a palavra**: conte marcadores por parágrafo, reescreva o parágrafo a partir de 3+, deixe um único marcador em paz a menos que seja uma ponte de revelação ou vazamento forense. O código-fonte completo dos regex, os mapas de substituição e as funções de detecção estão em `references/scrub-rules.md`; carregue esse arquivo ao executar a limpeza de fato.

**Nível FORENSIC** (sempre ativo): vazamento real de modelo que nenhum humano produz. Cobre marcadores de ferramenta de IA (oaicite, contentReference, turn0search0, attached_file, grok_card), avisos de corte de conhecimento ("Até minha última atualização..."), templates fraseológicos ([Your Name], 2025-XX-XX), densidade de travessão acima de 1 a cada 100 palavras, e fechamentos em fórmula de outline ("Apesar de seu X... Olhando para frente...").

**Nível STRICT** (ativo por padrão): o que os leitores e o filtro de slop percebem. Cobre normalização de pontuação (aspas curvas para retas, `--` para vírgula ou reescrita; excesso de travessões para vírgula, dois-pontos ou parênteses, nunca um ponto final), o conjunto durável de vocabulário de 2026 pontuado por densidade (significant, crucial, notably, particularly, comprehensive, insights, robust, leverage, foster, landscape, nuanced, multifaceted, holistic, streamline, elevate, empower), marcadores gramaticais (nominalizações, aberturas de frase com oração em "-ing"), a camada 2026 do LinkedIn (quietly, matters, compound, signal, "the work", "built different", load-bearing, "doing the heavy lifting", "let that sink in", "that's the real story"), pontes de revelação medidas como negativas para alcance ("The result?" -4,8%, "It's not X, it's Y" -4,9%, "Stop X, start Y" -6,7%, "Here's what/how" -4,3%), todas as 6 formas de paralelismo negativo, tríades empilhadas ou perfeitamente paralelas e qualquer 3ª tríade em um post, e indícios de fechamento clichê ("What do you think?", "Tag someone who needs this").

**Nível AESTHETIC** (apenas opcional, vai achatar escrita literária): padrões que a IA usa mas que humanos também usam legitimamente. Cobre a única tríade natural remanescente, o vocabulário de 2023-24 em queda que hoje é majoritariamente inofensivo (delve, tapestry, realm, intricate, journey, paradigm), inglês normal defensável (cultivate, vibrant, garner, showcase, underscore), e voz passiva (a defesa da escrita acadêmica é ignorada).

### Passo 2: RHYTHM (restaurar a variância natural)

Os detectores não pontuam burstiness (irregularidade de ritmo), e no LinkedIn a variância de comprimento de frase não é uma alavanca de engajamento em nenhum dos dois sentidos. O que os leitores de fato percebem é o indício de uniformidade mecânica (toda frase com o mesmo tamanho, mecanicamente achatada; estrutura é 36% dos julgamentos de especialistas) e, pior, a variância encenada que humanizadores de segunda geração adicionam. Então o Passo 2 tem duas funções: corrigir o ritmo apenas onde ele soa mecanicamente achatado, e remover variância fabricada em todo lugar. Ele nunca adiciona variância como tática.

- Por parágrafo: uma frase genuinamente longa (25+ palavras, com uma oração subordinada que cumpre uma função real) ao lado de uma curta é normal e é como a variância humana se parece. Duas ou três frases de comprimento médio seguidas também estão bem. Edite apenas quando toda frase do parágrafo tiver o mesmo comprimento e soar achatada, e então edite uma frase, não o parágrafo inteiro.
- Fragmentos isolados: no máximo 2 por post, no total. "Valeu a pena." uma vez é uma peculiaridade de voz. Três em um post é um padrão.
- Banido terminantemente (reescrever como frases completas): revelações do tipo "O X? Y."; "Nada de X. Nada de Y. Só Z."; "Tudo de X. Nada de Y."; empilhamentos de adjetivos como "Simples. Eficaz. Fácil."; parágrafos de uma única palavra ("Ainda." "Quase." "Exatamente."); pseudo-diálogo socrático ("Por quê? Porque..."); sequências staccato como "Curto. Direto. Pronto.". Sequências de fragmentos são o indício.
- Layout não é ritmo. Uma ou duas frases por parágrafo com linhas em branco entre elas é a formatação nativa para mobile do LinkedIn e permanece (nosso corpus mostra uma leve vantagem de ritmo uniforme para esse formato de uma-ideia-por-linha entre 112-204 palavras). Fragmentos por dramaticidade dentro desses parágrafos é o indício. Mantenha o layout, corrija as frases.
- Nota sobre extensão: no LinkedIn nosso corpus (n=397, normalizado por autor) mostra que a variância de comprimento de frase não é uma alavanca de engajamento (de nula a levemente negativa dentro do mesmo criador, sem inversão dependente de tamanho). A regra de "não force variância" das plataformas irmãs de formato curto (Threads, X curto) se aplica aqui em qualquer extensão.
- Quebre estruturas perfeitamente paralelas com uma frase assimétrica, uma vez. Nunca alterne longo/curto/longo/curto ao longo de um post; esse vaivém é a assinatura do humanizador.

Meta: facilidade de leitura Flesch >55. Não há meta de variância de comprimento de frase. O teste é "algum parágrafo soa mecanicamente achatado, e eu adicionei um padrão staccato", não um número.

### Passo 3: ADD (marcas de autenticidade humana)

Exija pelo menos:
- Um número de precisão incomum COM um referente nomeado: quem, o quê, quando, ou quanto custou ("R$ 4.730 em excedentes na Vercel, fatura de março", não "R$ 5 mil" e não "custos significativos"). Um número solto não é uma marca de autenticidade; textos de notícias gerados por LLM usam mais números do que humanos. O referente é o que carrega o sinal.
- Uma entidade nomeada (pessoa real, empresa, data, cidade, ferramenta)
- Um detalhe sensorial em primeira pessoa
- Uma contradição ou autocorreção, declarada como fato ("Eu previ 3 meses. Levou 11."), não emoldurada
- Um fato específico, datado e desconfortável declarado de forma seca, sem frase de introdução antes ou depois. Não "Vou ser sincero, isso doeu: perdemos o cliente." Apenas "Perdemos a Carta como cliente em 14 de fevereiro." O fato carrega a vulnerabilidade. Uma frase de introdução transforma isso em sinceridade encenada, o que os leitores hoje reconhecem como o indício.

Proibido como aberturas ou pivôs (anúncios de sinceridade, um indício nomeado de 2026): "deixa eu ser honesto", "vou ser real", "sinceramente?", "para ser direto", "a versão honesta é", "ressalva honesta", "falando sério", "vou dizer a parte quieta em voz alta", "posso ser vulnerável por um segundo", "opinião impopular:" como prefácio de uma opinião popular. Também proibido como inserções: hedges que o autor não escreveu ("talvez", "posso estar errado, mas", "parece que"). Hesitação encenada é 2x mais comum em texto de LLM do que em texto humano especializado; adicioná-la faz o rascunho soar mais como IA, não menos.

Variar o comprimento de frase é função do Passo 2. Não adicione ritmo aqui.

Se a entrada não tiver esses elementos, peça ao usuário um número, nome ou momento específico para inserir. Não invente.

### Passo 4: SELF-CHECK (proteção contra correção excessiva)

O resultado do humanizador tem sua própria assinatura. Antes de retornar, releia o resultado uma vez e responda três perguntas:

(a) O Passo 2 criou empilhamentos staccato, pontes de revelação do tipo "E o resultado?", parágrafos de uma única palavra, ou um vaivém longo/curto/longo/curto? Se sim, funda os fragmentos de volta em frases completas.
(b) O Passo 3 adicionou uma confissão emoldurada, um anúncio de sinceridade, ou um hedge que o autor nunca escreveu? Se sim, remova a moldura e mantenha apenas o fato seco, ou remova a inserção.
(c) A limpeza achatou a voz do autor: tom uniforme, nenhuma reação, nenhum detalhe concreto restante, todo travessão removido, toda tríade removida, toda frase longa cortada? Se sim, restaure o que o autor tinha. Zero travessões e zero tríades é, por si só, um indício.

Se qualquer resposta for sim, recue em vez de limpar mais agressivamente. As edições devem ser proporcionais a problemas reais: um rascunho limpo recebe dois ou três toques, não uma cota fixa. Na dúvida sobre se um padrão é do autor ou do modelo, deixe como está.

## Regras inegociáveis

Regras globais de voz: veja `SKILL.md` raiz §Voice rules. Regras adicionais específicas desta skill (V3):

- **A limpeza está sempre no escopo.** Quando solicitado a humanizar, tirar o "cheiro de IA", finalizar ou publicar um rascunho, você executa pelo menos os níveis forensic + strict antes de ele ir ao ar. Isso vale mesmo quando o usuário escreveu o rascunho sozinho, diz que ama do jeito que está, ou está com pressa. Identidade do autor, "já está bom assim" e pressão de tempo nunca são motivos para pular a limpeza. O passo forensic + strict não muda nenhum significado e leva segundos: execute-o e publique. Se uma restrição realmente proibir tocar no texto, diga isso explicitamente e nomeie cada indício que está sendo deixado; o padrão é limpar, não deixar passar.
- **Limpe de forma proporcional.** Um passo que não encontra nada não muda nada. Não invente edições para justificar a execução, e não reporte um escore de detector como resultado; reporte os indícios encontrados e corrigidos.
- Preserve a alegação e o significado reais do usuário. "Preservar a voz dele" cobre peculiaridades no nível da frase e o que ele está alegando, NÃO pontes de revelação, empilhamentos staccato, ou um parágrafo com 3+ marcadores de vocabulário. Remover isso não é mudar a voz ou a alegação dele; é o trabalho.
- Nunca introduza fatos que não estavam na entrada. Se um número estiver faltando, pergunte, ou publique sem ele. Não invente.
- Nunca introduza marcadores de sinceridade, hedges ou molduras confessionais. Se o rascunho precisar de um momento vulnerável, peça um fato datado e declare-o de forma seca.
- Mantenha as peculiaridades de voz do usuário no nível da frase (inícios em minúsculas, pausas suaves com `..`, um travessão, uma tríade natural).
- Paralelismo negativo é um BANIMENTO RÍGIDO (conforme Sergey em 2026-04-27, agora respaldado por dados de -4,9% de alcance): o nível strict sempre remove todas as 6 formas.
- Nunca prometa resultados de detector. Se o usuário perguntar "isso vai passar no GPTZero", responda com honestidade: ninguém pode prometer isso, o escore em um post de 200 palavras é ruído, e a subskill `sub-skills/detector-tester.md` existe para demonstrar a dispersão, não para certificar um rascunho.

## Justificativa dos níveis (versão curta)

O nível forensic existe porque tokens oaicite, avisos de corte de conhecimento e lacunas estilo Mad-Libs são vazamento puro de modelo que nenhum escritor humano jamais produz. Detectá-los é indefensável. O nível strict existe porque os marcadores duráveis de 2026 (palavras comuns a 3+ por parágrafo, pontes de revelação, empilhamentos staccato, tríades empilhadas) são exatamente o que leitores especializados citam quando identificam texto de IA e o que o filtro de slop do LinkedIn detecta, então removê-los melhora o post mesmo que o autor seja humano. O nível aesthetic existe porque uma única tríade natural, voz passiva e o vocabulário em queda de 2023-24 aparecem em saídas de IA mas também aparecem em Lincoln, em todo epidemiologista, e em todo livro impresso desde 1500. Baní-los cegamente identifica Hemingway como IA. Execute o modo aesthetic apenas quando a adequação ao público exigir.

Para justificativa por regra e defensores humanos famosos, veja `sub-skills/rules-explainer.md` (e o índice de regras em `references/rules-explainer.md`). Para as evidências e rótulos de confiança da V3, veja `references/tier-rationale.md` §V3.

Para a falta de confiabilidade dos detectores de IA em geral (61,3% de falso positivo em redações do TOEFL segundo Stanford 2023; taxa de captura de 92-95% em humanizadores no estilo prompt segundo VUB 2026), veja `sub-skills/detector-tester.md`. Execute-o via `python3 scripts/test_detectors.py --text "..." --demo` (offline) ou com chaves pagas configuradas em `scripts/detectors.env.example`. Ele documenta a discordância; não certifica rascunhos.

Para detecção de padrão de emoji (assinatura lâmpada, foguete, brilhos), veja `sub-skills/emoji-detector.md` e a tabela de frequência por emoji em `references/emoji-patterns.md`.

## Exemplo

Veja `references/examples.md` para exemplos trabalhados.

## Arquivos

- `SKILL.md` — este arquivo (limpador de reescrita + entrada do modo audit)
- `references/scrub-rules.md` — padrões regex completos por nível, pontuação de densidade, regras de ritmo
- `references/voice-fingerprint.md` — como preservar a voz do usuário durante a limpeza
- `references/tier-rationale.md` — justificativa longa por regra, mais a seção de evidências da V3
- `references/rules-explainer.md` — índice legível por máquina de cada regra com citações
- `references/emoji-patterns.md` — tabela de frequência de emoji correlacionado com IA
- `references/detector-list.md` — detectores de IA suportados com endpoints de API e notas de precisão
- `references/audit-ai-tells.md` — lista negra + regex usados no modo audit
- `references/audit-checklist.md` — checklist de 20 pontos pré-publicação com limites
- `references/audit-examples.md` — exemplos trabalhados de auditoria
- `sub-skills/post-audit.md` — fluxo de auditoria pré-publicação (apenas detecção, sem reescrita)
- `sub-skills/rules-explainer.md` — quando defender uma regra sinalizada (travessão, regra do três, voz passiva)
- `sub-skills/emoji-detector.md` — fluxo de varredura / pontuação / sugestão para densidade de emoji
- `sub-skills/detector-tester.md` — roda o texto por 5 detectores de IA em paralelo e reporta a discordância
- `sub-skills/voice-profile.md` — constrói/atualiza o Perfil de Voz & Marca do usuário (`--mode profile`); o `../../references/voice-profile.md` preenchido é então lido por toda skill de escrita para que os rascunhos combinem com a voz real do usuário
- `scripts/test_detectors.py` — executa o teste de detector em paralelo (suporta `--demo` para modo offline)
- `scripts/requirements.txt` — dependências Python para o script de detector (`requests`, `python-dotenv`)
- `scripts/detectors.env.example` — template para as 5 chaves de API de detector

## Skills relacionadas

- `linkedin-post-writer` — gera rascunhos que já passam pelo humanizador
