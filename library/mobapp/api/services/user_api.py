import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class UserApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='user')

    def get_user_info(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /user'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def logout_user(self, token=None, device_id=None, check_error=True, json=None) -> Response:
        with allure.step('Отправка запроса через метод /user/logout'):
            if token is not None:
                self.headers['Authorization'] = token
            if device_id is not None:
                self.headers['Device-Id'] = device_id
            response = self.post('/logout',
                                headers=self.headers,
                                json=json)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_user_chat_list(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /user/chatlist'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/chatlist',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
