# Testador de Detectores do LinkedIn

Passa qualquer texto por 5+ detectores de IA de uma vez e imprime o quanto eles discordam entre si. O objetivo não é encontrar o escore "certo". O objetivo é mostrar que não existe um escore certo.

## Por que isso existe

Detectores de IA são tratados como exames médicos. Não são. São vibe checks com um sinal de porcentagem.

Os comprovantes:

- **Stanford 2023** (Liang et al., Patterns / Cell Press): 7 detectores de IA sinalizaram **61,3% das redações do TOEFL de falantes não nativos de inglês** como geradas por IA. Os mesmos detectores sinalizaram 5,1% de alunos do 8º ano nascidos nos EUA. O viés é contra escritores de ESL, não contra IA.
- **A OpenAI desligou seu próprio AI Text Classifier em julho de 2023** porque ele atingiu apenas **26% de precisão** em texto escrito por IA. A empresa que constrói a IA não conseguia detectar a IA de forma confiável.
- **A Universidade Vanderbilt desativou a detecção de IA do Turnitin** citando risco de falso positivo para os alunos. Outras escolas R1 seguiram o exemplo.
- **Newby v. Adelphi University (outubro de 2025)**: um tribunal federal ordenou que a universidade expurgasse uma violação por "trapaça com IA" do registro de um estudante depois que a única "evidência" foi um escore de detector.
- **Teste da equipe do Sergey**: o mesmo artigo, três detectores, escores de **82% / 100% / 50%**. Isso é uma dispersão de 50 pontos no mesmo texto.

Se acusações estiverem vindo, esta skill produz a prova.

## Quando usar

- Alguém acusa um post, redação ou proposta de ter sido escrito por IA com base em um único escore de detector
- Antes de defender publicamente um escritor, registre a dispersão
- Como acompanhamento do post polêmico do Sergey sobre detectores — cole qualquer texto sinalizado, rode, tire um print da divergência
- QA interno em rascunhos da Co.Actor antes de publicar para públicos de alto risco

## Entrada

Qualquer texto. 200+ palavras dão a dispersão mais estável; abaixo de 100 palavras os detectores ficam ainda mais aleatórios.

Opcional: um rótulo (ex.: "redação de aluno ESL", "saída do GPT-4", "coluna de Carl Sagan de 1995") para o cabeçalho da saída.

## Saída

```
Text: "<primeiros 60 caracteres>..."
Length: 412 words

Detector scores (% AI probability):
  GPTZero         82
  Originality.ai  100
  ZeroGPT         50
  Sapling         34
  Copyleaks       91

Min: 34   Max: 100   Spread: 66

Verdict: USELESS — detectors disagree by more than 50 points.
Translation: nobody actually knows. The accusation is a coin flip.
```

## Os três veredictos

| Dispersão (máx - mín) | Veredito | O que significa |
|---|---|---|
| ≤ 15 pontos | **CONSENSUS** (consenso) | Os detectores concordam. Ainda não é prova, mas ao menos não estão se contradizendo. |
| 16-30 pontos | **MIXED** (misto) | Algum sinal, mas discordância suficiente para que nenhum escore único seja defensável. |
| 31-50 pontos | **DIVERGENT** (divergente) | Os detectores estão jogando cara ou coroa. |
| > 50 pontos | **USELESS** (inútil) | A dispersão é maior que metade da escala. Seja o que você decidir, o detector oposto também "prova" isso. |

## Como executar

```bash
cd /home/sbulaev/p/linkedin-skills/skills/linkedin-humanizer
python3 scripts/test_detectors.py --text "$(cat draft.txt)"
```

Ou via pipe:

```bash
cat draft.txt | python3 scripts/test_detectors.py --stdin
```

A maioria dos detectores esconde a API atrás de planos pagos. O script suporta três modos:

1. **Modo API** — copie `.env.example` para `.env` e preencha as chaves que você tiver (`GPTZERO_API_KEY`, `ORIGINALITY_API_KEY`, `ZEROGPT_API_KEY`, `SAPLING_API_KEY`, `COPYLEAKS_API_KEY` + `COPYLEAKS_EMAIL`). Detectores com chaves válidas rodam automaticamente; detectores sem chave são removidos do relatório.
2. **Modo colagem manual** (`--manual`) — abre a UI web de cada detector, pede ao usuário para colar o escore de volta. Mais lento, mas gratuito, e captura detectores sem API.
3. **Modo demo** (`--demo`) — offline. Retorna escores fictícios determinísticos derivados de um hash da entrada. Sem chamadas de API, sem chaves necessárias. Use para testar o fluxo de trabalho ou demonstrar o padrão de divergência sem gastar crédito de API.

Instale as dependências primeiro:

```bash
pip install -r requirements.txt
```

## Arquivos

- `../references/detector-list.md` — detectores suportados, endpoints de API, problemas de precisão conhecidos, citações
- `../scripts/test_detectors.py` — executa o teste paralelo, calcula a dispersão, imprime o veredito
- `../scripts/requirements.txt` — dependências Python (`requests`, `python-dotenv`)
- `../scripts/detectors.env.example` — template para as 5 chaves de API de detector (copiar para `.env`)

## Skills relacionadas

- `linkedin-humanizer` — reescreve o texto depois de um escore alto (ou antes, defensivamente)
- `post-audit.md` (irmã) — checagem pré-publicação que pega indícios de IA sem depender de detectores

## O que esta skill não é

Não é um detector. Não afirma que um texto foi ou não escrito por IA. Ela apenas documenta o quanto os detectores existentes discordam entre si, de forma que um único escore nunca mais possa ser usado como trunfo.
