from pydantic import BaseModel
from typing import List, Optional, Literal

class Actor(BaseModel):
    name: str
    surname: str

class Writer(BaseModel):
    name: str
    surname: str

class Film(BaseModel):
    Title: str
    Year: int
    Rated: str
    Runtime: int
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]
    Plot: str
    Writer: List[Writer]
    Released: Optional[str] = ""
    Director: Optional[str] = ""
    Awards: Optional[str] = ""
    Poster: Optional[str] = ""
    Metascore: Optional[int] = 0
    imdbRating: Optional[float] = 0.0
    imdbVotes: Optional[int] = 0
    imdbID: Optional[str] = ""
    Type: Literal["movie", "series"]
    Response: Optional[str] = ""
    Images: List[str] = []
    totalSeasons: Optional[str] = ""
    ComingSoon: Optional[bool] = False
