# Medidas de dispersão

## Amplitude

- A notação utilizada para representar a amplitude é: A.
- É definida como sendo a diferença entre o maior e o menor valor do conjunto de dados.
- A vantagem da amplitude é sua facilidade de cálculo porém, tem a desvantagem de levar em conta apenas dois valores, desprezando todos os outros.

## Variância e Desvio Padrão

- A variância e o desvio padrão medem a variação do conjunto de dados em torno da média. 
- As notações utilizadas para representarmos as duas medidas são:
  - $\sigma^2$: Variância populacional (Parâmetro)
  - $s^2$: Variância amostral (Estatística)
  - $\sigma$: Desvio padrão populacional (Parâmetro)
  - $s$: Desvio padrão amostral (Estatística)

!!! info Cálculo da variância amostral

    $$s^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$$

    onde:

    - $s$ é a variância amostral
    - $n$ é o número total de valores na amostra
    - $x_i$ representa cada valor individual da amostra
    - $\bar{x}$ é a média da amostra.

!!! info Cálculo da variância populacional

    $$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$$

    onde:

    - $\sigma^2$ é a variância populacional
    - $N$ é o número total de valores na população
    - $x_i$ representa cada valor individual da população
    - $\mu$ é a média da população.

- É possível perceber que a unidade de medida da variância equivale à unidade de medida dos dados ao quadrado. Dessa maneira, é mais comum trabalharmos com a raiz quadrada da variância, ou seja, com o desvio padrão.

## Coeficiente de Variação

- O desvio padrão embora seja a medida de dispersão mais utilizada, ela mede a dispersão em termos absolutos.
- O coeficiente de variação definido por
  > mede a dispersão em termos relativos.

$$
CV\%=\frac{s}{\bar{x}}.100
$$

- O coeficiente de variação torna-se útil quando queremos comparar a variabilidade de observações com diferentes unidades de medidas.
