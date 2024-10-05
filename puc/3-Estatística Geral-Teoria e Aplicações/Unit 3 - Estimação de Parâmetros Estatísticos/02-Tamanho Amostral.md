# Cálculo do Tamanho Amostral

- $n$: Tamanho da Amostra
- $E$: Margem de erro
- $z$: Valor crítico obtido a partir do nível de confiança. É encontrado na tabela da distribuição normal padrão
- $\sigma$: Desvio padrão da população
- $N$: Tamanho da população
- $\hat{p}$: Proporção de sucessos na amostra
- $\mu$: Média
- $p$: Proporção

!!! info Cálculo do $\sigma$

    A forma para o cálculo do tamanho amostral utilize o valor de $\sigma$ a parênteses desvio padrão populacional fecha parênteses, e se o $\sigma$ não for conhecido?

    - Utilizar a regra prática para estimar o desvio padrão da seguinte maneira:

    $$
    \sigma=\frac{Amplitude}{4}
    $$

    - Realizar um estudo piloto, iniciando o processo de amostragem.
    Com base na coleção de pelo menos 31 valores amostrais selecionados aleatoriamente, calcular o desvio padrão amostral s e utilizá-lo no lugar de $\sigma$

!!! info Cálculo do $\hat{p}$

    É interessante notar que a expressão para o cálculo do tamanho amostral depende de $\hat{p}$ que pode ser obtido por:

    - Estudo piloto ou de conhecimentos prévios
    - Quando dispomos de Tais informações, podemos atribuir o valor de 0,5 para $\hat{p}$, de forma que o tamanho da amostra resultante seja no mínimo tão grande quanto deveria ser

    | $\hat{p}$ | $(1-\hat{p})$ | $\hat{p}(1-\hat{p})$ |
    | --------- | ------------- | -------------------- |
    | 0,1       | 0,9           | 0,09                 |
    | 0,2       | 0,8           | 0,16                 |
    | 0,3       | 0,7           | 0,21                 |
    | 0,4       | 0,6           | 0,24                 |
    | **0,5**   | **0,5**       | **0,25**             |
    | 0,6       | 0,4           | 0,24                 |
    | 0,7       | 0,3           | 0,21                 |
    | 0,8       | 0,2           | 0,16                 |
    | 0,9       | 0,1           | 0,09                 |
    | 0,01      | 0,99          | 0,0099               |
    | 0,001     | 0,999         | 0,000999             |
    | 0,99      | 0,01          | 0,0099               |
    | 0,999     | 0,001         | 0,000999             |

!!! danger Amostra

    - O cálculo do tamanho da amostra deve ser arredondado para cima
    - A amostra deve refletir as características da população da qual foi retirada
    - Não é o tamanho da amostra que garante a representatividade da amostra, mas a forma como ela é obtida

## Para $\mu$ (média)

População Infinita:
$$
n = \left( \frac{z \cdot \sigma}{E} \right)^2
$$

População Finita:
$$
n = \frac{N \cdot \sigma^2 \cdot (z)^2}{(N - 1) \cdot E^2 + \sigma^2 \cdot (z)^2}
$$

## Para $p$ (Proporção)

População Infinita:
$$
n=\frac{z^2 \cdot \hat{p} \cdot (1 - \hat{p})}{E^2}
$$

População Finita:
$$
n=\frac{
    N \cdot \hat{p} \cdot (1 - \hat{p}) \cdot (z)^2
}{
    \hat{p} (1 - \hat{p}) \cdot (z)^2 + (N - 1) \cdot  E^2
}
$$
