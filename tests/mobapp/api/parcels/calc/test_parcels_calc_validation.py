import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestParcelsCalcValidation:
    @testit.workItemIds(35066)
    @testit.externalId('TestParcelsCalc_35066')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "senderCityCode"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "senderCityCode"')
    @allure.testcase(url='https://testit..ru/browse/35066')
    def test_parcels_calc_without_sender_city_code(self):
        error_field = 'senderCityCode'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request.pop(error_field)
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35076)
    @testit.externalId('TestParcelsCalc_35076')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "senderCityCode"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "senderCityCode"')
    @allure.testcase(url='https://testit..ru/browse/35076')
    def test_parcels_calc_not_found_sender_city_code(self, ):
        error_field = 'senderCityCode'
        error_text = 'Город отправителя не найден'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request[error_field] = '99999'
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35067)
    @testit.externalId('TestParcelsCalc_35067')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "receiverCityCode"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "receiverCityCode"')
    @allure.testcase(url='https://testit..ru/browse/35067')
    def test_parcels_calc_without_receiver_city_code(self):
        error_field = 'receiverCityCode'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request.pop(error_field)
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35077)
    @testit.externalId('TestParcelsCalc_35077')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "receiverCityCode"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "receiverCityCode"')
    @allure.testcase(url='https://testit..ru/browse/35077')
    def test_parcels_calc_not_found_receiver_city_code(self):
        error_field = 'receiverCityCode'
        error_text = 'Город получателя не найден'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request[error_field] = '99999'
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35068)
    @testit.externalId('TestParcelsCalc_35068')
    @testit.displayName('[403] POST parcels/calc - получение ошибки при отсутствии параметра "deliveryId"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[403] POST parcels/calc - получение ошибки при отсутствии параметра "deliveryId"')
    @allure.testcase(url='https://testit..ru/browse/35068')
    def test_parcels_calc_without_delivery_id(self):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request.pop('deliveryId')
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)

        with allure.step('Проверка параметров ответа'):
            assert response.status_code == 403, f"Ожидалось 403, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_err_schema)

    @testit.workItemIds(35078)
    @testit.externalId('TestParcelsCalc_35078')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "deliveryId"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "deliveryId"')
    @allure.testcase(url='https://testit..ru/browse/35078')
    def test_parcels_calc_not_found_delivery_id(self):
        error_field = 'deliveryId'
        error_text = 'Выбран неверный способ доставки'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request[error_field] = 'officeToOffic'
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35069)
    @testit.externalId('TestParcelsCalc_35069')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice.value"')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    @allure.testcase(url='https://testit..ru/browse/35069')
    def test_parcels_calc_without_declared_price_value(self, api_version):
        error_field = 'declaredPrice.value'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['declaredPrice'].pop('value')
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35087)
    @testit.externalId('TestParcelsCalc_35087')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при превышении граничных значений '
                        ' параметра "declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при превышении '
                  ' граничных значений параметра "declaredPrice.value"')
    @allure.testcase(url='https://testit..ru/browse/35087')
    @pytest.mark.parametrize(('declared_price_value', 'error_text'), [(0, 'Стоимость не может быть меньше 1000 рублей'),
                                                                      (999.99,
                                                                       'Стоимость не может быть меньше 1000 рублей'),
                                                                      (200000.01,
                                                                       'Стоимость не может быть больше 200000 '
                                                                       'рублей')])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_exceeding_the_boundary_values_declared_price_value(self, declared_price_value, error_text,
                                                                             api_version):
        error_field = 'declaredPrice.value'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['declaredPrice']['value'] = declared_price_value
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35070)
    @testit.externalId('TestParcelsCalc_35070')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice.code"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice.code"')
    @allure.testcase(url='https://testit..ru/browse/35070')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_without_declared_price_code(self, api_version):
        error_field = 'declaredPrice.code'
        error_text = 'Неверно указана валюта'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['declaredPrice'].pop('code')
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35079)
    @testit.externalId('TestParcelsCalc_35079')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "declaredPrice.code"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "declaredPrice.code"')
    @allure.testcase(url='https://testit..ru/browse/35079')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_not_found_declared_price_code(self, api_version):
        error_field = 'declaredPrice.code'
        error_text = 'Неверно указана валюта'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['declaredPrice']['code'] = 'abc'
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35071)
    @testit.externalId('TestParcelsCalc_35071')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "declaredPrice"')
    @allure.testcase(url='https://testit..ru/browse/35071')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_without_declared_price(self, api_version):
        error_field = 'declaredPrice'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request.pop(error_field)
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35072)
    @testit.externalId('TestParcelsCalc_35072')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.width"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.width"')
    @allure.testcase(url='https://testit..ru/browse/35072')
    def test_parcels_calc_without_custom_package_width(self):
        error_field = 'customPackage.width'
        error_text = 'Ширина упаковки обязательна для заполнения'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage'].pop('width')
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35073)
    @testit.externalId('TestParcelsCalc_35073')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.length"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.length"')
    @allure.testcase(url='https://testit..ru/browse/35073')
    def test_parcels_calc_without_custom_package_length(self):
        error_field = 'customPackage.length'
        error_text = 'Длина упаковки обязательна для заполнения'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage'].pop('length')
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35074)
    @testit.externalId('TestParcelsCalc_35074')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.height"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage.height"')
    @allure.testcase(url='https://testit..ru/browse/35074')
    def test_parcels_calc_without_custom_package_height(self):
        error_field = 'customPackage.height'
        error_text = 'Высота упаковки обязательна для заполнения'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage'].pop('height')
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35075)
    @testit.externalId('TestParcelsCalc_35075')
    @testit.displayName('[403] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[403] POST parcels/calc - получение ошибки при отсутствии параметра "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35075')
    def test_parcels_calc_without_custom_package(self):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request.pop('customPackage')
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)

        with allure.step('Проверка параметров ответа'):
            assert response.status_code == 403, f"Ожидалось 403, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_err_schema)

    @testit.workItemIds(35080)
    @testit.externalId('TestParcelsCalc_35080')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "package"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "package"')
    @allure.testcase(url='https://testit..ru/browse/35080')
    def test_parcels_calc_not_found_package(self):
        error_field = 'package'
        error_text = 'Упаковка не найдена'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_package_json)
            json_request[error_field] = '1000'
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35081)
    @testit.externalId('TestParcelsCalc_35081')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при несуществующем "promo"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при несуществующем "promo"')
    @allure.testcase(url='https://testit..ru/browse/35081')
    def test_parcels_calc_not_found_promo(self):
        error_field = 'promo'
        error_text = 'Указан неверный промокод'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_package_json)
            json_request[error_field] = 'fdfdffd'
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35082)
    @testit.externalId('TestParcelsCalc_35082')
    @testit.displayName('[403] POST parcels/calc - получение ошибки при несуществующем "additionalServices"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[403] POST parcels/calc - получение ошибки при несуществующем "additionalServices"')
    @allure.testcase(url='https://testit..ru/browse/35082')
    def test_parcels_calc_not_additional_services(self):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['additionalServices'] = ['99999']
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)

        with allure.step('Проверка параметров ответа'):
            assert response.status_code == 403, f"Ожидалось 403, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_err_schema)

    @testit.workItemIds(35083)
    @testit.externalId('TestParcelsCalc_35083')
    @testit.displayName(
        '[422] POST parcels/calc - получение ошибки при превышении граничных значений параметра "customPackage.width"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title(
        '[422] POST parcels/calc - получение ошибки при превышении граничных значений параметра "customPackage.width"')
    @allure.testcase(url='https://testit..ru/browse/35083')
    @pytest.mark.parametrize(('custom_package_width', 'error_text'), [(0, 'Ширина упаковки обязательна для заполнения'),
                                                                      (121,
                                                                       'Ширина упаковки не может превышать 120 см')])
    def test_parcels_calc_exceeding_the_boundary_values_custom_package_width(self, custom_package_width, error_text):
        error_field = 'customPackage.width'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage']['width'] = custom_package_width
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35084)
    @testit.externalId('TestParcelsCalc_35084')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при превышении граничных значений '
                        ' параметра "customPackage.length"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при превышении граничных значений '
                  ' параметра "customPackage.length"')
    @allure.testcase(url='https://testit..ru/browse/35084')
    @pytest.mark.parametrize(('custom_package_length', 'error_text'), [(0, 'Длина упаковки обязательна для заполнения'),
                                                                       (121,
                                                                        'Длина упаковки не может превышать 120 см')])
    def test_parcels_calc_exceeding_the_boundary_values_custom_package_length(self, custom_package_length, error_text):
        error_field = 'customPackage.length'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage']['length'] = custom_package_length
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35085)
    @testit.externalId('TestParcelsCalc_35085')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при превышении граничных значений '
                        ' параметра "customPackage.height"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при превышении граничных значений '
                  ' параметра "customPackage.height"')
    @allure.testcase(url='https://testit..ru/browse/35085')
    @pytest.mark.parametrize(('custom_package_height', 'error_text'),
                             [(0, 'Высота упаковки обязательна для заполнения'),
                              (121, 'Высота упаковки не может превышать 120 см')])
    def test_parcels_calc_exceeding_the_boundary_values_custom_package_height(self, custom_package_height, error_text):
        error_field = 'customPackage.height'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage']['height'] = custom_package_height
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35086)
    @testit.externalId('TestParcelsCalc_35086')
    @testit.displayName('[422] POST parcels/calc - получение ошибки при нарушении пропорции 120х80х50 в '
                        ' параметре "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST parcels/calc - получение ошибки при нарушении пропорции 120х80х50 в '
                  ' параметре "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35086')
    def test_parcels_calc_violation_of_proportion_dimensions_custom_package(self):
        error_field = 'customPackage.height'
        error_text = 'Высота упаковки не может превышать 50 см'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage'] = {"width": 120, "length": 65, "height": 65}
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"
