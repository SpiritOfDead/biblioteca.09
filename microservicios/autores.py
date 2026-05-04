from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Autor(BaseModel):
    id: int
    nombre: str
    pais_id: int

db_autores = []

@app.get("/autores")
def get_autores():
    return db_autores

@app.get("/autores/{item_id}")
def get_autor(item_id: int):
    for item in db_autores:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Autor no encontrado")

@app.post("/autores")
def post_autor(item: Autor):
    db_autores.append(item)
    return item

@app.put("/autores/{item_id}")
def put_autor(item_id: int, item_actualizado: Autor):
    for index, item in enumerate(db_autores):
        if item.id == item_id:
            db_autores[index] = item_actualizado
            return item_actualizado
    raise HTTPException(status_code=404, detail="Autor no encontrado")

@app.delete("/autores/{item_id}")
def delete_autor(item_id: int):
    for index, item in enumerate(db_autores):
        if item.id == item_id:
            del db_autores[index]
            return {"mensaje": "Autor eliminado"}
    raise HTTPException(status_code=404, detail="Autor no encontrado")
