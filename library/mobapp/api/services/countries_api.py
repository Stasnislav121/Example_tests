import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class CountriesApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='')

    def get_countries(self, token=None, check_error=True, offset=None, limit=None,
                      type=None, search=None) -> Response:
        with allure.step('Отправка запроса через метод /countries'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('countries',
                                headers=self.headers,
                                print_url=False,
                                params={"offset": offset,
                                        "limit": limit,
                                        "type": type,
                                        "search": search})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
