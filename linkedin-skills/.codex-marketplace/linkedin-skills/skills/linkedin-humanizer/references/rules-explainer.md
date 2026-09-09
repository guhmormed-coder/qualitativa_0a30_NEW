# Regras de Indícios de IA: Referência Classificada por Nível

Quinze regras do pacote `linkedin-humanizer`, ordenadas pelo tipo de evidência que cada uma realmente representa.

**Níveis:**
- **Forensic** - sinal real de IA, indefensável. O modelo ou seu template vazou.
- **Strict** - padrão humano real, mas o usuário o baniu por questão de estilo. Defendê-lo dentro desta voz de marca não faz sentido.
- **Aesthetic** - padrão sinalizado porque LLMs o usam, não porque sinaliza IA. Escritores humanos famosos construíram carreiras sobre isso.

**Força da defesa:** o quanto a regra sobrevive a um desafio do tipo "mas um humano escreveu isso". Baixa = a regra vence. Alta = o escritor vence.

## Conteúdo

- Nível 1 - Forensic (sinais reais de IA)
- Nível 2 - Strict (jargão corporativo, banimento fácil)
- Nível 3 - Aesthetic (exagero, defensável)
- Tabela-resumo
- Citações-chave

---

## Nível 1 - Forensic (sinais reais de IA)

### Regra 1. Marcadores `oaicite` / `contentReference` / `turn0search0`

- **Nível:** forensic
- **Por que é sinalizado:** São tokens internos do scaffold de uso de ferramentas da OpenAI (pílulas de citação, handles de resultado de busca). Aparecem quando alguém copia e cola do ChatGPT sem limpar a saída. Nenhum humano digita `:contentReference[oaicite:0]{index=0}` manualmente.
- **Usuário humano famoso:** nenhum. Zero casos registrados.
- **Força da defesa:** zero
- **Citação:** Wikipedia, "Signs of AI writing" - https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### Regra 2. Avisos de corte de conhecimento

- **Nível:** forensic
- **Por que é sinalizado:** Frases como "Até minha última atualização em janeiro de 2022..." ou "Não tenho acesso a informações em tempo real..." são boilerplate de corte de treinamento do GPT-3.5/4. Um humano escreveria "no ano passado" ou simplesmente daria a data.
- **Usuário humano famoso:** nenhum.
- **Força da defesa:** zero
- **Citação:** Wikipedia "Signs of AI writing"; TechCrunch sobre o classificador descontinuado da OpenAI - https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/

### Regra 3. Templates fraseológicos deixados sem preencher

- **Nível:** forensic
- **Por que é sinalizado:** Andaimes visíveis como `[Your Name]`, `2025-XX-XX`, `[Describe section X]`, `[Insert metric here]`. São artefatos de template de prompt em que o humano esqueceu de preencher o campo.
- **Usuário humano famoso:** nenhum.
- **Força da defesa:** zero
- **Citação:** Wikipedia "Signs of AI writing"

### Regra 4. Lacunas estilo Mad-Libs

- **Nível:** forensic
- **Por que é sinalizado:** Próxima da regra 3. Frases como "Eu [verbo] o [substantivo] a cada [período de tempo]" ou "O resultado foi um [adjetivo] [resultado]." Vêm de saídas ajustadas por instrução em que o modelo ecoou a estrutura do prompt em vez de resolvê-la.
- **Usuário humano famoso:** nenhum.
- **Força da defesa:** zero
- **Citação:** Wikipedia "Signs of AI writing"

### Regra 5. Uso excessivo de travessão - acima de ~1 a cada 100 palavras (3+ em um post curto)

- **Nível:** forensic (no limiar de excesso)
- **Por que é sinalizado:** Um único travessão é uma escolha estilística (veja a regra 11). Mas três ou mais travessões em um post de 200 palavras no LinkedIn foi um dos sinais estilométricos mais fortes que o GPT-4 emitia: o modelo colava orações onde um humano dividiria em duas frases. A V3 mantém o teto de densidade (~1 a cada 100 palavras, 1-2 por post) e substitui apenas o excesso, por vírgula, dois-pontos ou parênteses, nunca por um ponto final.
- **Defensora humana famosa:** Emily Dickinson é a defesa famosa, mas Dickinson usou travessões em poesia ao longo de centenas de poemas - não três em um único post comercial de 200 palavras. Densidade importa.
- **Força da defesa:** baixa (no limiar de excesso). A defesa de uso único (regra 11) é alta; o caso de excesso é forensic.
- **Citação:** Wikipedia "Signs of AI writing"; taxa do corpus GPT-5.4 de 1,43 a cada 1.000 palavras vs. 3,23 humana (2026)

---

## Nível 2 - Strict (jargão corporativo, banimento fácil)

### Regra 6. Vocabulário de IA: leverage, utilize, harness, delve, foster, cultivate

- **Nível:** strict
- **Por que é sinalizado:** Cada uma dessas palavras tem um equivalente anglo-saxão de uma sílaba (use, use, use, look, build, grow). LLMs usam em excesso a versão de origem latina porque as amostras de treinamento RLHF pendem para o corporativo. Humanos também as usam - mas o usuário as baniu da própria voz por questão de estilo.
- **Usuário humano famoso:** qualquer apresentação da McKinsey, qualquer artigo da HBR de 1995-2015. "Leverage" foi o verbo da consultoria de gestão dos anos 1990.
- **Força da defesa:** média em abstrato, **zero dentro desta voz de marca** - o usuário rejeitou explicitamente esse registro.
- **Citação:** Wikipedia "Signs of AI writing" lista todas as seis sob vocabulário de IA

### Regra 7. Advérbios de preenchimento: fundamentally, essentially, ultimately, crucially

- **Nível:** strict
- **Por que é sinalizado:** São muletas de abertura de frase que não acrescentam informação. "Fundamentalmente, a questão é X" se reduz a "a questão é X." LLMs os usam como hedges suaves; o usuário quer que sejam excluídos.
- **Usuário humano famoso:** artigos acadêmicos de filosofia (Daniel Dennett usa "fundamentally" constantemente). O registro acadêmico está bem na academia, não em um post do LinkedIn.
- **Força da defesa:** média em prosa acadêmica, **zero nesta voz**.
- **Citação:** Wikipedia "Signs of AI writing"

### Regra 8. Aberturas de preenchimento: "No mundo acelerado de hoje", "Na era da IA"

- **Nível:** strict
- **Por que é sinalizado:** São pura enrolação. O post ainda nem começou. LLMs as usam porque os dados de treinamento estão cheios de introduções de blog corporativo que faziam a mesma coisa.
- **Usuário humano famoso:** todo ghost-writer de LinkedIn de 2015-2022. O padrão é anterior ao GPT.
- **Força da defesa:** baixa. Mesmo antes da IA, guias de estilo de copywriting já matavam essas aberturas.
- **Citação:** Wikipedia "Signs of AI writing"; Ann Handley, *Everybody Writes* (2014) sobre aberturas de preenchimento

### Regra 9. Fechamentos clichê: "O que você acha?", "Marque alguém que precisa ver isso"

- **Nível:** strict
- **Por que é sinalizado:** Isca de engajamento genérica. O algoritmo do LinkedIn penaliza explicitamente isca de engajamento sob suas heurísticas de 2024+, e esses fechamentos sinalizam que o post não foi escrito para um leitor específico.
- **Usuário humano famoso:** todo influenciador do LinkedIn de 2016-2022. Anterior à IA.
- **Força da defesa:** baixa. Mesmo antes da IA, o algoritmo já odiava isso.
- **Citação:** política de isca de engajamento do LinkedIn (diretrizes de comunidade no app); Wikipedia "Signs of AI writing"

### Regra 10. Paralelismo negativo: "X não é Y, é Z"

- **Nível:** strict (banimento rígido do Sergey)
- **Por que é sinalizado:** "Não é um bug, é uma funcionalidade" / "Não é o que você diz, é como você diz." LLMs usam isso em excesso porque os modelos de recompensa do RLHF favorecem por ser citável. O usuário baniu explicitamente isso como padrão pessoal - limpo demais, arrumado demais, sem atrito.
- **Usuário humano famoso:** toda palestra do TED de 2010-2020. Tony Robbins, Simon Sinek. O padrão é retórica humana real, mas o usuário o rejeitou.
- **Força da defesa:** média em oratória, **zero nesta voz** (banimento rígido).
- **Citação:** Wikipedia "Signs of AI writing" sob "negative parallelism"

---

## Nível 3 - Aesthetic (exagero, defensável)

### Regra 11. Travessões - uso único

- **Nível:** aesthetic
- **Por que é sinalizado:** Folclore remanescente de 2023-24. Em 2026 os modelos de fronteira emitem menos travessões que humanos (GPT-5.4: 1,43 a cada 1.000 palavras vs. 3,23 humana) e a The Economist chamou o travessão de "não mais um sinal confiável". O sinal só existe acima de ~1 a cada 100 palavras (regra 5). Zero travessões em um post longo agora é, por si só, o indício de alguém tentando parecer humano.
- **Usuários humanos famosos:**
  - **Emily Dickinson** - construiu todo o seu estilo poético sobre travessões. "Because I could not stop for Death - / He kindly stopped for me -" (1863). Cerca de 1.800 poemas, travessões por toda parte.
  - **Cormac McCarthy** - usa travessões em *Blood Meridian*, *The Road*, *No Country for Old Men*. McCarthy é famoso por recusar aspas; os travessões fazem o trabalho do diálogo.
  - **Joan Didion**, *The Year of Magical Thinking* (2005) - travessões para luto parentético.
- **Força da defesa:** alta (uso único). O limiar de excesso (3+ em um post curto) vira forensic - veja a regra 5.
- **Citação:** Stanford HAI / Liang et al. (2023) sobre viés de detector - https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers ; TechCrunch sobre o desligamento do classificador da OpenAI por baixa precisão - https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/

### Regra 12. Regra do três

- **Nível:** aesthetic para a única tríade natural; strict para tríades empilhadas / perfeitamente paralelas e qualquer terceira tríade em um post
- **Por que é sinalizado:** A estrutura triádica ("X, Y, e Z") ocorre a 2x a densidade de especialistas humanos entre os modelos de fronteira de 2026 (arXiv 2604.19768). O indício é a densidade e os itens intercambiáveis, não a forma: 26% dos top tweets humanos contêm exatamente uma.
- **Usuários humanos famosos:**
  - **Lincoln**, Discurso de Gettysburg, 1863: "of the people, by the people, for the people."
  - **Júlio César**, 47 a.C.: *veni, vidi, vici* - "vim, vi, venci."
  - **Winston Churchill**, Câmara dos Comuns, 13 de maio de 1940: "blood, toil, tears and sweat" (tecnicamente quatro, mas a cadência é construída em três ao longo de todo o discurso).
  - **Thomas Jefferson**, Declaração de Independência, 1776: "life, liberty, and the pursuit of happiness."
  - **Aristóteles**, *Retórica*, século IV a.C. - identificou formalmente a regra do três como um dispositivo retórico fundamental.
- **Força da defesa:** alta. São 2.400 anos de retórica humana. Sinalizar isso como IA é exagero de detector.
- **Citação:** Aristóteles, *Retórica*, Livro III; Stanford HAI sobre falsos positivos de detector

### Regra 13. Voz passiva

- **Nível:** aesthetic
- **Por que é sinalizado:** O GPT-4 usa construções passivas em excesso. Humanizadores as removem por padrão. Mas a voz passiva tem usos legítimos - ocultar o agente, registro formal, neutralidade científica.
- **Usuários humanos famosos:**
  - **Watson & Crick**, *Nature*, 25 de abril de 1953: "It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material." Puro understatement passivo - a frase mais famosa da biologia do século XX.
  - **Joan Didion**, *Slouching Towards Bethlehem* (1968) - usa a passiva deliberadamente para distância narrativa.
  - **Toda a literatura científica** - a voz passiva é estilo de casa dos periódicos por um motivo. "As amostras foram tratadas com..." é correto; "Nós tratamos as amostras com..." soa informal.
- **Força da defesa:** alta em contextos técnicos/científicos, média em escrita de negócios. Não remova a passiva em um resumo de pesquisa.
- **Citação:** Watson & Crick, *Nature* 171:737-738 (1953); Wikipedia "Signs of AI writing" observa a voz passiva como sinalizada mas contestada

### Regra 14. Vocabulário de IA: "robust"

- **Nível:** aesthetic
- **Por que é sinalizado:** Agrupado com leverage/utilize/harness na lista de vocabulário da OriginalityAI.
- **Usuários humanos famosos:**
  - **Todo epidemiologista há um século** - "robust" tem um significado estatístico preciso: insensível a violações de premissas. "Um estimador robusto" é um termo técnico dos anos 1960 (Peter J. Huber, *Robust Statistics*, 1964).
  - **Engenheiros de software** - "sistema robusto" significa tolerante a casos extremos. Substituir por "sólido" perde o significado.
  - **Imunologistas** - "resposta imune robusta" é vocabulário padrão em *Nature* e *Cell*.
- **Força da defesa:** alta em escrita técnica, média em escrita de negócios. Mantenha "robust" se estiver cumprindo função técnica; substitua por "sólido" apenas quando for elogio genérico.
- **Citação:** Peter J. Huber, "Robust Estimation of a Location Parameter," *Annals of Mathematical Statistics* (1964); Stanford HAI sobre viés de detector contra inglês técnico

### Regra 15. Aspas curvas ("smart quotes")

- **Nível:** aesthetic
- **Por que é sinalizado:** Alguns detectores ponderam `"` `"` `'` `'` como sinal de IA porque saídas de LLM preservam esses caracteres e a digitação humana geralmente produz aspas retas `"` e `'`.
- **Usuários humanos famosos:**
  - **Microsoft Word**, **Google Docs**, **Apple Pages** - todos convertem automaticamente aspas retas em curvas por padrão. Qualquer pessoa digitando nessas ferramentas produz aspas curvas sem pensar.
  - **The New Yorker** - estilo de casa desde 1925 exige aspas curvas. Toda matéria publicada as usa.
  - **Todo livro tipografado tradicionalmente desde a invenção dos tipos móveis** - aspas curvas são a tipografia correta. Aspas retas são um compromisso ASCII.
- **Força da defesa:** alta. Sinalizar aspas curvas como IA é incompetência de detector - é sinalizar os padrões do Microsoft Word.
- **Citação:** *The Chicago Manual of Style*, 17ª ed., §6.115 sobre aspas; processo da Universidade Adelphi ilustrando o custo de falsos positivos - https://www.plagiarismtoday.com/2025/10/14/adelphi-university-sued-over-ai-allegation/

---

## Tabela-resumo

| # | Regra | Nível | Defesa | Defensor famoso |
|---|------|------|---------|------------------|
| 1 | Marcadores `oaicite` | forensic | zero | nenhum |
| 2 | Avisos de corte de conhecimento | forensic | zero | nenhum |
| 3 | Templates fraseológicos `[Your Name]` | forensic | zero | nenhum |
| 4 | Lacunas estilo Mad-Libs | forensic | zero | nenhum |
| 5 | Uso excessivo de travessão (acima de ~1 a cada 100 palavras) | forensic | baixa | nenhum nessa densidade |
| 6 | leverage / utilize / harness / delve / foster / cultivate | strict | média | apresentações da McKinsey |
| 7 | fundamentally / essentially / ultimately / crucially | strict | média | Daniel Dennett |
| 8 | "No mundo acelerado de hoje" | strict | baixa | ghost-writers do LinkedIn 2015-2022 |
| 9 | "O que você acha?" / "Marque alguém" | strict | baixa | manual de influenciador |
| 10 | "X não é Y, é Z" | strict | média | palestras do TED |
| 11 | Travessão (uso único) | aesthetic | alta | Dickinson, McCarthy, Didion |
| 12 | Regra do três (uma natural) / empilhada ou 3+ por post | aesthetic / strict | alta / baixa | Lincoln, César, Churchill, Aristóteles |
| 13 | Voz passiva | aesthetic | alta | Watson & Crick, Didion, toda a ciência |
| 14 | "robust" | aesthetic | alta | Huber 1964, toda a epidemiologia |
| 15 | Aspas curvas | aesthetic | alta | padrões do Word/Pages, New Yorker |

---

## Citações-chave

- **Stanford HAI / Liang et al. (2023)** - detectores de IA são tendenciosos contra escritores não nativos de inglês. O artigo mais citado para "detectores disparam em excesso sobre padrões estéticos." https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers
- **TechCrunch (25 de julho de 2023)** - a OpenAI desligou seu próprio classificador de texto de IA, citando baixa taxa de precisão. A empresa que construiu o GPT não conseguia detectar o GPT de forma confiável. https://techcrunch.com/2023/07/25/openai-scuttles-ai-written-text-detector-over-low-rate-of-accuracy/
- **Wikipedia, "Signs of AI writing"** - taxonomia mantida pela comunidade. Fonte para marcadores forenses (oaicite, corte de conhecimento) e a lista de vocabulário strict. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- **Processo da Universidade Adelphi (out 2025)** - estudante processou a universidade depois de uma acusação de IA em falso positivo. O custo legal de confiar em detectores sobre sinais estéticos. https://www.plagiarismtoday.com/2025/10/14/adelphi-university-sued-over-ai-allegation/

---

**Última atualização:** 2026-04-25
**Mantido por:** Claude Code e Codex, para Sergey Bulaev
**Propósito:** Base educacional para o post polêmico argumentando que as regras de escrita-por-IA são forenses em alguns casos e exagero estético em outros.
