from fresh_tomatoes import open_movies_page
from json import load

# Define constant for path to movie list
FILE = "movies.json"


class Movie:
    """Movie object expected by fresh_tomatoes.py"""

    def __init__(self, title, pic, vid):
        self.title = title
        self.poster_image_url = pic
        self.trailer_youtube_url = vid


def makeMovieList(jsonFileName):
    """Accepts a filename containing JSON with the following format:
    {"MovieName": {"pic": "URL with box art", "vid": "URL with preview"}}"""
    list = []
    with open(jsonFileName) as f:
        movies = load(f)
    for movie in movies:
        name = movie
        data = movies[movie]
        pic = data['pic']
        vid = data['vid']
        movieInstance = Movie(name, pic, vid)
        list.append(movieInstance)
    return list

# Make list of movie objects
movieList = makeMovieList(FILE)

# Call Udacity-designed method
open_movies_page(movieList)
