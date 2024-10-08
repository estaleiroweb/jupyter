# Prova

## Pergunta 1

As técnicas de discretização podem ser classificadas sobre vários aspectos: Supervisionadas e Não supervisionadas e pelo método utilizado, Divisão e Fusão. Avalie as afirmações a seguir:

1. A discretização Não supervisionada não considera o rótulo da classe, enquanto os Supervisionados o fazem.
2. A discretização Supervisionada utilizam informações da classe para determinar automaticamente o melhor número de intervalos para cada atributo.
3. Os métodos de Divisão realizam a discretização por meio de um processo iterativo de subdivisão do intervalo de valores inicial que é executado até que uma condição de parada seja satisfeita.
4. Os métodos de Fusão iniciam com os valores do atributo contínuo particionados e, iterativamente, realizam a junção dessas partições enquanto um critério de parada não é alcançado.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (3) e (4)
- [x] Todas estão corretas
- [ ] Apenas (1) e (2)
- [ ] Apenas (2) e (3)

## Pergunta 2

Para evitar a polarização dos modelos de aprendizado de máquina. As técnicas de balanceamento buscam equilibrar a quantidade de instâncias de cada classe do conjunto de dados. Dentre as diversas técnicas existentes podemos citar: Seleção aleatória pela menor classe, Seleção por agrupamento pela menor classe e Replicação de instâncias. Avalie as afirmações a seguir:

1. Dado dois conjuntos de registros com N e M registros (onde N<<M) vinculados a duas classes. O balanceamento por seleção aleatória ocorre selecionando de forma aleatória N registros dentro do conjunto contendo M registros.
2. Dado dois conjuntos de registros com N e M registros (onde N<<M) vinculados a duas classes. O balanceamento por seleção de grupo ocorre selecionando por meio de uma técnica de agrupamento os N registros mais representativos dentro do conjunto contendo M registros.
3. Dado dois conjuntos de registros com N e M registros (onde N<<M) vinculados a duas classes. O balanceamento ocorre gerando artificialmente instâncias a partir das instâncias do conjunto contendo M registros (classe maioritária).

Não é correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (2) e (3)
- [x] Apenas (3)
- [ ] Apenas (1) e (2)
- [ ] Todas estão incorretas

## Pergunta 3

Uma base de dados é considerada gigantesca se esta possui duas características: Alta dimensionalidade e grande número de registros. Avalie as afirmações a seguir:

1. Para gigantescas bases de dados, pode ser necessária uma etapa de redução de dados, antes de aplicar as técnicas de aprendizado de máquina.
2. Enquanto grandes bases de dados tem potencial para melhorar os resultados da mineração, não existe garantia que estas levem para um melhor conhecimento extraído, que as bases com menos dados.
3. É importante construir um conjunto de dados viável e com instâncias suficientes para a mineração.
4. O principal alvo da redução de dados é a redução da dimensão e a principal questão é saber quais atributos podem ser descartados sem afetar a qualidade dos resultados.
5. Se o algoritmo de Data Mining utilizado cresce exponencialmente com a dimensão, pode ser esperado grande ganho em relação à redução da dimensionalidade da base de dados.
6. A estruturação do problema, a seleção, a transformação e discretização são consideradas as etapas mais importantes do processo de descoberta de conhecimento.

Não é correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] [[Erro]] Somente (6)
- [ ] Somente (2)
- [x] Somente (5)
- [ ] Apenas (1) e (3)

## Pergunta 4

O cientista de dados deve avaliar a representatividade da base de dados criada a partir da análise dos domínios dos atributos (entende-se por representatividade conter dados suficientes para descrever o domínio de problema). Dentro desse contexto, avalie as afirmações a seguir:

1. Considerando os pontos por multa de transito = {7, 5, 4, 3, 0}. Para traçar o perfil dos motoristas é necessário ter uma representatividade equilibrada entre as combinações desses valores. A soma de pontos com valor elevado pode representar a existência de outliers, o que obrigaria a segmentar o estudo e colocar restrições aos resultados alcançados.
2. Considerando o estado civil de pessoas = {Solteiro, Casado, Viúvo, Divorciado}. A falta de registros ou o desequilibrio destes em relação ao estado civil pode levar a restrições nos resultados, dependendo do domínio de problema sendo tratado.
3. Se existir mais de 50 valores distintos numa variável discreta. Então, uma amostra de dados não pode conter menos de 50 instâncias observadas.
4. Caso existam mais valores que instâncias observadas a amostra não está completa e deverá ser coletada uma amostra maior. É importante contar com uma base de dados suficientemente grande e representativa.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [x] [[Eu]] Todas estão corretas
- [ ] Apenas em (1) e (3)
- [ ] Apenas (2), (3) e (4)
- [ ] [[Erro]] Apenas em (2) e (4)

## Pergunta 5

Considere as seguintes afirmações em torno das principais tarefas para um projeto de aprendizado de máquina com sucesso. Avalie as afirmações a seguir:

1. O cientista de dados, com auxílio do especialista de domínio, deverá entender o domínio do problema e caracterizá-lo utilizando modelos de ontologia ou mapas conceituais. Este processo ajudará a avaliar posteriormente a representatividade do modelo.
2. O cientista de dados deve identificar os atributos que possam enriquecer a base de dados levando a conhecimento útil e não óbvio.
3. A experiência mostra que o conhecimento não óbvio é resultado muitas vezes de características consideradas ‘fatos’.
4. A descoberta de conhecimento útil e não óbvio considerando unicamente atributos “Julgamentos” pode não levar a conhecimento relevante.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [x] Apenas (1) e (2)
- [ ] Apenas (3) e (4)
- [ ] Somente (2)
- [ ] Somente (1)

## Pergunta 6

Durante a etapa do pré-processamento da base de dados a análise de Outliers é uma tarefa comum e relevante para obter modelos de aprendizado de máquina consistentes. A presença de outliers pode levar a modelos imprecisos quando o modelo é testado ou colocado em produção. Avalie as afirmações a seguir:

1. Outliers são dados com padrões muito diferentes aos demais que fogem ao padrão dos dados. Estes dados precisam ser identificados e analisados.
2. Outliers podem ser produzidos por erros de medição, valores default assumidos durante o preenchimento de uma base de dados ou podem corresponder a valores corretos mas pertencentes a uma base de dados desbalanceada.
3. Na prática, os outliers comumente são eliminados. Porém, poderemos estar negligenciando um conjunto de instâncias que podem trazer novos conhecimentos acerca do domínio de problema.
4. A detecção de outliers pode ser feita por meio de técnicas univariadas, que consistem em explorar cada atributo e variabilidade dos valores em torno da média. Quando a variabilidade é grande pode indicar registros, potenciais outliers.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (2), (3) e (4)
- [ ] Apenas (2) e (4)
- [x] Todas são corretas
- [ ] Apenas (1), (2) e (3)

## Pergunta 7

Durante a caracterização dos dados e para fins de classificação, é importante observar os domínios dos atributos. Isto porque uma classificação equivocada pode levar a modelos inconsistentes. Por exemplo, um domínio baseado em regras para definir o perfil ADIPLENTE e INADIPLENTE no setor bancário pode ser:

1. SE VALOR DA DÍVIDA < R$ 50,00 então o CLIENTE NÂO pode ser considerado perfil INADIPLENTE.
2. SE VALOR DA DÍVIDA < R$ 500,00, mas o CLIENTE nunca ficou INADIPLENTE durante toda sua relação com o banco, NÂO pode ser considerado perfil INADIPLENTE.
3. SE VALOR DA DÍVIDA < R$ 500,00, mas o CLIENTE possui um histórico permanente de dívidas ativas com o banco isso NÂO pode caracterizar um perfil INADIPLENTE.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Somente (3)
- [x] Apenas (1) e (2)
- [ ] Todas estão corretas
- [ ] Somente (1)

## Pergunta 8

Durante a etapa do pré-processamento da base de dados a análise de dados ausentes é uma tarefa relevante para obter modelos de aprendizado de máquina consistentes. Uma estratégia seria imputar valores aos dados faltantes. De forma a imputar valores consistentes seria interessante conhecer previamente o mecanismo que os gerou. A literatura aponta três mecanismos principais: MCAR, MAR e NMAR. Avalie as afirmações a seguir:

1. No mecanismo MCAR, os valores ausentes estão distribuídos aleatoriamente, ou seja, a probabilidade de encontrar um valor ausente é a mesma para qualquer valor do atributo.
2. No mecanismo MAR a probabilidade de encontrar um valor ausente depende de outro valor de outro atributo.
3. No mecanismo NMAR: a probabilidade de encontrar um valor ausente depende do próprio valor do atributo que possui dado ausente.
4. Um mecanismo híbrido pode combinar os mecanismos MAR e MCAR, mas não o NMAR.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Somente em (1)
- [ ] Somente em (4)
- [ ] Apenas (2) e (3)
- [x] Apenas (1), (2) e (3)

## Pergunta 9

Durante a etapa do pré-processamento da base de dados a análise de dados ausentes é uma tarefa relevante para obter modelos de aprendizado de máquina consistentes. Para alguns autores dados ausentes correspondem não somente a dados não preenchidos na base de dados, mas também a dados falsos, pois o valor real não está na base de dados. Avalie as afirmações a seguir:

1. O especialista deve tomar uma decisão pela eliminação ou não do atributo ou do registro, contendo valores ausentes. Isto pode levar a perda de representatividade da base de dados.
2. Uma alternativa para o menor impacto é procurar pela recuperação dos valores ausentes. Esta pode ser uma tarefa árdua que exige nova coleta de dados.
3. O responsável pela condução do projeto pode optar por técnicas de aprendizado de maquina que lidam melhor com a presença de valores ausentes. Por exemplo, técnicas como de redes neurais artificiais (RNA) e suporte vector machine (SVM).
4. Uma estratégia para lidar com alores ausentes é optar pela imputação pela média.

Não é correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] [[Erro]] Apenas (3) e (4)
- [ ] Somente em (2)
- [ ] Somente em (1)
- [x] Somente em (3)

## Pergunta 10

Considere as seguintes afirmações em torno das principais tarefas de um projeto de aprendizado de máquina. Avalie as afirmações a seguir:

1. Um valor ausente corresponde àquela variável cujo valor não foi inserido no conjunto de dados, mas seu valor atual existe no domínio de problema. Quando o mecanismo de aussência é MAR recomenda-se a busca do mecanismo de forma a imputar o valor mais adequado.
2. Algoritmos de classificação como árvores de decisão, baseado na entropia e classificador bayesiano, baseado na probabilidade de ocorrência dos eventos, podem apresentar bons resultados desde que existam poucos dados ausentes na base.
3. Consideremos um problema para classificação binária. O desbalanceamento em relação às aos conjuntos de treinamento pode não exigir técnicas de balanceamento prévias se o desbalanceamento for menor que 1:10.
4. A etapa de “seleção de atributos” é essencial para diminuir a redundância, a dimensionalidade e aumentar a precisão dos algoritmos de data mining, como também à compreensibilidade do modelo.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [x] [[Eu]] Todas estão corretas
- [ ] Apenas (2) e (3)
- [ ] Somente (1)
- [ ] [[Erro]] Apenas (2), (3) e (4)
