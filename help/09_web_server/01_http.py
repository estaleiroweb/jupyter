# -*- coding: utf-8 -*-
import http.server
import http.cookies
import threading
from session import Session
from webserver import WebServer


class HttpHandler(http.server.SimpleHTTPRequestHandler):
    encoding = "utf-8"

    def _load(self) -> Session:
        """Carrega a sessão do usuário ou cria uma nova."""

        id = None
        # Check cookie
        if "Cookie" in self.headers:
            cookies = http.cookies.SimpleCookie(self.headers["Cookie"])
            if "session_id" in cookies:
                id = cookies["session_id"].value
        return Session(id)

    def do_GET(self):
        """Responde às requisições GET e gerencia a sessão."""

        oSess = self._load()

        # Update counter of session
        data = oSess()
        data["acessos"] = data.get("acessos", 0) + 1
        oSess.save(data)

        # Config HTTP response
        self.send_response(200)
        self.send_header("Content-type", f"text/html; charset={self.encoding}")
        # self.send_header("Set-Cookie", f"session_id={oSess}; Path=/")
        # self.send_header("Set-Cookie", f"session_id={self.__id}; Path=/; Max-Age=3600; HttpOnly")
        self.send_header("Set-Cookie", f"session_id={oSess}; Path=/; HttpOnly")
        self.end_headers()
        content_length = int(self.headers.get('Content-Length', 0))
        payload = self.rfile.read(content_length) if content_length else None

        # Show info
        resposta = f"""
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Título da Página</title>
            <meta name="description" content="Descrição da página para SEO.">
            <meta name="keywords" content="palavras-chave, para, SEO">
            <!-- 
            <meta charset="{self.encoding}">
            <link rel="icon" href="favicon.ico" type="image/x-icon">
            <link rel="stylesheet" href="style.css">
            <script src="script.js" defer></script>
            -->
        </head>
        <body>
            <h1>Servidor HTTP com Sessão</h1>
            <p>Seu ID de sessão: <b>{oSess}</b></p>
            <p>Você acessou esta página <b>{data['acessos']}</b> vezes.</p>
            <ul>
                <li><b>server</b>: {self.server}</li>
                <li><b>client_address</b>: {self.client_address}</li>
                <li><b>command</b>: {self.command}</li>
                <li><b>path</b>: {self.path}</li>
                <li><b>headers</b>: <pre>{self.headers}</pre></li>
                <li><b>rfile</b>: {self.rfile}</li>
                <li><b>wfile</b>: {self.wfile}</li>
                <li><b>protocol_version</b>: {self.protocol_version}</li>
                <li><b>request_version</b>: {self.request_version}</li>
                <li><b>close_connection</b>: {self.close_connection}</li>
                <li><b>timeout</b>: {self.timeout}</li>
                <li><b>requestline</b>: {self.requestline}</li>
                <li><b>content_length</b>: {content_length}</li>
                <li><b>payload</b>: <pre>{payload}</pre></li>
            </ul>
            <a href='/aaaa'>Clique aqui</a>
        </body>
        </html>
        """
        self.wfile.write(
            resposta.encode(self.encoding)
        )

    def do_POST(self):
        self.do_GET()

    def do_PUT(self):
        self.do_GET()

    def do_DELETE(self):
        self.do_GET()

    def do_HEAD(self):
        self.do_GET()

    def do_OPTIONS(self):
        self.do_GET()


class HttpHandler_Redirect(http.server.SimpleHTTPRequestHandler):
    REDIRECT_PORT = 443

    def do_GET(self):
        """Responde às requisições GET e gerencia a sessão."""
        if self.server.server_port != self.REDIRECT_PORT:  # Se acessado via HTTP
            host = self.headers['Host'].split(':')[0]
            https_url = f"https://{host}:{self.REDIRECT_PORT}{self.path}"
            self.send_response(301)
            self.send_header("Location", https_url)
            self.end_headers()
            return True
        return False

    def do_POST(self):
        self.do_GET()


# Iniciar servidores com parâmetros
threading.Thread(
    target=WebServer,
    kwargs={"https":True, "hander":HttpHandler}, # HTTPS
    daemon=True
).start()
o = WebServer(hander=HttpHandler_Redirect) # HTTP


# HTTPS
# linux: openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
