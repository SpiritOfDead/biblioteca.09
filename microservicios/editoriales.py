from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Editorial(BaseModel):
    id: int
    nombre: str
    pais_id: int

db_editoriales = []

@app.get("/editoriales")
def get_editoriales():
    return db_editoriales

@app.get("/editoriales/{item_id}")
def get_editorial(item_id: int):
    for item in db_editoriales:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Editorial no encontrada")

@app.post("/editoriales")
def post_editorial(item: Editorial):
    db_editoriales.append(item)
    return item

@app.put("/editoriales/{item_id}")
def put_editorial(item_id: int, item_actualizado: Editorial):
    for index, item in enumerate(db_editoriales):
        if item.id == item_id:
            db_editoriales[index] = item_actualizado
            return item_actualizado
    raise HTTPException(status_code=404, detail="Editorial no encontrada")

@app.delete("/editoriales/{item_id}")
def delete_editorial(item_id: int):
    for index, item in enumerate(db_editoriales):
        if item.id == item_id:
            del db_editoriales[index]
            return {"mensaje": "Editorial eliminada"}
    raise HTTPException(status_code=404, detail="Editorial no encontrada")
    
