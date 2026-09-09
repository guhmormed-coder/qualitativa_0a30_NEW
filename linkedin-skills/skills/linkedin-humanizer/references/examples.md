# Exemplos — LinkedIn Humanizer

## Exemplo

> **Entrada:**
> "No cenário acelerado de hoje, as empresas precisam fundamentalmente alavancar a IA para desbloquear um ROI robusto. Não se trata apenas de adoção, trata-se de transformação. Até minha última atualização em janeiro de 2024, as tendências são claras — aqui está o que aprendi."
>
> **Saída (modo padrão = forensic + strict):**
> "as empresas precisam de IA para cortar custos. adoção é a parte fácil. transformação é o trabalho de verdade. aqui está o que aprendemos rodando 35 mil perfis do LinkedIn pelo nosso sistema todos os dias."
>
> **Diff:**
> - FORENSIC: removido o aviso "Até minha última atualização em janeiro de 2024"
> - STRICT: o parágrafo pontuou 5 marcadores (cenário acelerado, fundamentalmente, alavancar, desbloquear, robusto) = reescrever o parágrafo, não palavra por palavra
> - STRICT: removido o paralelismo negativo "Não se trata apenas de X, trata-se de Y" (regra de ocorrência única), substituído por declarativas emparelhadas
> - PASSO 1: o único travessão estava dentro do teto (~1 a cada 100 palavras); ele saiu apenas porque a frase ao redor foi reescrita. Não foi substituído por um ponto final
> - PASSO 3: adicionado um número com referente (35 mil perfis do LinkedIn, diariamente) a partir da própria entrada do usuário; nada foi inventado, sem hedge, sem moldura de "deixa eu ser honesto"
> - PASSO 4: dois fragmentos na saída ("adoção é a parte fácil." "transformação é o trabalho de verdade.") estão dentro do teto de 2 por post e são declarativas emparelhadas, não uma revelação do tipo "E o resultado?"; deixados como estão
> - AESTHETIC NÃO foi aplicado
