import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class OfficesApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='offices')

    def get_offices_by_city_code(self, token=None, check_error=True, city_code='68', filters=None, latitude=None,
                    longitude=None, offset=None, limit=None) -> Response:
        with allure.step('Отправка запроса через метод /offices'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('',
                                headers=self.headers,
                                print_url=False,
                                params={"cityCode": city_code,
                                        "filters": filters,
                                        "latitude": latitude,
                                        "longitude": longitude,
                                        "offset": offset,
                                        "limit": limit})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_information_about_office(self, token=None, check_error=True, code='01734') -> Response:
        with allure.step(f'Отправка запроса через метод /offices/{code}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get(f'/{code}',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def search_offices(self, token=None, check_error=True, search='баж', city_code=None,
                       final=None, is_global_search=None) -> Response:
        with allure.step('Отправка запроса через метод /offices/search'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/search',
                                headers=self.headers,
                                print_url=False,
                                params={"search": search,
                                        "cityCode": city_code,
                                        "final": final,
                                        "isGlobalSearch": is_global_search})
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_offices_filters(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /offices/filters'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/filters',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
