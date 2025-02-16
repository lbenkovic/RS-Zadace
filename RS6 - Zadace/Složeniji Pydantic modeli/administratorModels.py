from pydantic import BaseModel
from typing import Literal, Optional

class Administrator(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: Optional[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []