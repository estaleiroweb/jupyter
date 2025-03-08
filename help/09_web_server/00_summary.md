# Web Server

Criar um **web server completo** no Python pode variar de algo **simples** com `http.server` até algo **complexo e robusto** com frameworks como **Flask, FastAPI ou Django**.

Aqui vou te mostrar algumas abordagens, desde a mais básica até uma solução robusta.  

1. Servidor HTTP Simples com `http.server` (Sem Framework): `01-01_http.py`
   - Se precisar de um **servidor rápido**, o Python tem um servidor embutido:
   - O `http.server` cria um servidor HTTP básico.  
   - O método `do_GET()` responde às requisições `GET`.  
   - Responde sempre com `<h1>Servidor HTTP Python</h1>`.  
   - **Rápido para testes** ❌ **Não escalável para produção**  

2. Webserver com Flask (Rápido e Simples): `01-02_flask.py`
   - Se precisar de **rotas dinâmicas e APIs REST**, use **Flask**:
   - `@app.route("/")` → Define uma rota para a página principal.  
   - `@app.route("/hello/<nome>")` → Rota dinâmica que recebe um parâmetro.  
   - `app.run(debug=True, host="0.0.0.0", port=8080)` → Inicia o servidor.  
   - ✔ **Simples e rápido** ❌ **Menos eficiente que FastAPI para APIs**  

3. Webserver com FastAPI (Melhor para APIs): `01-03_fastapi.py`
   - Se precisar de **performance**, **documentação automática** e **assincronismo**, use **FastAPI**:
   - `@app.get("/")` → Define uma rota GET que retorna JSON.  
   - `@app.get("/soma/{a}/{b}")` → Recebe dois números e retorna a soma.  
   - **Executado com** `uvicorn.run(app, host="0.0.0.0", port=8080)`.  
   - ✔ **Muito rápido e assíncrono** ❌ **Pode ser mais complexo para iniciantes**  

4. Webserver Completo com Django (Mais Estruturado):
   - Se precisar de um **sistema web completo**, **Django** é uma boa opção.
   - ✔ **Ótimo para sistemas grandes** ❌ **Mais pesado para APIs simples**  
   - Isso já cria um servidor completo com autenticação e ORM integrado!  

     ```sh
     pip install django
     django-admin startproject meu_projeto
     cd meu_projeto
     python manage.py runserver
     ```

## Qual Escolher?

| Solução       | Melhor Para                 | Fácil de Usar? | Performance |
| ------------- | --------------------------- | -------------- | ----------- |
| `http.server` | Servidor rápido para testes | Simples        | Baixa       |
| Flask         | Pequenos sites/APIs         | Fácil          | Média       |
| FastAPI       | APIs rápidas e escaláveis   | Intermediário  | Alta        |
| Django        | Aplicações web grandes      | Complexo       | Alta        |
