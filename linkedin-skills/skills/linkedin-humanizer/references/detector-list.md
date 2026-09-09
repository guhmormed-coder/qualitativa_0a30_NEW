# Detectores de IA Suportados

Última atualização: 2026-04-25

Cinco detectores principais mais extras opcionais. Cada entrada cobre: endpoint de API, autenticação, problemas de precisão conhecidos e a citação que documenta o problema.

## Conteúdo

- 1. GPTZero
- 2. Originality.ai
- 3. ZeroGPT
- 4. Sapling
- 5. Copyleaks
- Detectores opcionais / estendidos
- Por que a dispersão importa
- Estatísticas rápidas para usar em uma resposta

---

## 1. GPTZero

- **Web**: https://gptzero.me
- **Documentação da API**: https://api.gptzero.me/v2/predict/text
- **Autenticação**: header `x-api-key`. Plano gratuito: 10 mil palavras/mês. Pago a partir de $9,99/mês.
- **Retorna**: `documents[0].class_probabilities.ai` (0,0-1,0) mais um detalhamento por frase.

**Problemas conhecidos:**
- O estudo de Stanford (Liang et al. 2023) incluiu o GPTZero no grupo que sinalizou **61,3% das redações do TOEFL** de autores não nativos de inglês como IA. O viés contra falantes de ESL (inglês como segunda língua) está documentado e é reproduzível.
- Infla os escores em prosa técnica / densa independentemente da autoria.
- Não roda em textos com menos de 250 caracteres; dá escores instáveis abaixo de 100 palavras.

**Citação**: Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., & Zou, J. (2023). "GPT detectors are biased against non-native English writers." *Patterns*, 4(7). https://doi.org/10.1016/j.patter.2023.100779

---

## 2. Originality.ai

- **Web**: https://originality.ai
- **Documentação da API**: https://docs.originality.ai/
- **Autenticação**: header `X-OAI-API-KEY`. Sem plano gratuito — mínimo de $0,01 por 100 palavras.
- **Retorna**: `score.ai` (0,0-1,0), `score.original` (0,0-1,0).

**Problemas conhecidos:**
- Vendido como "99% preciso", mas múltiplos testes independentes colocam a precisão real na faixa de 60-80%.
- Sinaliza agressivamente qualquer texto que tenha sido editado pelo Grammarly ou ferramentas similares, já que os padrões de edição imitam padrões de LLM.
- Teste da reunião de equipe do Sergey (2026): pontuou um artigo escrito à mão como **100% IA**, enquanto o GPTZero pontuou o mesmo artigo em 82% e o ZeroGPT em 50%. Dispersão de 50 pontos no mesmo texto.

**Citação**: Teste interno da equipe CCC, transcrição de reunião de março de 2026 (`projects/coactor/transcripts/`); também referenciado no post de abril de 2026 de Sergey Bulaev no LinkedIn sobre a falta de confiabilidade dos detectores.

---

## 3. ZeroGPT

- **Web**: https://www.zerogpt.com
- **Documentação da API**: https://api.zerogpt.com/api/detect/detectText
- **Autenticação**: header `ApiKey`. Plano gratuito: 5 requisições/min. Planos pagos disponíveis.
- **Retorna**: `data.fakePercentage` (inteiro de 0-100), booleano `data.isHuman`.

**Problemas conhecidos:**
- Famoso por ser instável — a mesma entrada colada duas vezes com 30 segundos de diferença pode retornar escores com 20+ pontos de diferença.
- Sinaliza a Constituição dos EUA, versículos da Bíblia e a Declaração de Independência como 90%+ IA quando colados como texto simples.
- Suscetível a paráfrases triviais — adicionar dois erros de digitação derruba um escore de 95% para 30%.

**Citação**: Múltiplas demonstrações replicadas no Twitter/X 2023-2024; comunicado da Universidade Vanderbilt sobre a desativação do Turnitin (ago 2023) citou instabilidade semelhante em toda a categoria de detectores. https://www.vanderbilt.edu/brightspace/2023/08/16/guidance-on-ai-detection-and-why-were-disabling-turnitins-ai-detector/

---

## 4. Sapling

- **Web**: https://sapling.ai/ai-content-detector
- **Documentação da API**: https://sapling.ai/docs/api/aidetect
- **Autenticação**: campo `key` no corpo JSON. Plano gratuito: 50 requisições/dia.
- **Retorna**: `score` (0,0-1,0), `sentence_scores` por frase.

**Problemas conhecidos:**
- Tende a pontuar mais baixo que GPTZero/Originality no mesmo texto — útil como sinal contrário no teste paralelo.
- Pior em escrita criativa do que em prosa técnica.
- Não lida com markdown — remova a formatação antes de enviar.

**Citação**: Os próprios benchmarks publicados da Sapling (https://sapling.ai/ai-content-detector/benchmark) reconhecem uma taxa de falso positivo de ~3-5% mesmo no dataset de melhor caso deles.

---

## 5. Copyleaks

- **Web**: https://copyleaks.com/ai-content-detector
- **Documentação da API**: https://api.copyleaks.com/documentation/v3/writer-detector/submit
- **Autenticação**: 2 etapas. POST para `/v3/account/login` com email + chave, obtém um token bearer, depois POST para `/v2/writer-detector/{scanId}/check`.
- **Retorna**: `summary.ai` (0-100), detalhamento por parágrafo.

**Problemas conhecidos:**
- A Universidade Adelphi usou a saída de um detector no estilo Copyleaks como única evidência no caso que se tornou *Newby v. Adelphi University* (out 2025). Um tribunal federal ordenou que a violação fosse expurgada.
- Penaliza fortemente a escrita acadêmica formal independentemente da autoria.
- Instável em resubmissões do mesmo texto.

**Citação**: *Newby v. Adelphi University*, Tribunal Distrital dos EUA (E.D.N.Y.), outubro de 2025. Cobertura: Inside Higher Ed, "Court Orders University to Drop AI-Cheating Charge" (out 2025).

---

## Detectores opcionais / estendidos

Podem ser adicionados via flag `--extra`. Nenhum tem API gratuita.

- **Turnitin AI Writing** — desativado por Vanderbilt, Cambridge, entre outras. Sem API pública; apenas institucional.
- **Winston AI** — https://gowinston.ai. Apenas pago.
- **Crossplag AI** — https://crossplag.com. Apenas pago.
- **Writer.com AI Content Detector** — UI web gratuita, sem API. Use o modo `--manual`.
- **Scribbr AI Detector** — UI web gratuita, sem API. Use o modo `--manual`.

---

## Por que a dispersão importa

A OpenAI desligou seu próprio AI Text Classifier em julho de 2023 com esta declaração pública: "baixa taxa de precisão" — medida internamente em 26%. Se a própria empresa que lança o modelo não consegue detectar de forma confiável a saída dele, nenhum detector de terceiros construído sobre sinais mais fracos pode ser tratado como verdade absoluta.

Referência: blog da OpenAI, "New AI classifier for indicating AI-written text" (31 de janeiro de 2023), atualizado em julho de 2023 com aviso de descontinuação.

---

## Estatísticas rápidas para usar em uma resposta

- **61,3%** — redações do TOEFL de autores ESL classificadas incorretamente como IA por 7 detectores (Stanford 2023)
- **5,1%** — taxa de falso positivo dos mesmos detectores em redações de alunos do 8º ano nos EUA (Stanford 2023)
- **26%** — precisão do próprio classificador da OpenAI antes do desligamento (julho de 2023)
- **50 pontos** — dispersão observada em um único artigo no teste da equipe CCC (2026)
- **0** — número de tribunais dos EUA que sustentaram uma decisão baseada apenas em "o detector disse" sem evidência corroborante até abril de 2026
