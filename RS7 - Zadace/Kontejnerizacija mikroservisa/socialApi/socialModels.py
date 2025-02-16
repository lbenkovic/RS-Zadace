from pydantic import BaseModel, constr, Field
from typing import Optional, List
from datetime import datetime

class ObjavaCreate(BaseModel):
    korisnik: str = Field(..., max_length = 20)
    tekst: str = Field(..., max_length = 280)

class Objava(BaseModel):
    id: int
    korisnik: str = Field(..., max_length = 20)
    tekst: str = Field(..., max_length = 280)
    vrijeme: datetime
