from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Izdavac(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: Optional[int] = datetime.now().year
    broj_stranica: int
    izdavac: Izdavac
