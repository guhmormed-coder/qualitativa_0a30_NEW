# Padrões de Emoji — IA vs. Humano

Dados de padrão da análise de LinkedIn da MagicPost (fev 2026, post viral com 220 de engajamento).

Frequências de origem medidas em um corpus de posts do LinkedIn gerados por IA vs. escritos por humanos. A coluna de porcentagem mostra com que frequência cada emoji aparece em conteúdo gerado por IA.

## Emojis correlacionados com IA (os "indícios")

| Emoji | Nome | Frequência em IA | Por que é um indício | Alternativa de padrão humano |
|-------|------|--------------|-----------------|---------------------------|
| 💡 | lâmpada | 2,57% | Assinatura do ChatGPT para "insight" / "dica" — o emoji único mais diagnóstico | 🪛 (chave de fenda) para posts de "como consertar", 📍 (alfinete) para destaques, ou remover |
| 🚀 | foguete | 3,28% | Emoji de IA com maior frequência. Sinaliza "lançamento" / "crescimento" de forma modelada | 📦 (caixa) para envio, 🛫 (decolagem) para viagem, ou remover |
| ✨ | brilhos | 3,11% | Clichê de "IA mágica" / "transformação". Quase nunca aparece em conteúdo humano de operações | Remover. Sem substituto limpo |
| ♻️ | reciclagem | 2,93% | Usado para sinalizar republicações e ciclos de "lições aprendidas". IA usa em excesso como preenchimento | 🔁 (repetir) apenas se for literalmente sobre repetição, ou remover |
| 🎯 | alvo | 2,07% | Clichê de "metas" / "objetivos" | 📌 (alfinete de mapa) para itens específicos, ou remover |
| 📈 | gráfico_crescente | 1,89% | Sinal modelado de "crescimento" / "métricas" | Use um número real em texto simples em vez disso |
| 🔑 | chave | 1,74% | Template de "principal aprendizado" / "insight principal" | Pule o emoji, escreva o aprendizado em prosa simples |
| 🎯 | dardo | 1,68% | Mesma família do alvo acima — ambos sinalizam estrutura modelada | Igual ao alvo |
| 💪 | músculo | 1,45% | Clichê de "força" / "resiliência" | Remover ou substituir por um detalhe concreto |
| 🔥 | fogo | 1,31% | Limítrofe — usado em conteúdo humano também, mas sinalizado quando agrupado com outros | Manter se isolado, trocar por 🌶️ (pimenta) ou 🥵 (rosto de calor) para variar |

## Regras de agrupamento

- 1 emoji de padrão IA isolado: geralmente está bem
- 2 em um post: limítrofe — sinalizar no modo `--strict`
- 3+ em um post: provável IA — sinalizar em todos os modos
- Mesmo emoji 2+ vezes: indício de repetição — sinalizar em todos os modos

## Regras de posição

Posts gerados por IA tendem a colocar emojis em:
- Fim da linha de gancho de abertura (lâmpada, foguete, brilhos)
- Início de cada item de uma lista (alvo, chave, fogo)
- Fim da linha de CTA (foguete, fogo, músculo)

Se o rascunho tiver emojis nas três posições, trate como provável IA independentemente de quais emojis sejam.

## Emojis de padrão humano (correlação com IA abaixo de 1%)

Estes aparecem com frequência muito menor em conteúdo gerado por IA. Não são "à prova de IA" — apenas menos um indício:

| Emoji | Nome | Notas |
|-------|------|-------|
| ☕ | café | Concreto, mundano — IA raramente usa |
| 🍕 | pizza | Comida específica — IA raramente usa |
| 📦 | pacote | Envio / operações — concreto |
| 🪛 | chave de fenda | Posts de "como consertar" — emoji mais novo, o treinamento de IA está atrasado |
| 🌶️ | pimenta | Substituto de "opinião picante" para o fogo |
| 📍 | alfinete_de_mapa | Destaque de local / item específico |
| 🛫 | avião_decolando | Viagem / lançamento — mais específico que o foguete |
| 🥵 | rosto_de_calor | Emoji de reação — menos modelado que o fogo |
| 🪟 | janela | Emoji mais novo, o treinamento de IA está atrasado |
| 🧃 | caixinha_de_suco | Emoji mais novo, o treinamento de IA está atrasado |

## O que estes dados NÃO provam

- Não provam que esses emojis estão "errados" — humanos também usam 💡 e 🚀
- Provam que eles aparecem 2-3x mais em conteúdo gerado por IA do que a referência
- Um único emoji de padrão IA em um post não é um veredito — o padrão de agrupamento + repetição é o indício
- Emojis novos lançados depois do corte de treinamento dos modelos têm mecanicamente menos chance de aparecer em saídas de IA, por isso a lista de padrão humano tende a favorecer adições mais recentes do Unicode

## Frequência de atualização

As frequências devem ser remedidas trimestralmente conforme os dados de treinamento de IA mudam. Última atualização: fev 2026 (MagicPost).
