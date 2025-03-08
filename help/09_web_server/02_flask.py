from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo ao meu servidor Flask!</h1>"

@app.route("/hello/<nome>")
def hello(nome):
    return f"<h1>Olá, {nome}!</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)