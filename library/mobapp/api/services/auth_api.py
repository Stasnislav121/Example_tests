import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *
from library.common.helpers import StringHelper


class AuthApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='auth')

    def login(self, device_id, json, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /auth/login'):
            if device_id is not None:
                self.headers['Device-Id'] = device_id
            response = self.post('/login', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def registration(self, json, *, device_id=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /auth/registration'):
            if device_id is not None:
                self.headers['Device-Id'] = device_id
            else:
                self.headers['Device-Id'] = ('TKzmgFjAW5Gv2gHaTGfe42E3wYYrYU0hGwwj' +
                                             StringHelper().get_random_string(length=7))
            response = self.post('/registration', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
