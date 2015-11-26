from fresh_tomatoes import open_movies_page
from json import load

# Define constant for path to movie list
FILE = "movies.json"


class Movie:
    """Movie object expected by fresh_tomatoes.py"""

    def __init__(self, title, pic, vid, stars, director):
        self.title = title
        self.poster_image_url = pic
        self.trailer_youtube_url = vid

        # Addtional information
        self.stars = stars
        self.director = director


def makeMovieList(jsonFileName):
    """Accepts a filename containing JSON with the following format:
    {
      "MovieName": {
        "pic": "URL with box art",
        "vid": "URL with preview",
        "director": "Director's name",
        "stars": ["Names", "of", "stars"]
      }
    }"""
    list = []
    with open(jsonFileName) as f:
        movies = load(f)
    for movie in movies:
        name = movie
        data = movies[movie]
        pic = data['pic']
        vid = data['vid']
        stars = data['stars']
        director = data['director']
        movieInstance = Movie(name, pic, vid, stars, director)
        list.append(movieInstance)
    return list

# Make list of movie objects
movieList = makeMovieList(FILE)
for movie in movieList:
    print movie.stars

# Call Udacity-designed method
open_movies_page(movieList)
