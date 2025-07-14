import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class CitiesApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='cities')

    def get_cities(self, token=None, check_error=True, offset=None, limit=None,
                      country_code=None, search=None) -> Response:
        with allure.step('Отправка запроса через метод /cities'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('',
                                headers=self.headers,
                                print_url=False,
                                params={"offset": offset,
                                        "limit": limit,
                                        "countryCode": country_code,
                                        "search": search})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_cities_nearest(self, token=None, check_error=True, lat=None, lng=None) -> Response:
        with allure.step('Отправка запроса через метод /cities/nearest'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/nearest',
                                headers=self.headers,
                                print_url=False,
                                params={"lat": lat,
                                        "lng": lng})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_additional_info(self, token=None, check_error=True, sender_city_code=None,
                            receiver_city_code=None) -> Response:
        with allure.step('Отправка запроса через метод /cities/additional-info'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/additional-info',
                                headers=self.headers,
                                print_url=False,
                                params={"senderCityCode": sender_city_code,
                                        "receiverCityCode": receiver_city_code})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
