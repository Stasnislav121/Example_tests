import allure
import pytest

from library.mobapp.api.services import AuthApi
from library.mobapp.api.api_const import AUTOTEST_USER


class AuthHelper:
    @staticmethod
    def get_auth_token(phone=AUTOTEST_USER[0], password=AUTOTEST_USER[1], device_id=None) -> str:
        with allure.step(f'Авторизоваться под пользователем: {phone} и получить токен авторизации'):
            client = AuthApi()
            response = client.login(device_id=device_id,
                                    json={
                                        "phone": phone,
                                        "password": password
                                    })
            token = response.json()['data']['authToken']
            auth_token = f'Bearer {token}'

        return auth_token


@pytest.fixture
def auth_helper():
    return AuthHelper()
