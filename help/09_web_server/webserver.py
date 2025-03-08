import os
import ssl
import http.server
import socketserver
# from singleton import singleton
import signal

def signal_handler(sig, frame):
    print("\nInterrupt Ctrl+C pressed!")
    quit()
    import sys
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class WebServer:
    KEYFILE: str = "/cer/key.pem"
    CERTFILE: str = "/cer/cert.pem"
    HTTP_PORT: int = 80
    HTTPS_PORT: int = 443

    def __init__(self,
                 port: int = None,
                 host: str = '',
                 https: bool = False,
                 socket: bool = False,
                 keyfile: str = None,
                 certfile: str = None,
                 hander: http.server.SimpleHTTPRequestHandler = http.server.SimpleHTTPRequestHandler
                 ):
        self.host: str = host
        self.keyfile: str = keyfile or self.KEYFILE
        self.certfile: str = certfile or self.CERTFILE
        self.socket: bool = socket
        self.https: bool = https\
            and self.keyfile \
            and self.certfile \
            and os.path.exists(self.keyfile) \
            and os.path.exists(self.certfile)
        self.port: int = port or (
            self.HTTPS_PORT if self.https else self.HTTP_PORT
        )
        self.hander = hander
        self.httpd: 'socketserver.TCPServer|http.server.HTTPServer' = None

        self.start()

    def start(self, https=False):
        """Inicia o servidor HTTP"""
        if https and not self.https:
            return

        if self.socket:
            with socketserver.TCPServer(
                (self.host, self.port),
                self.hander
            ) as self.httpd:
                self.send()
        else:
            self.httpd = http.server.HTTPServer(
                (self.host, self.port),
                self.hander
            )
            self.send()

    def send(self):
        if self.https:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            context.load_cert_chain(
                certfile=self.certfile,
                keyfile=self.keyfile
            )
            self.httpd.socket = context.wrap_socket(
                self.httpd.socket,
                server_side=True
            )

        print(
            "Web Server running " +
            ('HTTPS' if self.https else 'HTTP') +
            f"://{self.host}:{self.port}"
        )

        self.httpd.serve_forever()
