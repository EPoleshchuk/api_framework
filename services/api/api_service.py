# genre
# movie
# reviews
from helpers.api.genre_helper import GenreHelper
from helpers.api.movie_helper import MovieHelper
from services.api.models.genre.create_genre_dto import CreateGenreDto
from services.api.models.genre.genre_response import GenreResponse
from services.api.models.movies.create_movie_dto import CreateMovieDto
from services.api.models.movies.movie_response import MovieResponse


class ApiService:
    def __init__(self, api_utils):
        self.api_utils = api_utils

        self.genre_helper = GenreHelper(self.api_utils)
        self.movie_helper = MovieHelper(self.api_utils)

    def post_genre(self, create_genre: CreateGenreDto):
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True,
                                                                             exclude_defaults=True))
        return GenreResponse(**response.json())

    def post_movie(self, create_movie: CreateMovieDto):
        response = self.movie_helper.post_movie(create_movie.model_dump(by_alias=True,
                                                                        exclude_defaults=True))
        print(response.json())
        return MovieResponse(**response.json())
