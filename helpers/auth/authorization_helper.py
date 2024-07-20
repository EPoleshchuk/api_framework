from faker import Faker

from utils.api_utils import ApiUtils

faker = Faker()


class AuthorizationHelper:
    REGISTER_ENDPOINT = "/register"
    LOGIN_ENDPOINT = "/login"

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    def register_user(self,
                      email,
                      password):
        response = self.api_utils.post(self.REGISTER_ENDPOINT,
                                       json={"email": email,
                                             "fullName": faker.first_name() + " " + faker.last_name(),
                                             "password": password,
                                             "passwordRepeat": password})
        return response

    def login_user(self,
                   email,
                   password):
        response = self.api_utils.post(self.LOGIN_ENDPOINT,
                                       json={"email": email,
                                             "password": password})
        return response
