# Employee Advocacy — Quatro Princípios Operacionais

Fonte: https://co.actor/use-cases/marketing-teams + pesquisa de mercado de 2026

## 1. Escale com autenticidade

Cada pessoa escreve com **sua própria voz**, não em linguagem corporativa.

- Textos escritos pelo time que soam como a marca = engajamento 3x menor do que voz pessoal
- Use uma entrevista curta de captura de voz no onboarding (5-10 min) para documentar o tom de cada pessoa
- Não normalize — mantenha a variação. Quem xinga ocasionalmente continua assim. Quem escreve em prosa técnica continua assim.

**Teste decisivo:** se alguém ler 5 posts aleatórios do seu time e conseguir identificar quem escreveu cada um, você está fazendo certo.

## 2. Mantenha o controle

Diretrizes de marca integradas ao fluxo de trabalho. A etapa de revisão é **opcional, não bloqueante**.

- Papéis de alta confiança (VPs, Diretores) pulam a revisão por completo
- Papéis de confiança média (Gerentes, ICs) passam por uma janela de revisão de 4 horas
- Novas contratações entram por padrão na revisão, ganham a dispensa após 4 semanas de posts sem problemas

**O que a revisão detecta:**
- Erros factuais sobre produtos / clientes
- Vazamentos de informação confidencial
- Questões regulatórias (finanças, saúde, regras de divulgação)

**O que a revisão NÃO altera:**
- Voz, tom, formatação
- Opiniões que o integrante do time tem sobre seu próprio trabalho
- Seleção de tema (dentro dos pilares)
- Hashtags, emojis

## 3. Remova atrito

Orçamento de tempo por post: **5 minutos**. Qualquer coisa além disso e o programa morre até a semana 3.

- A IA faz o trabalho pesado: ideação, rascunhos, sugestões visuais
- O integrante do time revisa, edita, aprova, publica
- O fluxo de aprovação é assíncrono e tem SLA <4h
- Publicar pelo celular é um caminho de primeira classe (não só desktop)

**Matemática:** 5 min/post × 3 posts/semana × 11 pessoas = **2,75 horas de tempo total do time por semana** para a produção completa do programa.

## 4. Comprove o ROI

Acompanhe alcance do time, engajamento e impacto no pipeline. Sem atribuição, o programa é cortado na primeira revisão de orçamento.

### Os 3 KPIs

- **Alcance do time** — soma das impressões de todos os criadores
- **Engajamento do time** — comentários + reações + compartilhamentos
- **Impacto no pipeline** — DMs recebidas, reuniões agendadas, negócios fechados com o LinkedIn como primeiro toque

### O que NÃO usar como KPI principal

- Número de seguidores (vaidade, muda devagar)
- Frequência de posts (esforço, não resultado)
- Desempenho de hashtags (não é uma métrica de negócio)

## Benchmarks (2026)

- Lançamento → primeiro post do time: meta de **14 dias**
- Tamanho de time ativo: **8-11** integrantes para uma produção relevante
- Produção do time: **70+ posts/semana** com 8 integrantes (~10 por pessoa a cada 4 semanas)
- Tempo por post: **5 min** no máximo
- Pontos de contato do time: **40.000/mês** com 11 pessoas × 3 posts/semana
- Piso de impressões por post: **300** (abaixo disso, audite perfil/gancho)
- Funcionário vs. página de empresa: **8x engajamento**, **6-8x alcance**

## Exemplo de configuração de time

```yaml
team:
  VP Marketing (author: Alice):
    cadence: 2 posts/week
    review: bypass
    pillars: [thought leadership, contrarian takes]
  Senior PMM (author: Bob):
    cadence: 3 posts/week
    review: bypass
    pillars: [product positioning, competitive teardowns]
  Marketing Manager (author: Carol):
    cadence: 3 posts/week
    review: 4h SLA
    pillars: [campaign recaps, customer wins]
  Content Writer (author: Dan):
    cadence: 4 posts/week
    review: 4h SLA
    pillars: [industry analysis, frameworks]
  ... (5 more team members)

weekly_output: 23 posts total from 8 members
weekly_time_cost: 1.9 hours
target_team_reach: 15,000 impressions/week (growing toward 40,000/month)
```
