# Medidas de Posição Relativa

Quartis, Decis e Percentis

## Quartis

Os quartis dividem um conjunto de dados ordenado em quatro partes iguais. Eles são:

!!! info Primeiro Quartil (Q_1):

    $$
    Q_1 = \text{Valor na posição} \left(\frac{n + 1}{4}\right)
    $$

    É o valor que separa os 25% menores dados dos 75% maiores dados.

!!! info Segundo Quartil (Q_2) ou Mediana:

    $$
    Q_2 = \text{Valor na posição} \left(\frac{n + 1}{2}\right)
    $$

    Também conhecido como mediana, separa os 50% menores dados dos 50% maiores dados.

!!! info Terceiro Quartil (Q_3):

    $$
    Q_3 = \text{Valor na posição} \left(\frac{3(n + 1)}{4}\right)
    $$

    É o valor que separa os 75% menores dados dos 25% maiores dados.

    onde (n) é o número total de valores no conjunto de dados.

## Decis

Os decis dividem um conjunto de dados ordenado em dez partes iguais. Cada décimo (ou "decis") corresponde a uma posição que separa os dados em 10% das observações.

$$
d_i = \text{Valor na posição} \left(\frac{i(n + 1)}{10}\right)
$$

onde (i) varia de 1 a 9 e (n) é o número total de valores no conjunto de dados. O décimo 1 ((d_1)) é o primeiro decis, (d_2) é o segundo, e assim por diante até o nono decis ((d_9)).

## Percentis

Os percentis dividem um conjunto de dados ordenado em cem partes iguais. Cada percentil corresponde a um ponto que separa os dados em 1% das observações.

1º: Ordenar os dados do menor para o maior (ordem crescente);
2º: Calcular a posição ocupada pelo percentil (Pk) por meio da seguinte fórmula:

onde, n é o tamanho da amostra, k é o percentil que se deseja calcular e L é a posição do percentil na amostra.

$$
L=\left(\frac{k}{100}\right).n
$$

- Se o valor de L é um número inteiro: o percentil Pk será obtido pela média entre os valores que ocupam as posições L e L+1.
- Se o valor de L é um número decimal: devemos arredondar o valor de L para o maior inteiro mais próximo, aí sim o percentil Pk será obtido pelo valor que ocupa a posição L já arrendondada

$$
P_k = \text{Valor na posição} \left(\frac{k(n + 1)}{100}\right)
$$

onde (k) varia de 1 a 99 e (n) é o número total de valores no conjunto de dados. O percentil 25 (P_{25}) é o primeiro quartil, o percentil 50 (P_{50}) é a mediana, e o percentil 75 (P_{75}) é o terceiro quartil.

## Desvio Padrão

O desvio padrão é uma medida que expressa a quantidade de variação ou dispersão dos valores de um conjunto de dados. Quanto maior o desvio padrão, mais dispersos estão os dados em relação à média. Quanto menor o desvio padrão, mais concentrados estão os dados em torno da média.

!!! info Desvio Padrão da População

    Se você está lidando com uma população inteira, a fórmula do desvio padrão é:

    $$
    \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}
    $$

    onde:

    - $\sigma$ é o desvio padrão da população,
    - $N$ é o número total de valores na população,
    - $x_i$ representa cada valor individual da população,
    - $\mu$ é a média da população.

!!! info Desvio Padrão da Amostra

    Se você está lidando com uma amostra de uma população, a fórmula do desvio padrão é:

    $$
    s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
    \newline
    .\\
    .\\
    Exemplo:\newline
    U=\{71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83\}
    \\
    \bar{x} = \frac{71+73+73+74+74+75+76+77+77+79+81+83}{12}=76.0833
    \\
    s = \sqrt{\frac{
        (71-76.0833)^2+
        (73-76.0833)^2+
        ...
        (83-76.0833)^2
    }{12-1}} = 3.5280

    $$

    - $s$ é o desvio padrão da amostra,
    - $n$ é o número total de valores na amostra,
    - $x_i$ representa cada valor individual da amostra,
    - $\bar{x}$ é a média da amostra.

- Desvio padrão da população ($\sigma$): Utiliza $N$ no denominador, pois calcula a dispersão em relação à média da população inteira.
- Desvio padrão da amostra ($s$): Utiliza $n−1$ no denominador, um ajuste conhecido como correção de Bessel, para compensar o fato de que a amostra é uma estimativa da população.

## Escore z ou escore padronizado

- O objetivo de se calcular o escore z é expressar em unidades de desvio padrão quanto um determinado número está distante da média. 
- Para o cálculo do escore z é necessário conhecer a média ( )e o desvio padrão (s):

$$
z=\frac{x - \bar{x}}{s}
\\
.\\
.\\
Exemplo:\\
z=\frac{83− 76.0833}{3.5280}= +1.9605
\\
z=\frac{71− 76.0833}{3.5280}= -1.4408

$$
