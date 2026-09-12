# Série LinkedIn — CS como insumo de Produto

8 posts sobre como Customer Success já pratica boa parte da disciplina de Product Management — só não formaliza. Cada post pode ser publicado isoladamente, em qualquer ordem.

---

## 1. Jobs to be Done — o que CS já faz e ninguém documenta

Toda ligação de suporte carrega uma frase parecida com esta:

"Eu só queria conseguir fazer X antes do fim do dia."

Isso é Jobs to be Done. Clayton Christensen resumiu assim: cliente não compra produto, ele "contrata" um produto pra resolver um trabalho específico, num contexto específico.

O CS ouve esse trabalho todos os dias. E na maioria das empresas, essa informação morre no ticket fechado.

O problema não é falta de dado. É formato. "Cliente reclamou de tal coisa" não é JTBD — é sintoma. PM não consegue agir em cima de sintoma solto.

Um jeito simples de virar isso em insumo real:

→ Situação: em que contexto o cliente estava quando bateu no obstáculo
→ Motivação: o que ele estava, de fato, tentando resolver
→ Obstáculo: o que o produto não deu conta de fazer
→ Critério de sucesso: como ele saberia que o trabalho foi bem feito

Quatro campos. Cabe num template de CRM, numa tag de ticket, numa linha de planilha compartilhada com o time de produto.

A diferença entre "cliente pediu integração com X" e "cliente precisa consolidar relatório financeiro até o fechamento do mês, hoje faz isso manualmente cruzando 3 sistemas" é a diferença entre um pedido descartável e um insight que orienta roadmap.

CS já tem a matéria-prima. Falta o formato que o outro lado do processo consegue usar.

Como o seu time registra hoje o "motivo real" por trás de um ticket? Existe algum campo pra isso, ou fica só na cabeça de quem atendeu?

---

## 2. Continuous Discovery Habits e o ponto cego do CS

Teresa Torres defende uma regra que virou consenso em Produto: PM precisa de contato semanal com cliente pra tomar decisão boa. Sem isso, toda priorização vira palpite educado.

Só que na prática, em boa parte das empresas B2B, quem tem contato semanal — às vezes diário — com o cliente não é o PM. É o CS.

O ponto cego não é falta de discovery. É que o discovery já está acontecendo, só que sem esse nome, sem estrutura, sem chegar como sinal confiável na mesa de quem decide o que construir.

A diferença entre "feedback solto de CS" e "discovery contínuo" está em três coisas:

Recorrência registrada — não é "um cliente falou isso uma vez", é "isso apareceu 6 vezes nas últimas 3 semanas, em segmentos diferentes"

Contexto de uso — o que o cliente estava tentando fazer quando o problema apareceu, não só a reclamação

Separação de sinal e ruído — nem todo pedido é oportunidade; PM precisa confiar que o que chegou já passou por um filtro

Sem isso, "CS ouve o cliente toda semana" e "PM decide sem dado de cliente" continuam sendo verdades que convivem na mesma empresa, cada uma isolada na sua função.

Discovery contínuo já existe aí dentro. Falta virar processo que os dois lados reconhecem como tal.

Sua empresa trata o que o CS ouve como discovery, ou como reclamação a ser resolvida e arquivada?

---

## 3. O Build Trap visto de quem segura o cliente depois do lançamento

Melissa Perri descreve o "Build Trap": empresas que medem sucesso por quantidade de feature lançada, não pelo valor que ela gera. Ship vira a métrica. Adoção vira detalhe.

Quem vê isso de perto, na prática, não é quem lança. É quem sustenta o cliente depois.

O padrão se repete: feature lançada com expectativa alta, adoção não acontece, e o CS descobre isso não no dashboard de produto, mas na ligação em que o cliente pergunta "cadê aquilo que vocês anunciaram?" — ou pior, nem pergunta, porque nem percebeu que existe.

Esse dado de adoção pós-launch — quem usou, quantas vezes, se voltou a usar na semana seguinte — geralmente chega ao produto como anexo de relatório trimestral de CS. Tarde demais pra evitar o problema, cedo o suficiente só pra documentar que ele existiu.

Devia estar na mesa de priorização, não no relatório de resultado.

Isso muda a pergunta que se faz antes de aprovar a próxima feature: não é só "vale a pena construir", é "quem vai garantir que isso é adotado, e em que prazo alguém vai olhar pra esse número — antes que vire estatística de churn".

Ship de feature é output. Adoção é o primeiro sinal real de outcome.

Na sua empresa, quem é o dono do número de adoção 30 dias após o lançamento — e ele senta na reunião de priorização?

---

## 4. RICE prioriza por confiança — CS tem o dado que falta

RICE, ICE, qualquer framework de priorização decente pede um "confidence score": o quão confiante o time está de que aquela aposta vai gerar o impacto estimado.

Na prática, esse número nasce de opinião em reunião. "Eu acho que isso resolve", "o mercado está pedindo", "senti isso em três conversas de venda". Confiança vira sensação de quem fala mais alto na sala.

Só que existe dado melhor disponível — e ele está no CS.

Padrão observado em atendimento real é o material bruto de um confidence score honesto: quantos clientes bateram no mesmo obstáculo, em que contexto, com que frequência, o que fizeram como contorno na ausência da solução. Isso é evidência. Anedota de stakeholder não é.

O gargalo não é o dado existir. É ele não chegar formatado como insumo de scoring. Read-out de CS costuma virar apresentação de trimestre — bonita, guardada, sem conexão direta com a próxima planilha de priorização.

Pra virar insumo formal, precisa de três coisas: recorrência quantificada (não "vários clientes", e sim "42 tickets, 18 contas distintas, últimos 60 dias"), segmento afetado, e o custo que o cliente já paga hoje contornando o problema.

Com isso, o confidence score de uma aposta de roadmap deixa de ser opinião calibrada e passa a ser número rastreável até a fonte.

Como sua empresa calcula hoje o "confidence" de uma priorização — tem fonte auditável, ou é consenso de sala?

---

## 5. A métrica que o produto escolhe raramente é a que prediz churn

North Star Metric virou item obrigatório de estratégia de produto. O problema é qual métrica vira a estrela.

Ativação, frequência de login, número de sessões — métricas de engajamento são fáceis de medir e fáceis de mover no curto prazo. Por isso viram North Star com frequência maior do que deveriam.

O que elas não capturam: profundidade de uso. Um cliente pode abrir o produto todos os dias e usar 10% do que pagou. Pode logar pouco e depender de uma única funcionalidade de forma crítica pro negócio dele — e isso não aparece em nenhum dashboard de engajamento.

Esse segundo padrão é o que o CS enxerga primeiro, semanas ou meses antes de virar número de churn. Não é frequência. É se o cliente está usando o produto pra resolver o problema que o fez comprar, ou se ele orbita em torno de features periféricas enquanto o caso de uso principal fica capenga.

Métrica de vaidade de produto mede se as pessoas estão entrando. Métrica de sobrevivência de receita mede se elas estão dependendo.

Não é sobre trocar a North Star Metric da empresa inteira. É sobre reconhecer que o sinal mais forte de risco de conta às vezes não está em nenhum dashboard de produto — está na cabeça de quem atende aquela conta.

Sua North Star atual, se ela subisse 20% amanhã, isso reduziria churn — ou só melhoraria um gráfico?

---

## 6. PLG vs. CS-led growth: o falso dilema

Product-Led Growth virou mantra de tanto repetir: o produto deveria vender sozinho, sem fricção, sem intervenção humana.

Funciona muito bem em certos contextos — ticket baixo, decisão individual, valor óbvio em minutos de uso. Não é acidente que os exemplos mais citados de PLG venham de produtos assim.

Em produto complexo, B2B, com múltiplos usuários e decisão por comitê, o padrão que mais gera expansão de conta costuma ser outro: um CSM identifica o momento certo — um pico de uso, um time novo entrando, um caso de sucesso interno — e propõe upsell naquela janela específica. O produto não "vendeu sozinho". Alguém leu o contexto e agiu.

O risco não é adotar PLG. É usar PLG como justificativa pra não investir em CS — "o produto devia se vender sozinho" virando desculpa pra não ter estrutura de expansão de conta.

PLG funciona de verdade quando o valor é auto-evidente e a fricção de decisão é baixa. Onde a decisão é complexa, o "product-led" sem camada humana costuma significar só: ninguém está olhando pra essa conta até ela cancelar.

Não é produto vs. pessoas. É reconhecer em qual dos dois modelos o seu produto realmente vive — e parar de aplicar o playbook errado por estar na moda.

No seu contexto, a maior parte da expansão de conta vem do produto sozinho, ou de alguém que percebeu o momento certo?

---

## 7. Opportunity Solution Tree: CS parar de pedir feature, começar a nomear problema

Padrão comum: CS chega no PM já com a solução pronta. "Cliente quer um botão que faça X." "Precisamos de um filtro ali."

O PM ouve isso e, com razão, sente que está sendo mandado a executar em vez de decidir. Isso gera atrito — não porque o pedido seja ruim, mas porque pula uma etapa inteira do raciocínio.

Teresa Torres descreve essa etapa como Opportunity Solution Tree: parte de um objetivo de negócio, desce pra oportunidades (problemas ou necessidades reais do cliente), e só depois — e só aí — chega em soluções possíveis, com mais de uma opção na mesa.

O erro do "cliente quer botão X" não é estar errado sobre a dor. É queimar as duas primeiras etapas e entregar a terceira pronta, sem permitir que quem decide roadmap avalie se aquela é mesmo a melhor solução — ou só a mais óbvia.

Reformular isso não é complicado: em vez de "cliente quer botão X", registrar "cliente precisa fazer Y, hoje leva Z passos manuais pra isso, botão X foi a ideia dele de solução, mas o problema de fundo é esse".

Isso muda a conversa de "por que vocês não implementam o que o cliente pediu" pra "aqui está o problema, vamos decidir juntos qual é a melhor forma de resolver".

CS ganha credibilidade. PM ganha espaço pra decidir. O atrito cai porque o pedido para de soar como ordem.

Da próxima vez que um cliente pedir uma feature específica, você registra o pedido dele — ou o problema por trás?

---

## 8. Influência sem autoridade é o mesmo jogo em CS e em Produto

Isso aqui é mais pessoal.

PM não manda em engenharia. Time de engenharia decide o que é tecnicamente viável, prioriza sprint, discorda de prazo — e o PM convence, não ordena.

CS vive exatamente a mesma posição em relação a produto. Não decide roadmap, não aprova prioridade, não define o que entra no próximo trimestre. Convence — ou não é ouvido.

As duas funções sobrevivem da mesma habilidade: influência sem hierarquia. E é curioso que boa parte da literatura de Product Management sobre isso — gestão de stakeholder, storytelling com dado, como levar uma proposta pra sala sem ter o cargo que te dá o direito de decidir — foi escrita pensando em PM, mas se aplica quase sem adaptação a quem está em CS tentando influenciar roadmap.

Foi isso que comecei a perceber tarde: eu não precisava mudar de cargo pra pensar como PM. Precisava aprender a levar o que eu já sabia — porque converso com cliente toda semana — de um jeito que quem decide roadmap conseguisse usar sem se sentir empurrado.

Dado sem narrativa vira ignorado. Narrativa sem dado vira opinião. A habilidade que aproxima CS de Produto não é aprender a escrever PRD. É aprender a montar o argumento que faz alguém sem obrigação nenhuma de te ouvir, escutar mesmo assim.

Quem trabalha com CS e sente que "tem a informação certa mas não consegue fazer ela virar prioridade" — o que mais trava isso, na sua experiência: falta de dado, falta de formato, ou falta de espaço na mesa?

---

*Cada post foi escrito pra ficar de pé sozinho — pode ir em qualquer ordem, com 1-2 dias de intervalo entre publicações pra manter a série coerente sem cansar o feed.*
