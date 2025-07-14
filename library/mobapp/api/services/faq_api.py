import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class FaqApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='faq')

    def get_faq(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /faq'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

            return response
