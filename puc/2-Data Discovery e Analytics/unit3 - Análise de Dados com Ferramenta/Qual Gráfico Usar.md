# Qual Gráfico Usar?

```mermaid
flowchart TD

    t{"Dados <br>são Temporais <br>(dia, mês, ano)?"}
        t--"Sim"-->c{"Tem <br>Categoria(s)?"}
            c--"Zero"-->t0{"%% TODO"}
            c--"Uma"-->t1{"O que é <br>importante?"}
                t1--"Detalhe"-->t1d{"Muitos <br>Pontos de <br>Dados?"}
                    t1d--"Sim"-->t1dp["Gráfico de Colunas <img src="https://s3.amazonaws.com/thumbnails.venngage.com/template/78d5559b-a1f1-4f1a-b586-9d574fb8055e.png" />"]
                    t1d--"Não"-->t1dm["Gráfico de Linha <img src="https://i.pinimg.com/736x/2e/10/cd/2e10cdca310e5ff1c413da07dee0000e.jpg" />"]
                t1--"Tendência"-->t1t["Gráfico de Linha <img src="https://i.pinimg.com/736x/2e/10/cd/2e10cdca310e5ff1c413da07dee0000e.jpg" />"]
            c--"Várias"-->tn{"Categorias <br>Compõem:"}
                tn--"Um Todo"-->tnt{"Totaliza <br>100%?"}
                    tnt--"Sim"-->tntt["Gráfico de Colunas<br>Sobrepostas <img src="https://exceleasy.com.br/wp-content/uploads/2020/03/Gr%C3%A1fico-de-colunas-100-empilhadas.png" />"]
                    tnt--"Não"-->tntn["Gráfico de Área <img src="https://ninjadoexcel.com.br/wp-content/uploads/2019/01/Segundo-gr%C3%A1fico-de-%C3%A1rea-no-Excel.png" />"]
                tn--"Parciais"--->tnc["Quero Comparar"]
                    tnc-->tncl["Gráfico de Linhas <img src="https://help.qlik.com/pt-BR/qlikview/May2024/Subsystems/Client/Content/Resources/Images/ui_gen_IntroLine.png" />"]
                    tnc-->tncc["Gráfico de Colunas <br>+ Colunas <img src="https://learn.microsoft.com/pt-br/power-bi/visuals/media/power-bi-visualization-combo-chart/power-bi-combo-chart-visualization.png" />"]
        t--"Não"-->s{"Quantas <br>Séries <br>de Ddos?"}
            s--"Uma"-->s1{"Comparar <br>Pontos Fortes<br>e Fracos?"}
                s1--"Sim"-->s1ppoa["Gráfico de Radar <img src="https://www.researchgate.net/profile/Antonio-Francisco-2/publication/276228693/figure/fig1/AS:330433951748098@1455793001530/Figura-2-Grafico-radar-da-inovacao-da-empresa-estudada-gerado-pelo-Assessment-da_Q320.jpg" />"]
                s1--"Não"-->s1n["Gráfico de Barras <br>Horizontais<img src="https://www.slideteam.net/wp/wp-content/uploads/2023/04/Drivers-de-aumento-de-eficiencia-com-grafico-de-barras-horizontais-2.png" />"]
            s--"Duas"-->s2{"Comparar <br>Séries?"}
                s2--"Sim"-->s2c["Gráfico de Dispersão <img src="https://vidadeproduto.com.br/wp-content/uploads/2020/09/diagrama-dispersao-1.png" />"]
                s2--"Não"-->s2n["Gráfico de Barras<br>Soprepostas <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiub35rq-CnB47f_KwgvCC9Ib9396OjwDQww&s" />"]
            s--"Várias"-->sn{"3 Dimensões <br>por Série?"}
                sn--"Sim"-->sn3d["Gráfico de Bolhas <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoGaH3TCdvIbApuVBAPnffuQiQ6ZUdq8alsea-Vsj6MdD6TNKvgX93agzXbQ2dCWE6CzA&usqp=CAU" />"]
                sn--"Não"--->snn["Minhas séries<br>formam um <br>todo de 100%"]
                    snn-->snn1["Gráfico de Pizza <img src="https://miro.medium.com/v2/resize:fit:1400/1*VZSSrmKn4SmzP2vPuCw0DQ.png" />"]
                    snn-->snn2["Gráfico de Rosca <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRd2yqFXMNdyw0wVMI6VqfKl4ClqJuPHqH_cw&s" />"]
```

## Power BI

1. **Gráfico de Barras (Bar Chart)**: Mostra comparações entre diferentes categorias. Pode ser horizontal ou vertical (gráfico de colunas).
2. **Gráfico de Colunas (Column Chart)**: Similar ao gráfico de barras, mas as barras são verticais.
3. **Gráfico de Linhas (Line Chart)**: Mostra tendências ao longo do tempo conectando pontos de dados com linhas.
4. **Gráfico de Pizza (Pie Chart)**: Mostra a proporção de categorias em um todo, dividido em fatias.
5. **Gráfico de Área (Area Chart)**: Similar ao gráfico de linhas, mas as áreas sob as linhas são preenchidas.
6. **Gráfico de Dispersão (Scatter Chart)**: Mostra a relação entre duas variáveis numéricas usando pontos no gráfico.
7. **Gráfico de Bolhas (Bubble Chart)**: Extensão do gráfico de dispersão, onde o tamanho dos pontos reflete uma terceira variável.
8. **Histograma**: Mostra a distribuição de dados dividindo em intervalos (bins).
9. **Gráfico de Rosca (Donut Chart)**: Similar ao gráfico de pizza, mas com um centro vazio.
10. **Gráfico de Cascata (Waterfall Chart)**: Mostra a contribuição individual para o total acumulado ao longo de uma sequência.
11. **Gráfico de Funil (Funnel Chart)**: Mostra um processo em fases, com cada fase representando uma parte do total.
12. **Gráfico de Ponto (Dot Plot)**: Mostra a distribuição de uma ou mais variáveis usando pontos.
13. **Mapa de Calor (Heatmap)**: Mostra os dados em uma matriz colorida, onde as cores representam valores.
14. **Gráfico de Gantt**: Usado para mostrar cronogramas de projetos.
15. **Gráfico de Rede (Network Chart)**: Mostra conexões e interações entre diferentes entidades.
16. **Gráfico de Radar (Radar Chart)**: Mostra múltiplas variáveis em torno de um ponto central.
17. **Mapa Coroplético (Choropleth Map)**: Mapa onde áreas são coloridas de acordo com um valor.
18. **Gráfico de Linhas Empilhadas (Stacked Line Chart)**: Similar ao gráfico de linhas, mas as linhas são empilhadas.
19. **Gráfico de Barras Empilhadas (Stacked Bar Chart)**: Similar ao gráfico de barras, mas as barras são empilhadas.
20. **Sankey Chart**: Mostra o fluxo de dados de uma categoria para outra com larguras variáveis.

## Excel

1. **Gráfico de Colunas**: Usado para mostrar comparações entre diferentes itens.
2. **Gráfico de Linhas**: Mostra tendências ao longo do tempo.
3. **Gráfico de Barras**: Gráfico de colunas orientado horizontalmente.
4. **Gráfico de Pizza**: Mostra a proporção de partes de um todo.
5. **Gráfico de Área**: Gráfico de linhas com áreas preenchidas.
6. **Gráfico de Dispersão**: Mostra a correlação entre duas variáveis.
7. **Gráfico de Bolhas**: Gráfico de dispersão com tamanhos variados de bolhas.
8. **Histograma**: Mostra a distribuição de dados dividida em intervalos.
9. **Gráfico de Rosca**: Similar ao gráfico de pizza, mas com um buraco no meio.
10. **Gráfico de Cascata**: Mostra a contribuição incremental para um total.
11. **Gráfico de Superfície (Surface Chart)**: Mostra uma superfície 3D que conecta dados ao longo de um grid.
12. **Gráfico de Radar**: Mostra variáveis múltiplas em uma grade radial.
13. **Gráfico de Pareto**: Tipo de gráfico de colunas combinado com um gráfico de linhas que mostra a frequência dos valores.
14. **Gráfico de Caixas e Bigodes (Box and Whisker)**: Mostra a distribuição dos dados com quartis e mediana.
15. **Mapa de Árvores (Treemap)**: Mostra hierarquias com retângulos aninhados.
16. **Gráfico de Funil**: Mostra fases de um processo, cada uma representando um total menor.
17. **Mapa (Map Chart)**: Mapa que mostra dados geograficamente.

## Tableau

1. **Gráfico de Barras**: Usado para comparações entre categorias.
2. **Gráfico de Linhas**: Mostra tendências ao longo do tempo.
3. **Gráfico de Pizza**: Mostra proporções em um círculo dividido.
4. **Histograma**: Distribuição dos dados em intervalos.
5. **Gráfico de Dispersão**: Relaciona duas variáveis numéricas com pontos.
6. **Gráfico de Mapa**: Mostra dados geográficos em um mapa.
7. **Gráfico de Bolhas**: Similar ao gráfico de dispersão, com tamanhos variáveis para bolhas.
8. **Mapa de Calor**: Matriz de cores representando valores.
9. **Gráfico de Barras Empilhadas**: Mostra a composição das categorias.
10. **Treemap**: Mostra hierarquias usando retângulos de tamanhos variados.
11. **Mapa de Árvore**: Representa dados hierárquicos com cores e tamanho.
12. **Gráfico de Gantt**: Usado para cronogramas e planejamento de projetos.
13. **Gráfico de Pareto**: Combinação de barras e linhas, mostrando a distribuição cumulativa.
14. **Gráfico de Rede (Network Graph)**: Visualiza interações e conexões entre diferentes entidades.
15. **Mapa de Símbolos**: Usa símbolos em vez de áreas preenchidas para representar valores em um mapa.
16. **Gráfico de Caixas e Bigodes**: Representa a distribuição estatística dos dados.
17. **Sankey Diagram**: Visualiza fluxos de dados ou processos.
18. **Gráfico de Violin (Violin Plot)**: Mostra a distribuição dos dados em torno de uma mediana.

```mermaid
flowchart LR
    A((Início)) --> B{Dados <br>Quantitativos ou <br>Categóricos?}
    
    B -->|Quantitativos| C{Distribuição, <br>Comparação ou <br>Relação?}
    B -->|Categóricos| D{Número de <br>Categorias?}
    
    C -->|Distribuição| E[Histograma <br> Box Plot]
    C -->|Comparação| F[Barras <br>Colunas <br> Linhas]
    C -->|Relação| G[Dispersão <br> Bolhas]

    D -->|"Poucas <br>(<= 5)"| H[Pizza <br> Rosca]
    D -->|"Muitas <br>(> 5)"| I[Barras <br>Colunas <br> Treemap]

    A --> J{Temporal, <br>Geográfico ou <br>Hierárquico?}
    J -->|Temporal| K[Linhas <br>Área]
    J -->|Geográfico| L[Mapa Coroplético <br>Mapa de Símbolos]
    J -->|Hierárquico| M[Treemap <br>Mapa de Árvore]

    A --> N{Número de <br>Variáveis?}
    N -->|Uma Variável| O[Barras <br>Colunas <br>Histograma]
    N -->|Duas Variáveis| P[Dispersão <br>Bolhas]
    N -->|Três ou Mais| Q[Bolhas <br>Rede <br>Violin Plot]

    A --> R{Interatividade <br>Necessária?}
    R -->|Sim| S[Dashboard com Gráficos Interativos]
    R -->|Não| T[Gráficos Estáticos]
```
