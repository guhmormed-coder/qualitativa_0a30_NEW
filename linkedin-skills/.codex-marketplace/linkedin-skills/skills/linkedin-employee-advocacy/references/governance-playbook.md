# Playbook de Governança — O que revisar, o que não revisar, SLA

A forma mais rápida de matar um programa de advocacy é uma fila de revisão de 24 horas. A forma mais rápida de constranger a empresa é não ter revisão nenhuma. Este playbook é o caminho do meio.

## Conteúdo

- Princípio central: revise a superfície de risco, confie na superfície de voz
- A fila de revisão em 3 níveis
- Compromissos de SLA
- O que os revisores NUNCA devem editar
- O que os revisores DEVEM sinalizar
- Placar do revisor
- Auditoria contínua de 30 dias
- Bypass para incidentes
- Expectativas de ferramental (não requisitos)

## Princípio central: revise a superfície de risco, confie na superfície de voz

Todo post tem duas coisas nele:

- **Superfície de risco:** afirmações específicas, nomes de clientes, compromissos de roadmap de produto, orientação para setores regulados, números financeiros, menções a concorrentes.
- **Superfície de voz:** opinião, narrativa, estilo de gancho, ritmo das frases, uso de emoji, vulnerabilidade.

Revise a superfície de risco. Nunca revise a superfície de voz. Se você corrige a voz de alguém, essa pessoa para de postar; o programa morre em 6 semanas.

## A fila de revisão em 3 níveis

### Nível A — Sem revisão (publicação automática)

- Comentários em posts de terceiros
- Reposts com uma opinião pessoal de 1-2 frases
- Posts em que o integrante do time compartilha uma lição pessoal, história ou opinião sem afirmações sobre clientes específicos, finanças, roadmap ou concorrentes
- Enquetes, exceto quando as respostas constituiriam um sinal de roadmap ou de preço

**Cobertura estimada:** 70-80% do conteúdo de advocacy.

### Nível B — Revisão de captura de voz (SLA de 24h, assíncrona)

- Posts que nomeiam um cliente (mesmo que publicamente conhecido)
- Posts que citam um número específico de dados internos (receita, retenção, churn, ARR, taxa de conversão)
- Posts que criticam um concorrente nomeado
- Posts que anunciam algo que ainda não anunciamos

**Revisor:** um IC de marketing com autoridade de marca (não um gerente). Um revisor para cada 5-10 advogados de marca.
**Ação:** verificar se a entidade nomeada pode ser mencionada publicamente, verificar se o número pode ser divulgado, verificar o timing. Quase nunca editar a voz.

**Cobertura estimada:** 15-25% do conteúdo de advocacy.

### Nível C — Revisão jurídica / executiva (SLA de 48h)

- Posts sobre um tema regulado (HIPAA, SOX, GDPR, CCPA, valores mobiliários, alegações médicas)
- Posts que poderiam ser lidos como declarações prospectivas (projeção de receita, fusões e aquisições, captação de recursos)
- Posts sobre uma disputa em curso, processo judicial ou incidente de relações públicas
- Posts que nomeiam um cliente cuja confidencialidade contratual é uma questão em aberto

**Revisor:** Jurídico + pelo menos um C-level (dependendo do tema).

**Cobertura estimada:** <5% do conteúdo de advocacy.

## Compromissos de SLA

| Nível | Meta de SLA | O que significa "perder o prazo" |
|---|---|---|
| A | 0 minutos (automático) | n/a |
| B | 24 horas úteis | O autor pode publicar se não houver resposta até a hora 24 (regra de aprovação silenciosa) |
| C | 48 horas úteis | O autor precisa esperar pelo sinal verde/vermelho explícito |

A aprovação silenciosa no Nível B é o que faz o programa sobreviver. Se você não consegue se comprometer com 24h, não pode rodar um programa de advocacy; escolha um SLA mais longo e aceite o volume menor.

## O que os revisores NUNCA devem editar

- Início de frase em minúscula (voz de assinatura)
- `..` como pausa suave
- Frases fragmentadas
- Vulnerabilidade / riscos em primeira pessoa
- O gancho (reescrever o gancho = reescrever o post)
- Números específicos que o autor testemunhou pessoalmente (vs. métricas apenas internas)
- Cadência (o timing é escolha do autor)

Se um revisor fizer qualquer coisa disso, os próximos 3 posts do autor serão um discurso corporativo higienizado, e ele vai parar silenciosamente em 4 semanas.

## O que os revisores DEVEM sinalizar

- Nome de cliente sem permissão confirmada
- Números específicos de receita / retenção / churn vindos de dashboards internos
- Alegações sobre capacidade de produto que ainda não foi lançada
- Orientação financeira, mesmo que direcional ("estamos crescendo rápido" sugere crescimento → potencialmente material)
- Alegações específicas contra concorrentes (factuais ou não)
- Qualquer menção a um funcionário atual pelo nome sem o consentimento dele
- Qualquer coisa que mencione uma questão jurídica em curso

## Placar do revisor

Acompanhe isto por revisor para manter o programa saudável:

| Métrica | Saudável | Alerta |
|---|---|---|
| Taxa de cumprimento do SLA do Nível B | >90% | <75% |
| Edições por post no Nível B | <0,5 | >2 |
| Violações de regra de voz introduzidas pelo revisor | 0 | qualquer |
| Atrito de revisão relatado pelo autor (pesquisa trimestral) | <2/10 | >4/10 |

O revisor que fica em Alerta em qualquer linha recebe coaching ou é rotacionado.

## Auditoria contínua de 30 dias

Uma vez por mês, amostre 10% dos posts do Nível A (publicação automática) e verifique se eram realmente Nível A. Procure por:

- Nomes de clientes que deveriam ter sido Nível B
- Números específicos que deveriam ter sido Nível B
- Menções a concorrentes que deveriam ter sido Nível B

Se a auditoria revelar mais de 2 classificações erradas a cada 100 amostradas, aperte a definição do Nível A. Se revelar menos de 1 a cada 1.000, afrouxe-a (você está revisando demais).

## Bypass para incidentes

Durante um incidente ativo de RP / instabilidade, toda publicação automática do Nível A é suspensa por 5-7 dias para o time afetado. A comunicação passa a fluir exclusivamente pela voz designada de comunicação de incidentes. Retome o Nível A assim que o time de comunicação de incidentes der o sinal verde.

## Expectativas de ferramental (não requisitos)

- Uma ferramenta de fila (canal do Slack, base do Notion, plataforma dedicada) onde os rascunhos do Nível B chegam com o revisor designado
- Um pré-filtro por palavra-chave que marca automaticamente rascunhos como B/C com base em lista de nomes de clientes, lista de concorrentes, lista de palavras-chave reguladas
- Um log de auditoria de toda decisão de Nível B/C com revisor + timestamp

O programa pode rodar com um canal do Slack + planilha. Não precisa de um SaaS dedicado.
