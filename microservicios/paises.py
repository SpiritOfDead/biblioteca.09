from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Pais(BaseModel):
    id: int
    nombre: str

db_paises = []

@app.get("/paises")
def get_paises():
    return db_paises

@app.get("/paises/{item_id}")
def get_pais(item_id: int):
    for item in db_paises:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="País no encontrado")

@app.post("/paises")
def post_pais(item: Pais):
    db_paises.append(item)
    return item

@app.put("/paises/{item_id}")
def put_pais(item_id: int, item_actualizado: Pais):
    for index, item in enumerate(db_paises):
        if item.id == item_id:
            db_paises[index] = item_actualizado
            return item_actualizado
    raise HTTPException(status_code=404, detail="País no encontrado")

@app.delete("/paises/{item_id}")
def delete_pais(item_id: int):
    for index, item in enumerate(db_paises):
        if item.id == item_id:
            del db_paises[index]
            return {"mensaje": "País eliminado"}
    raise HTTPException(status_code=404, detail="País no encontrado")
  
