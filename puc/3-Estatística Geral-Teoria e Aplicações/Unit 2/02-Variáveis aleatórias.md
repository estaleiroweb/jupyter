# Variáveis aleatórias

O resultado de um experimento probabilístico pode ser, frequentemente, uma
contagem ou uma medida. Quando isso ocorre, o resultado é chamado de variável aleatória.

A variável aleatória x representa um valor numérico associado a cada um dos
resultados de um experimento probabilístico. Alguns exemplos de variáveis aleatórias seriam:

- Número de coroas numa jogada de uma moeda, ou seja, x = 0 ou 1.
- Número de fregueses que entram numa grande loja no espaço de 20 minutos, ou seja, x = 0, 1, 2, ...
- Altura (em metros) dos estudantes numa sala de aula, ou seja, 1,40 < x < 2,20.

Existem dois tipos de variáveis aleatórias: as discretas e as contínuas.

- Uma variável aleatória é discreta se assume valores que podem ser contados, ou seja, se houver um número finito ou contável de resultados possíveis que possam ser enumerados;
- Uma variável é considerada contínua quando pode assumir qualquer valor dentro de um intervalo, ou seja, se houver um número incontável de resultados possíveis, representados por um intervalo sobre o eixo real.

## Exercício 1

Determine se a variável aleatória X é discreta ou contínua:

1. Número de acidentes numa semana: Discreta
1. Número de defeitos em uma peça: Discreta
1. Duração de uma conversa telefônica: Contínua
1. Número de falhas numa safra: Discreta
1. Tempo necessário para produzir uma peça: Contínua
1. Peso de contêineres contendo minério de ferro: Contínua

## Variáveis aleatórias discretas

### Distribuição discreta de probabilidade

A cada valor de uma variável aleatória discreta pode ser atribuída uma probabilidade. Ao enumerar cada valor da variável aleatória com a sua probabilidade correspondente, forma-se uma distribuição de probabilidade.

Definição: Uma distribuição discreta de probabilidade enumera cada valor que a variável aleatória pode assumir, ao lado de sua probabilidade. Uma distribuição de probabilidade deve satisfazer às seguintes condições:

- A probabilidade de cada valor da variável discreta deve estar no intervalo de 0 a 1, ou seja, 0< P(X=x) < 1;
- A soma de todas as probabilidades deve ser 1, ou seja, P(X=xi) = 1.

Uma vez que as probabilidades representam frequências relativas, uma distribuição discreta de probabilidade pode ser representada da seguinte maneira:

P(X=x1) = x1
P(X=x2) = x2
P(X=x3) = x3
...
P(X=xn) = xn

Uma observação sobre notação: variáveis aleatórias sempre devem ser denotadas com letra maiúscula e os valores assumidos pelas variáveis serão denotados pelas letras minúsculas correspondentes. Portanto, a variável X pode assumir o valor xi, e i = 1, 2, 3, ...

### Função de Distribuição Acumulada

Definição: Dada a variável aleatória X, chamaremos de função de distribuição acumulada (f.d.a.), ou simplesmente função de distribuição (f.d.) a função:

F(x) = P(X < x)

Média, Variância e Desvio Padrão para variáveis aleatórias discretas

É possível medir a tendência central de uma distribuição de probabilidade por meio de sua média e determinar a variabilidade por meio de sua variância e desvio padrão. A média de uma variável aleatória discreta é definida da seguinte maneira:

A média ou valor esperado ou ainda a esperança matemática de uma variável aleatória discreta é dada por: $\mu=(\sum{x_i . P(X=x_i)})$. Cada valor de x deve ser multiplicado por sua probabilidade correspondente e os produtos devem ser somados

Embora a média da variável aleatória de uma distribuição de probabilidade descreva um resultado típico, ela não fornece informações sobre a variabilidade dos resultados. Para estudar a variação dos resultados, podem-se usar a variância e o desvio padrão da variável aleatória de uma distribuição de probabilidade.

A variância de uma variável aleatória discreta pode ser obtida por: $\sigma^2=E(X^2)-\mu^2$, onde $E(X^2)=(\sum{x_i^3 . P(X=x_i)})$. O desvio padrão, como já foi visto, é obtido pela raiz quadrada da variância : $\sigma=\sqrt{\sigma^2}$

### Propriedades da Esperança Matemática

1. Propriedade 1: Se X = c, onde c é uma constante, então $E(X) = c$.
1. Propriedade 2: Suponha-se que c seja uma constante e X seja uma variável aleatória. Então $E(cX) = cE(X)$.
1. Propriedade 3: Sejam X e Y duas variáveis aleatórias quaisquer. Então, $E(X+Y) = E(X) + E(Y)$.
   - Se $Y = aX + b$, onde a e b são constantes, então $E(Y) = aE(X) + b$. \
     Em linguagem corrente: o valor esperado de uma função linear de $X$.\
     Isto não será verdadeiro, a menos que se trate de função linear.
   - Sejam n variáveis aleatórias $X_1, X_2, ..., X_n$. Então, $E(X_1 + X_2 +...+ X_n) = E(X_1) + E(X_2) + ... + E(X_n)$.

### Propriedades da Variância

1. Propriedade 1: Se c é uma constante, então $Var(X+c) = Var(X)$.
1. Propriedade 2: Suponha-se que c seja uma constante e X seja uma variável aleatória. Então $Var(cX) = c2Var(X)$.
1. Propriedade 3: Se (X , Y) for uma variável aleatória bidimensional, e se X e Y forem independentes. Então, $Var(X+Y) = Var(X) + Var(Y)$.\
   Comentário: É importante compreender que a variância não é, em geral, aditiva, como é o valor esperado. Com a hipótese complementar de independência a propriedade torna-se válida. A variância também não possui a propriedade de linearidade do valor médio, isto é, $Var(aX+b)≠aVar(X)+b$. Em vez disso, teremos $Var(aX+b)=a2Var(X)$.

> As propriedades da média e da variância apresentadas são válidas tanto para variáveis aleatórias discretas quanto para variáveis aleatórias contínuas.

### Variáveis aleatórias contínuas

As variáveis aleatórias contínuas são aquelas que assumem seus valores em uma escala real e que se ajustam de tal maneira às situações práticas que podem ser consideradas adequadas para fornecer respostas a hipóteses de interesse. Elas surgem da mensuração em uma escala, como peso, tempo, distância ou volume, por exemplo.

Definição: Uma variável aleatória X, definida sobre o espaço amostral  e assumindo valores num intervalo de número reais, é dita uma variável aleatória contínua.

Exemplos: Salário de indivíduos, tempo de espera em uma fila, precipitação pluviométrica, altura, temperatura, etc.

#### Função densidade de probabilidade

**Definição**: Diz-se que X é uma variável aleatória contínua, se existir uma função f(x), denominada função densidade de probabilidade (f.d.p.) de X que satisfaça as seguintes condições:

1. $f(x) > 0$, para todo x;
1. A área definida por $f(x)$ é igual a 1, ou seja, $\int_{-\infin}^{+\infin}{f(x)dx=1}$
1. Para quaisquer $a$ e $b$, com $--\infin < a < b< +\infin$, teremos. $P(a \leq X \leq b)=\int_{a}^b f(x) dx$.

Uma conseqüência de 3. é que, para qualquer valor especificado de X, digamos x0, teremos $P(X = x_0) = 0$, porque $P(X=x_0)= \int_{x_0}^{x_0} f(x)dx=0$.

Na prática, isso poderia parecer contraditório. Então a probabilidade de um indivíduo ter exatamente 1,75m de altura é zero? É impossível existir um indivíduo com essa estatura? Para resolver isso, devemos admitir que a precisão dos instrumentos de medida é limitada. Na prática, 1,75 não se distingue de qualquer outro valor no intervalo, digamos, [1,745 ; 1,755], ou [1,7495 ; 1,7505]. O que nos interessa é, na realidade, a probabilidade de a variável aleatória estar em um intervalo, por pequeno que seja, e a probabilidade correspondente então já não é zero.

Em consequência disso – e ao contrário do que ocorre com as v. a. discretas –
é indiferente considerarmos, ou não, os extremos quando especificamos um intervalo de uma v. a. contínua, ou seja,

$$P( a < x < b)=P(a \leq x < b)=P(a < x \leq b)=P(a \leq x \leq b)$$

Comentário: f(x) não representa probabilidade alguma! Anteriormente já salientamos que, por exemplo, P(X = 2) = 0 e, conseqüentemente, f(2)
certamente não representa essa probabilidade. Somente quando a função for integrada entre dois limites, ela produzirá uma probabilidade.

Média, Variância e Desvio Padrão para variáveis aleatórias contínuas
O valor esperado ou média da variável aleatória contínua X, com função densidade de probabilidade dada por f(x), é obtida pela expressão:

$$
E(X) = \mu = \int_{-\infin}^{+\infin} xf(x)dx
$$

Para uma variável aleatória X com densidade f(x), a variância é dada por:

$$
Var(X) = \int_{-\infin}^{+\infin} (x-\mu)^2 f(x)dx
$$

Como no caso discreto, a variância é a medida de dispersão mais utilizada na prática. Aqui podemos, também, utilizar a expressão alternativa:

$$
Var(X) = E(X^2) - \mu^2
$$

onde $E(X^2)$ é calculado por $E(X^2) = \int_{-\infin}^{+\infin} x^2 f(x)dx$

O desvio padrão é a raiz quadrada da variância e, como já sabemos, tem a mesma unidade de medida da variável original, o que facilita sua interpretação.
