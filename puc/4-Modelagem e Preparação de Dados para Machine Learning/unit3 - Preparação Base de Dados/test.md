# Test

## Pergunta 1

Uma base de dados é considerada desbalanceada se existe nela objetos (instâncias) pertencentes a uma classe, em menor número em relação à outra. Avalie as afirmações a seguir:

1. De acordo com a literatura pode ser considerado base desbalanceada se a relação do número de objetos das classes são da ordem de 1:10.
2. O desbalanceamento nas bases de dados pode ocorrer por motivos intrínsecos devido à própria natureza do problema. Por exemplo, em detecção de fraudes, existem poucas instâncias (pessoas) que cometem fraudes em relação às outras.
3. O desbalanceamento nas bases de dados pode ocorrer por motivos não intrínsecos devido ao limitado processo da coleta de dados, por razões econômicas ou de privacidade. Uma alternativa é inserir novas instâncias para diminuir o desbalanceamento.
4. Quando a base de dados é desbalanceada é necessário aplicar métodos para equilibrar a quantidade de objetos de cada classe. Se não for feito isto, o modelo pode apresentar comportamento polarizado.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (3) e (4)
- [ ] Apenas (1) e (2)
- [x] Apenas (2), (3) e (4)
- [ ] Apenas (2) e (3)

## Pergunta 2

O pré-processamento da base de dados busca adequar o conjunto de dados para serem aplicados aos algoritmos de Aprendizado de máquina. Avalie as afirmações a seguir:

1. Todos os atributos do conjunto de dados precisam ser codificados e transformados de forma que possam servir de entrada para os algoritmos de Mineração de Dados.
2. Normalmente quando se deseja aplicar uma medida de dissimilaridade (por exemplo, cálculo da distância euclideana) é necessária a transformação ou mudanças de escala dos atributos. Isto para garantir que não existam atributos com maior significado que outras.
3. A melhor forma de transformar os dados é verificar quais requisitos a solução precisa atender e quais são os requisitos que a técnica de mineração de dados impõe.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Somente em (1)
- [x] Apenas em (2) e (3)
- [ ] Apenas em (1) e (3)
- [ ] Apenas em (1) e (2)

## Pergunta 3

As técnicas de discretização podem ser classificadas sobre vários aspectos: Supervisionadas e Não supervisionadas e pelo método utilizado, Direto e Incremental. Avalie as afirmações a seguir:

1. A discretização Supervisionada não leva em consideração a informação dos grupos a que pertencem as instâncias de treinamento.
2. A discretização Não supervisionada leva em conta os grupos a que pertencem as instâncias no conjunto de treinamento.
3. Os métodos de discretização diretos dividem os valores do atributo em um número de intervalos previamente definido pelo usuário.
4. Os métodos incrementais para a discretização de atributos é realizado iterativamente até que um critério de parada seja alcançado.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (1) e (2)
- [ ] Apenas (2) e (3)
- [x] Apenas (3) e (4)
- [ ] Todas estão corretas

## Pergunta 4

Durante a preparação de dados podem existir valores “outliers”. Caso nosso objetivo NÂO seja minerar eventos raros e considerando uma variável com GRANDE VARIABILIDADE (desvio padrão alto) a prática mostra que a eliminação de outliers pode seguir as seguintes regras:

1. Eliminar registros se: Valor atributo > Média + 3*Desvio-padrão ou Valor atributo < Média - 3*Desvio-padrão.
2. Eliminar registros se: Valor atributo > Média + 1*Desvio-padrão ou Valor atributo < Média - 1*Desvio-padrão.
3. Eliminar registros se: Valor atributo > Média + 2*Desvio-padrão.
4. Eliminar registros se: Valor atributo < Média - 2*Desvio-padrão.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Eliminar registros se: Valor atributo > Média + 2*Desvio-padrão.
- [x] Eliminar registros se: Valor atributo > Média + 2*Desvio-padrão ou Valor atributo < Média - 2*Desvio-padrão.
- [ ] Eliminar registros se: Valor atributo > Média + 1*Desvio-padrão ou Valor atributo < Média - 1*Desvio-padrão.
- [ ] Eliminar registros se: Valor atributo < Média - 2*Desvio-padrão.

## Pergunta 5

Durante a preparação de dados a aplicação de técnicas de discretização possuem algumas vantagens e desvantagens. Avalie as afirmações a seguir:

1. Os Algoritmos de aprendizado de máquina, como redes neurais artificiais e SVM são capazes de lidar com dados contínuos, porém são menos eficientes para interpretabilidade dos resultados.
2. O processo de discretização também pode ser entendido como uma técnica para redução de dados a qual facilita a interpretabilidade dos resultados.
3. O processo de discretização pode acarretar perda de informação. Isso pelo fato de que o intervalo de discretização pode esconder “insights” interessantes.
4. Reduzir a perda de informação é o principal objetivo quando aplicamos técnicas de discretização.

É correto o que se afirma em:

Grupo de escolhas da pergunta

- [ ] Apenas (1), (2) e (4)
- [x] Todas estão corretas
- [ ] Apenas (2) e (4)
- [ ] Apenas (1) e (4)
