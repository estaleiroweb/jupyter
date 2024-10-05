# Prova

## Pergunta 1

Em uma pesquisa estatística foi construída uma tabela com o perfil dos pesquisados a partir das seguintes variáveis: Sexo; raça; cor dos olhos; cor do cabelo; altura; idade (anos); peso; estado civil; salário mensal (R$); número de dependentes.

Considerando as variáveis apresentadas, assinale a alternativa que apresenta apenas as variáveis qualitativas:

Grupo de escolhas da pergunta

- [ ] Altura; idade (anos); peso; salário mensal (em reais); número de dependentes.
- [x] Sexo; raça; cor dos olhos; cor do cabelo; estado civil.
- [ ] Altura; peso; salário mensal (em reais); número de dependentes.
- [ ] Cor dos olhos; número de dependentes; sexo; raça; cor do cabelo; estado civil.

!!! info Resposta

    As variáveis qualitativas são aquelas que representam categorias ou características descritivas que não podem ser medidas numericamente de forma direta. Vamos classificar as variáveis mencionadas:

    - **Qualitativas** (categóricas):
    - Sexo
    - Raça
    - Cor dos olhos
    - Cor do cabelo
    - Estado civil

    - **Quantitativas** (numéricas):
    - Altura
    - Idade (anos)
    - Peso
    - Salário mensal (R$)
    - Número de dependentes

    Portanto, a alternativa que apresenta apenas **variáveis qualitativas** é:

## Pergunta 2

Uma empresa avaliou o volume de vendas (em salários mínimos) dos 15 funcionários do setor de vendas no último mês e encontrou o seguinte:

![sss](https://pucminas.instructure.com/users/7268/files/791103/preview?verifier=vljeSEW63TePixytQmx6VMqmXMJuqqDhZnnWUqxZ)

Marque a afirmação incorreta:

Grupo de escolhas da pergunta

- [ ] 50% dos funcionários venderam de 23 a 32 salários mínimos no último mês.
- [ ] O funcionário que vendeu menos no último mês, vendeu 16 salários mínimos.
- [ ] Temos três valores discrepantes nas vendas do último mês.
- [x] 25% dos funcionários venderam 23 salários mínimos no último mês.

!!! info Resposta

    Com base na análise do boxplot mostrado, podemos verificar as seguintes informações:

    - A caixa representa o intervalo interquartil, ou seja, os 50% centrais dos dados. No caso, 50% dos funcionários venderam entre 23 e 32 salários mínimos, conforme indicado pelos limites da caixa.
    - O menor valor de vendas, mostrado pela linha externa (bigode) à esquerda, é 16, que representa o funcionário que vendeu menos.
    - Existem três pontos fora do intervalo interquartil, que são considerados valores discrepantes (outliers) e correspondem às vendas de 48, 50 e 54 salários mínimos.
    - A afirmação sobre 25% dos funcionários venderem exatamente 23 salários mínimos está incorreta. O valor de 23 representa o primeiro quartil (Q1), o que significa que 25% dos funcionários venderam **até** 23 salários mínimos, e não que exatamente 25% venderam esse valor.

## Pergunta 3

Em um sistema de transmissão de dados, existe uma probabilidade igual a 0,05 de um lote de dados ser transmitido erroneamente. Foram transmitidos 20 lotes de dados para a realização de um teste de análise da confiabilidade do sistema. Para encontrar a probabilidade de haver erro na transmissão, marque a afirmação incorreta:

Grupo de escolhas da pergunta

- [ ] Utiliza-se a distribuição binomial porque temos um experimento com 20 tentativas.
- [ ] Não é utilizada a distribuição exponencial porque o número de erros na transmissão pode variar de 0 a 20.
- [x] Utiliza-se a distribuição Poisson porque o número médio de erros na transmissão é igual a 1.
- [ ] Utiliza-se a distribuição binomial porque a probabilidade de haver erro na transmissão é igual a 5%.

!!! info Resposta

    Vamos analisar as afirmações com base nas propriedades das distribuições estatísticas mencionadas:

    1. **Distribuição Binomial**: Essa distribuição é usada quando temos um número fixo de tentativas independentes (n = 20), cada uma com dois resultados possíveis (sucesso ou fracasso, neste caso, transmissão correta ou incorreta), e a probabilidade de sucesso (erro na transmissão) é constante (p = 0,05). Portanto, é correto dizer que se utiliza a distribuição binomial para modelar esse cenário.
    
    - Afirmativas corretas: 
        - "Utiliza-se a distribuição binomial porque temos um experimento com 20 tentativas."
        - "Utiliza-se a distribuição binomial porque a probabilidade de haver erro na transmissão é igual a 5%."

    2. **Distribuição Exponencial**: Esta distribuição é usada geralmente para modelar o tempo entre eventos contínuos, como o tempo até que ocorra o primeiro erro de transmissão. Aqui, o foco está no número de erros em 20 tentativas discretas, não no tempo até o erro. Portanto, a distribuição exponencial não é apropriada para esse contexto, e a afirmativa sobre isso também está correta.
    
    - Afirmativa correta:
        - "Não é utilizada a distribuição exponencial porque o número de erros na transmissão pode variar de 0 a 20."

    3. **Distribuição de Poisson**: Esta distribuição é utilizada para modelar o número de eventos (como erros) que ocorrem em um intervalo fixo, desde que a taxa média de ocorrências seja conhecida. Entretanto, no caso de dados binomiais com um número pequeno de tentativas e baixa probabilidade de sucesso, a distribuição de Poisson pode ser uma aproximação da binomial. No entanto, aqui temos apenas 20 tentativas e a probabilidade de erro é 0,05, o que não configura uma condição ideal para o uso da Poisson.

    - Afirmativa incorreta:
        - **"Utiliza-se a distribuição Poisson porque o número médio de erros na transmissão é igual a 1."** 

## Pergunta 4

Em certo banco de dados, o tempo para a realização das buscas é aproximadamente normal com média de 53 segundos e desvio padrão de 14 segundos. Depois de realizadas algumas modificações no sistema, observou-se que, em 30 consultas, o tempo médio caiu para 45 segundos. Há evidências de melhora? Admita que as 30 observações possam ser consideradas uma amostra aleatória e que não houve alteração na variância. O valor p encontrado é igual a 0,00087. Utilizando um nível de significância de 1%, marque a alternativa correta.

Grupo de escolhas da pergunta

- [ ] Utilizou-se o teste Z para uma média. Como o valor p > 0,01, indica que há indícios de melhoria no tempo médio para realização das buscas.
- [ ] Utilizou-se o teste t-Student para uma média. Como o valor p < 0,01, indica que há indícios de melhoria no tempo médio para realização das buscas.
- [ ] Utilizou-se o teste t-Student para uma média. Como o valor p > 0,01, indica que não há indícios de melhoria no tempo médio para realização das buscas.
- [x] Utilizou-se o teste Z para uma média. Como o valor p < 0,01, indica que há indícios de melhoria no tempo médio para realização das buscas.

!!! info Resposta

    Para resolver essa questão, vamos analisar os detalhes fornecidos:

    - Média antes das modificações: 53 segundos.
    - Desvio padrão populacional (assumido não alterado): 14 segundos.
    - Após as modificações, a média amostral com 30 consultas: 45 segundos.
    - Valor p encontrado: 0,00087.
    - Nível de significância (α): 1% (ou seja, 0,01).

    Agora, analisemos as alternativas com base nos seguintes critérios:

    1. **Teste Z ou t-Student?**
    - Neste caso, a amostra é de tamanho razoável (n = 30) e temos o desvio padrão populacional conhecido (14 segundos). Como o desvio padrão populacional é conhecido, devemos usar o **teste Z**, não o teste t-Student.

    2. **Comparando o valor p ao nível de significância (α = 0,01)**:
    - O valor p dado é 0,00087, que é **menor** que o nível de significância de 0,01.
    - Isso significa que rejeitamos a hipótese nula ($H_0$: a média do tempo das buscas não mudou) e aceitamos que há **evidências de que houve melhora no tempo médio**.

## Pergunta 5

Sabe-se que a vida, em horas, de uma bateria é aproximadamente normalmente distribuída, com desvio-padrão σ = 1,87 hora. Uma amostra aleatória de 17 baterias tem uma vida média de 36,3 horas. O valor p que avalie que a vida da bateria exceda 35 horas é igual a:

Grupo de escolhas da pergunta

- [ ] 0,083
- [x] 0,002
- [ ] 0,206
- [ ] 0,103

!!! info Resposta

    Para calcular o valor p que avalia se a vida média da bateria excede 35 horas, podemos usar o **teste Z** para uma média, já que o desvio-padrão populacional ($\sigma$) é conhecido.

    Os dados fornecidos são:

    - Média da amostra ($\bar{x}$): 36,3 horas
    - Tamanho da amostra ($n$): 17 baterias
    - Desvio-padrão populacional ($\sigma$): 1,87 horas
    - Hipótese nula ($H_0$): A vida média das baterias é 35 horas
    - Hipótese alternativa ($H_1$): A vida média das baterias excede 35 horas

    ### Fórmula do teste Z para uma média:

    $$
    Z = \frac{\bar{x} - \mu_0}{\frac{\sigma}{\sqrt{n}}}
    $$

    Onde:
    - $\bar{x}$ é a média amostral (36,3 horas)
    - $\mu_0$ é a média sob a hipótese nula (35 horas)
    - $\sigma$ é o desvio-padrão populacional (1,87 horas)
    - $n$ é o tamanho da amostra (17)

    Substituindo os valores:

    $$
    Z = \frac{36,3 - 35}{\frac{1,87}{\sqrt{17}}}
    $$

    Calculando:

    $$
    Z = \frac{1,3}{\frac{1,87}{\sqrt{17}}}
    $$

    $$
    Z \approx \frac{1,3}{0,453}
    $$

    $$
    Z \approx 2,87
    $$

    Agora, encontrando o valor p associado a um valor Z de 2,87 para um teste unilateral (pois estamos interessados apenas se a média **excede** 35 horas):

    Consultando uma tabela de distribuição normal padrão, o valor p para $Z = 2,87$ é aproximadamente **0,002**.

## Pergunta 6

Suponha que o tempo de resposta na execução de um algoritmo é uma variável aleatória com distribuição Normal de média 23 segundos e desvio padrão de 4 segundos. A probabilidade do tempo de resposta ser menor do que 26 segundos é:

Grupo de escolhas da pergunta

- [ ] 0,5468
- [ ] 0,2734
- [x] 0,7734
- [ ] 0,2266

!!! info Resposta

    Para resolver essa questão, vamos utilizar a **distribuição normal padrão**. Precisamos padronizar o valor de 26 segundos usando a fórmula do **Z-score**:

    ### Fórmula do Z-score:

    $$
    Z = \frac{X - \mu}{\sigma}
    $$

    Onde:
    - $X$ é o valor de interesse (26 segundos),
    - $\mu$ é a média da distribuição (23 segundos),
    - $\sigma$ é o desvio padrão (4 segundos).

    Substituindo os valores:

    $$
    Z = \frac{26 - 23}{4} = \frac{3}{4} = 0,75
    $$

    Agora, usando a **tabela da distribuição normal padrão** ou uma calculadora estatística, encontramos a probabilidade associada ao Z-score de 0,75.

    A área acumulada até $Z = 0,75$ é aproximadamente **0,7734**.

    Portanto, a probabilidade do tempo de resposta ser menor que 26 segundos é **0,7734**.

## Pergunta 7

Um sensor tem vida média de 2000 dias com desvio-padrão de 80 dias. O sensor tem distribuição aproximadamente normal. A partir dessa informação são feitas as afirmações:

- I. O número máximo de dias necessários para que se tenha que repor no máximo 5% dos produtos é 1750,412 dias.
- II. O número máximo de dias necessários para que se tenha que repor no máximo 95% dos produtos é 2131,588 dias.
- III. A probabilidade de este sensor durar entre 2100 e 2200 dias é 0,09944.

Está(ão) correta(s) a(s) afirmação(ões):

Grupo de escolhas da pergunta

- [ ] I e III.
- [x] II e III.
- [ ] Apenas I.
- [ ] Apenas II.

!!! info Resposta

    Vamos analisar cada afirmação com base na distribuição normal fornecida:

    ### Dados:
    - Vida média $\mu = 2000$ dias
    - Desvio padrão $\sigma = 80$ dias
    - Distribuição normal

    ### Análise de cada afirmação:

    #### I. O número máximo de dias necessários para que se tenha que repor no máximo 5% dos produtos é 1750,412 dias.

    Para determinar o número máximo de dias para que 5% dos sensores falhem, precisamos encontrar o valor associado ao **percentil de 5%** na distribuição normal. Para isso, usamos o valor de Z correspondente a 5%, que é aproximadamente **-1,645** (de uma tabela de Z-scores).

    Aplicando a fórmula para converter o valor de Z para a distribuição normal:

    $$
    X = \mu + Z \cdot \sigma
    $$

    Substituindo os valores:

    $$
    X = 2000 + (-1,645) \cdot 80 = 2000 - 131,6 = 1868,4 \, \text{dias}
    $$

    Portanto, a primeira afirmação **está incorreta**, pois o valor correto seria **1868,4 dias**, não **1750,412 dias**.

    #### II. O número máximo de dias necessários para que se tenha que repor no máximo 95% dos produtos é 2131,588 dias.

    O número máximo de dias para 95% dos sensores é associado ao **percentil de 95%**, que tem um Z-score de **1,645**.

    Aplicando a fórmula novamente:

    $$
    X = 2000 + 1,645 \cdot 80 = 2000 + 131,6 = 2131,6 \, \text{dias}
    $$

    Portanto, a segunda afirmação **está correta**, já que o valor é **2131,588 dias** (aproximadamente).

    #### III. A probabilidade de este sensor durar entre 2100 e 2200 dias é 0,09944.

    Para calcular essa probabilidade, precisamos encontrar os valores de Z para 2100 e 2200 dias:

    Para 2100 dias:
    $$
    Z = \frac{2100 - 2000}{80} = 1,25
    $$

    Para 2200 dias:
    $$
    Z = \frac{2200 - 2000}{80} = 2,5
    $$

    Agora, usando a tabela de Z, encontramos:

    - A área acumulada até $Z = 1,25$ é aproximadamente **0,8944**.
    - A área acumulada até $Z = 2,5$ é aproximadamente **0,9938**.

    A probabilidade de o sensor durar entre 2100 e 2200 dias é a diferença entre essas áreas:

    $$
    P(2100 < X < 2200) = 0,9938 - 0,8944 = 0,0994
    $$

    Portanto, a terceira afirmação **está correta**, pois a probabilidade é **0,09944**.

## Pergunta 8

Estão sendo estudadas as taxas de queima de dois diferentes propelentes sólidos usados no sistema de escapamento de aeronaves. Sabe-se que ambos os propelentes têm aproximadamente os mesmo desvio-padrão, ou seja, σ1 = σ2 e que essas taxas seguem distribuição normal. Duas amostras aleatórias de n1 = 19 e n2 = 18 espécimes foram testadas resultando em taxas médias de 18 cm/s e desvio de 2,8 cm/s para a primeira amostra e de média de 21 cm/s e desvio de 3,0 cm/s na segunda. Para avaliar se existe diferença na taxa média dos dois propelentes foi conduzido um teste de hipóteses obtendo-se um valor p = 0,003 e um intervalo de confiança para a diferença das médias de [-4,936 ; -1,064]. Considerando-se um nível de 5% de significância. Assinale a resposta correta:

Grupo de escolhas da pergunta

- [x] A partir do intervalo de confiança pode-se dizer que a taxa média de queima na amostra 2 é significativamente maior do que na amostra 1.
- [ ] Como o valor p > 5%, pode-se dizer que existe diferença estatisticamente significativa na taxa média de queima entre os dois problemas.
- [ ] Como o valor p < 5%, pode-se dizer que não existe diferença estatisticamente significativa na taxa média de queima entre os dois problemas.
- [ ] A partir do intervalo de confiança pode-se dizer que a taxa média de queima na amostra 1 é significativamente maior do que na amostra 2.

!!! info Resposta

    ### Análise:

    - **Dados fornecidos**:
    - $n_1 = 19$, $n_2 = 18$
    - $\bar{X}_1 = 18$ cm/s, $\bar{X}_2 = 21$ cm/s
    - $s_1 = 2,8$ cm/s, $s_2 = 3,0$ cm/s
    - Valor p = 0,003
    - Intervalo de confiança para a diferença das médias: [-4,936 ; -1,064]
    - Nível de significância = 5% (0,05)

    ### Interpretação:

    1. **Teste de Hipóteses**:
    - Hipótese nula ($H_0$): As taxas médias de queima dos dois propelentes são iguais.
    - Hipótese alternativa ($H_a$): As taxas médias de queima dos dois propelentes são diferentes.

    2. **Intervalo de Confiança**:
    - O intervalo de confiança para a diferença das médias é [-4,936 ; -1,064]. Isso significa que o intervalo não inclui o valor 0, o que indica uma diferença significativa entre as taxas médias de queima dos dois propelentes. Além disso, como o intervalo é **negativo**, significa que a taxa média de queima do **propelente 2** é maior que a do **propelente 1**.

    3. **Valor-p**:
    - O valor-p encontrado foi 0,003, que é **menor** que o nível de significância de 5% (0,05). Isso indica que rejeitamos a hipótese nula ($H_0$) e concluímos que há diferença significativa entre as taxas de queima dos dois propelentes.

    ### Conclusão:

    A partir do **intervalo de confiança negativo** e do **valor-p menor que 5%**, podemos concluir que a taxa média de queima da **amostra 2 é significativamente maior** que a da amostra 1.

## Pergunta 9

O tempo de vida (em horas) de um transistor é uma variável aleatória T com distribuição exponencial. O tempo médio de vida do transistor é de 500 horas. A probabilidade do transistor durar entre 300 e 1000 horas é de:

Grupo de escolhas da pergunta

- [ ] 0,8647
- [ ] 0,6321
- [x] 0,4135
- [ ] 0,4512

!!! info Resposta

    Sabemos que o tempo de vida do transistor segue uma **distribuição exponencial** com um tempo médio de vida ($\mu$) de 500 horas.

    A função de densidade da distribuição exponencial é dada por:

    $$ f(t) = \lambda e^{-\lambda t} $$

    Onde $\lambda = \frac{1}{\mu}$ é a taxa da distribuição.

    ### Passos para o cálculo:

    1. **Taxa $\lambda$:**
    - $\lambda = \frac{1}{500} = 0,002$.

    2. **Cálculo da probabilidade:**
    A probabilidade de que o transistor dure entre 300 e 1000 horas é dada por:

    $$ P(300 \leq T \leq 1000) = P(T \leq 1000) - P(T \leq 300) $$

    A função de distribuição acumulada (CDF) para a distribuição exponencial é dada por:

    $$ F(t) = 1 - e^{-\lambda t} $$

    Portanto:

    $$ P(T \leq 1000) = 1 - e^{-\lambda \cdot 1000} $$
    $$ P(T \leq 300) = 1 - e^{-\lambda \cdot 300} $$

    3. **Substituindo os valores:**

    - $P(T \leq 1000) = 1 - e^{-0,002 \cdot 1000} = 1 - e^{-2}$
    - $P(T \leq 300) = 1 - e^{-0,002 \cdot 300} = 1 - e^{-0,6}$

    Agora, calculamos:

    - $e^{-2} \approx 0,1353$
    - $e^{-0,6} \approx 0,5488$

    Portanto:

    - $P(T \leq 1000) = 1 - 0,1353 = 0,8647$
    - $P(T \leq 300) = 1 - 0,5488 = 0,4512$

    4. **Probabilidade final:**

    $$ P(300 \leq T \leq 1000) = 0,8647 - 0,4512 = 0,4135 $$

## Pergunta 10

ENADE - As taxas de emprego para mulheres são afetadas diretamente por ciclos econômicos e por políticas de governo que contemplam a inclusão das mulheres no mercado de trabalho. O gráfico a seguir apresenta variações das taxas percentuais de emprego par mulheres em alguns países, no período de 2000 a 2011.

![img](https://pucminas.instructure.com/users/7268/files/791219/preview?verifier=UMTpvH4ruZl295leQeNUNik2Nv4guY90PensMSNo)

- [ ] Manteve-se superior a 60% no Canadá, na Alemanha e nos Estados Unidos.
- [ ] Manteve-se crescente na França e no Japão.
- [x] Aumentou mais na Alemanha que nos demais países pesquisados.
- [ ] Atingiu, na Grã-Bretanha, seu valor máximo em 2011.
