import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class PagesApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='pages')

    def get_pages(self, page_name, token=None, check_error=True) -> Response:
        with allure.step(f'Отправка запроса через метод /pages/{page_name}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get(f'/{page_name}',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

            return response


class PagesDocumentsApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='pages')

    def get_documents(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /pages/documents'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/documents',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)
        return response
