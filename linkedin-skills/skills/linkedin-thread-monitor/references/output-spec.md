# Modo 1. Monitoramento de threads — especificação de saída

Exemplos canônicos de saída do relatório diário de monitoramento de threads. Veja `SKILL.md` para as etapas do workflow.

## Relatório diário

| Postado | Autor | Post | Comentário | Resposta? | Estágio | Ação |
|---|---|---|---|---|---|---|
| 18h atrás | Author A | SaaS Co. | "moat moved to taste" | autor respondeu há 14h | Morno (janela 6-24h) | Responder agora |
| 22h atrás | Author B | Enterprise SaaS | "integration depth moat" | Não | Frio | Ignorar |
| 3h atrás | Author C | AI vendor | "twin economies" | Não | Observação | Verificar em 3h |

## Para cada thread morna

- Prévia da thread (últimos 3 turnos)
- Resposta sugerida (redigida via `linkedin-reply-handler`)
- Alvo da reação (a URN da resposta específica, não a do post)
- Prioridade (alta / média / baixa)

## Consolidado semanal

- Total de comentários postados
- Taxa de resposta do autor (meta 15%+)
- Conversão para DM (quando a thread fecha morna)

## Execução de exemplo

> Entrada: monitorar o perfil sbulaev, últimas 24h

> Saída:
> - 1 thread morna: o autor respondeu há 14h no post dele. Estágio atual: Morno (8-24h). Resposta sugerida pronta. Ação: postar em até 2 horas.
> - 8 threads frias (sem engajamento do autor). Ignorar.
> - 3 threads em observação (<6h, o autor ainda pode responder). Verificar de novo em 3-6h.
