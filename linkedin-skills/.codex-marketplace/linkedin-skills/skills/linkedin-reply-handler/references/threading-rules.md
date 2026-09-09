# Regras de Threading de Comentários do LinkedIn

## Achatamento em dois níveis

A interface do LinkedIn mostra respostas com até dois níveis de profundidade. Toda resposta, não importa quantos turnos lógicos de conversa se passaram, é armazenada com `parentComment` apontando para o comentário de NÍVEL SUPERIOR.

```
Publicação (urn:li:activity:P)
│
├─ Comentário A (id: 111)             ← nível superior
│    parentComment: nenhum
│    URN: urn:li:comment:(urn:li:activity:P, 111)
│
│  ├─ Resposta B (id: 222)             ← 2º nível
│  │    parentComment: urn:li:comment:(urn:li:activity:P, 111)
│  │
│  └─ Resposta C (id: 333)             ← AINDA 2º nível (sob o Comentário A)
│       parentComment: urn:li:comment:(urn:li:activity:P, 111)
│       (NÃO sob a Resposta B, mesmo que logicamente C responda a B)
│
└─ Comentário D (id: 444)             ← nível superior
     parentComment: nenhum
```

## Regra de publicação

Ao chamar `POST /linkedin-comments` com `parentComment`:
- Se você está respondendo a um comentário de nível superior → `parentComment` = o URN desse comentário
- Se você está respondendo a uma resposta de 2º nível → `parentComment` = o URN do comentário de NÍVEL SUPERIOR (suba a árvore)
- Se `parentComment` for omitido, o comentário é publicado como nível superior

## Por que isso importa

Um URN de parentComment errado causa um destes:
- 400 Bad Request (algumas publicações rejeitam de imediato)
- Comentário publicado silenciosamente sob o pai errado (o usuário o vê no lugar errado)
- Comentário fica órfão se o URN de 2º nível for rejeitado

## Derivando o URN do comentário de NÍVEL SUPERIOR

Dado o URN de uma resposta de 2º nível, busque a árvore de comentários da publicação e suba:

```python
def find_top_comment_urn(post_urn: str, comment_id: str, post_comments: list) -> str:
    for top in post_comments:  # cada elemento é um dict de comentário de nível superior
        if top["id"] == comment_id:
            return f"urn:li:comment:({post_urn},{comment_id})"
        for reply in top.get("replies", []):
            if reply["id"] == comment_id:
                return f"urn:li:comment:({post_urn},{top['id']})"
    raise ValueError("Comment not found in tree")
```

## Formatos de URL que a skill aceita

**Link direto do comentário de nível superior:**
```
https://www.linkedin.com/feed/update/urn:li:activity:P?commentUrn=urn%3Ali%3Acomment%3A%28activity%3AP%2C111%29
```

**Link de resposta (observe a query `replyUrn`):**
```
https://www.linkedin.com/feed/update/urn:li:activity:P?commentUrn=urn%3Ali%3Acomment%3A%28activity%3AP%2C111%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3AP%2C222%29
```

Quando `replyUrn` está presente, esse é o comentário específico sendo respondido (para reações). O `commentUrn` já é o pai de nível superior.

## Alvos de reação

Reações podem ser colocadas em:
- A própria publicação (`post_urn` passado para `create_reaction`)
- Qualquer comentário ou resposta (passe o URN do comentário como `post_urn` — sim, um nome meio confuso)

Fluxo padrão: reagir no comentário específico sendo respondido. Nunca pule a reação — uma resposta pura sem reação soa transacional.
