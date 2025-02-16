from pydantic import BaseModel
from typing import TypedDict

class StolInfo(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    lista_jela: list[Jelo]
    ukupna_cijena: float