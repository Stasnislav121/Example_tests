import allure
import pytest
import testit
import copy

from library.mobapp import *


class TestParcelsDelivery:
    @testit.workItemIds(35159)
    @testit.externalId('TestParcelsDelivery_35159')
    @testit.displayName('[201] POST /parcels/delivery - РФ-СНГ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - РФ-СНГ')
    @allure.testcase(url='https://testit..ru/browse/35159')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_from_rf_to_cis(self, api_version):
        sender_city_code = '03379'
        receiver_city_code = 'Н00163804'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['senderCityCode'] = sender_city_code
            json_request['receiverCityCode'] = receiver_city_code
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_export_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']
            delivery_id_resp = delivery_type_resp[0]['id']
            delivery_title_resp = delivery_type_resp[0]['title']
            delivery_price_resp = delivery_type_resp[0]['price']['value']
            delivery_small_description_resp = delivery_type_resp[0]['deliverySmallDescription']

            days = int(delivery_type_resp[0]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)

            assert delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {delivery_id_resp}"
            assert delivery_title_resp == OFFICE_TO_OFFICE_TITLE, \
                f"Ожидалось {OFFICE_TO_OFFICE_TITLE}, получено {delivery_title_resp}"
            assert delivery_price_resp > 0, f"Ожидалось items.price.value > 0, получено {delivery_price_resp}"
            assert delivery_small_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {delivery_small_description_resp}"

    @testit.workItemIds(35163)
    @testit.externalId('TestParcelsDelivery_35163')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра кода города')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при отсутствии параметра кода города')
    @allure.testcase(url='https://testit..ru/browse/35163')
    @pytest.mark.parametrize('error_field', ['senderCityCode', 'receiverCityCode'])
    def test_parcels_delivery_without_sender_city_code(self, error_field):
        error_text = 'Параметр отсутствует или не заполнен'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request.pop(error_field)
            client = ParcelsApi()
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

    @testit.workItemIds(35164)
    @testit.externalId('TestParcelsDelivery_35164')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при несуществующем коде города')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при несуществующем коде города')
    @allure.testcase(url='https://testit..ru/browse/35164')
    @pytest.mark.parametrize(('error_field', 'error_text'), [('senderCityCode', 'Город отправителя не найден'),
                                                             ('receiverCityCode', 'Город получателя не найден')])
    def test_parcels_delivery_not_found_sender_city_code(self, error_field, error_text):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request[error_field] = '99999'
            client = ParcelsApi()
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
