from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

precos = {1: {"titulo": "Cintaralho", "preco": 200, "vendido": True}}


class Item(BaseModel):
    titulo: str
    preco: int
    vendido: bool


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/items/{item_id}", response_model=Item)
def pega_posicao(item_id: int):
    return precos[item_id]
