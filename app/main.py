from fastapi import FastAPI

app = FastAPI()

@app.get("/sum")
def somar_numeros(a: int, b: int):
    return {"resultado": a + b}
