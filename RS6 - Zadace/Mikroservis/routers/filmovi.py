from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Literal
from models import filmModel

router = APIRouter(prefix="/filmovi")

filmovi =[
  {
    "Title": "Avatar",
    "Year": 2009,
    "Rated": "PG-13",
    "Runtime": 162,
    "Genre": "Action, Adventure, Fantasy",
    "Language": "English, Spanish",
    "Country": "USA, UK",
    "Actors": [
      {"name": "Sam", "surname": "Worthington"},
      {"name": "Zoe", "surname": "Saldana"},
      {"name": "Sigourney", "surname": "Weaver"},
      {"name": "Stephen", "surname": "Lang"}
    ],
    "Plot": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "Writer": [
      {"name": "James", "surname": "Cameron"}
    ],
    "Released": "18 Dec 2009",
    "Director": "James Cameron",
    "Awards": "Won 3 Oscars. Another 80 wins & 121 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
    "Metascore": 83,
    "imdbRating": 7.9,
    "imdbVotes": 890617,
    "imdbID": "tt0499549",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTYyMzUxNl5BMl5BanBnXkFtZTcwNTg0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM2MDk3MTcyMV5BMl5BanBnXkFtZTcwNjg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "I Am Legend",
    "Year": 2007,
    "Rated": "PG-13",
    "Runtime": 101,
    "Genre": "Drama, Horror, Sci-Fi",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Will", "surname": "Smith"},
      {"name": "Alice", "surname": "Braga"},
      {"name": "Charlie", "surname": "Tahan"},
      {"name": "Salli", "surname": "Richardson-Whitfield"}
    ],
    "Plot": "Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.",
    "Writer": [
      {"name": "Mark", "surname": "Protosevich"},
      {"name": "Akiva", "surname": "Goldsman"},
      {"name": "Richard", "surname": "Matheson"},
      {"name": "John", "surname": "William Corrington"},
      {"name": "Joyce", "surname": "Hooper Corrington"}
    ],
    "Released": "14 Dec 2007",
    "Director": "Francis Lawrence",
    "Awards": "9 wins & 21 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU4NzMyNDk1OV5BMl5BanBnXkFtZTcwOTEwMzU1MQ@@._V1_SX300.jpg",
    "Metascore": 65,
    "imdbRating": 7.2,
    "imdbVotes": 533874,
    "imdbID": "tt0480249",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI0NTI4NjE3NV5BMl5BanBnXkFtZTYwMDA0Nzc4._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIwMDg2MDU4M15BMl5BanBnXkFtZTYwMTA0Nzc4._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MDM1OTU5OV5BMl5BanBnXkFtZTYwMjA0Nzc4._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0MTI2NjMzMzFeQTJeQWpwZ15BbWU2MDMwNDc3OA@@._V1_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "300",
    "Year": 2006,
    "Rated": "R",
    "Runtime": 117,
    "Genre": "Action, Drama, Fantasy",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Gerard", "surname": "Butler"},
      {"name": "Lena", "surname": "Headey"},
      {"name": "Dominic", "surname": "West"},
      {"name": "David", "surname": "Wenham"}
    ],
    "Plot": "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
    "Writer": [
      {"name": "Zack", "surname": "Snyder"},
      {"name": "Kurt", "surname": "Johnstad"},
      {"name": "Michael", "surname": "Gordon"},
      {"name": "Frank", "surname": "Miller"},
      {"name": "Lynn", "surname": "Varley"}
    ],
    "Released": "09 Mar 2007",
    "Director": "Zack Snyder",
    "Awards": "16 wins & 42 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_SX300.jpg",
    "Metascore": 52,
    "imdbRating": 7.7,
    "imdbVotes": 611046,
    "imdbID": "tt0416449",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMwNTg5MzMwMV5BMl5BanBnXkFtZTcwMzA2NTIyMw@@._V1_SX1777_CR0,0,1777,937_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQwNTgyNTMzNF5BMl5BanBnXkFtZTcwNDA2NTIyMw@@._V1_SX1777_CR0,0,1777,935_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0MjQzOTEwMV5BMl5BanBnXkFtZTcwMzE2NTIyMw@@._V1_SX1777_CR0,0,1777,947_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "The Avengers",
    "Year": 2012,
    "Rated": "PG-13",
    "Runtime": 143,
    "Genre": "Action, Sci-Fi, Thriller",
    "Language": "English, Russian",
    "Country": "USA",
    "Actors": [
      {"name": "Robert", "surname": "Downey Jr."},
      {"name": "Chris", "surname": "Evans"},
      {"name": "Mark", "surname": "Ruffalo"},
      {"name": "Chris", "surname": "Hemsworth"}
    ],
    "Plot": "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
    "Writer": [
      {"name": "Joss", "surname": "Whedon"},
      {"name": "Zak", "surname": "Penn"}
    ],
    "Released": "04 May 2012",
    "Director": "Joss Whedon",
    "Awards": "Nominated for 1 Oscar. Another 34 wins & 75 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SX300.jpg",
    "Metascore": 69,
    "imdbRating": 8.1,
    "imdbVotes": 1003301,
    "imdbID": "tt0848228",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA0NjY0NzE4OTReQTJeQWpwZ15BbWU3MDczODg2Nzc@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE1MzEzMjcyM15BMl5BanBnXkFtZTcwNDM4ODY3Nw@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMwMzM2MTg1M15BMl5BanBnXkFtZTcwNjM4ODY3Nw@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4NzM2Mjc5MV5BMl5BanBnXkFtZTcwMTkwOTY3Nw@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3MzQ3NjA5N15BMl5BanBnXkFtZTcwMzY5OTY3Nw@@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "The Wolf of Wall Street",
    "Year": 2013,
    "Rated": "R",
    "Runtime": 180,
    "Genre": "Biography, Comedy, Crime",
    "Language": "English, French",
    "Country": "USA",
    "Actors": [
      {"name": "Leonardo", "surname": "DiCaprio"},
      {"name": "Jonah", "surname": "Hill"},
      {"name": "Margot", "surname": "Robbie"},
      {"name": "Matthew", "surname": "McConaughey"}
    ],
    "Plot": "Based on the True story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
    "Writer": [
      {"name": "Terence", "surname": "Winter"},
      {"name": "Jordan", "surname": "Belfort"}
    ],
    "Released": "25 Dec 2013",
    "Director": "Martin Scorsese",
    "Awards": "Nominated for 5 Oscars. Another 35 wins & 154 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX300.jpg",
    "Metascore": 75,
    "imdbRating": 8.2,
    "imdbVotes": 786985,
    "imdbID": "tt0993846",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDIwMDIxNzk3Ml5BMl5BanBnXkFtZTgwMTg0MzQ4MDE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NzAxODAyMl5BMl5BanBnXkFtZTgwMDg0MzQ4MDE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTExMDk1MDE4NzVeQTJeQWpwZ15BbWU4MDM4NDM0ODAx._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg3MTY4NDk4Nl5BMl5BanBnXkFtZTgwNjc0MzQ4MDE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgzMTg4MDI0Ml5BMl5BanBnXkFtZTgwOTY0MzQ4MDE@._V1_SY1000_CR0,0,1553,1000_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "Interstellar",
    "Year": 2014,
    "Rated": "PG-13",
    "Runtime": 169,
    "Genre": "Adventure, Drama, Sci-Fi",
    "Language": "English",
    "Country": "USA, UK",
    "Actors": [
      {"name": "Ellen", "surname": "Burstyn"},
      {"name": "Matthew", "surname": "McConaughey"},
      {"name": "Mackenzie", "surname": "Foy"},
      {"name": "John", "surname": "Lithgow"}
    ],
    "Plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    "Writer": [
      {"name": "Jonathan", "surname": "Nolan"},
      {"name": "Christopher", "surname": "Nolan"}
    ],
    "Released": "07 Nov 2014",
    "Director": "Christopher Nolan",
    "Awards": "Won 1 Oscar. Another 39 wins & 134 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX300.jpg",
    "Metascore": 74,
    "imdbRating": 8.6,
    "imdbVotes": 937412,
    "imdbID": "tt0816692",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA3NTEwOTMxMV5BMl5BanBnXkFtZTgwMjMyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzQ5ODE2MzEwM15BMl5BanBnXkFtZTgwMTMyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4Njk4MzY0Nl5BMl5BanBnXkFtZTgwMzIyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMzE3MTM0MTc3Ml5BMl5BanBnXkFtZTgwMDIyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjYzNjE2NDk3N15BMl5BanBnXkFtZTgwNzEyODgxMzE@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "Game of Thrones",
    "Year": 2011,
    "Rated": "TV-MA",
    "Runtime": 56,
    "Genre": "Adventure, Drama, Fantasy",
    "Language": "English",
    "Country": "USA, UK",
    "Actors": [
      {"name": "Peter", "surname": "Dinklage"},
      {"name": "Lena", "surname": "Headey"},
      {"name": "Emilia", "surname": "Clarke"},
      {"name": "Kit", "surname": "Harington"}
    ],
    "Plot": "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, plans to return after thousands of years in the North.",
    "Writer": [
      {"name": "David", "surname": "Benioff"},
      {"name": "D.B.", "surname": "Weiss"}
    ],
    "Released": "17 Apr 2011",
    "Director": "N/A",
    "Awards": "Won 1 Golden Globe. Another 185 wins & 334 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjM5OTQ1MTY5Nl5BMl5BanBnXkFtZTgwMjM3NzMxODE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 9.5,
    "imdbVotes": 1046830,
    "imdbID": "tt0944947",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDc1MGUyNzItNWRkOC00MjM1LWJjNjMtZTZlYWIxMGRmYzVlXkEyXkFqcGdeQXVyMzU3MDEyNjk@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BZjZkN2M5ODgtMjQ2OC00ZjAxLWE1MjMtZDE0OTNmNGM0NWEwXkEyXkFqcGdeQXVyNjUxNzgwNTE@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMDk4Y2Y1MDAtNGVmMC00ZTlhLTlmMmQtYjcyN2VkNzUzZjg2XkEyXkFqcGdeQXVyNjUxNzgwNTE@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjZjNWIzMzQtZWZjYy00ZTkwLWJiMTYtOWRkZDBhNWJhY2JmXkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNTMyMTRjZWEtM2UxMS00ZjU5LWIxMTYtZDA5YmJhZmRjYTc4XkEyXkFqcGdeQXVyMjk3NTUyOTc@._V1_SX1777_CR0,0,1777,999_AL_.jpg"
    ],
    "totalSeasons": "7",
    "ComingSoon": False
  },
  {
    "Title": "Vikings",
    "Year": 2013,
    "Rated": "TV-14",
    "Runtime": 44,
    "Genre": "Action, Drama, History",
    "Language": "English",
    "Country": "Ireland, Canada",
    "Actors": [
      {"name": "Travis", "surname": "Fimmel"},
      {"name": "Clive", "surname": "Standen"},
      {"name": "Gustaf", "surname": "Skarsgård"},
      {"name": "Katheryn", "surname": "Winnick"}
    ],
    "Plot": "The world of the Vikings is brought to life through the journey of Ragnar Lothbrok, the first Viking to emerge from Norse legend and onto the pages of history - a man on the edge of myth.",
    "Writer": [
      {"name": "Michael", "surname": "Hirst"}
    ],
    "Released": "03 Mar 2013",
    "Director": "N/A",
    "Awards": "Nominated for 7 Primetime Emmys. Another 17 wins & 49 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMjM5MTM1ODUxNV5BMl5BanBnXkFtZTgwNTAzOTI2ODE@._V1_.jpg",
    "Metascore": 0,
    "imdbRating": 8.6,
    "imdbVotes": 198041,
    "imdbID": "tt2306299",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM5MTM1ODUxNV5BMl5BanBnXkFtZTgwNTAzOTI2ODE@._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNzU2NDcxODMyOF5BMl5BanBnXkFtZTgwNDAzOTI2ODE@._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMzMzIzOTU2M15BMl5BanBnXkFtZTgwODMzMTkyODE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2NTQ2MDA3NF5BMl5BanBnXkFtZTgwODkxMDUxODE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxOTQ3NTA5N15BMl5BanBnXkFtZTgwMzExMDUxODE@._V1_SY1000_SX1500_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "Gotham",
    "Year": 2014,
    "Rated": "TV-14",
    "Runtime": 42,
    "Genre": "Action, Crime, Drama",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Ben", "surname": "McKenzie"},
      {"name": "Donal", "surname": "Logue"},
      {"name": "David", "surname": "Mazouz"},
      {"name": "Sean", "surname": "Pertwee"}
    ],
    "Plot": "The story behind Detective James Gordon's rise to prominence in Gotham City in the years before Batman's arrival.",
    "Writer": [
      {"name": "Bruno", "surname": "Heller"}
    ],
    "Released": "01 Aug 2014",
    "Director": "N/A",
    "Awards": "Nominated for 4 Primetime Emmys. Another 3 wins & 22 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTY2MjMwNDE4OV5BMl5BanBnXkFtZTgwNjI1NjU0OTE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 8.0,
    "imdbVotes": 133375,
    "imdbID": "tt3749900",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDI3ODYyODY4OV5BMl5BanBnXkFtZTgwNjE5NDMwMDI@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5OTExMTIwNF5BMl5BanBnXkFtZTgwMjI5NDMwMDI@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3MDY2NjA3MzBeQTJeQWpwZ15BbWU4MDU0MDkzODgx._V1_SX1499_CR0,0,1499,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3MzYzNDgzOV5BMl5BanBnXkFtZTgwMjQwOTM4ODE@._V1_SY1000_CR0,0,1498,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQwODAyNjk0NF5BMl5BanBnXkFtZTgwODU4MzMyODE@._V1_SY1000_CR0,0,1500,1000_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "Power",
    "Year": 2014,
    "Rated": "TV-MA",
    "Runtime": 50,
    "Genre": "Crime, Drama",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Omari", "surname": "Hardwick"},
      {"name": "Joseph", "surname": "Sikora"},
      {"name": "Andy", "surname": "Bean"},
      {"name": "Lela", "surname": "Loren"}
    ],
    "Plot": "James \"Ghost\" St. Patrick, a wealthy New York night club owner who has it all, catering for the city's elite and dreaming big, lives a double life as a drug kingpin.",
    "Writer": [
      {"name": "Courtney", "surname": "Kemp Agboh"}
    ],
    "Released": "N/A",
    "Director": "N/A",
    "Awards": "1 win & 6 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BOTA4NTkzMjUzOF5BMl5BanBnXkFtZTgwNzg5ODkxOTE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 8.0,
    "imdbVotes": 14770,
    "imdbID": "tt3281796",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2ODg0MzMzM15BMl5BanBnXkFtZTgwODYxODA5NTE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyMjA0MzczNV5BMl5BanBnXkFtZTgwNTIyODA5NTE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk0MTI0NzQ2NV5BMl5BanBnXkFtZTgwMDkxODA5NTE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4Mzk1ODcxM15BMl5BanBnXkFtZTgwNDQyODA5NTE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwNTE0NDI1M15BMl5BanBnXkFtZTgwMDQyODA5NTE@._V1_SY1000_SX1500_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": False
  },
  {
    "Title": "Narcos",
    "Year": 2015,
    "Rated": "TV-MA",
    "Runtime": 49,
    "Genre": "Biography, Crime, Drama",
    "Language": "English, Spanish",
    "Country": "USA",
    "Actors": [
      {"name": "Wagner", "surname": "Moura"},
      {"name": "Boyd", "surname": "Holbrook"},
      {"name": "Pedro", "surname": "Pascal"},
      {"name": "Joanna", "surname": "Christie"}
    ],
    "Plot": "A chronicled look at the criminal exploits of Colombian drug lord Pablo Escobar.",
    "Writer": [
      {"name": "Carlo", "surname": "Bernard"},
      {"name": "Chris", "surname": "Brancato"},
      {"name": "Doug", "surname": "Miro"},
      {"name": "Paul", "surname": "Eckstein"}
    ],
    "Released": "28 Aug 2015",
    "Director": "N/A",
    "Awards": "Nominated for 2 Golden Globes. Another 4 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU0ODQ4NDg2OF5BMl5BanBnXkFtZTgwNzczNTE4OTE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 8.9,
    "imdbVotes": 118680,
    "imdbID": "tt2707408",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2MDMzMTc0MF5BMl5BanBnXkFtZTgwMTAyMzA1OTE@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMDkyOTEyNV5BMl5BanBnXkFtZTgwNjY3Mjc3OTE@._V1_SY1000_SX1500_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA2NDUwMTU2NV5BMl5BanBnXkFtZTgwNTI1Mzc3OTE@._V1_SY1000_CR0,0,1499,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BODA1NjAyMTQ3Ml5BMl5BanBnXkFtZTgwNjI1Mzc3OTE@._V1_SY1000_CR0,0,1499,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU0NzQ0OTAwNl5BMl5BanBnXkFtZTgwMDAyMzA1OTE@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    ],
    "totalSeasons": "2",
    "ComingSoon": False
  },
  {
    "Title": "Breaking Bad",
    "Year": 2008,
    "Rated": "TV-14",
    "Runtime": 49,
    "Genre": "Crime, Drama, Thriller",
    "Language": "English, Spanish",
    "Country": "USA",
    "Actors": [
      {"name": "Bryan", "surname": "Cranston"},
      {"name": "Anna", "surname": "Gunn"},
      {"name": "Aaron", "surname": "Paul"},
      {"name": "Dean", "surname": "Norris"}
    ],
    "Plot": "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's financial future.",
    "Writer": [
      {"name": "Vince", "surname": "Gilligan"}
    ],
    "Released": "20 Jan 2008",
    "Director": "N/A",
    "Awards": "Won 2 Golden Globes. Another 132 wins & 218 nominations.",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 9.5,
    "imdbVotes": 889883,
    "imdbID": "tt0903747",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyMzI5NDc5Nl5BMl5BanBnXkFtZTgwMjM0MTI2MDE@._V1_SY1000_CR0,0,1498,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2NDkwNDk5NV5BMl5BanBnXkFtZTgwNDM0MTI2MDE@._V1_SY1000_CR0,0,1495,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4NDcyNDMzMF5BMl5BanBnXkFtZTgwOTI0MTI2MDE@._V1_SY1000_CR0,0,1495,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzMTczMjM3NjFeQTJeQWpwZ15BbWU4MDc1MTI1MzAx._V1_SY1000_CR0,0,1495,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5MTE3MTgwMF5BMl5BanBnXkFtZTgwOTQxMjUzMDE@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
    ],
    "totalSeasons": "5",
    "ComingSoon": False
  },
  {
    "Title": "Doctor Strange",
    "Year": 2016,
    "Rated": "N/A",
    "Runtime": 0,
    "Genre": "Action, Adventure, Fantasy",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Rachel", "surname": "McAdams"},
      {"name": "Benedict", "surname": "Cumberbatch"},
      {"name": "Mads", "surname": "Mikkelsen"},
      {"name": "Tilda", "surname": "Swinton"}
    ],
    "Plot": "After his career is destroyed, a brilliant but arrogant and conceited surgeon gets a new lease on life when a sorcerer takes him under her wing and trains him to defend the world against evil.",
    "Writer": [
      {"name": "Scott", "surname": "Derrickson"},
      {"name": "C. Robert", "surname": "Cargill"},
      {"name": "Jon", "surname": "Spaihts"}
    ],
    "Released": "04 Nov 2016",
    "Director": "Scott Derrickson",
    "Awards": "N/A",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BNjgwNzAzNjk1Nl5BMl5BanBnXkFtZTgwMzQ2NjI1OTE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 0.0,
    "imdbVotes": 0,
    "imdbID": "tt1211837",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM3ODc1ODI5Ml5BMl5BanBnXkFtZTgwODMzMDY3OTE@._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxNTAyNTU0NV5BMl5BanBnXkFtZTgwNzMzMDY3OTE@._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE5NDc5NzUwNV5BMl5BanBnXkFtZTgwMDM3MDM2NzE@._V1_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": True
  },
  {
    "Title": "Rogue One: A Star Wars Story",
    "Year": 2016,
    "Rated": "N/A",
    "Runtime": 0,
    "Genre": "Action, Adventure, Sci-Fi",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Felicity", "surname": "Jones"},
      {"name": "Riz", "surname": "Ahmed"},
      {"name": "Mads", "surname": "Mikkelsen"},
      {"name": "Ben", "surname": "Mendelsohn"}
    ],
    "Plot": "The Rebellion makes a risky move to steal the plans to the Death Star, setting up the epic saga to follow.",
    "Writer": [
      {"name": "Chris", "surname": "Weitz"},
      {"name": "Tony", "surname": "Gilroy"},
      {"name": "John", "surname": "Knoll"},
      {"name": "Gary", "surname": "Whitta"},
      {"name": "George", "surname": "Lucas"}
    ],
    "Released": "16 Dec 2016",
    "Director": "Gareth Edwards",
    "Awards": "1 nomination.",
    "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQyMzI2OTA3OF5BMl5BanBnXkFtZTgwNDg5NjQ0OTE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
    "Metascore": 0,
    "imdbRating": 0.0,
    "imdbVotes": 0,
    "imdbID": "tt3748528",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE3MzA4Nzk3NV5BMl5BanBnXkFtZTgwNjAxMTc1ODE@._V1_SX1777_CR0,0,1777,744_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNDMxMTQzMjQxM15BMl5BanBnXkFtZTgwNzAxMTc1ODE@._V1_SX1777_CR0,0,1777,744_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNjkxOTk5NV5BMl5BanBnXkFtZTgwODAxMTc1ODE@._V1_SX1777_CR0,0,1777,744_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BNjM4MzExNDAyNl5BMl5BanBnXkFtZTgwOTAxMTc1ODE@._V1_SX1777_CR0,0,1777,744_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE3NTgxMDcyNV5BMl5BanBnXkFtZTgwMDExMTc1ODE@._V1_SX1777_CR0,0,1777,744_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": True
  },
  {
    "Title": "Assassin's Creed",
    "Year": 2016,
    "Rated": "N/A",
    "Runtime": 0,
    "Genre": "Action, Adventure, Fantasy",
    "Language": "English",
    "Country": "UK, France, USA, Hong Kong",
    "Actors": [
      {"name": "Michael", "surname": "Fassbender"},
      {"name": "Michael", "surname": "Kenneth Williams"},
      {"name": "Marion", "surname": "Cotillard"},
      {"name": "Jeremy", "surname": "Irons"}
    ],
    "Plot": "When Callum Lynch explores the memories of his ancestor Aguilar and gains the skills of a Master Assassin, he discovers he is a descendant of the secret Assassins society.",
    "Writer": [
      {"name": "Bill", "surname": "Collage"},
      {"name": "Adam", "surname": "Cooper"},
      {"name": "Michael", "surname": "Lesslie"}
    ],
    "Released": "21 Dec 2016",
    "Director": "Justin Kurzel",
    "Awards": "N/A",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTU2MTQwMjU1OF5BMl5BanBnXkFtZTgwMDA5NjU5ODE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 0.0,
    "imdbVotes": 0,
    "imdbID": "tt2094766",
    "Type": "movie",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyYzgyOWEtNTY2NS00NjRjLWJiNDYtMWViMjg5MWZjYjgzXkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOWYzOTctOTc4My00ZmJkLTgzMTctMmUxNDI5ODQzYzNjXkEyXkFqcGdeQXVyNDAyODU1Njc@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BZTY5ZGUxMTAtYTU0OC00NGQ2LTkzNzgtZGZmNjlmNjY3MGU0XkEyXkFqcGdeQXVyNTY0MTkxMTg@._V1_SY1000_CR0,0,1500,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BZjA0MWYwZTEtYzc5Yi00NGM2LTg1YTctNjY2YzQ0NDJhZDAwXkEyXkFqcGdeQXVyNDAyODU1Njc@._V1_SY1000_CR0,0,1499,1000_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": True
  },
  {
    "Title": "Luke Cage",
    "Year": 2016,
    "Rated": "TV-MA",
    "Runtime": 55,
    "Genre": "Action, Crime, Drama",
    "Language": "English",
    "Country": "USA",
    "Actors": [
      {"name": "Mahershala", "surname": "Ali"},
      {"name": "Mike", "surname": "Colter"},
      {"name": "Frankie", "surname": "Faison"},
      {"name": "Erik", "surname": "LaRay Harvey"}
    ],
    "Plot": "Given superstrength and durability by a sabotaged experiment, a wrongly accused man escapes prison to become a superhero for hire.",
    "Writer": [
      {"name": "Cheo", "surname": "Hodari Coker"}
    ],
    "Released": "30 Sep 2016",
    "Director": "N/A",
    "Awards": "N/A",
    "Poster": "http://ia.media-imdb.com/images/M/MV5BMTcyMzc1MjI5MF5BMl5BanBnXkFtZTgwMzE4ODY2OTE@._V1_SX300.jpg",
    "Metascore": 0,
    "imdbRating": 0.0,
    "imdbVotes": 0,
    "imdbID": "tt3322314",
    "Type": "series",
    "Response": "True",
    "Images": [
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxNjc1NjI0NV5BMl5BanBnXkFtZTgwNzA0NzY0ODE@._V1_SY1000_CR0,0,1497,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI1MDg3NjY2OF5BMl5BanBnXkFtZTgwNDE1NDU4OTE@._V1_SY1000_CR0,0,1497,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BOTYzOTQyNDYxNl5BMl5BanBnXkFtZTgwNzA1NDU4OTE@._V1_SY1000_CR0,0,1498,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgxMjA3MTQ5Ml5BMl5BanBnXkFtZTgwOTA1NDU4OTE@._V1_SY1000_CR0,0,1498,1000_AL_.jpg",
      "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNjg5ODYwNF5BMl5BanBnXkFtZTgwMTE1NDU4OTE@._V1_SY1000_CR0,0,1477,1000_AL_.jpg"
    ],
    "totalSeasons": "",
    "ComingSoon": True
  }
]
@router.get("/all", response_model=list[filmModel.Film])
def get_all(
    min_year: Optional[int] = Query(
        None, ge=1900, le=2100, description="Minimal production year"
    ),
    max_year: Optional[int] = Query(
        None, ge=1900, le=2100, description="Maximum production year"
    ),
    min_rating: Optional[float] = Query(
        None, ge=0.0, le=10.0, description="Minimum rating"
    ),
    max_rating: Optional[float] = Query(
        None, ge=0.0, le=10.0, description="Maximum rating"
    ),
    type: Optional[Literal["movie", "series"]] = Query(
        None, description="Type of content: 'movie' or 'series'"
    )):
    if min_year is not None and max_year is not None and min_year > max_year:
        raise HTTPException(
            status_code=400,
            detail="Vrijednost min_year ne može biti veća od max_year."
        )
    if min_rating is not None and max_rating is not None and min_rating > max_rating:
        raise HTTPException(
            status_code=400,
            detail="Vrijednost min_rating ne može biti veća od max_rating."
        )
    filtered_films = filmovi
    if min_year is not None:
        filtered_films = [film for film in filtered_films if film.get("year", 0) >= min_year]
    if max_year is not None:
        filtered_films = [film for film in filtered_films if film.get("year", 0) <= max_year]
    if min_rating is not None:
        filtered_films = [film for film in filtered_films if film.get("rating", 0) >= min_rating]
    if max_rating is not None:
        filtered_films = [film for film in filtered_films if film.get("rating", 0) <= max_rating]
    if type is not None:
        filtered_films = [film for film in filtered_films if film.get("type") == type]
    return filtered_films

@router.get("/imdbId", response_model=filmModel.Film)
def get_by_imdbId(imdbId: str):
    for film in filmovi:
        if film["imdbID"] == imdbId:
            return film
    raise HTTPException(status_code=404, detail=f"Film s imdbID-em {imdbId} nije pronađen.")

@router.get("/title", response_model=filmModel.Film)
def get_by_title(title: str):
    for film in filmovi:
        if film["Title"].lower() == title.lower():
            return film
    raise HTTPException(status_code=404, detail=f"Film s nazivom {title} nije pronađen.") 
