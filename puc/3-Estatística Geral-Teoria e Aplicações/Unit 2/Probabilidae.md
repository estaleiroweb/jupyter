# Probabilidade

A probabilidade está diariamente presente em nossas vidas: “Será que vai chover?” e “Quem vai ganhar as eleições?” são algumas das várias perguntas que nos fazemos que envolve o cálculo de probabilidades.

O conceito de probabilidade é fundamental para o estudo de situações onde os
resultados são variáveis, isto é, situações em que os resultados possíveis são
conhecidos, mas não se pode saber a priori qual deles ocorrerá.

Os gestores freqüentemente fundamentam suas decisões em uma análise de incertezas, como:

- o Quais são as chances de queda das vendas se aumentarmos os preços?
- o Qual é a chance de um novo investimento ser lucrativo?
- o Qual é a probabilidade do projeto ser concluído no prazo?

!!! question  O que é a probabilidade?
    A probabilidade é uma medida numérica da possibilidade de um evento ocorrer. Valores probabilísticos são sempre atribuídos em uma escala de 0 a 1. Uma probabilidade próxima de 0 indica que é pouco provável que um evento ocorra; uma probabilidade próxima de 1 revela que a ocorrência de um evento é quase certa.

## Experimento aleatório

São aqueles experimentos cujos resultados podem não ser os mesmos, ainda que
sejam repetidos sob condições essencialmente idênticas. Além disso, não se conhece
um particular valor do experimento “a priori", porém podem-se descrever todos os
possíveis resultados, as possibilidades. Quando o experimento for repetido um grande
número de vezes surgirá uma regularidade.

Exemplos:

- E 1 : Lançamento de um dado e observar a face superior.
- E 2 :Lançamento de uma moeda quatro vezes e observar o número de caras.
- E 3 : Acompanhar os 30 alunos matriculados na disciplina e observar o número de aprovados.
- E 4 : Ligar uma lâmpada nova e observar o seu tempo de duração (em minutos).

## Espaço amostral

Chama-se espaço amostral o conjunto de todos os possíveis resultados de um
experimento aleatório ou, em outras palavras, é o conjunto universo relativo aos
resultados de um experimento.

Geralmente esse conjunto é representado pela letra . Assim, pode-se dizer que, a
cada experimento aleatório, sempre estará associado um conjunto de resultados
possíveis ou espaço amostral.

Aos experimentos aleatórios exemplificados anteriormente estão associados os
seguintes espaços amostrais, respectivamente:

- $\Omega_1$ = { 1, 2, 3, 4, 5, 6 }
- $\Omega_2$ = { 0, 1, 2, 3, 4 }
- $\Omega_3$ = { 0, 1, 2, ... 28, 29, 30 }
- $\Omega_4$ = { t  R | t  0 }

## Eventos

É um subconjunto de elementos do espaço amostral.

Aos espaços amostrais exemplificados anteriormente estão associados os seguintes
eventos, respectivamente:

```
A 1 = { 2, 4, 6 }, ou seja, obter uma face par.
B 2 = { 2 }, ou seja, obter duas caras.
C 3 = { 24, 25, 26, 27, 28, 29, 30 }, ou seja, pelo menos 80% de alunos
aprovados na disciplina.
D 4 = { t  10000 }, ou seja, a lâmpada durar pelo menos 10000 minutos.
```
##### AAxxiioommaass ddaa PPrroobbaabbiilliiddaaddee

```
Dado um espaço amostral, Ω, suponha que estamos estudando um evento A. A
probabilidade do evento A ocorrer é denotada por P(A). A função P(A) só será uma
probabilidade se ela satisfaz três condições básicas:
o 0 < P(A) < 1
o P() = 1
o P(A 1  A 2  A 3 ...) = P(A 1 )+P(A 2 )+P(A 3 )+..., se os eventos A 1 , A 2 ,... forem
disjuntos (isto é, mutuamente exclusivos).
```
##### CCoommoo aattrriibbuuiirr pprroobbaabbiilliiddaaddeess aaooss eelleemmeennttooss ddoo eessppaaççoo aammoossttrraall??

```
Existem várias maneiras de se atribuir probabilidades aos elementos do espaço
amostral, dentre elas, vamos citar:
```

```
Por meio das características teóricas do experimento (Visão clássica): Seja E um
experimento e Ω um espaço amostral, a ele associado, composto de n pontos
amostrais. Define-se a probabilidade da ocorrência de um evento A, indicada por P(A),
como sendo a relação entre o número de pontos favoráveis (f) à realização do evento
A e o número total de pontos (n), ou seja:
```
####  

```
Número total de casos possíveis
```
```
Número de casos favoráveis
PA
```
```
Por exemplo, ao lançarmos uma moeda equilibrada sabemos que, teoricamente, cada
face tem a mesma probabilidade de ocorrência, isto é, P(C) = P(C) = ½.
```
```
Por meio das freqüências de ocorrências (Visão frequentista): Se o fenômeno sob análise
puder ser repetido: indefinidamente, nas mesmas condições e de forma independente (sem
que uma repetição afete a seguinte), então, se A é um evento de interesse, a probabilidade
de ocorrência de A é dada por:
```
####  

```
Número total de repetições do experimento
```
```
Número de vezes que A ocorreu
PA 
```
```
Exemplo 1 : De acordo com o IBGE (1988), a distribuição dos suicídios
ocorridos no Brasil em 1986, segundo a causa atribuída foi a seguinte:
```
```
Causa do suicídio Freqüência
Alcoolismo (A) 263
Dificuldade financeira (F) 198
Doença mental (M) 700
Outro tipo de doença (O) 189
Desilusão amorosa (D) 416
Outras causas (C) 217
Total 1983
```
Ao selecionarmos aleatoriamente uma das pessoas que tentaram suicídio,
determine a probabilidade de que a causa atribuída tenha sido:
Desilusão amorosa:

####   02097

###### 1983

###### PD ^416  ,

```
Doença mental:
```
####   03530

###### 1983

###### PM ^700  ,

##### IInntteerrsseeççããoo ddee eevveennttooss

A interseção de dois eventos A e B corresponde à ocorrência simultânea dos eventos A e
B. Contém todos os pontos do espaço amostral comuns a A e B. É denotada por A  B. A
interseção é ilustrada pela área hachurada do diagrama de Venn abaixo.


##### EEvveennttooss ddiissjjuunnttooss oouu mmuuttuuaammeennttee eexxcclluussiivvooss

Dois eventos A e B são chamados disjuntos ou mutuamente exclusivos quando não
puderem ocorrer juntos, ou seja, quando não têm elementos em comum, isto é, A  B =.
O diagrama de Venn a seguir ilustra esta situação.

##### UUnniiããoo^ ddee eevveennttooss

A união dos eventos A e B equivale à ocorrência de A, ou de B, ou de ambos, ou seja, a
ocorrência de pelo menos um dos eventos A ou B. É denotada por A  B. A área
hachurada na figura abaixo ilustra esta situação.

Para encontrar a união de dois eventos deve-se utilizar a seguinte fórmula:

```
P(A  B) = P(A) + P(B) – P(A  B)
```
##### CCoommpplleemmeennttaarreess

Dois eventos A e B são complementares se sua união corresponde ao espaço amostral e
sua interseção é vazia. O diagrama a seguir ilustra tal situação.

###### 

###### 


```
o Para dois eventos A e B serem complementares: A  B =  e A  B =.
Além disso, AC = B e BC = A, ou seja, o complementar do evento A ocorre
quando o evento A não ocorrer!
o Pode-se observar também que: P(A) = 1- P(B) e que P(AC) = P(B) =1 –
P(A).
```
```
Exemplo: Estudo da relação entre o hábito de fumar e a causa da morte, entre
1000 empresários.
```
```
Fumante
```
```
Causa da morte
Total
Câncer (C) Doença
cardíaca (D)
Outros (O)
```
```
Sim (F) 135 310 205 650
Não (FC) 55 155 140 350
Total 190 465 345 1000
```
```
Um indivíduo é selecionado aleatoriamente entre os observados na amostra.
Determine as seguintes probabilidades:
a.) Ser fumante.
b.) Ter morrido de câncer.
c.) Não ser fumante e ter morrido de doença cardíaca.
d.) Ser fumante ou ter morrido de outras causas.
```
```
Resolução:
```
#### a.)   065

###### 1000

###### 650

###### PF   ,

#### b.)   019

###### 1000

###### 190

###### PC   ,

## c.)   0155

###### 1000

###### 155

###### PFCD   ,

#### d.)         0790

###### 1000

###### 205

###### 1000

###### 345

###### 1000

###### 650

###### PFO PF PO PFO     ,

##### PPrroobbaabbiilliiddaaddee ccoonnddiicciioonnaall

```
Em diversas situações práticas, a probabilidade de ocorrência de um evento A se
modifica quando dispomos de informação sobre a ocorrência de um outro evento
associado.
A probabilidade condicional de A dado B é a probabilidade de ocorrência do evento A,
sabido que o evento B já ocorreu. Pode ser determinada dividindo-se a probabilidade
de ocorrência de ambos os eventos A e B pela probabilidade de ocorrência do evento
B, como é mostrado a seguir:
```

####    

####  

####   , PB 0

###### PB

###### PA|B PA B

```
Da definição de probabilidade condicional, deduzimos a regra do produto de
probabilidades que é uma relação bastante útil:
```
#### PABPA|B.PB , PB 0

##### IInnddeeppeennddêênncciiaa ddee^ eevveennttooss^

```
Dois eventos A e B são independentes se a ocorrência de um deles não afeta a
```
#### probabilidade de ocorrência do outro, ou seja, PA|BPA e PB|APB. Se

#### dois eventos A e B são independentes então PABPA.PB.

```
Exemplo: Estudo da relação entre o criminoso e a vítima
```
```
Criminoso
Vítima
Total
Homicídio (H) Furto (F) Assalto (A)
Estranho (E) 12 379 727 1118
Conhecido (C) 39 106 642 787
Ignorado (I) 18 20 57 95
Total 69 505 1426 2000
```
```
Se uma pessoa é escolhida ao acaso entre os estudados na amostra. Determine as
probabilidades de:
a.) Ter sofrido um homicídio ou ter sido vítima de um estranho.
b.) Dado que a pessoa sofreu um assalto, ter sido vítima de um conhecido.
c.) A pessoa ter sofrido um furto, dado que ela foi vítima de um estranho.
```
```
Resolução:
```
#### a.)         0587

###### 2000

###### 12

###### 2000

###### 1118

###### 2000

###### 69

###### PHE PH PEPHE     ,^

#### b.)    

####  

###### 0450

###### 2000

###### 1426

###### 2000

###### 642

###### ,

###### P A

###### PC|A PCA  

#### c.)    

####  

###### 0338

###### 1118

###### 379

###### ,

###### PE

###### PF E

###### PF|E  

###### 

###### ^


##### TTeeoorreemmaa ddaa pprroobbaabbiilliiddaaddee ttoottaall

Sejam A 1 , A 2 , A 3 ... An eventos dois a dois disjuntos que formam uma partição do espaço
amostral, isto é,

### 

```
n
i
```
```
Ai
 1
```
###### 

e assuma que P(Ai)>0 para i=1, 2, 3,...n. Então, para qualquer evento , temos que

#### PBPA 1 BPA 2 B...PAnB

Aplicando a regra do produto temos

#### PBPA 1 PB|A 1 PA 2 PB|A 2 ...PAnPB|An

####    i  i

```
i
```
### PB  P A PB|A

##### TTeeoorreemmaa ddee BBaayyeess ee uussoo ddaa áárrvvoorree ddee pprroobbaabbiilliiddaaddeess

Sejam A 1 , A 2 , A 3 ... An eventos que formam uma partição do espaço amostral, e assuma
que P(Ai)>0 para todo i. Então, para qualquer evento B tal que P(B)>0, temos que

####    

####  

####    

####          n  n

```
i i i i
PB A P A PB A PA PB A PA
```
###### PB A PA

###### PB

###### PA B PA B

###### |. |. ... |.

###### | |.

###### 1 1  2 2  

######   

#### Para verificar o teorema de Bayes, basta notar que PAiB=PBAi e que, por sua

#### vez, PB|Ai.PAi=PAi|B.PB, o que garante o numerador. O denominador segue da

aplicação do teorema da probabilidade total para B.

A árvore de probabilidades é um diagrama que consiste em representar os eventos e as
probabilidades condicionais associadas às realizações. Cada um dos caminhos da árvore
indica uma possível ocorrência ou interseção de eventos.

```
Exemplo: Suponha que você é o gerente de uma fábrica de sorvetes. Você sabe
que 20% de todo o leite que utiliza na fabricação dos sorvetes provém da fazenda
F 1 , 30% são de uma outra fazenda F 2 e 50% de uma fazenda F 3. Um órgão de
fiscalização inspecionou as fazendas de surpresa, e observou que 20% do leite
produzido por F 1 estava adulterado por adição de água, enquanto que para F 2 e F 3 ,
essa proporção era de 5% e 2%, respectivamente. Na indústria de sorvetes que
você gerencia os galões de leite são armazenados em um refrigerador sem
identificação das fazendas. Para um galão escolhido ao acaso, calcule:
a) A probabilidade de que o galão contenha leite adulterado.
b) A probabilidade de que o galão tenha vindo da fazenda F 3 , sabendo que
contém leite não adulterado.
```

Resolução:
Observe que o diagrama de Venn a seguir ilustra os três eventos associados as
fazendas (F 1 , F 2 e F 3 ) e ao leite adulterado (A) ou não adulterado (Ac):

```
Se denotarmos por A o evento “o leite está adulterado”, temos que P(A|F 1 )=0,20,
P(A|F 2 )=0,05 e P(A|F 3 )=0,02. Além disso, a probabilidade do leite ser produzido por
cada uma das fazendas (F 1 , F 2 e F 3 ) é denotada por P(F 1 )=0,2, P(F 2 )=0,3 e
P(F 3 )=0,5. A partir daí, podemos construir a árvore de probabilidades da seguinte
maneira:
```
###### F 1

###### F 2

###### F 3

###### A

###### AC^

###### A

###### AC^

###### A

###### AC^

###### 0,

###### 0,

###### 0,

###### 0,

###### 0,

###### 0,

###### 0,

###### 0,

###### 0,

###### F 1 F^2

###### F 3

###### A


```
a)
```
####        

####               

####  0202   00503   00205  0065

```
1 1 2 2 3 3
```
```
1 2 3
```
###### ,. , ,. , ,. , ,

###### PA|F .PF P A|F .PF PA|F .PF

###### P A PF A PF A PF A

######    

######    

######       

```
b)
```
##  

##  

##  

##    

####  

###### 0 , 5241

###### 1 0 , 065

###### 0 , 98. 0 , 5

###### 1

###### |.

###### 3 |^333 

###### 

###### 

###### 

###### 

###### 

###### 

###### P A

###### PA F PF

###### PA

###### PF A

###### PF A

```
C
C
```
```
C
C
```
##### EExxeerrccíícciiooss^ ddee FFiixxaaççããoo

1. Na Tabela 1, temos os dados referentes a alunos matriculados em quatro cursos de
    uma universidade em dado ano.

Tabela 1 – Distribuição de alunos segundo o sexo e a escolha do curso.

Curso
Sexo
Masculino Feminino Total^
Computação 70 40 110
Matemática 15 15 30
Estatística 10 20 30
Ciências Atuariais 20 10 30
Total 115 85 200

Selecionado-se ao acaso um aluno do conjunto desses quatro cursos determine a
probabilidade:
a) Que o aluno seja do sexo masculino.
b) Que o aluno esteja matriculado no curso de Estatística.
c) Que o aluno seja do sexo feminino e matriculado em Matemática.
d) Que o aluno seja do sexo masculino ou matriculado em Ciências Atuariais.
Respostas: a) 0,575 b) 0,15 c)0,075 d)0,

2. Uma determinada peça é manufaturada por três fábricas A, B e C. Sabe-se que a
    fábrica A produz o dobro de peças que B, e B e C produziram o mesmo número de
    peças (durante um período de produção especificado). Sabe-se também que 2% das
    peças produzidas por A e 2% das peças produzidas por B são defeituosas, enquanto
    4% daquelas produzidas por C são defeituosas. Todas as peças produzidas são
    colocadas em um depósito, e depois uma peça é extraída ao acaso.
    a) Qual é a probabilidade de que essa peça seja defeituosa?
    b) Qual é a probabilidade de que a peça tenha sido produzida pela fábrica B,
       sabendo-se que é perfeita?
    Dica: Utilize a árvore de probabilidades.
    Respostas: a) 0,025 b) 0,


3. Uma escola do ensino médio do interior de São Paulo tem 40% de estudantes do sexo
    masculino. Entre estes, 20% nunca viram o mar, ao passo que, entre as meninas,
    essa porcentagem é de 50%. Qual a probabilidade de que um aluno selecionado ao
    acaso seja:
       a) Do sexo masculino e nunca tenha visto o mar?
       b) Do sexo feminino ou nunca tenha visto o mar?
    Dica: Utilize a árvore de probabilidades e na letra b aplique a fórmula da união de eventos.
    Respostas: a) 0,08 b) 0,
4. Na tabela abaixo, os números que aparecem são probabilidades relacionadas com a
    ocorrência de A, B, A  B, etc. Assim, P(A) = 0,10, enquanto P(A  B) = 0,04.

```
B BC^ Total
A 0,04 0,06 0,
AC^ 0,08 0,82 0,
Total 0,12 0,88 1,
Verifique se A e B são independentes.
Resposta: Como P(AB) ≠ P(A).P(B), A e B não são independentes.
```
5. Você entrega a seu amigo uma carta, destinada à sua namorada, para ser colocada
    no correio. Entretanto, ele pode se esquecer com probabilidade 0,1. Se não se
    esquecer, a probabilidade de que o correio extravie a carta é de 0,1. Finalmente, se foi
    enviada pelo correio a probabilidade de que a namorada não a receba é de 0,1.
       a) Sua namorada não recebeu a carta, qual a probabilidade de seu amigo ter
       esquecido?
       b) Avalie as possibilidades desse namoro continuar se a comunicação depender
       das cartas enviadas.
    Dica: Utilize a árvore de probabilidades. Ela ‘cresce’ mais para um lado do que para o outro. Não se preocupe!
    Respostas: a) 0,369 b) 0,


