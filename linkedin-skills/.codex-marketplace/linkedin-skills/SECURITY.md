# Política de Segurança

## Versões Suportadas

Somente a versão mais recente lançada deste pacote de skills recebe atualizações
de segurança. Instale a partir da branch `main` ou do release mais novo com tag.

| Versão | Suportada |
| ------- | --------- |
| release mais recente | sim |
| tags antigas | não |

## Reportando uma Vulnerabilidade

Se você encontrar um problema de segurança neste repositório (por exemplo: uma
instrução de skill que possa ser explorada para injeção de prompt, um script que
manipula credenciais de forma incorreta, ou um padrão de comando inseguro), por favor
reporte de forma privada:

- **Preferencial:** abra um relatório privado via
  [GitHub Security Advisories](https://github.com/sergebulaev/linkedin-skills/security/advisories/new)
- **Alternativa:** envie um e-mail para `s@bulaev.org` com o assunto `[SECURITY] linkedin-skills`

Por favor, inclua:

1. Uma descrição do problema e onde ele está (caminho do arquivo, nome da skill)
2. Passos para reproduzir ou uma prova de conceito
3. O impacto que você acredita que ele tem

Você pode esperar uma confirmação de recebimento em até 72 horas e uma correção ou
decisão de divulgação pública em até 14 dias.

## Notas de escopo

- Este pacote nunca distribui credenciais fixas no código. Os tokens de API (Apify,
  Publora) são lidos de variáveis de ambiente ou arquivos `.env` que estão no
  gitignore; veja `.env.example`.
- Os scripts em `lib/` e `scripts/` fazem chamadas HTTP apenas para as APIs do Apify,
  Publora e Pixfaro, e nunca constroem um comando a partir de conteúdo remoto.
  Um caminho de código realmente executa um comando: o backend opcional "DIY" do Nível 2
  executa o que quer que `LINKEDIN_SKILLS_CUSTOM_POSTER` nomeie, via `subprocess`
  sem shell. Essa variável não é definida por padrão; qualquer coisa capaz de
  defini-la ganha execução de código na próxima publicação aprovada, então trate-a como uma
  credencial.
- Conteúdo obtido do LinkedIn pela camada de leitura do Apify é entrada não confiável
  para o agente. Veja `references/untrusted-content.md`.
- Por favor, não teste vulnerabilidades contra serviços de terceiros
  (LinkedIn, Apify, Publora) fora dos seus próprios programas de divulgação.
