# Tabelas

Um dos primeiros passos para analisar um arquivo de dados, especialmente quando o número de observações for grande, é a distribuição de frequências de cada variável.
- Uma distribuição de frequências é uma tabela que mostra categorias, valores ou intervalos de valores de acordo com as ocorrências.

[Título]
| cabeçalho 1         | cabeçalho 2       | cabeçalho 3 |
| ------------------- | ----------------- | ----------- |
| Coluna indicadora 1 | Casa ou Célula 12 | Corpo       |
| Coluna indicadora 2 | Casa ou Célula 22 | ^^          |
| Coluna indicadora 3 | Casa ou Célula 32 | ^^          |
| Coluna indicadora 4 | Casa ou Célula 42 | ^^          |
> Fonte: xpto

## Distribuição de frequências

[Tabela 1 – Distribuição de freqüências do provedor usado pelo visitante do site]
| Provedor  | Frequência | Porcentagem |
| --------- | ---------- | ----------- |
| A         | 10         | 25,0        |
| B         | 17         | 42,5        |
| C         | 7          | 17,5        |
| D         | 6          | 15,0        |
|           |            |             |
| **Total** | **40**     | **100,0**   |

[Tabela 2 – Distribuição de frequências do número de defeitos encontrados em escadas no final da linha de produção]
| Provedor | Frequência | Porcentagem | Frequência <br>acumulada | Porcentagem <br>acumulada |
| -------- | ---------- | ----------- | ------------------------ | ------------------------- |
| A        | 10         | 25,0        | 13                       |
| B        | 17         | 42,5        | 28                       |
| C        | 7          | 17,5        | 38                       |
| D        | 6          | 15,0        | 45                       |
|          |            |             | 47                       |


| Nº de defeitos<br>encontrados | Frequência | Porcentagem | Frequência<br>acumulada | Porcentagem<br>acumulada |
| ----------------------------- | ---------- | ----------- | ----------------------- | ------------------------ |
| 0                             | 13         | 27,1        | 13                      | 27,1                     |
| 1                             | 15         | 31,3        | 28                      | 58,4                     |
| 2                             | 10         | 20,8        | 38                      | 79,2                     |
| 3                             | 7          | 14,6        | 45                      | 93,8                     |
| 4                             | 2          | 4,2         | 47                      | 98                       |
| 7                             | 1          | 2,1         | 48                      | 100                      |
| **Total**                     | **48**     | **100,0**   |                         |                          |

# Distribuição de frequências por intervalos

A Regra de Sturges é uma das regras mais utilizadas na Estatística para construção de uma tabela de frequências por intervalos. Isso porque a fórmula de Sturges nos fornece uma quantidade adequada de classes para os mais variados tamanhos de amostras.

A regra de Sturges envolve os seguintes passos:

Cálculo Ampitude da Amostra:
$$A= max-min$$

Cálculo Intervalos ou Classes da Tabela:
$$
k=1+3.322 . \log{n}
\\
florr(k) | ceil(k)
$$

Os dados, a seguir, representam o tempo (em segundos) que operadores gastam para montar um equipamento na linha de produção de uma empresa: 

4,7 4,9 5,1 5,4 5,7 6 6,3 6,8 7,3 8,9 4,8 4,9 5,2 5,5 5,7 6,2 6,4 6,9 8,2 9,1 4,8 5 5,3 5,6 5,7 6,2 6,5 7 8,2 9,9 4,9 5 5,4 5,6 5,9 6,2 6,7 7,1 8,3 14,1 4,9 5 5,4 5,7 6 6,3 6,8 7,3 8,4 15,

Cálculo da amplitude dos intervalos:
$$a_k=\frac{A}{k}$$

Utilizando os passos da regra de Sturges, temos:
$$A = 15,2 – 4,7 = 10,5$$

$$K = 1 + 3,322 . log 50 = 1 + 3,322 . 1,699 = 6,644$$
(pode-se escolher entre 6 ou 7 classes)

$$Ak= 10,5 / 6 = 1,75$$
(nesse caso, escolhendo 6 classes, cada classe deverá ter uma amplitude de 1,8 segundos, seguimos o mesmo número de casas decimais dos dados da amostra)

[Tabela 3 - Distribuição de frequências do tempo gasto (em segundos) para a montagem de um equipamento na linha de produção (⊢, -, ⊣)]

| Tempo       | Frequência | Porcentagem | Frequência<br>acumulada | Porcentagem<br>acumulada |
| ----------- | ---------- | ----------- | ----------------------- | ------------------------ |
| 4,7 ⊢ 6,5   | 32         | 64,0        | 32                      | 64,0                     |
| 6,5 ⊢ 8,3   | 11         | 22,0        | 43                      | 86,0                     |
| 8,3 ⊢ 10,1  | 5          | 10,0        | 48                      | 96,0                     |
| 10,1 ⊢ 11,9 | 0          | 0,0         | 48                      | 96,0                     |
| 11,9 ⊢ 13,7 | 0          | 0,0         | 48                      | 96,0                     |
| 13,7 ⊢ 15,5 | 2          | 4,0         | 50                      | 100,0                    |
| Total       | 50         | 100,0       | -                       | -                        |

## Tabelas de contingência

As tabelas de contingência são a forma usual de apresentar uma distribuição de frequência conjunta de duas ou mais variáveis.

| Lado     | Posição            || Total |
| ^^       | Dianteira | Traseira | ^^  |
| -------- | --------- | -------- | --- |
| Direito  | 32        | 28       | 60  |
| Esquerdo | 35        | 57       | 92  |
| Total    | 67        | 85       | 152 |

| Lado     | Posição            || Total |
| ^^       | Dianteira | Traseira | ^^   |
| -------- | --------- | -------- | ---- |
| Direito  | 53%       | 47%      | 100% |
| Esquerdo | 38%       | 62%      | 100% |
| Total    | 44%       | 56%      | 100% |

| Lado     | Posição            || Total |
| ^^       | Dianteira | Traseira | ^^   |
| -------- | --------- | -------- | ---- |
| Direito  | 48%       | 33%      | 39%  |
| Esquerdo | 52%       | 67%      | 61%  |
| Total    | 100%      | 100%     | 100% |

| Lado     | Posição            || Total |
| ^^       | Dianteira | Traseira | ^^   |
| -------- | --------- | -------- | ---- |
| Direito  | 21%       | 18%      | 39%  |
| Esquerdo | 23%       | 38%      | 61%  |
| Total    | 44%       | 56%      | 100% |

Estatística | Matemática|||Totais
| ^^     | 0⊢4 | 4-7 | 7⊢10 | ^^  |
| ------ | --- | --- | ---- | --- |
| 0⊢4    | 32  | 25  | 5    | 62  |
| 4-7    | 20  | 183 | 82   | 285 |
| 7⊢10   | 7   | 27  | 19   | 53  |
| Totais | 59  | 235 | 106  | 400 |
