import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class ParcelsApi(BaseApiClient):
    def __init__(self, version='v2'):
        super().__init__(service='parcels', version=version)

    def create(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/create'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/create', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def multi_create(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/multi/create'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/multi/create', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_parcel(self, parcel_id, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/{id} (get)'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get(f'/{parcel_id}', headers=self.headers, print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_duplicate_parcel(self, parcel_id, token=None, check_error=True, platform=None) -> Response:
        with allure.step('Отправка запроса через метод parcels/duplicate)'):
            if token is not None:
                self.headers['Authorization'] = token
            if platform is not None:
                self.headers['Platform'] = platform
            response = self.get('/duplicate', headers=self.headers, print_url=False,
                                params={"parcelId": parcel_id})
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def delete_parcel(self, parcel_id, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/{id} (delete)'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.delete(f'/{parcel_id}', headers=self.headers)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def delete_parcels(self, parcel_ids: list, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/delete'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/delete', headers=self.headers, json={
                "parcels": parcel_ids
            })
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_calculate(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/calc'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/calc', headers=self.headers, json=json)
            print()
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_multi_calculate(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/calc/multi'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/calc/multi', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def search_parcel(self, token=None, check_error=True, offset=None, limit=None,
                      type=None, search=None, status=None, favorite=None) -> Response:
        with allure.step('Отправка запроса через метод parcels/search'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/search',
                                headers=self.headers,
                                print_url=False,
                                params={"offset": offset,
                                        "limit": limit,
                                        "type": type,
                                        "search": search,
                                        "status": status,
                                        "isFavorite": favorite})
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_delivery(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/delivery'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/delivery', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_multi_delivery(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/delivery/multi'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/delivery/multi', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def get_insurance_limit(self, sender_city=68, receiver_city=16, package_id=800, token=None,
                            check_error=True) -> Response:
        with allure.step(f'Отправка запроса через \
         метод parcels/insurance/limit?senderCity={sender_city}&receiverCity={receiver_city}&packageId={package_id}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/insurance/limit', headers=self.headers, params={
                "senderCity": sender_city,
                "receiverCity": receiver_city,
                "packageId": package_id})
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def add_parcel_favorite(self, parcel: str, token=None, check_error=True) -> Response:
        with allure.step(f'Отправка запроса через метод parcels/{parcel}/favorites'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.put(f'/{parcel}/favorites', headers=self.headers)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def delete_parcel_favorite(self, parcel: str, token=None, check_error=True) -> Response:
        with allure.step(f'Отправка запроса через метод parcels/{parcel}/favorites'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.delete(f'/{parcel}/favorites', headers=self.headers)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def create_custom_package(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/custom-package/create'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/custom-package/create', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def delete_custom_package(self, id_package, token=None, check_error=True) -> Response:
        with allure.step(f'Отправка запроса через метод /parcels/custom-package/{id_package}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.delete(f'/custom-package/{id_package}', headers=self.headers)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def upload_custom_package_image(self, file_path=None, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/custom-package/file'):
            if token is not None:
                self.headers['Authorization'] = token
            if file_path is not None:
                try:
                    with open(file_path, 'rb') as file:
                        files = {'file': (os.path.basename(file_path), file)}
                        response = self.post('/custom-package/file', headers=self.headers, files=files)
                except Exception as ex:
                    raise Exception(f'Файл по пути {file_path} не найден', ex.args) from ex
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response

    def sync_favorites_parcels(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/favorites/sync'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.put('/favorites/sync', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)
        return response

    def delete_favorite_parcel(self, parcels, token=None, check_error=True) -> Response:
        if isinstance(parcels, str):
            parcels = [parcels]
        if token is not None:
            self.headers['Authorization'] = token
        for parcel in parcels:
            with allure.step(f'Отправка запроса через метод /parcels/{parcel}/favorites'):
                response = self.delete(f'/{parcel}/favorites', headers=self.headers)
                if check_error:
                    ResponseHandler.check_response_code_is_201(response)
                    ResponseHandler.check_response_has_success_is_true(response)
        return response

    def validate_package(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /parcels/custom-package/validate'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/custom-package/validate', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response


class ParcelsInsuranceLimit(BaseApiClient):
    def __init__(self, version='v3'):
        super().__init__(service='parcels', version=version)

    def get_insurance_limit(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод parcels/insurance/limit'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/insurance/limit', headers=self.headers, json=json)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

        return response
