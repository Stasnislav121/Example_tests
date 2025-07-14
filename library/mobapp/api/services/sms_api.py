import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class SmsApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='sms/code')

    def request_sms_code_send(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /sms/code/send'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/send',
                                 headers=self.headers,
                                 json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def request_sms_code_verify(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /sms/code/verify'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/verify',
                                 headers=self.headers,
                                 json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
