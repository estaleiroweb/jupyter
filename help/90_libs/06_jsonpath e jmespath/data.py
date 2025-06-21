# JSON de Exemplo para JSONPath, JMESPath e JSON Pointer
json_data = {
  "livraria": {
    "titulo": "Catálogo de Livros Técnicos",
    "autorPrincipal": "Dr. Tech",
    "livros": [
      {
        "titulo": "Aprendendo JSONPath",
        "autores": ["Alice", "Bob"],
        "ano": 2020,
        "preco": 25.50,
        "disponivel": True,
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
        "disponivel": False,
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
        "disponivel": True,
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
        "disponivel": True,
        "tags": ["Programação", "Iniciante"]
      }
    ]
  },
  "usuarios": [
    {
      "id": 1,
      "nome": "Ana",
      "isAdmin": True,
      "ultimosAcessos": ["2025-06-19", "2025-06-20"]
    },
    {
      "id": 2,
      "nome": "Bruno",
      "isAdmin": False,
      "ultimosAcessos": ["2025-06-18"]
    }
  ],
  "configuracoes": {
    "tema": "escuro",
    "notificacoes": True,
    "chave~com/traco": "valor" # Chave com caracteres especiais para teste
  }
}

# HTML de Exemplo para CSS Path e XPath
html_doc = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Exemplo BeautifulSoup</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Bem-vindo ao Meu Site</h1>
        <nav>
            <ul id="lista-produtos">
                <li><a href="/" class="menu-link active" id="home">Home</a></li>
                <li><a href="/sobre" class="menu-link">Sobre Nós</a></li>
                <li><a href="/contato" class="menu-link">Contato</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="primeira-secao">
            <h2>Nossa História</h2>
            <p class="paragrafo-info">Este é um parágrafo sobre a história da empresa.</p>
            <p>Este é outro parágrafo.</p>
            <img src="historia.jpg" alt="Foto histórica" data-id="123">
        </section>

        <section class="conteudo-extra">
            <h3>Nossos Serviços</h3>
            <div class="servico" data-tipo="web">
                <h4>Desenvolvimento Web</h4>
                <span>Sites modernos e responsivos.</span>
            </div>
            <div class="servico" data-tipo="mobile">
                <h4>Desenvolvimento Mobile</h4>
                <span>Aplicativos inovadores para Android e iOS.</span>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Exemplo. Todos os direitos reservados.</p>
        <a href="#topo" class="scroll-top">Voltar ao topo</a>
    </footer>
</body>
</html>
"""

# Documento XML de exemplo
xml_doc = """<?xml version="1.0" encoding="UTF-8"?>
<livros>
    <livro id="bk001" categoria="ficcao">
        <titulo>A Jornada Estelar</titulo>
        <autor>Alice Smith</autor>
        <ano>2020</ano>
        <preco moeda="USD">25.00</preco>
    </livro>
    <livro id="bk002" categoria="tecnologia">
        <titulo>Python Avançado</titulo>
        <autor>Bob Johnson</autor>
        <ano>2022</ano>
        <preco moeda="BRL">120.00</preco>
    </livro>
</livros>
"""
