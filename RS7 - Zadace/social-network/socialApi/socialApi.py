from fastapi import FastAPI, HTTPException, Body
from socialModels import Objava, ObjavaCreate, UserAuth
from datetime import datetime
import httpx

app = FastAPI()

objave = []
id_counter = 1

@app.post("/objava", response_model=Objava, status_code=201)
def create_objava(nova_objava: ObjavaCreate):
    global id_counter
    # Koristimo trenutno vrijeme za objavu
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

@app.post("/korisnici/{korisnik}/objave", response_model=list[Objava])
async def get_objave_by_korisnik(korisnik: str, auth: UserAuth = Body(...)):
    if auth.korisnicko_ime != korisnik:
        raise HTTPException(status_code=400, detail="Korisnicko ime u putanji i tijelu se ne podudaraju")
    
    async with httpx.AsyncClient() as client:
        response = await client.post("http://authapi:9000/login", json=auth.dict())
    
    if response.status_code != 200 or not response.json().get("authorized", False):
        raise HTTPException(status_code=401, detail="Neispravni korisnički podaci")
    
    user_objave = [o for o in objave if o["korisnik"] == korisnik]
    if not user_objave:
        raise HTTPException(status_code=404, detail="Nema objava za zadanog korisnika")
    return user_objave
