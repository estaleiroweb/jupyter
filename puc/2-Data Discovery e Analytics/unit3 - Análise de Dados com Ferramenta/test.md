# Test

## Pergunta 1

Assinale Verdade ou Falso para afirmação a seguir sobre criar Previsão na ferramenta Tableau.

"Para produzir uma previsão, basta ter uma série temporal com a coluna Ano, não sendo necessária a utilização da coluna data completa."

>Falso.
>
> Para criar uma previsão no Tableau, é necessário utilizar uma série temporal, mas a granularidade da data é importante. O Tableau precisa de dados em uma coluna de data completa (com dia, mês e ano, ou pelo menos mês e ano) para fazer previsões com maior precisão. A coluna apenas com o ano pode ser insuficiente, especialmente para previsões mais detalhadas.

## Pergunta 2

Assinale Verdade ou Falso para afirmação a seguir sobre utilização do nome de cidades na ferramenta Tableau.

Caso seus dados não apresentem a Latitude e Longitude e apenas o nome das cidades, você poderá utilizá-lo desde que, o nome das cidades tenha pelo menos 50 mil habitantes.

> Falso.
>
> No Tableau, é possível utilizar o nome das cidades para mapeamento geográfico, mesmo que seus dados não incluam as coordenadas de latitude e longitude. O Tableau possui um banco de dados interno com informações geográficas que permite identificar cidades e localidades, independentemente do número de habitantes. Contudo, quanto mais conhecida a cidade, maior a chance de o Tableau identificá-la corretamente, mas não há uma exigência mínima de 50 mil habitantes para essa funcionalidade.

## Pergunta 3

Analise a imagem abaixo da confecção de um Mapa na ferramenta Power BI, mostrando as localizações dos Estados brasileiros, baseados nas siglas das UFs. Veja que estão espalhadas em outros países diferentemente do Brasil.

Desta forma, marque dentre as opções, aquela que apresenta a sintaxe correta que corrigirá este problema ao adotar uma nova coluna:

- [ ] UFs Brasil = [UF] || ", Brasil"
- [x] UFs Brasil = [UF] & ", Brasil"
- [ ] UFs Brasil = [UF] + ', ' + 'Brasil'
- [ ] UFs Brasil = [UF] + ', Brasil'

## Pergunta 4

Sobre os conceitos da ferramenta Tableau, assinale a alternativa VERDADEIRA dentre as alternativas abaixo:
Grupo de escolhas da pergunta

- [ ] Possui o gráfico de Rosca nativo.
- [ ] Compartilhamento das informações depende da TI.
- [x] As visualizações não tem interações entre elas, por definição. Mas no Painel, ações podem ser criadas para que isso ocorra.
- [ ] Apenas as siglas dos Estados do Brasil, presentes em uma determinada base de dados, utilizando um Windows (utilizando as Configurações Regionais) em português, não é suficiente para que o Tableau posicione corretamente em um mapa.

## Pergunta 5

Avalie as 03 afirmações abaixo como sendo verdadeiras ou falsas sobre a ferramenta Tableau e assinale a alternativa correspondente.

- I - No Tableau não se pode criar o recurso Dicas de Ferramentas, como é criado em outras ferramentas.
  > Falso. No Tableau, é possível criar o recurso Dicas de Ferramentas (tooltips) que fornecem informações adicionais quando o usuário passa o cursor sobre um elemento da visualização.
- II - Tableau Desktop, é possível criar dashboards interativos que podem ser publicados diretamente no Tableau Server (pago) e Tableau Public, por exemplo.
  > Verdadeiro. No Tableau Desktop, é possível criar dashboards interativos e publicá-los tanto no Tableau Server (pago) quanto no Tableau Public (gratuito).
- III - O Tableau Desktop não permite a conexão com fontes de dados em tempo real, apenas com arquivos estáticos.
  > Falso. O Tableau Desktop permite conexões com fontes de dados em tempo real, além de suportar arquivos estáticos.

Grupo de escolhas da pergunta

- [x] II, apenas
- [ ] III, apenas
- [ ] II e III, apenas
- [ ] I e II, apenas
