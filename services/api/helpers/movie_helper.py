import random

from faker import Faker

from utils.api_utils import ApiUtils

faker = Faker()


class MovieHelper:
    MOVIES_ENDPOINT = "/movies"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def post_movie(self, json):
        response = self.api_utils.post(endpoint_url=self.MOVIES_ENDPOINT,
                                       json=json)
        return response
