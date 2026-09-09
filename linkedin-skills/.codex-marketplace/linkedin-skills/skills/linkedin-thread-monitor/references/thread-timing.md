# Matriz de Timing de Threads

## Classificação do estágio da thread

| Tempo desde o comentário do usuário | Tempo desde a última resposta | Estágio | Prioridade |
|---|---|---|---|
| <6h | qualquer | Observação (o autor ainda pode responder) | Baixa — verificar depois |
| 6-24h | autor respondeu há <2h | **Quente** — responder em até 90 min | ALTA |
| 6-24h | autor respondeu há 2-12h | **Morno** — responder em até 2h | ALTA |
| 6-24h | sem resposta do autor | Frio — ignorar | — |
| 24-72h | autor respondeu recentemente | Ameno — responder em até 4h | Média |
| 24-72h | sem resposta do autor | Dormente | — |
| >72h | qualquer | Dormente — mudar para DM | Média (se for inbound de qualidade) |

## A janela de resposta morna explicada

Exemplo real de 2026-04:
- 14:27 UTC: Serge postou um comentário no post de um CEO ("moat moved from tools to taste")
- 12:06 UTC do dia seguinte (~22h depois): o autor respondeu pessoalmente ("How are you building that conviction muscle with your team?")
- 16:24 UTC daquele dia (~28h depois do comentário original, ~4h depois da resposta do autor): Serge respondeu com a resposta dele

Esta é exatamente a janela que o skill mira. Perdê-la por mais de 12h faz a resposta cair numa thread dormente, onde o autor não recebe a notificação em destaque.

## Primeiros 60 min nos próprios posts

Métrica diferente — quão rápido o USUÁRIO responde aos comentários nos próprios posts:
- Meta: todo comentário respondido em 5-15 min durante os primeiros 60 min
- Cada resposta em até 90 min gera um boost de ~90% naquela thread
- 3+ comentários substanciais nos primeiros 30 min = segundo empurrão do algoritmo

## Meia-vida do engajamento

- **0-6h:** 70% de todas as reações/comentários eventuais acontecem aqui
- **6-24h:** 25% — a cauda longa
- **24-72h:** 5% — gotejamento
- **>72h:** essencialmente morto (<1% do engajamento eventual)

## Regra: quando a thread morre, mude para DM

Se uma thread está dormente (>72h desde o último turno), mas a contraparte era de alta qualidade, não responda na thread — o post não vai fazer a notificação dela aparecer. Em vez disso, redija uma DM:

```
[Name] — circling back on our thread about [specific topic from thread].

[Your one new thought or data point].

Worth a 15-min conversation? Tuesday or Thursday this week if yes.
```

A DM deve referenciar a thread especificamente, não ser um pitch genérico.

## Antipadrões

- Encadear 3+ respostas sob um mesmo comentário principal (parece sequestro de thread)
- Responder depois de 72h na própria thread (baixa visibilidade, parece desesperado)
- "Retomando esta thread" genérico, sem um pensamento novo
- Enviar DM antes de a thread pública se encerrar naturalmente (pula a etapa conquistada)
- Responder a respostas DE respostas (o LinkedIn achata — ele não aninha tão fundo)

## Janelas de timing adjacentes à publicação (posts próprios)

| Fase | Janela | Ação |
|---|---|---|
| Aquecimento | 15 min **ANTES** de publicar | Deixe 3-5 comentários substanciais em posts de outras pessoas |
| Crítica | Primeiros 30 min DEPOIS de publicar | Responda a todo comentário em minutos; a distribuição encolhe se ficar parado |
| Semeadura | 15-30 min depois de postar | Deixe 3-5 comentários bônus no próprio post para criar profundidade de thread |
| Salto de visibilidade | Responder na 1ª hora | +35% de aumento de visibilidade (sinal de resposta do autor) |

## Engajamento entre pares (padrão seguro, não é um pod)

Um **grupo de pares seguro** é de 5-8 pessoas em áreas adjacentes que realmente leem o trabalho umas das outras e comentam só quando têm algo substancial a dizer.

Diferencia-se de um pod por:
- Timing variado (sem horário fixo diário)
- Comentaristas variados por post (não as mesmas 6 pessoas sempre)
- Substância do comentário >10 palavras, com ângulos novos
- Sem obrigação de reciprocidade

O que a detecção de pods pega:
- As mesmas contas engajando no mesmo minuto do relógio todo dia (ex.: 9h01)
- 15+ comentários caindo numa janela de 90 segundos
- Padrão idêntico de curtida/comentário em todo post

Penalidade real observada: um criador caiu de 8.500 para 340 impressões da noite para o dia após detecção de pod. Recuperação: 6-8 semanas.
