# Voice Fingerprint — Preservando a voz do usuário durante a limpeza

O humanizador é destrutivo por design. Todo passo exclui ou substitui tokens. Isso é bom para indícios de IA. É um bug para a voz real do usuário.

Este arquivo lista os sinais a preservar, mesmo quando se sobrepõem a regras em `scrub-rules.md`.

## Conteúdo

- Preserve incondicionalmente (NÃO limpe isto)
- Preserve quando uma amostra de voz for fornecida
- Resolução de conflito
- Como construir um fingerprint de voz a partir de amostras (esboço)
- Exemplos
- Não invente

---

## Preserve incondicionalmente (NÃO limpe isto)

Estas são assinaturas de voz, não indícios de IA. Deixe-as em paz em todos os níveis, incluindo `--mode all`.

| Padrão | Por que é voz, não IA |
|---|---|
| Inícios de frase em minúsculas (`fechamos nosso seed numa terça...`) | Usuários como o Serge usam isso como uma deixa de cadência deliberada. Capitalizar achata a voz deles. |
| `..` como pausa suave | Esta é a alternativa oficialmente abençoada pelo humanizador ao travessão. Removê-la não tem para onde ir. |
| Fragmentos de frase (`Valeu a pena.`, `Toda vez.`, `Nem perto.`) | O Passo 2 ADICIONA fragmentos. Não remova os que já existem. |
| Contrações (`don't`, `it's`, `you're`, `we're`) | Obrigatórias para ritmo natural. Limpar aspas curvas está bem; expandir contrações não. |
| Detalhe sensorial em primeira pessoa (`minhas mãos tremeram`, `a sala ficou em silêncio`) | O Passo 3 exige isso. Nunca remova. |
| Números específicos (`R$ 47 mil`, `9h14`, `47 dias`) | O Passo 3 exige isso. Nunca remova. |
| Entidades nomeadas (`HubSpot`, `terça de manhã`, nomes de marca) | O Passo 3 exige isso. Capitalize corretamente conforme a regra inegociável. |
| Autocorreção dentro de um parágrafo (`na verdade não`, `correção:`) | Sinal de burstiness. Humanos de verdade voltam atrás. |

---

## Preserve quando uma amostra de voz for fornecida

Se o usuário passar `target_voice_samples` opcionais (seus últimos 5-10 posts do LinkedIn), extraia:

1. **Distribuição de comprimento de frase.** Se ele costuma escrever frases de 4-6 palavras, não force "comprimentos mínimos" de 12+ palavras no Passo 2.
2. **Fingerprint de vocabulário.** Palavras que ele usa 3+ vezes nas amostras fazem parte da voz dele — mesmo que essas palavras estejam na lista negra strict. Sinalize para revisão do usuário em vez de substituir automaticamente.
3. **Hábitos de pontuação.** Alguns usuários usam `...` em vez de `..`, ou cadeias de vírgula ininterruptas. Combine com o padrão dominante.
4. **Padrões de abertura.** Se ele sempre começa com um número (`há 47 dias`, `R$ 2 mi de ARR`) ou um nome (`Jake disse`), preserve esse template.
5. **Padrões de fechamento.** Se ele sempre fecha com um único fragmento + ponto final (sem pergunta), não force um CTA de pergunta.

---

## Resolução de conflito

Quando uma regra de limpeza dispara em um token que também está no fingerprint de voz do usuário:

| Nível | Comportamento |
|---|---|
| Forensic | Sempre limpar. Regras forenses pegam vazamento de modelo; se o fingerprint de voz do usuário contém `oaicite` é porque ele colou saída de IA. |
| Strict | Sinalizar para revisão do usuário. Não substitua automaticamente. O usuário decide. |
| Aesthetic | Pule a regra por completo. Regras aesthetic já toleram explicitamente defesas de escritor humano. |

---

## Como construir um fingerprint de voz a partir de amostras (esboço)

```python
from collections import Counter
import re

def build_voice_fingerprint(samples: list[str]) -> dict:
    text = "\n".join(samples)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    return {
        "sentence_lengths": [len(s.split()) for s in sentences],
        "vocab_freq": Counter(re.findall(r"\b[a-z][a-z']{2,}\b", text.lower())),
        "starts_lowercase_pct": sum(1 for s in sentences if s and s[0].islower()) / max(len(sentences), 1),
        "uses_double_dot": ".." in text,
        "uses_triple_dot": "..." in text,
        "punctuation_freq": Counter(c for c in text if c in ".!?,;:"),
        "fragment_pct": sum(1 for s in sentences if len(s.split()) <= 4) / max(len(sentences), 1),
    }
```

A skill deve chamar isso em `target_voice_samples` antes de executar o Passo 1.

---

## Exemplos

### Exemplo 1 — `..` como pausa suave (preservar)

Entrada: `fechamos nosso seed.. daí tudo desmoronou`

Errado (limpa o `..`): `fechamos nosso seed. daí tudo desmoronou`

Certo (preservar): `fechamos nosso seed.. daí tudo desmoronou`

O `..` está na lista explícita de preservação. A substituição por ponto final é para `--`, não para `..`.

### Exemplo 2 — início em minúscula (preservar)

Entrada: `fechamos nosso seed numa terça de manhã às 9h14`

Errado (capitaliza): `Fechamos nosso seed numa Terça de manhã às 9h14`

Certo (preservar `fechamos`, capitalizar `Terça`): `fechamos nosso seed numa Terça de manhã às 9h14`

A regra inegociável diz para capitalizar NOMES — Terça é um substantivo próprio em contexto de data, mas o `fechamos` no início da frase permanece em minúscula por regra de voz.

### Exemplo 3. Colisão de vocabulário do fingerprint de voz (sinalizar, não substituir)

As amostras do usuário contêm `harness` 4 vezes em 6 posts (claramente parte da voz dele — ele trabalha com tecnologia de treinamento de cavalos).

A regra de limpeza do nível strict diz: `harness → use`.

Comportamento correto: sinalizar para revisão do usuário. Saída: `[CONFLITO-DE-VOZ: 'harness' está no seu fingerprint de voz (4 usos em amostras passadas) mas corresponde à limpeza do nível strict. Manter ou substituir?]`

---

## Não invente

A regra inegociável (SKILL.md linha: "Nunca introduza fatos que não estavam na entrada") tem precedência sobre a correspondência do fingerprint de voz. Se uma amostra contém números específicos, NÃO carregue esses números para um post diferente. Use apenas números que a entrada atual já fornece.
