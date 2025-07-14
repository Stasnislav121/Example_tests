import pytest
import allure
from library.mobapp.api.api_const import AUTOTEST_USER_LONG_EXPIRATION_TOKEN, DEVICE_ID
from library.mobapp.helpers.auth_helper import *


class TestSetup:
    @pytest.mark.setup
    @allure.epic('MobApp ')
    @allure.title('Настройки перед запуском автотестов')
    def test_setup(self, test_perform_authorization):
        pass

    @pytest.fixture
    def test_perform_authorization(self, auth_helper):
        with allure.step(f'Создать запись активной сессии в таблице "users_sessions" '
                         f' для пользователя {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["phone"]}, выполнив авторизацию'):
            token = auth_helper.get_auth_token(phone=AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
                                               password=AUTOTEST_USER_LONG_EXPIRATION_TOKEN['password'],
                                               device_id=DEVICE_ID)
        with (allure.step(f'Проверить, что полученный в ответе токен соответствует '
                          f' константе токена пользователя {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["phone"]}')):
            assert token == AUTOTEST_USER_LONG_EXPIRATION_TOKEN['token'], (
                f'Ожидался {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["token"]}, получен {token}')
