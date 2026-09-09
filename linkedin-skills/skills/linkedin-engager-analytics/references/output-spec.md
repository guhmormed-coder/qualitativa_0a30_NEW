# Modo 2. Análise de engajadores — especificação de saída

Exemplos canônicos de saída do relatório de análise de engajadores. Veja `SKILL.md` para as etapas do workflow.

## Roster de engajadores

| # | Tipo | Nome | Cargo | Empresa | Perfil | Camada ICP |
|---|---|---|---|---|---|---|
| 1 | comentarista | Author A | Director | Cosmetics Co | linkedin.com/in/... | Prospect |
| 2 | comentarista | Author B | Senior PM | Enterprise SaaS Co | linkedin.com/in/... | Aspiracional |
| 3 | curtidor | Author C | Founder | Solo brand LLC | linkedin.com/in/... | Peer |

## Detalhamento por camada

| Camada | Definição | Quantidade | % do total |
|---|---|---|---|
| Peer | Fundador / operador em empresa do mesmo nicho, 5-50 funcionários | 12 | 24% |
| Aspiracional | Líder sênior em empresa com 50+ funcionários num nicho adjacente | 9 | 18% |
| Prospect | Director / C-suite em empresa que corresponde ao ICP | 18 | 36% |
| Outro | Não se encaixa em nenhuma camada | 11 | 22% |

## Listas de ação

- **Seguir de volta** (peers que merecem engajamento recíproco): top 5 por atividade
- **Alvos de comment-drop** (criadores aspiracionais com posts próprios): top 5
- **Prospects DM-áveis** (com a justificativa): top 5 com semente de abridor de uma linha

## Execução de exemplo

> Entrada: analisar engajadores em https://www.linkedin.com/posts/<author>_..., máximo 100

> Saída:
> - 50 comentaristas obtidos ($0,25)
> - Divisão por camada: 6 Peer / 14 Aspiracional / 18 Prospect / 12 Outro
> - 3 engajadores cross-post detectados (também engajaram com meu post 2 semanas atrás)
> - Top 5 prospects DM-áveis com abridores de uma linha anexados
