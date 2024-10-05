# Test

## Pergunta 1

Um experimento (hipotético) sobre o efeito do álcool na habilidade perceptual motora é conduzido. 10 indivíduos são testado duas vezes, uma depois de ter tomado dois drinks e uma depois de tomado dois copos de água. Os dois testes foram realizados em dois dias diferentes para evitar influência do efeito do álcool. Metade dos indivíduos tomou a bebida alcoólica primeiro e a outra metade água. Os escores dos 10 indivíduos são mostrados abaixo. Escores mais altos refletem uma melhor performance.

| Indivíduo | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Água      | 16  | 15  | 11  | 20  | 19  | 14  | 13  | 15  | 14  | 16  |
| Álcool    | 13  | 13  | 12  | 16  | 16  | 11  | 10  | 15  | 9   | 16  |

Deseja-se testar se houve alteração na habilidade perceptual motora mediante as duas bebidas testadas. Utilize um nível de significância de 1%.

Grupo de escolhas da pergunta:

- [ ] a) Ao executar o teste t para comparação de duas médias (amostras independentes) encontramos um valor p igual a 0,005. Dessa forma, podemos dizer que houve alteração na habilidade perceptual motora mediante as duas bebidas testadas, considerando um nível de 1% de significância.
- [x] b) Ao executar o teste t para comparação de duas médias (amostras pareadas) encontramos um valor p igual a 0,005. Dessa forma, podemos dizer que houve alteração na habilidade perceptual motora mediante as duas bebidas testadas, considerando um nível de 1% de significância.
- [ ] c) [[Erro]] Ao executar o teste t para comparação de duas médias (amostras pareadas) encontramos um valor p igual a 0,0025. Dessa forma, podemos dizer que houve alteração na habilidade perceptual motora mediante as duas bebidas testadas, considerando um nível de 1% de significância.
- [ ] d) [[Não]] Ao executar o teste t para comparação de duas médias (amostras independentes) encontramos um valor p igual a 0,0025. Dessa forma, podemos dizer que não houve alteração na habilidade perceptual motora mediante as duas bebidas testadas, considerando um nível de 1% de significância.

!!! info Cálculo

    Para resolver essa questão, vamos realizar um teste *t* para amostras pareadas, já que os mesmos indivíduos foram testados sob duas condições diferentes (com álcool e com água). As etapas principais são:

    1. **Calcular a diferença entre os escores para cada indivíduo** (Água - Álcool).
    2. **Calcular a média e o desvio padrão dessas diferenças**.
    3. **Aplicar a fórmula do teste *t* para amostras pareadas**.

    As diferenças entre os escores para cada indivíduo são:

    | Indivíduo | Diferença (Água - Álcool) |
    | --------- | ------------------------- |
    | 1         | 16 - 13 = 3               |
    | 2         | 15 - 13 = 2               |
    | 3         | 11 - 12 = -1              |
    | 4         | 20 - 16 = 4               |
    | 5         | 19 - 16 = 3               |
    | 6         | 14 - 11 = 3               |
    | 7         | 13 - 10 = 3               |
    | 8         | 15 - 15 = 0               |
    | 9         | 14 - 9 = 5                |
    | 10        | 16 - 16 = 0               |

    Agora temos as diferenças: \(3, 2, -1, 4, 3, 3, 3, 0, 5, 0\).

    A seguir, calculemos a média (\(\bar{d}\)) e o desvio padrão (\(s_d\)) dessas diferenças.

    **Passos para o cálculo:**

    1. **Média das diferenças**:
    $$
    \bar{d} = \frac{3 + 2 - 1 + 4 + 3 + 3 + 3 + 0 + 5 + 0}{10} = 2.2
    $$

    2. **Desvio padrão das diferenças**:
    $$
    s_d = \sqrt{\frac{\sum (d_i - \bar{d})^2}{n-1}} = \sqrt{\frac{(3 - 2.2)^2 + (2 - 2.2)^2 + (-1 - 2.2)^2 + ... + (0 - 2.2)^2}{9}} \approx 1.989
    $$

    3. **Estatística do teste *t* para amostras pareadas**:
    $$
    t = \frac{\bar{d}}{s_d/\sqrt{n}} = \frac{2.2}{1.989/\sqrt{10}} \approx 3.499
    $$

    Agora, precisamos comparar o valor obtido de *t* com o valor crítico de *t* da distribuição *t* de Student para \(n-1 = 9\) graus de liberdade e um nível de significância de 1% (\(\alpha = 0.01\)). O valor crítico de *t* para 9 graus de liberdade e \(\alpha = 0.01\) em um teste bilateral é aproximadamente 3.249.

    Como o valor calculado de *t* (3.499) é maior que o valor crítico (3.249), rejeitamos a hipótese nula (\(H_0\)) de que não há diferença significativa.

## Pergunta 2

Um banco realiza um estudo idealizado para identificar as diferenças na utilização das contas correntes pelos clientes em duas de suas filiais. Uma amostra aleatória de 28 contas correntes é selecionada da filial situada em CG e uma amostra aleatória independente de 22 contas correntes é selecionada da sua filial em BM. O saldo atual da conta corrente é registrado para cada uma das contas. A seguir temos um resumo dos saldos bancários:

|                        | Filial CG | Filial BM |
| ---------------------- | --------- | --------- |
| Média amostral         | $1025     | $910      |
| Desvio padrão amostral | $150      | $125      |

O saldo médio das contas correntes mantidas pela população de clientes difere entre as duas filiais? Utilize um nível de 5% de significância.

Grupo de escolhas da pergunta:

- [x] a) As populações são homocedásticas. Ao executar o teste t para comparação de duas médias encontramos um valor p igual a 0,005 indicando que existe diferença significativa no saldo médio das contas correntes mantidas pela população de clientes entre as duas filiais.
- [ ] b) As populações são heterocedásticas. Ao executar o teste t para comparação de duas médias encontramos um valor p igual a 0,0025 indicando que NÃO existe diferença significativa no saldo médio das contas correntes mantidas pela população de clientes entre as duas filiais.
- [ ] c) As populações são heterocedásticas. Ao executar o teste t para comparação de duas médias encontramos um valor p igual a 0,005 indicando que NÃO existe diferença significativa no saldo médio das contas correntes mantidas pela população de clientes entre as duas filiais.
- [ ] d) As populações são homocedásticas. Ao executar o teste t para comparação de duas médias encontramos um valor p igual a 0,0025 indicando que existe diferença significativa no saldo médio das contas correntes mantidas pela população de clientes entre as duas filiais.

!!! info Cálculo

    Para resolver essa questão, vamos realizar um **teste *t* para amostras independentes** para comparar as médias dos saldos bancários entre as duas filiais (CG e BM). As etapas são:

    ### Hipóteses do teste:

    - \( H_0 \): Não há diferença significativa entre as médias dos saldos das contas correntes das duas filiais (\(\mu_{CG} = \mu_{BM}\)).
    - \( H_1 \): Há diferença significativa entre as médias dos saldos das contas correntes das duas filiais (\(\mu_{CG} \neq \mu_{BM}\)).

    ### Informações fornecidas:

    - **Filial CG**:
    - \( \bar{X}_{CG} = 1025 \) (média amostral)
    - \( s_{CG} = 150 \) (desvio padrão amostral)
    - \( n_{CG} = 28 \) (tamanho da amostra)
    
    - **Filial BM**:
    - \( \bar{X}_{BM} = 910 \)
    - \( s_{BM} = 125 \)
    - \( n_{BM} = 22 \)

    ### Passos para o cálculo:

    1. **Verificar homogeneidade ou heterogeneidade das variâncias**:
    - O desvio padrão das duas amostras é diferente (\( s_{CG} = 150 \) e \( s_{BM} = 125 \)). Como as variâncias parecem diferentes, vamos assumir que as populações são **heterocedásticas** (variâncias diferentes).

    2. **Fórmula do teste *t* para amostras independentes com variâncias diferentes**:

    $$
    t = \frac{\bar{X}_{CG} - \bar{X}_{BM}}{\sqrt{\frac{s_{CG}^2}{n_{CG}} + \frac{s_{BM}^2}{n_{BM}}}}
    $$

    3. **Substituindo os valores**:

    $$
    t = \frac{1025 - 910}{\sqrt{\frac{150^2}{28} + \frac{125^2}{22}}}
    = \frac{115}{\sqrt{\frac{22500}{28} + \frac{15625}{22}}}
    = \frac{115}{\sqrt{803.57 + 710.23}} = \frac{115}{\sqrt{1513.80}} = \frac{115}{38.91} \approx 2.955
    $$

    4. **Graus de liberdade aproximados** (fórmula de Welch):

    $$
    df \approx \frac{\left( \frac{s_{CG}^2}{n_{CG}} + \frac{s_{BM}^2}{n_{BM}} \right)^2}{\frac{\left( \frac{s_{CG}^2}{n_{CG}} \right)^2}{n_{CG} - 1} + \frac{\left( \frac{s_{BM}^2}{n_{BM}} \right)^2}{n_{BM} - 1}}
    $$

    Substituindo os valores:

    $$
    df \approx \frac{(803.57 + 710.23)^2}{\frac{803.57^2}{27} + \frac{710.23^2}{21}} = \frac{(1513.80)^2}{\frac{645733.92}{27} + \frac{504437.65}{21}} \approx \frac{2291530.44}{23990.14 + 24020.84} \approx 47.75
    $$

    Aproximamos \(df = 47\).

    5. **Valor crítico de *t* e comparação**:
    - Com 47 graus de liberdade e um nível de significância de 5% (\(\alpha = 0.05\)), o valor crítico de *t* para um teste bilateral é aproximadamente \( t_{crítico} \approx 2.013 \).

    Como o valor calculado de *t* (2.955) é maior que o valor crítico (2.013), rejeitamos a hipótese nula \( H_0 \).

    6. **Conclusão**:
    O valor de *p* associado a \( t = 2.955 \) é aproximadamente 0,005.

## Pergunta 3

As companhias de seguro de automóvel estão cogitando elevar os prêmios para aqueles que falam ao telefone enquanto dirigem. Um grupo de defesa dos consumidores alega que este problema não é tão sério, porque menos de 10% dos motoristas usam o telefone. Uma companhia de seguro faz uma pesquisa e constata que, entre 500 motoristas selecionados aleatoriamente, 72 usam o telefone. Teste a afirmação do grupo de consumidores ao nível de 2% de significância.
Grupo de escolhas da pergunta

- [ ] a) [[Erro]] O valor p para o teste é igual a 0,001, indicando que NÃO há evidências que comprovem a alegação do grupo de defesa dos consumidores.
- [ ] b) O valor p para o teste é igual a 0,999, indicando que há evidências que comprovem a alegação do grupo de defesa dos consumidores.
- [ ] c) [[Não]] O valor p para o teste é igual a 0,001, indicando que há evidências que comprovem a alegação do grupo de defesa dos consumidores.
- [x] d) O valor p para o teste é igual a 0,999, indicando que NÃO há evidências que comprovem a alegação do grupo de defesa dos consumidores.

!!! info Cálculo

    Neste caso, estamos realizando um **teste de hipótese para uma proporção**. As etapas para o teste são as seguintes:

    ### Hipóteses:

    - \( H_0 \): A proporção de motoristas que usam o telefone enquanto dirigem é maior ou igual a 10% (\( p \geq 0,10 \)).
    - \( H_1 \): A proporção de motoristas que usam o telefone enquanto dirigem é menor que 10% (\( p < 0,10 \)).

    Esse é um **teste unilateral** à esquerda.

    ### Informações fornecidas:

    - Tamanho da amostra (\( n \)) = 500 motoristas.
    - Número de motoristas que usam o telefone (\( x \)) = 72.
    - Proporção amostral (\( \hat{p} \)) = \( \frac{72}{500} = 0,144 \).

    ### Passos para o cálculo:

    1. **Calcular a estatística do teste** \( z \):

    $$
    z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1 - p_0)}{n}}}
    $$

    Onde:
    - \( \hat{p} = 0,144 \) (proporção observada na amostra),
    - \( p_0 = 0,10 \) (proporção populacional hipotética).

    Substituindo os valores:

    $$
    z = \frac{0,144 - 0,10}{\sqrt{\frac{0,10(1 - 0,10)}{500}}} = \frac{0,044}{\sqrt{\frac{0,10 \times 0,90}{500}}} = \frac{0,044}{\sqrt{0,00018}} = \frac{0,044}{0,0134} \approx 3,28
    $$

    2. **Calcular o valor-p** associado ao valor de \( z \):

    Consultando a tabela da distribuição normal padrão, o valor de \( z = 3,28 \) corresponde a um **valor-p** muito pequeno, aproximadamente \( p \approx 0,001 \).

    ### Conclusão:

    Como o valor-p é menor que o nível de significância de 2% (\( \alpha = 0,02 \)), rejeitamos a hipótese nula \( H_0 \).

    Isso significa que **há evidências** para rejeitar a afirmação de que a proporção de motoristas que usam o telefone enquanto dirigem é inferior a 10%.

## Pergunta 4

Uma revista de viagens de negócios quer classificar os aeroportos internacionais de acordo com a avaliação média da população de pessoas que viajam a negócios. Será usada uma escala de classificação, sendo 0 uma avaliação baixa e 10 uma avaliação elevada, e os aeroportos que receberem uma avaliação média populacional maior que 7 serão designados como aeroportos com um atendimento de alto nível. A equipe da revista pesquisou uma amostra de 27 viajantes de negócios em cada aeroporto para obter os dados da avaliação. A amostra do aeroporto de Londres produziu uma avaliação média igual a 7,25 com desvio padrão igual a 1,052. Os dados indicam que o aeroporto de Londres deveria ser designado como um aeroporto de alto nível? Utilize um nível de 5% de significância.
Grupo de escolhas da pergunta

- [ ] a) O valor p para o teste é igual a 0,25, indicando que o aeroporto de Londres deve ser designado como um aeroporto de alto nível.
- [ ] b) O valor p para o teste é igual a 0,375, indicando que o aeroporto de Londres deve ser designado como um aeroporto de alto nível.
- [x] c) O valor p para o teste é igual a 0,125, indicando que o aeroporto de Londres NÃO deve ser designado como um aeroporto de alto nível.
- [ ] d) O valor p para o teste é igual a 0,875, indicando que o aeroporto de Londres NÃO deve ser designado como um aeroporto de alto nível.

!!! info Cálculo

    Aqui, estamos lidando com um **teste de hipótese para uma média** para determinar se o aeroporto de Londres deve ser classificado como de alto nível.

    ### Hipóteses:

    - \( H_0 \): A média populacional das avaliações do aeroporto de Londres é menor ou igual a 7 (\( \mu \leq 7 \)).
    - \( H_1 \): A média populacional das avaliações do aeroporto de Londres é maior que 7 (\( \mu > 7 \)).

    Esse é um **teste unilateral** à direita.

    ### Informações fornecidas:

    - Tamanho da amostra (\( n \)) = 27.
    - Média amostral (\( \bar{X} \)) = 7,25.
    - Desvio padrão amostral (\( s \)) = 1,052.
    - Hipótese nula (\( \mu_0 \)) = 7.

    ### Passos para o cálculo:

    1. **Calcular a estatística do teste *t* para uma amostra**:

    $$
    t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
    $$

    Substituindo os valores:

    $$
    t = \frac{7,25 - 7}{1,052 / \sqrt{27}} = \frac{0,25}{1,052 / 5,196} = \frac{0,25}{0,2024} \approx 1,235
    $$

    2. **Determinar os graus de liberdade**:

    $$
    df = n - 1 = 27 - 1 = 26
    $$

    3. **Calcular o valor-p** associado ao valor de \( t \):

    Consultando a tabela de distribuição *t* de Student com 26 graus de liberdade para um teste unilateral à direita, um valor de \( t = 1,235 \) resulta em um **valor-p** de aproximadamente \( 0,125 \).

    ### Conclusão:

    Como o valor-p \( 0,125 \) é maior que o nível de significância de 5% (\( \alpha = 0,05 \)), **não rejeitamos a hipótese nula**. Isso significa que **não há evidências suficientes** para afirmar que a média das avaliações do aeroporto de Londres é maior que 7, ou seja, ele **não deve ser classificado como um aeroporto de alto nível**.

## Pergunta 5

Em um concurso público promovido por uma empresa estatal, os candidatos às vagas de Engenharia constituem a nossa população de interesse. Entre eles, os que se submeteram a uma preparação específica para o concurso constituem a subpopulação A e os que não fizeram essa preparação constituem a sub-população B. Foram coletadas amostras aleatórias em ambas as sub-populações e os resultados obtidos foram os seguintes:

| Sub-população         | Tamanho amostral | Aprovados |
| --------------------- | ---------------- | --------- |
| Prepararam-se (A)     | 140              | 34        |
| Não se prepararam (B) | 230              | 53        |

Pode-se dizer que houve diferença na proporção de aprovados entre as duas sub-populações estudadas? Utilize um nível de 10% de significância.

Grupo de escolhas da pergunta

- [ ] a) Ao executar o teste Z para comparação de duas proporções encontramos um valor p = 0,1064, ou seja, considerando um nível de 10% de significância, podemos dizer que NÃO houve diferença na proporção de aprovados entre as duas sub-populações estudadas.
- [ ] b) Ao executar o teste Z para comparação de duas proporções encontramos um valor p = 0,3936, ou seja, considerando um nível de 10% de significância, podemos dizer que houve diferença na proporção de aprovados entre as duas sub-populações estudadas.
- [x] c) Ao executar o teste Z para comparação de duas proporções encontramos um valor p = 0,78, ou seja, considerando um nível de 10% de significância, podemos dizer que NÃO houve diferença na proporção de aprovados entre as duas sub-populações estudadas.
- [ ] d) Ao executar o teste Z para comparação de duas proporções encontramos um valor p = 0,078, ou seja, considerando um nível de 10% de significância, podemos dizer que houve diferença na proporção de aprovados entre as duas sub-populações estudadas.

!!! info Cálculo

    Aqui, estamos realizando um **teste de hipótese para comparar duas proporções**. As sub-populações são aquelas que se prepararam para o concurso (A) e aquelas que não se prepararam (B).

    ### Hipóteses:

    - \( H_0 \): Não há diferença entre as proporções de aprovados das sub-populações A e B (\( p_A = p_B \)).
    - \( H_1 \): Há diferença entre as proporções de aprovados das sub-populações A e B (\( p_A \neq p_B \)).

    Esse é um **teste bilateral**.

    ### Informações fornecidas:

    - Tamanho da amostra na sub-população A (\( n_A \)) = 140.
    - Número de aprovados na sub-população A (\( x_A \)) = 34.
    - Proporção amostral da sub-população A (\( \hat{p}_A = \frac{34}{140} = 0,243 \)).

    - Tamanho da amostra na sub-população B (\( n_B \)) = 230.
    - Número de aprovados na sub-população B (\( x_B \)) = 53.
    - Proporção amostral da sub-população B (\( \hat{p}_B = \frac{53}{230} = 0,230 \)).

    ### Passos para o cálculo:

    1. **Proporção conjunta** (\( \hat{p} \)):

    $$
    \hat{p} = \frac{x_A + x_B}{n_A + n_B} = \frac{34 + 53}{140 + 230} = \frac{87}{370} \approx 0,2351
    $$

    2. **Estatística do teste Z** para comparar duas proporções:

    $$
    Z = \frac{\hat{p}_A - \hat{p}_B}{\sqrt{\hat{p}(1 - \hat{p}) \left( \frac{1}{n_A} + \frac{1}{n_B} \right)}}
    $$

    Substituindo os valores:

    $$
    Z = \frac{0,243 - 0,230}{\sqrt{0,2351 \times (1 - 0,2351) \left( \frac{1}{140} + \frac{1}{230} \right)}}
    = \frac{0,013}{\sqrt{0,2351 \times 0,7649 \left( 0,00714 + 0,00435 \right)}}
    = \frac{0,013}{\sqrt{0,2351 \times 0,7649 \times 0,01149}} = \frac{0,013}{\sqrt{0,002066}} = \frac{0,013}{0,04547} \approx 0,286
    $$

    3. **Calcular o valor-p** associado ao valor de \( Z = 0,286 \):

    Consultando a tabela da distribuição normal padrão para um teste bilateral, o valor de \( Z = 0,286 \) corresponde a um **valor-p** de aproximadamente 0,78.

    ### Conclusão:

    Como o valor-p \( 0,78 \) é muito maior que o nível de significância de 10% (\( \alpha = 0,10 \)), **não rejeitamos a hipótese nula**. Isso significa que **não há evidências suficientes** para afirmar que há uma diferença significativa nas proporções de aprovados entre as duas sub-populações.
