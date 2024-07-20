import os
import random

from faker import Faker

from helpers.auth.authorization_helper import AuthorizationHelper
from services.api.api_service import ApiService
from services.api.models.genre.create_genre_dto import CreateGenreDto
from services.api.models.movies.create_movie_dto import CreateMovieDto, LocationEnum
from utils.api_utils import ApiUtils

faker = Faker()
AUTH_URL = "https://auth.dev-cinescope.store"

API_URL = "https://api.dev-cinescope.store"

email = os.environ["SUPER_ADMIN_EMAIL"]
password = os.environ["SUPER_ADMIN_PASSWORD"]

api_utils_anonym = ApiUtils(url=AUTH_URL)
authorization_helper = AuthorizationHelper(api_utils_anonym)
access_token = authorization_helper.login_user(email=email, password=password).json()["accessToken"]

api_utils_super_admin = ApiUtils(url=API_URL,
                                 headers={"Authorization": f"Bearer {access_token}"})
api_service = ApiService(api_utils=api_utils_super_admin)

genre = CreateGenreDto(name=faker.name())
created_genre = api_service.post_genre(genre)
movie = CreateMovieDto(name=faker.name(),
                       price=random.randint(100, 1000),
                       description=faker.pystr(),
                       location=LocationEnum.SPB,
                       published=True,
                       genre_id=created_genre.id)
created_movie = api_service.post_movie(movie)
