# JSONPath vs JMESPath

## Base JSON de Exemplo

Usaremos o seguinte JSON para todos os nossos exemplos:

```json
{
  "livraria": {
    "titulo": "Catálogo de Livros Técnicos",
    "autorPrincipal": "Dr. Tech",
    "livros": [
      {
        "titulo": "Aprendendo JSONPath",
        "autores": ["Alice", "Bob"],
        "ano": 2020,
        "preco": 25.50,
        "disponivel": true,
        "editora": {
          "nome": "Editora Inovação",
          "cidade": "São Paulo"
        }
      },
      {
        "titulo": "Dominando JMESPath",
        "autores": ["Charlie"],
        "ano": 2021,
        "preco": 30.00,
        "disponivel": false,
        "editora": {
          "nome": "Editora Global",
          "cidade": "Rio de Janeiro"
        }
      },
      {
        "titulo": "Introdução ao Web Scraping",
        "autores": ["David", "Eve", "Frank"],
        "ano": 2019,
        "preco": 20.00,
        "disponivel": true,
        "editora": {
          "nome": "Editora Inovação",
          "cidade": "São Paulo"
        }
      },
      {
        "titulo": "Python para Iniciantes",
        "autores": ["Grace"],
        "ano": 2022,
        "preco": 35.00,
        "disponivel": true,
        "tags": ["Programação", "Iniciante"]
      }
    ]
  },
  "usuarios": [
    {
      "id": 1,
      "nome": "Ana",
      "isAdmin": true,
      "ultimosAcessos": ["2025-06-19", "2025-06-20"]
    },
    {
      "id": 2,
      "nome": "Bruno",
      "isAdmin": false,
      "ultimosAcessos": ["2025-06-18"]
    }
  ],
  "configuracoes": {
    "tema": "escuro",
    "notificacoes": true
  }
}
```

## Exemplos Comparativos de JSONPath e JMESPath

Vamos ver como ambos lidam com diferentes cenários.

### 1. Selecionando um Valor Simples

- **Objetivo:** Obter o título principal da livraria.

  - **JSONPath:** `$.livraria.titulo`
  - **JMESPath:** `livraria.titulo`
  - **Resultado:** `"Catálogo de Livros Técnicos"`
  - **Comentário:** Ambos são diretos. JMESPath é um pouco mais conciso ao não exigir o `$`.

### 2. Selecionando Todos os Títulos dos Livros

- **Objetivo:** Listar os títulos de todos os livros no array `livros`.

  - **JSONPath:** `$.livraria.livros[*].titulo`
  - **JMESPath:** `livraria.livros[*].titulo` ou `livraria.livros[].titulo`
  - **Resultado:** `["Aprendendo JSONPath", "Dominando JMESPath", "Introdução ao Web Scraping", "Python para Iniciantes"]`
  - **Comentário:** Novamente, muito semelhantes. JMESPath oferece a sintaxe `[]` como um atalho para `[*]`.

### 3. Selecionando o Primeiro Autor do Segundo Livro

- **Objetivo:** Obter o nome do primeiro autor do livro "Dominando JMESPath".

  - **JSONPath:** `$.livraria.livros[1].autores[0]`
  - **JMESPath:** `livraria.livros[1].autores[0]`
  - **Resultado:** `"Charlie"`
  - **Comentário:** Idênticos na sintaxe para acessar índices de array.

### 4. Filtrando Livros Disponíveis (Condição Simples)

- **Objetivo:** Listar os títulos dos livros que estão `disponivel: true`.

  - **JSONPath:** `$.livraria.livros[?(@.disponivel == true)].titulo`
  - **JMESPath:** `livraria.livros[?disponivel].titulo` (ou ` livraria.livros[?disponivel == `true`].titulo`)
  - **Resultado:** `["Aprendendo JSONPath", "Introdução ao Web Scraping", "Python para Iniciantes"]`
  - **Comentário:** JMESPath é mais conciso para booleanos verdadeiros. Note que o JMESPath não exige `(@.)` como o JSONPath (em algumas implementações) e usa crases para literais booleanos/numéricos.

### 5. Filtrando Livros por Preço e Editora

- **Objetivo:** Encontrar os títulos dos livros que custam mais de 25.00 E são da "Editora Inovação".

  - **JSONPath:** `$.livraria.livros[?(@.preco > 25 && @.editora.nome == 'Editora Inovação')].titulo`
  - **JMESPath:** ` livraria.livros[?preco > `25.00` && editora.nome == 'Editora Inovação'].titulo `
  - **Resultado:** `["Aprendendo JSONPath"]`
  - **Comentário:** Ambos suportam múltiplos filtros com operadores lógicos (`&&` ou `and` dependendo da implementação do JSONPath). A sintaxe de JMESPath costuma ser mais direta.

### 6. Selecionando Último Acesso do Usuário Admin (Funções e Múltiplos Filtros)

- **Objetivo:** Obter a data do último acesso do usuário que é admin.

  - **JSONPath:** Pode ser feito em duas etapas na maioria das implementações:
        1. `$.usuarios[?(@.isAdmin == true)]` (seleciona o objeto do admin)
        2. `$.usuarios[?(@.isAdmin == true)].ultimosAcessos[-1]` (se a implementação suportar o índice negativo direto no filtro, o que não é padrão em todas). Ou então, selecionar o array e pegar o último elemento via código.
  - **JMESPath:** `usuarios[?isAdmin].ultimosAcessos | [0] | [-1]` ou `users[?isAdmin][0].ultimosAcessos | [-1]`
        *Ou, mais elegantemente, se só houver um admin:*
        ` usuarios[?isAdmin][0].ultimosAcessos | [length(@) - `1`]`
        *Ou para qualquer array `ultimosAcessos` onde o último elemento é desejado:*
        `usuarios[?isAdmin].ultimosAcessos[-1]`
  - **Resultado:** `"2025-06-20"`
  - **Comentário:** JMESPath tem o operador pipe (`|`) que permite encadear operações, tornando a extração do último elemento de um array mais fluida e explícita, especialmente com a função `length()` e índices negativos, que são padrão. JSONPath tem mais variações na implementação do índice negativo.

### 7. Cenário: Remodelando a Saída (Projeções) - **JMESPath Vantagem**

- **Objetivo:** Criar um novo array de objetos contendo apenas o `titulo` e o `primeiroAutor` de cada livro.

  - **JSONPath:** **Não suporta remodelagem (projeções) de saída diretamente.** Você teria que selecionar os dados e depois usar código (JavaScript, Python, etc.) para iterar sobre o resultado e construir a nova estrutura.
    - Etapa 1: `$.livraria.livros[*].titulo`
    - Etapa 2: `$.livraria.livros[*].autores[0]`
    - Etapa 3: Combinar isso em código.
  - **JMESPath:** `livraria.livros[*].{titulo: titulo, primeiroAutor: autores[0]}`
  - **Resultado:**

     ```json
     [
       {"titulo": "Aprendendo JSONPath", "primeiroAutor": "Alice"},
       {"titulo": "Dominando JMESPath", "primeiroAutor": "Charlie"},
       {"titulo": "Introdução ao Web Scraping", "primeiroAutor": "David"},
       {"titulo": "Python para Iniciantes", "primeiroAutor": "Grace"}
     ]
     ```

  - **Comentário:** Este é um dos pontos mais fortes do JMESPath. Ele permite criar novas estruturas JSON a partir dos dados existentes, algo que JSONPath não faz nativamente. Isso reduz muito a necessidade de pós-processamento com código.

### 8. Cenário: Acessando Chaves com Caracteres Especiais - Ambos Suportam

- **Objetivo:** Acessar a configuração de "notificações".

  - **JSONPath:** `$.configuracoes.notificacoes`
  - **JMESPath:** `configuracoes.notificacoes`
  - **Resultado:** `true`
  - **Comentário:** Ambos lidam bem com nomes de chaves normais. Se houvesse uma chave como `"minha-chave-com-traco"`, JMESPath usaria `"minha-chave-com-traco"` e JSONPath usaria `['minha-chave-com-traco']` ou `."minha-chave-com-traco"` dependendo da implementação.

### 9. Cenário: Uso de Funções Complexas (e.g., `contains`) - **JMESPath Vantagem**

- **Objetivo:** Encontrar os títulos dos livros que têm "Programação" em suas `tags`.

  - **JSONPath:** Algumas implementações de JSONPath permitem funções customizadas, mas `contains` para verificar um item em um array **não é parte da especificação padrão**. Você teria que selecionar todos os livros e filtrar em código.
  - **JMESPath:** `livraria.livros[?contains(tags, 'Programação')].titulo`
  - **Resultado:** `["Python para Iniciantes"]`
  - **Comentário:** JMESPath tem um conjunto rico de funções embutidas (string, numéricas, array, etc.) que expandem muito suas capacidades de filtragem e transformação, enquanto JSONPath é mais focado em navegação e filtros baseados em comparação simples.

## Conclusão Comparativa

| Característica             | JSONPath                                                           | JMESPath                                                             |
| :------------------------- | :----------------------------------------------------------------- | :------------------------------------------------------------------- |
| **Foco Principal**         | Seleção e extração de dados existentes.                            | Seleção, extração e **transformação/remodelagem** de dados.          |
| **Sintaxe**                | Inspirada em XPath e JavaScript. Pode variar entre implementações. | Mais consistente, com operadores e funções claras.                   |
| **Projeções/Remodelagem**  | **Não suporta nativamente.** Requer código adicional.              | **Suporte nativo forte** (`{}` e `[]` para criar novas estruturas).  |
| **Funções**                | Limitadas ou dependentes da implementação (ex: `length`, `count`). | Rico conjunto de funções embutidas (string, numéricas, array, etc.). |
| **Encadeamento**           | Geralmente indireto (seleciona, depois processa).                  | Direto com o operador \| (pipe), para operações sequenciais.         |
| **Expressividade**         | Boa para seleções diretas e filtros simples.                       | Mais expressivo para consultas complexas e transformações.           |
| **Índices Negativos**      | Varia entre implementações.                                        | Suporte padrão (`[-1]`).                                             |
| **Booleano/Null Literais** | Varia (ex: `true`, `null`).                                        | Usa crases (`true`, `null`) ou `!chave` para ausência.               |

Em resumo, se sua necessidade é primariamente **selecionar e filtrar dados existentes** de uma estrutura JSON, o **JSONPath** é uma ferramenta adequada e geralmente mais leve. No entanto, se você precisa de capacidades mais avançadas como **remodelar a estrutura da saída, encadear operações complexas ou usar funções embutidas para manipulação de dados**, o **JMESPath** é significativamente mais poderoso e flexível, reduzindo a quantidade de código que você precisaria escrever.
