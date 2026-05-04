from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(docs_url=None, redoc_url=None)

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
    raise HTTPException(status_code=404, detail="No encontrado")

@app.post("/autores")
def post_autor(item: Autor):
    db_autores.append(item)
    return item

@app.put("/autores/{item_id}")
def put_autor(item_id: int, item_act: Autor):
    for i, item in enumerate(db_autores):
        if item.id == item_id:
            db_autores[i] = item_act
            return item_act
    raise HTTPException(status_code=404, detail="No encontrado")

@app.delete("/autores/{item_id}")
def delete_autor(item_id: int):
    for i, item in enumerate(db_autores):
        if item.id == item_id:
            del db_autores[i]
            return {"msj": "Eliminado"}
    raise HTTPException(status_code=404, detail="No encontrado")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
