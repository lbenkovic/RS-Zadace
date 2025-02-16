from fastapi import FastAPI
from filmModels import OutFilm,CreateFilm
app = FastAPI()

filmovi = [
{"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
{"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
{"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
{"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi")
def filter_film(genre: str = None, min_godina: int = 2000):
    pronadeni_filmovi = [film for film in filmovi if (genre is None or film["genre"] == genre) and (min_godina is None or film["godina"] >= min_godina)]
    return pronadeni_filmovi

@app.get("/filmovi/{id}", response_model=OutFilm)
def get_filmovi_by_id(id: int):
    film = next((film for film in filmovi if film["id"] == id), None)
    return film

@app.post("/filmovi", response_model=OutFilm)
def post_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    new_film : OutFilm = {"id": new_id, **film.model_dump()}
    filmovi.append(new_film)
    return new_film