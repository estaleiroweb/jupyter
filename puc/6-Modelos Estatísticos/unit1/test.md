# Test

## Pergunta 1

A partir de um desenvolvido para avaliar os cursos de graduação ofertados no país. O modelo de regressão múltipla foi estimado pelo método de mínimos quadrados ordinários (MQO) e apresentou os seguintes resultados para o Fator de Tolerância (1/VIF) e Fator Inflacionário da Variância (VIF):

| Variable |   VIF |    1/VIF |
| -------- | ----: | -------: |
| pobres   | 14.88 | 0.067190 |
| educacao |  7.41 | 0.134940 |
| theil    |  4.64 | 0.215448 |

Pelos valores apresentados para o (1/VIF) e (VIF), é correto afirmar que o modelo apresenta

Grupo de escolhas da pergunta

- [x] a. Multicolinearidade
- [ ] b. Homocedasticidade
- [ ] c. Autocorrelação
- [ ] d. heterocedasticidade

## Pergunta 2

Considere um conjunto de dados fictício que relaciona o preço de casas (variável dependente) com o tamanho da casa (variável independente 1) e o número de quartos (variável independente 2).

    Multiple linear regression model:
        Coefficients:
                     Estimate  Std. Error  t value  Pr(>|t|)
    (Intercept)      10.032      1.234       8.125    0.000
    Tamanho_casa     0.905       0.123       7.352    0.000
    Num_quartos      2.317       0.543       4.271    0.001
    Residual standard error: 5.012 on 47 degrees of freedom
    Multiple R-squared:  0.842,    Adjusted R-squared:  0.832
    F-statistic:  82.19 on 2 and 47 DF,  p-value: 0.000123

Métricas de avaliação:

- AIC: 275.34
- BIC: 285.55
- MAE: 3.42
- MSE: 24.63

Selecione a alternativa que melhor interpreta a saída da regressão

Grupo de escolhas da pergunta

- [ ] a. Para cada unidade adicional no tamanho da casa, espera-se um aumento de $1.234 no preço da casa. Mantendo o tamanho da casa constante, para cada quarto adicional, espera-se um aumento de $1.543 no preço da casa. O coeficiente de determinação (R²) é 0.729, o que significa que o modelo explica 72.9% da variabilidade observada nos preços das casas.
- [x] b. Para cada unidade adicional no tamanho da casa, espera-se um aumento de $0.905 no preço da casa. Mantendo o tamanho da casa constante, para cada quarto adicional, espera-se um aumento de $2.317 no preço da casa. O modelo explica 83.2% da variabilidade observada nos preços das casas.
- [ ] c. Para cada unidade adicional no tamanho da casa, espera-se um aumento de $0.905 no preço da casa. Mantendo o tamanho da casa constante, para cada quarto adicional, espera-se um aumento de $2.317 no preço da casa. O coeficiente de determinação (R²) é 0.729, o que significa que o modelo explica 72.9% da variabilidade observada nos preços das casas.
- [ ] d. Para cada unidade adicional no tamanho da casa, espera-se um aumento de $2.317 no preço da casa. Mantendo o tamanho da casa constante, para cada quarto adicional, espera-se um aumento de $0.905 no preço da casa. O coeficiente de determinação (R²) é 0.842, o que significa que o modelo explica 84.2% da variabilidade observada nos preços das casas.

## Pergunta 3

Na regressão linear simples, os resíduos são as diferenças entre os valores observados e os valores previstos pelo modelo de regressão.

Por que é importante verificar a distribuição dos resíduos na análise de regressão linear simples?

Grupo de escolhas da pergunta

- [ ] a. A distribuição dos resíduos indica a precisão do modelo de regressão.
- [ ] b. A distribuição dos resíduos fornece informações sobre a normalidade dos dados.
- [x] c. A distribuição dos resíduos ajuda a identificar possíveis violações das suposições do modelo.
- [ ] d. A distribuição dos resíduos não é importante na análise de regressão linear simples.

## Pergunta 4

Na regressão linear simples, o coeficiente de determinação (R²) é uma medida que indica a proporção da variabilidade na variável dependente explicada pela variável independente.

Como você interpretaria um valor de R² igual a 0,75 em um modelo de regressão linear simples?

Grupo de escolhas da pergunta

- [x] a. Isso significa que 75% da variabilidade na variável dependente é explicada pela variável independente.
- [ ] b. Isso significa que 75% da variabilidade na variável independente é explicada pela variável dependente.
- [ ] c. Isso significa que 75% da variabilidade na população é explicada pelo modelo de regressão.
- [ ] d. Isso significa que o modelo de regressão explica 75% da variabilidade total nos dados.
