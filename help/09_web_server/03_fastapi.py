from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"mensagem": "Bem-vindo ao FastAPI!"}

@app.get("/soma/{a}/{b}")
async def soma(a: int, b: int):
    return {"resultado": a + b}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)