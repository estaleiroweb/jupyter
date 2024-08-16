# Medidas de Tendência Central

São valores que tendem a resumir a minha amostra  de forma que esse valor tende estar no centro dessa distribuição

!!! info Média aritmética simples
    $$
    \bar{x} = \frac{\sum x_i}{n}
    $$
    A média aritmética simples é uma medida que representa o valor central de um conjunto de dados. Ela é calculada somando todos os valores e dividindo pelo número total de valores.
  
!!! info Média Aritmética Composta
    $$
    \bar{x}_c = \frac{\sum_{i=1}^{n} (x_i \cdot w_i)}{\sum_{i=1}^{n} w_i}
    $$

    A média aritmética composta é uma medida usada quando os valores têm diferentes pesos ou importâncias. É calculada somando o produto de cada valor pelo seu peso e dividindo pela soma dos pesos.

!!! info Mediana
    Se \(n\) é ímpar:
    $$
    \text{Mediana} = x_{\left(\frac{n+1}{2}\right)}
    $$
    Se \(n\) é par:
    $$
    \text{Mediana} = \frac{x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2} + 1\right)}}{2}
    $$

    A mediana é o valor que divide um conjunto de dados ordenados ao meio. Se o número de valores for ímpar, é o valor central. Se o número de valores for par, é a média dos dois valores centrais.

!!! info Moda
    A moda é a medida de tendência central que representa o valor ou os valores que aparecem com maior frequência em um conjunto de dados. Um conjunto de dados pode ter:

    - Uma única moda (unimodal): quando apenas um valor aparece com a maior frequência.
    - Duas modas (bimodal): quando dois valores aparecem com a mesma frequência máxima.
    - Mais de duas modas (multimodal): quando vários valores aparecem com a mesma frequência máxima.
    - Amodal ou Nenhuma moda: quando todos os valores aparecem com a mesma frequência ou se a frequência máxima é única para vários valores.

## Discrepante

Valor Discrepante: É um valor que se afasta muito dos outros valores no conjunto de dados. Esses valores são frequentemente identificados através de métodos estatísticos e gráficos.

1. Método do Desvio Padrão:
   - Valores que estão a mais de 2 ou 3 desvios padrão da média podem ser considerados discrepantes.
     > Se um valor \( x_i \) está a mais de 2 ou 3 desvios padrão (\( \sigma \)) da média (\( \mu \)), pode ser considerado um valor discrepante:
     > 
     > $$ |x_i - \mu| > k \cdot \sigma $$
     > 
     > onde \( k \) é um fator, geralmente 2 ou 3.
2. Método do Intervalo Interquartil (IQR):
  - Valores que estão fora do intervalo interquartil ajustado por um fator multiplicador, tipicamente 1.5, são considerados discrepantes.
    > $$ \text{IQR} = Q_3 - Q_1 $$
    >
    > Valores discrepantes são definidos como:
    > $$ x_i < Q_1 - 1.5 \times \text{IQR} $$
    > $$ x_i > Q_3 + 1.5 \times \text{IQR} $$
    >
    > onde \( Q_1 \) é o primeiro quartil e \( Q_3 \) é o terceiro quartil.
3. Gráficos de Dispersão e Boxplots:
   - Gráficos de Dispersão: Permitem visualizar a distribuição dos dados e identificar valores que se destacam.
   - Boxplots: Usam caixas e bigodes para mostrar a mediana, quartis e possíveis valores discrepantes.

## Qual é a melhor medida de tendência central?

De preferência trabalhando com média que envolve todos os valores.
Se a média e a mediana forem similares ou quase similares significa que há uma possibilidade de ausência de valor discrepante. Neste caso poderemos trabalhar com a média com medida de tendência Central.

Caso haja valores discrepantes devemos analisar se os valores discrepantes realmente são passíveis de acontecer ou apenas eventualidades.
A mediana irá mitigar a possibilidade de valores discrepantes caso haja.
