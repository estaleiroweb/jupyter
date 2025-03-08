# `http.server`

## Atributos Principais

| Atributo           | Descrição                                                                   |
| ------------------ | --------------------------------------------------------------------------- |
| `server`           | Referência ao servidor que está manipulando a requisição.                   |
| `client_address`   | Endereço IP do cliente que fez a requisição.                                |
| `command`          | Método HTTP usado (GET, POST, etc.).                                        |
| `path`             | Caminho da URL solicitada pelo cliente.                                     |
| `headers`          | Dicionário com todos os cabeçalhos da requisição HTTP.                      |
| `rfile`            | Stream de entrada para leitura do corpo da requisição (usado em POST, PUT). |
| `wfile`            | Stream de saída para enviar a resposta ao cliente.                          |
| `protocol_version` | Versão do protocolo HTTP (ex: "HTTP/1.0" ou "HTTP/1.1").                    |
| `request_version`  | Versão do HTTP enviada pelo cliente.                                        |
| `close_connection` | Define se a conexão deve ser fechada após a resposta.                       |
| `timeout`          | Tempo máximo antes de encerrar a conexão.                                   |
| `requestline`      | Primeira linha da requisição HTTP recebida.                                 |

## Métodos Importantes

### Métodos para Lidar com Requisições

| Método         | Descrição                                                                   |
| -------------- | --------------------------------------------------------------------------- |
| `do_GET()`     | Lida com requisições **GET** (quando o cliente pede um recurso).            |
| `do_POST()`    | Lida com requisições **POST** (quando o cliente envia dados).               |
| `do_PUT()`     | Manipula **PUT**, usado para enviar dados ao servidor.                      |
| `do_DELETE()`  | Manipula **DELETE**, usado para apagar recursos.                            |
| `do_HEAD()`    | Responde a requisições **HEAD** (como GET, mas sem o corpo da resposta).    |
| `do_OPTIONS()` | Responde a requisições **OPTIONS** (permite consultar métodos disponíveis). |

### Métodos para Enviar Respostas

| Método                              | Descrição                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------- |
| `send_response(code, message=None)` | Envia o status HTTP (ex: `send_response(200)`).                            |
| `send_error(code, message=None)`    | Envia um erro HTTP e exibe uma página de erro.                             |
| `send_header(key, value)`           | Define um cabeçalho HTTP (ex: `send_header("Content-Type", "text/html")`). |
| `end_headers()`                     | Finaliza os cabeçalhos da resposta.                                        |

### Métodos para Manipular Arquivos

| Método                         | Descrição                                                                           |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| `translate_path(path)`         | Converte a URL solicitada para um caminho no sistema de arquivos do servidor.       |
| `guess_type(path)`             | Retorna o tipo MIME com base na extensão do arquivo (ex: "text/html" para `.html`). |
| `copyfile(source, outputfile)` | Copia o conteúdo de um arquivo para a saída (`wfile`).                              |
| `list_directory(path)`         | Retorna uma página HTML com a listagem de arquivos se o diretório for acessado.     |

### Métodos Auxiliares

| Método                             | Descrição                                                            |
| ---------------------------------- | -------------------------------------------------------------------- |
| `log_message(format, *args)`       | Exibe mensagens de log (padrão: mostra na saída padrão do servidor). |
| `version_string()`                 | Retorna a versão do servidor HTTP.                                   |
| `date_time_string(timestamp=None)` | Retorna a data e hora formatadas no estilo HTTP.                     |
| `log_error(format, *args)`         | Exibe mensagens de erro no log.                                      |

## Exemplo de Uso

Aqui está um exemplo que usa alguns desses métodos para criar um **servidor HTTP personalizado**:

```python
import http.server

class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Responde a requisições GET"""
        self.send_response(200)  # Código HTTP 200 OK
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Servidor Python!</h1></body></html>")

    def log_message(self, format, *args):
        """Sobrescreve o log padrão para exibir apenas mensagens personalizadas."""
        print(f"[LOG] {self.client_address[0]} - {format % args}")

# Inicia o servidor
if __name__ == "__main__":
    with http.server.HTTPServer(("localhost", 8080), HttpHandler) as server:
        print("Servidor rodando em http://localhost:8080")
        server.serve_forever()
```

## Conclusão

A classe `SimpleHTTPRequestHandler` já tem **muitos métodos prontos**, mas podemos sobrescrever qualquer um deles para personalizar o comportamento do servidor.

Se precisar de algo mais avançado, como:
✅ Autenticação  
✅ Sessões persistentes  
✅ Manipulação de JSON  
