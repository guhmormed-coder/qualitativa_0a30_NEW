# Subskill: Gerar uma ilustração para um post

Adiciona uma imagem opcional a um rascunho (ilustração de feed, slide de
carrossel ou quote-card) e a anexa na publicação. Usa a camada de imagem
Pixfaro através de `lib.illustrate`, que retorna uma URL hospedada que flui
diretamente para a mídia do Publora. Roda em qualquer agente (Claude Code,
Codex, OpenClaw).

## Quando isso roda

- O usuário diz "adicione uma imagem", "faça uma ilustração", "faça um
  quote-card", ou "adicione uma capa" para um post.
- Ofereça uma vez depois que um rascunho de post for aprovado, quando um
  visual elevaria o alcance (posts com imagem no LinkedIn têm mais tempo de
  permanência do que texto puro).

## Backends (espelha a camada de publicação)

- **pixfaro** — com `PIXFARO_TOKEN` (`pf_live_...`) definido: a imagem é
  gerada e anexada automaticamente.
- **manual** — sem token: a skill rascunha o prompt da imagem e pede ao
  usuário para gerá-la ele mesmo e colar a URL. Nunca bloqueia um rascunho.

`lib.image_backend()` reporta qual está ativo.

## Passos

1. **Escolha o tipo** (mapeia para uma proporção automaticamente):
   - `wide` / `link` (1200:628) - imagem de link-preview / imagem única no feed (padrão para um post de texto)
   - `portrait` / `carousel` / `quote` (4:5) - retrato de feed, slide de carrossel, quote-card
   - `square` (1:1) - genérico
   Sobrescreva com um `aspect_ratio="w:h"` explícito quando necessário.
2. **Elabore o prompt.** Descreva a cena de forma concreta: assunto,
   composição, estilo, paleta. Use como padrão um visual editorial limpo,
   não-literal e profissional, a menos que o Perfil de Voz & Marca §6 defina
   um `Visual style default`. NÃO tente renderizar as palavras do post
   dentro da arte (veja overlay abaixo).
3. **Aplique overlay de marca (se o perfil tiver um).** Leia
   `../../../references/voice-profile.md` §6 Ativos de marca. Se um handle,
   cor de marca ou logo estiver definido, passe um `overlay` para que o
   texto/logo seja composto com precisão de pixel (nítido mesmo em um
   modelo barato):
   ```python
   from lib import illustrate
   r = illustrate(
       "Minimal flat-vector lighthouse cutting through fog, calm blue palette, editorial",
       kind="wide",
       overlay={"text": "@yourhandle", "position": "bottom-right", "color": "#0A66C2"},
   )
   ```
   Para um **quote-card**, coloque a linha de gancho extraída no `text` do
   overlay (não no prompt) para que renderize nítida: `kind="quote"`,
   `overlay={"text": "<gancho>", ...}`.
4. **Escolha do modelo.** Padrão `nano-banana-2` (equilibrado, ~$0,08). O
   overlay cuida do texto, então um modelo base barato serve bem. Só recorra
   ao `gemini-pro-image` quando o usuário quiser arte premium. Nunca faça
   upgrade de nível silenciosamente.
5. **Mostre + confirme.** Apresente a `url` e o `cost` retornados. Após a
   aprovação, anexe ao publicar:
   `publish("post", draft_text, target_url, media_urls=[r["url"]])`.
6. **Modo manual.** Se `r["backend"] == "manual"`, mostre `r["message"]` (o
   prompt rascunhado + a proporção) e peça uma URL colada para anexar.

## Refine em vez de regenerar

Quando o usuário quiser um ajuste ("deixe o céu mais escuro", "troque o
título", "mais espaço em branco"), NÃO regenere do zero. Mantenha o `id` do
resultado anterior e edite-o:

```python
from lib import illustrate, refine
first = illustrate("<scene>", kind="wide")     # -> {"id": "img_...", "url": ...}
fixed = refine(first["id"], "make the background darker and increase contrast")
```

`refine` edita pelo id `img_...` (não pela URL), herda o formato/nível da
fonte quando você omite `aspect_ratio`/`resolution`, e é mais barato e mais
consistente que uma geração nova. Encadeie quantas vezes forem necessárias.

## Proteção de custo

- Cada resultado carrega `cost` e `balance_after`; se `low_balance` for
  True, avise o usuário que o saldo do Pixfaro está baixo antes de gerar
  mais.
- Padrão para `nano-banana-2` + 1K. Os modelos premium (`gemini-pro-image`,
  `gpt-5-image`) cobram várias vezes mais - use-os apenas quando o usuário
  pedir pelo nome; `illustrate`/`refine` nunca fazem upgrade por conta
  própria. A flag `premium` de um resultado é True quando um modelo com
  preço premium foi usado - confirme que isso era intencional.
- `lib.available_models()` retorna preço/latência ao vivo quando você
  precisar mostrá-los.

## Grid de múltiplas imagens (LinkedIn, até 10)

Posts do LinkedIn podem carregar até 10 imagens em layout de grid (não um
carrossel deslizável, que a API não suporta). Gere um conjunto e anexe todas:

```python
from lib import illustrate_set, publish
shots = illustrate_set(["scene A prompt", "scene B prompt", "scene C prompt"],
                       kind="wide", overlay={"text": "@handle", "color": "#0A66C2"})
urls = [s["url"] for s in shots if s.get("url")]
publish("post", draft_text, target_url, media_urls=urls)
```

`illustrate_set` recebe de 2 a 10 prompts e retorna uma lista de resultados
de `illustrate()` na ordem. O LinkedIn não permite misturar imagens com
vídeo em um mesmo post.

## Regras rígidas

- Uma imagem por requisição (`n>1` não é suportado); para um grid de
  múltiplas imagens, use `illustrate_set` (ela gera um prompt de cada vez
  por baixo dos panos).
- Mantenha palavras reais no `overlay`, não embutidas na arte do prompt.
- Respeite o custo do usuário: padrão para o modelo barato + resolução 1K a
  menos que solicitado.
- Nunca anexe uma imagem que o usuário não tenha visto e aprovado.
