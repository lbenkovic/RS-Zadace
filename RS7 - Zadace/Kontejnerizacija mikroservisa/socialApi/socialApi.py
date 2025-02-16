from fastapi import FastAPI, HTTPException
from socialModels import Objava, ObjavaCreate
from datetime import datetime
app = FastAPI()

objave = []
id_counter = 1


@app.post("/objava", response_model=Objava, status_code=201)
def create_objava(nova_objava: ObjavaCreate):
    global id_counter
    objava = Objava(
        id=id_counter,
        korisnik=nova_objava.korisnik,
        tekst=nova_objava.tekst,
        vrijeme=datetime.now()
    )
    id_counter += 1
    objave.append(objava.dict())
    return objava

@app.get("/objava/{id}", response_model=Objava)
def get_objava(id: int):
    for o in objave:
        if o["id"] == id:
            return o
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.get("/korisnici/{korisnik}/objave", response_model=list[Objava])
def get_objave_by_korisnik(korisnik: str):
    user_objave = [o for o in objave if o["korisnik"] == korisnik]
    if not user_objave:
        raise HTTPException(status_code=404, detail="Nema objava za zadanog korisnika")
    return user_objave
