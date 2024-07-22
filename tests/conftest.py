import os

import pytest

from services.api.api_service import ApiService
from services.auth.auth_service import AuthService
from services.auth.models.authorization.login_user_dto import LoginUserDto
from utils.api_utils import ApiUtils

AUTH_URL = "https://auth.dev-cinescope.store"
API_URL = "https://api.dev-cinescope.store"


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_auth():
    api_utils_anonym = ApiUtils(url=AUTH_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_anonym_api():
    api_utils_anonym = ApiUtils(url=API_URL)
    yield api_utils_anonym


@pytest.fixture(scope="session", autouse=False)
def api_utils_super_admin_api(api_utils_anonym_auth):
    email = os.environ["SUPER_ADMIN_EMAIL"]
    password = os.environ["SUPER_ADMIN_PASSWORD"]

    auth_service = AuthService(api_utils=api_utils_anonym_auth)
    login_user = LoginUserDto(email=email, password=password)
    login_response = auth_service.login_user(login_user)

    api_utils_super_admin = ApiUtils(url=API_URL,
                                     headers={"Authorization": f"Bearer {login_response.access_token}"})
    yield api_utils_super_admin


@pytest.fixture(scope="session", autouse=False)
def api_service_super_admin_api(api_utils_super_admin_api):
    api_service = ApiService(api_utils=api_utils_super_admin_api)
    yield api_service
