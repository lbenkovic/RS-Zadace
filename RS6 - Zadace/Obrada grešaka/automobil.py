from fastapi import FastAPI, HTTPException, Query, Path
from autoModels import ResponseAuto, RequestAuto, BaseAuto

app = FastAPI()

auta = [
    {
        "id": 1,
        "marka": "Toyota",
        "model": "Corolla",
        "godina_proizvodnje": 2015,
        "cijena": 12000,
        "boja": "siva"
    },
    {
        "id": 2,
        "marka": "Honda",
        "model": "Civic",
        "godina_proizvodnje": 2018,
        "cijena": 15000,
        "boja": "crna"
    },
    {
        "id": 3,
        "marka": "Ford",
        "model": "Focus",
        "godina_proizvodnje": 2016,
        "cijena": 10000,
        "boja": "bijela"
    },
    {
        "id": 4,
        "marka": "BMW",
        "model": "320i",
        "godina_proizvodnje": 2019,
        "cijena": 25000,
        "boja": "plava"
    },
    {
        "id": 5,
        "marka": "Mercedes",
        "model": "C-Class",
        "godina_proizvodnje": 2020,
        "cijena": 30000,
        "boja": "siva"
    }
]

@app.get("/auto/{id}", response_model=ResponseAuto)
def get_auto_by_id(id: int = Path(..., gt=0)):
    for car in auta:
        if car["id"] == id:
            return car
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")


@app.get("/auto", response_model=list[ResponseAuto])
def get_auto_by_id(max_godina: int, max_cijena: float, min_cijena: float = Query(ge=1), min_godina: int = Query(ge=1960)):
    if min_godina > max_godina: 
        raise HTTPException(status_code=400, detail="Minimalna godina mora biti veća od maksimalne.")
    if min_cijena > max_cijena:
        raise HTTPException(status_code=400, detail="Minimalna cijena mora biti veća od maksimalne.")
    filtrirana_auta = []
    for auto in auta:
        if auto["godina_proizvodnje"] >= min_godina and auto["godina_proizvodnje"] <= max_godina and auto["cijena"] >= min_cijena and auto["cijena"] <= max_cijena:
            filtrirana_auta.append(auto)
    return filtrirana_auta

@app.post("/auto", response_model=BaseAuto)
def add_auto(auto: RequestAuto):
    for car in auta:
        if auto.marka == car["marka"] and auto.model == car["model"] and auto.godina_proizvodnje == car["godina_proizvodnje"] and auto.cijena == car["cijena"] and auto.boja == car["boja"]:
            raise HTTPException(status_code=400, detail="Auto već postoji")
    new_id = len(auta) + 1
    pdv_multi = 1.25
    cijena_s_pdv = auto.cijena * pdv_multi
    novi_auto : BaseAuto = {"id": new_id, "cijena_pdv": cijena_s_pdv, **auto.model_dump()}
    auta.append(novi_auto)
    return novi_auto