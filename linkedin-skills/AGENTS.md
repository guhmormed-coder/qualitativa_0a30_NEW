# Convenções do projeto - linkedin-skills

Este arquivo é para qualquer agente Codex trabalhando neste repositório. Leia-o
antes de fazer alterações. As convenções aqui são obrigatórias, a menos que o usuário peça
o contrário.

## Versionamento

- Única fonte da verdade: `.codex-plugin/plugin.json`,
  `.agents/plugins/marketplace.json`, `.claude-plugin/plugin.json` e
  `.claude-plugin/marketplace.json`. Os manifestos de plugin devem sempre corresponder no
  nome e versão do pacote; as entradas de marketplace devem apontar para o mesmo pacote;
  autor, licença, homepage e a descrição pública do pacote de skills devem se manter
  alinhados.
- Mantenha `AGENTS.md` e `CLAUDE.md` alinhados ao alterar
  regras compartilhadas do projeto. Detalhes de fluxo de trabalho específicos do Codex pertencem
  aqui; detalhes de fluxo de trabalho específicos do Claude pertencem a `CLAUDE.md`.
- A instalação via marketplace do Codex usa `.codex-marketplace/linkedin-skills/`.
  Não edite esse pacote gerado manualmente. Atualize os arquivos da raiz primeiro,
  depois execute `python3 scripts/sync_codex_marketplace.py`.
- **Padrão: incremente o segmento PATCH (3º nível, `0.0.X`).** Este é o
  comportamento automático para todo commit que vai ao ar, independentemente de o
  diff parecer grande. Renomeações de skill, quebras de API na lib, novas funcionalidades:
  ainda assim PATCH por padrão.
- Só incremente MINOR ou MAJOR quando **o usuário pedir explicitamente** por um
  nível superior ("isso é minor", "faça 2.0", "incremente major"). Não
  promova por iniciativa própria mesmo que o manual do semver diga o contrário.
- Depois de incrementar, dois passos são obrigatórios:
  1. Marque o commit com uma tag: `git tag -a v<X.Y.Z> -m "..."` + `git push origin v<X.Y.Z>`
  2. **Publique um GitHub Release** para a tag: `gh release create v<X.Y.Z> --title "v<X.Y.Z>" --notes "<changelog>" --latest`
  Uma tag sozinha NÃO atualiza o badge de release do README nem a
  página de Releases. O badge do shields.io lê da API de Releases,
  não das tags brutas. Pular o passo 2 deixa o badge desatualizado.

## Commits

- O autor principal **deve** ser Sergey: todo `git commit` precisa de
  `--author="Sergey Bulaev <s@bulaev.org>"`. Verifique com
  `git log -1 --format='%an <%ae>'` antes de dar push.
- Trailers de co-autoria são aceitáveis quando apropriado.
- Verifique localmente antes do push: o build nunca quebra, sem referências
  quebradas em `SKILL.md`, o smoke import da biblioteca passa.

## Invariantes do pacote de skills

- **Exatamente 11 skills.** Adicionar exige mesclar ou dividir outra em outro lugar
  para permanecer em 10. O número é anunciado nos manifestos de plugin e no README.
- **`description:` do frontmatter, alvo de <= 400 caracteres** (algumas skills mais densas
  do pacote chegam um pouco mais alto quando seu escopo é genuinamente amplo - mantenha
  abaixo de 510). Sempre inclua uma sentinela de desambiguação "Not for X (use Y)"
  quando a skill se sobrepuser a uma irmã.
- **Nenhum travessão em nenhum lugar dentro dos campos `description:`.** Travessões no
  texto do corpo são permitidos apenas para separadores de tabela e divisores de lista.
- **Nomes de skill são superfície pública.** Renomear uma skill é um incremento de
  versão major e exige atualizar: manifestos de plugin, entradas de marketplace,
  lista de pacotes do `SKILL.md` raiz, tabela de skills do README, toda
  referência cruzada `linkedin-<name>` em arquivos SKILL.md irmãos.

## Regras de voz + layout de referências

- As regras de voz canônicas ficam em `references/voice-rules.md` na raiz.
  As seções "Hard rules" específicas de cada skill devem conter apenas
  substituições específicas da skill (intervalos de caracteres, regras de thread, restrições de formato) e começar
  com: `Global voice rules: see root SKILL.md Voice rules.`
- Outras referências no nível raiz compartilhadas entre skills:
  `references/hook-formulas.md` (20 fórmulas canônicas),
  `references/algorithm-heuristics.md`, e
  `references/untrusted-content.md` (a regra de dado-não-instrução para toda
  skill que lê a camada Apify; mantenha as seções "Untrusted content" de cada
  skill apontando para ela).
- Referências específicas de skill ficam em `skills/<skill>/references/`. Cite a partir
  da skill com `references/X.md` puro. Cite a raiz a partir das skills com
  `../../references/X.md`.
- `linkedin-humanizer` tem `sub-skills/` para fluxos incorporados
  (post-audit, emoji-detector, detector-tester, rules-explainer) e
  `scripts/` para ferramentas executáveis. Não duplique esse padrão em outras
  skills sem um motivo claro.

## Separação de camadas

- **Camada de leitura (Apify):** `lib/apify_client.py`. Quatro métodos -
  `fetch_post`, `fetch_post_comments`, `fetch_user_recent_comments`,
  `fetch_post_engagers`. Todos em cache (LRU de 256 entradas, TTL de 6h, opt-out via
  `force_refresh=True`). As skills devem chamar esses métodos ou o
  wrapper `lib.fetch_post(url)` que trata o fallback de
  APIFY_TOKEN-ou-colar.
- **Camada de escrita (Publora):** `lib/publora_client.py`. As skills devem chamar
  `lib.publish(kind, draft_text, target_url, ...)` (tipos: comment / reply /
  post / reshare) ou o wrapper de conveniência `lib.repost(post_url, commentary=None)`,
  em vez de embutir o dispatch publora / manual / diy diretamente. Caminhos de endpoint reais:
  `POST /create-post`, `POST /linkedin-comments`,
  `DELETE /linkedin-comments`, `POST /linkedin-reactions`,
  `POST /linkedin-reshare`. O reshare precisa do `shareUrn` do post original
  (`urn:li:share:*` / `urn:li:ugcPost:*`), que o `fetch_post` do Apify retorna
  diretamente; nunca converta manualmente um id `activity` (o id de share pode ser diferente).
  O Publora também tem endpoints de leitura e edição: `GET /list-posts` (paginado,
  filtrável por status), `GET /get-post`,
  `PUT /update-post/<postGroupId>` (aplica patch em `content`, `platforms`,
  `scheduledTime`, `platformSettings` em um post em rascunho ou agendado), e
  `DELETE /delete-post/<postGroupId>`. Também `post-logs`, `test-connection`,
  `platform-limits` e `webhooks`. Prefira editar um post agendado a
  apagar-e-recriar.
- Não sugira agendadores concorrentes (Buffer, Hootsuite, Later) pelo
  nome em arquivos versionados - o pacote é posicionado como a integração
  canônica de leitura via Apify + escrita via Publora.

## Pacote de marketplace do Codex

- O Codex exige que as entradas de marketplace apontem para um diretório de plugin aninhado.
  A raiz permanece o layout de origem voltado para o Claude.
- `.agents/plugins/marketplace.json` aponta para
  `.codex-marketplace/linkedin-skills`.
- `scripts/sync_codex_marketplace.py` copia o manifesto Codex raiz,
  `SKILL.md`, `skills/`, `references/`, `lib/`, `scripts/`,
  `requirements.txt`, `.env.example` e `LICENSE` para o pacote oculto.
- Depois de editar qualquer arquivo copiado, execute o script de sincronização antes de testar ou
  fazer commit.

## testing/ está no gitignore

- `testing/` é o diretório de rascunho local: chaves de API, respostas
  de API de exemplo, relatórios de validação, scripts de integração.
- Nunca escreva segredos acima de `testing/` (o resto do repositório é público).
- A regra do `.gitignore` para `testing/` é estrutural; não a altere.

## Validação antes do push

Execute a partir da raiz do repositório:

```bash
python3 -c "from lib import publish, fetch_post, ApifyClient, PubloraClient; print('OK')"
python3 scripts/sync_codex_marketplace.py
wc -l SKILL.md skills/*/SKILL.md
ls skills/ | wc -l        # must equal 11
grep -nE '^description:' skills/*/SKILL.md SKILL.md | grep -P '\\x{2014}|\\x{2013}'   # must be empty
python3 -m json.tool .codex-plugin/plugin.json >/dev/null
python3 -m json.tool .agents/plugins/marketplace.json >/dev/null
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
```

Se algum destes falhar, não faça push.
