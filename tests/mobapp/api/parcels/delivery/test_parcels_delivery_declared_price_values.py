import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestParcelsDelivery:
    @testit.workItemIds(35157)
    @testit.externalId('TestParcelsDelivery_35157')
    @testit.displayName('[201] POST /parcels/delivery - РФ-РФ, граничные значения "declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - РФ-РФ, граничные значения "declaredPrice.value"')
    @allure.testcase(url='https://testit..ru/browse/35157')
    @pytest.mark.parametrize('declared_price', [1000.00, 200000.00])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_with_declared_price_boundary_values(self, declared_price, api_version):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_package_json)
            json_request['declaredPrice']['value'] = declared_price
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_two_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']

            assert first_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"

            assert second_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"

    @testit.workItemIds(35170)
    @testit.externalId('TestParcelsDelivery_35170')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений параметра  '
                        '"declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений параметра  '
                  '"declaredPrice.value"')
    @allure.testcase(url='https://testit..ru/browse/35170')
    @pytest.mark.parametrize(('declared_price_value', 'error_text'), [(0, 'Стоимость не может быть меньше 1000 рублей'),
                                                                      (999.99,
                                                                       'Стоимость не может быть меньше 1000 рублей'),
                                                                      (200000.01,
                                                                       'Стоимость не может быть больше 200000 '
                                                                       'рублей')])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_exceeding_the_boundary_values_declared_price_value(self, declared_price_value,
                                                                                 error_text, api_version):
        error_field = 'declaredPrice.value'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['declaredPrice']['value'] = declared_price_value
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35169)
    @testit.externalId('TestParcelsDelivery_35169')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при отсутствии'
                        ' параметра "declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра "declaredPrice.value"')
    @allure.testcase(url='https://testit..ru/browse/35169')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_without_declared_price_value(self, api_version):
        error_field = 'declaredPrice.value'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['declaredPrice'].pop('value')
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35171)
    @testit.externalId('TestParcelsDelivery_35171')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра  '
                        '"declaredPrice.code"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра  "declaredPrice.code"')
    @allure.testcase(url='https://testit..ru/browse/35171')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_without_declared_price_code(self, api_version):
        error_field = 'declaredPrice.code'
        error_text = 'Неверно указана валюта'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['declaredPrice'].pop('code')
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35172)
    @testit.externalId('TestParcelsDelivery_35172')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при несуществующем "declaredPrice.code"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при несуществующем "declaredPrice.code"')
    @allure.testcase(url='https://testit..ru/browse/35172')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_not_found_declared_price_code(self, api_version):
        error_field = 'declaredPrice.code'
        error_text = 'Неверно указана валюта'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['declaredPrice']['code'] = 'abc'
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35173)
    @testit.externalId('TestParcelsDelivery_35173')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра "declaredPrice"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра "declaredPrice"')
    @allure.testcase(url='https://testit..ru/browse/35173')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_without_declared_price(self, api_version):
        error_field = 'declaredPrice'
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request.pop(error_field)
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"
