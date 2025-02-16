from pydantic import BaseModel

class RequestAuto(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str

class ResponseAuto(RequestAuto):
    id: int

class BaseAuto(ResponseAuto):
    cijena_pdv: float