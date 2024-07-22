from services.auth.helpers.authorization_helper import AuthorizationHelper
from services.auth.models.authorization.login_response import LoginResponse
from services.auth.models.authorization.login_user_dto import LoginUserDto


class AuthService:
    def __init__(self, api_utils):
        self.api_utils = api_utils

        self.authorization_helper = AuthorizationHelper(self.api_utils)

    def register_user(self):
        raise NotImplementedError("Cannot register users!")

    def login_user(self, login_user: LoginUserDto):
        response = self.authorization_helper.login_user(login_user.model_dump(by_alias=True,
                                                                              exclude_defaults=True))
        return LoginResponse(**response.json())
