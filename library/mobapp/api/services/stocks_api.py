import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class StocksApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='stocks')

    def get_stocks(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /stocks'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_stock_by_id(self, id, token=None, check_error=True) -> Response:
        with allure.step(f'Отправка запроса через метод /stocks/{id}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get(f'/{id}',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response


class StocksBottomSheetApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='stocks', version='v1')

    def get_stock_for_bottom_sheet(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /stocks/bottom-sheet'):
            client = BaseApiClient(service='stocks', version='v1')
            if token is not None:
                client.headers['Authorization'] = token
            response = client.get('/bottom-sheet',
                                  headers=self.headers,
                                  print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
