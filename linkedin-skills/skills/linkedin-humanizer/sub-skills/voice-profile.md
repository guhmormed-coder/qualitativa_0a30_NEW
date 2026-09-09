# Subskill: Construir / atualizar o Perfil de Voz & Marca

Constrói ou atualiza `../../../references/voice-profile.md` para que toda skill
de escrita neste pacote rascunhe na voz real do usuário em vez de uma voz
"humana" genérica. Roda em qualquer agente (Claude Code, Codex, OpenClaw): o
caminho principal só precisa da própria escrita do usuário colada. O Apify é
um acelerador opcional, nunca obrigatório.

## Quando isso roda

- O usuário diz "construa meu perfil de voz", "aprenda minha voz", "configure
  meu perfil", ou invoca `linkedin-humanizer --mode profile`.
- Também ofereça na primeira vez que uma skill de escrita rodar e encontrar
  `filled: no`.

## Entradas (qualquer uma já basta)

1. **Amostras coladas (padrão portátil).** Peça 3-6 posts ou comentários reais
   do usuário no LinkedIn. Isso sozinho já basta; sem token, sem histórico
   necessário.
2. **Assistido por Apify (opcional).** Se `APIFY_TOKEN` estiver definido e o
   usuário der a URL do perfil dele, puxe a atividade recente com
   `lib.fetch_user_recent_comments(username=...)` (e quaisquer URLs de post que
   ele compartilhar via `lib.fetch_post`) para reunir mais amostras. Trate
   como um acelerador em cima das amostras coladas, não como substituto delas.
3. **Manual.** O usuário também pode simplesmente dizer o nicho, as regras e
   os links dele.

## Passos

1. **Reúna 3+ amostras reais** da escrita do usuário (coladas ou puxadas).
2. **Extraia o fingerprint de voz** a partir das amostras, não de suposições:
   - ritmo de comprimento de frase (curto/médio/misto, e com que frequência
     aparece uma linha longa)
   - aberturas e transições recorrentes que ele realmente usa
   - hábitos de pontuação (pausa suave com `..`? nunca travessões? quebras de
     linha por ideia?)
   - vocabulário em que ele se apoia, e quaisquer palavras/clichês que ele
     claramente evita
   - comportamento de emoji e hashtag
3. **Infira nicho, ICP e pilares** a partir dos temas das amostras; confirme
   com o usuário em vez de adivinhar.
4. **Capture regras rígidas e o estilo de CTA/link** que as amostras revelam
   ou que o usuário declara.
5. **Escreva `../../../references/voice-profile.md`**: preencha as seções 1-5,
   copie as 2-4 linhas mais fortes literalmente em "Exemplos de assinatura", e
   defina o bloco de Status como `filled: yes`, `source: <pasted|apify|manual>`,
   `updated: <data de hoje>`.
6. **Mostre ao usuário o perfil preenchido para aprovação** antes de salvar, e
   diga a ele que qualquer skill de escrita agora vai combinar com isso
   automaticamente. Ele pode editar o arquivo a qualquer momento.

## Regras rígidas

- Construa o fingerprint a partir das amostras REAIS do usuário. Nunca invente
  uma voz.
- Preserve as peculiaridades dele (uma frase favorita, um ritmo incomum). Esse
  é o ponto. Apenas a limpeza genérica de indícios de IA continua se
  aplicando aos rascunhos depois, não ao perfil em si.
- Mantenha honestidade sobre a cobertura: com 3 amostras, diga que o perfil é
  uma primeira versão e vai se refinar conforme ele adicionar mais; sugira
  rodar de novo depois de 10+ posts.
- Nunca coloque segredos, dados privados, ou qualquer coisa que o usuário não
  tenha fornecido no arquivo.

## Relacionado

- O perfil preenchido é lido por `linkedin-post-writer`, `linkedin-comment-drafter`,
  `linkedin-reply-handler`, e `linkedin-repurposer` antes de eles rascunharem.
- Rode isso de novo sempre que a voz ou o foco do usuário mudar, para
  atualizar o perfil.
