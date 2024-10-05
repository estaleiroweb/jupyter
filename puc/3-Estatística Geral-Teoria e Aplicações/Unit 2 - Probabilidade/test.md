# Test

## Pergunta 1

A distribuição da altura de 500 estudantes do sexo masculino de uma escola é aproximadamente Normal com média igual a 1,70 metro e desvio padrão igual a 2,5 centímetros. Aproximadamente quantos têm altura superior a 1,65m?



Para resolver esse problema, precisamos calcular a probabilidade de um estudante ter altura superior a 1,65 metros. Como a altura é normalmente distribuída, utilizaremos a distribuição normal padrão.

- [ ] 239
- [ ] 250
- [x] 489
- [ ] 11

A variável altura dos alunos tem uma distribuição normal com média = 1,70 metros e desvio padrão = 0,025 metros (É necessário uniformizar as unidades de medida). Devemos então calcular:

P(X>1,65)=P(Z> -2) = 0.5+0,4772 = 0,9772 x 500 alunos = 488,6.

**Passo 1: Converter a altura para um valor z**

A fórmula para calcular o valor z é:

$$ z = \frac{X - \mu}{\sigma} $$

onde:
- $X = 1,65$ metros (a altura que queremos comparar)
- $\mu = 1,70$ metros (média)
- $\sigma = 0,025$ metros (desvio padrão, convertido de 2,5 cm)

$$ z = \frac{1,65 - 1,70}{0,025} = \frac{-0,05}{0,025} = -2 $$

**Passo 2: Encontrar a probabilidade associada ao valor z**

Usando uma tabela da distribuição normal padrão, encontramos a probabilidade associada a $z = -2$.

A probabilidade de $z < -2$ é aproximadamente 0,0228. Como queremos a probabilidade de altura superior a 1,65 metros (ou $z > -2$), subtraímos este valor de 1:

$$ P(z > -2) = 1 - 0,0228 = 0,9772 $$

**Passo 3: Calcular o número de estudantes**

Multiplicamos a probabilidade pelo número total de estudantes (500):

$$ 0,9772 \times 500 = 488,6 $$

Arredondando para o número inteiro mais próximo, temos aproximadamente 489 estudantes.

**Resposta correta: 489**.

## Pergunta 2

Uma indústria de tintas recebe pedidos de seus vendedores através de telefone e internet. O número médio de pedidos, que chegam por qualquer meio, é de 5 por hora. Em um dia de trabalho (8 horas), qual seria a probabilidade de haver 50 pedidos?

- [x] 0,0177
- [ ] 0,0227
- [ ] 0,0575
- [ ] 0,177


Aplicando a distribuição Poisson com parâmetro igual a 5x8=40 pedidos em um dia de trabalho, temos então que calcular: P(X=50).

$$ P(X = 50) = \frac{40^{50} \cdot e^{-40}}{50!} $$

## Pergunta 3

O tempo de utilização de um caixa eletrônico por clientes de um certo banco, em minutos,  foi modelado por uma variável T com distribuição exponencial com parâmetro igual a 3. Determine a probabilidade de que um cliente demore menos de um minuto utilizando o caixa eletrônico.

- [ ] 0,0474
- [ ] 0,0498
- [x] 0,9502
- [ ] 0,8512

Temos uma variável aleatória modelada pela distribuição exponencial com parâmetro igual a 3. Devemos calcular: P(T<1)=P(0<T<1)=0,9502.

Para resolver esse problema, utilizamos a distribuição exponencial, que é adequada para modelar o tempo entre eventos em um processo de Poisson.

A função de densidade de probabilidade (PDF) de uma distribuição exponencial é dada por:

$$ f(t) = \lambda e^{-\lambda t} $$

onde:
- $\lambda = 3$ (o parâmetro da distribuição exponencial)
- $t$ é o tempo (em minutos) que estamos interessados

Queremos calcular a probabilidade de que o tempo $T$ seja menor que 1 minuto, ou seja, $P(T < 1)$.

A probabilidade acumulada $P(T < t)$ para uma distribuição exponencial é dada por:

$$ P(T < t) = 1 - e^{-\lambda t} $$

Substituindo $t = 1$ e $\lambda = 3$:

$$ P(T < 1) = 1 - e^{-3 \times 1} = 1 - e^{-3} $$

**Cálculo:**

$$ P(T < 1) = 1 - e^{-3} $$

Calculando $e^{-3}$:

$$ e^{-3} \approx 0,0498 $$

Portanto:

$$ P(T < 1) = 1 - 0,0498 \approx 0,9502 $$

**Resposta:** A probabilidade de que um cliente demore menos de um minuto utilizando o caixa eletrônico é aproximadamente **0,9502** ou **95,02%**.

## Pergunta 4

(Magalhães) A Tabela a seguir apresenta informações de alunos de uma universidade quanto às variáveis: Período, sexo e opinião sobre a reforma agrária.

[Reforma agrária]
| Período | Sexo      | Contra | A favor | Sem opinião |
| ------- | --------- | ------ | ------- | ----------- |
| Diurno  | Feminino  | 2      | 8       | 2           |
| ^^      | Masculino | 8      | 9       | 8           |
| Noturno | Feminino  | 4      | 8       | 2           |
| ^^      | Masculino | 12     | 10      | 1           |

Determine a probabilidade de escolhermos, aleatoriamente, uma pessoa do sexo masculino e sem opinião sobre a reforma agrária?

- [ ] 0,0811
- [x] 0,1216
- [ ] 0,1538
- [ ] 0,4865

Probabilidade da interseção entre os eventos 'sexo masculino' e 'sem opinião':

9/74=0,1216

Para calcular a probabilidade de escolher uma pessoa do sexo masculino e que esteja sem opinião sobre a reforma agrária, usamos a fórmula:

$$
P(\text{Masculino e Sem Opinião}) = \frac{\text{Número de pessoas do sexo masculino e sem opinião}}{\text{Número total de pessoas}}
$$

**Número de pessoas do sexo masculino e sem opinião:**

- Diurno: 8 pessoas
- Noturno: 1 pessoa

Total:
$$
8 + 1 = 9
$$

**Número total de pessoas:**

- Diurno, Feminino: $2 + 8 + 2 = 12$
- Diurno, Masculino: $8 + 9 + 8 = 25$
- Noturno, Feminino: $4 + 8 + 2 = 14$
- Noturno, Masculino: $12 + 10 + 1 = 23$

Total:
$$
12 + 25 + 14 + 23 = 74
$$

**Cálculo da probabilidade:**

$$
P(\text{Masculino e Sem Opinião}) = \frac{9}{74} \approx 0,1216
$$

**Resposta correta: 0,1216.**

## Pergunta 5

Uma companhia fabrica motores. As especificações requerem que o comprimento de uma certa haste deste motor esteja entre 7,48 cm e 7,52 cm. Os comprimentos destas hastes, fabricadas por um fornecedor, têm uma distribuição normal com média 7,505 cm e desvio padrão 0,01 cm. Qual a probabilidade de uma haste escolhida ao acaso estar dentro das especificações?

- [ ] 0,0606
- [ ] 0,5668
- [x] 0,9270
- [ ] 0,0062

Temos uma variável descrita pela distribuição normal com média igual a 7,505cm e desvio padrão 0,01 cm. Temos que calcular a seguinte probabilidade:

P(7,48<X<7,52)=P(-2,5<Z<1,5)=0,4938+0,4332=0,9270

Para encontrar a probabilidade de que o comprimento da haste esteja dentro do intervalo especificado, usamos a distribuição normal.

**Dados:**
- Média ($\mu$): 7,505 cm
- Desvio padrão ($\sigma$): 0,01 cm
- Intervalo de especificação: entre 7,48 cm e 7,52 cm

**Passos:**

1. **Converter os valores para a distribuição normal padrão ($z$):**

   A fórmula para calcular o valor $z$ é:

   $$
   z = \frac{X - \mu}{\sigma}
   $$

   Onde $X$ é o comprimento da haste.

   - Para $X = 7,48$ cm:
     $$
     z_{1} = \frac{7,48 - 7,505}{0,01} = \frac{-0,025}{0,01} = -2,5
     $$

   - Para $X = 7,52$ cm:
     $$
     z_{2} = \frac{7,52 - 7,505}{0,01} = \frac{0,015}{0,01} = 1,5
     $$

2. **Encontrar a probabilidade acumulada para esses valores de $z$:**

   Usando a tabela da distribuição normal padrão ou uma calculadora:

   - A probabilidade para $z < -2,5$ é aproximadamente 0,0062.
   - A probabilidade para $z < 1,5$ é aproximadamente 0,9332.

   A probabilidade de uma haste estar dentro do intervalo é dada por:

   $$
   P(7,48 < X < 7,52) = P(z < 1,5) - P(z < -2,5)
   $$

   Substituindo os valores:

   $$
   P(7,48 < X < 7,52) = 0,9332 - 0,0062 = 0,9270
   $$

**Resposta:** A probabilidade de que uma haste escolhida ao acaso esteja dentro das especificações é aproximadamente **0,9270** ou **92,70%**.
