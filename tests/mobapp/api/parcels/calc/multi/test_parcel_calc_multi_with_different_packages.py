import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestParcelsCalcMulti:
    @testit.workItemIds(35914)
    @testit.externalId('TestParcelsCalcMulti_35914')
    @testit.displayName('[200] POST /parcels/calc/multi - граничные значения "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/calc/multi - граничные значения "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35914')
    @pytest.mark.parametrize('custom_package_size', [{"width": 1, "length": 1, "height": 1},
                                                  {"width": 120, "length": 80, "height": 50}])
    def test_parcels_calc_multi_with_custom_package_size_boundary_values(self, custom_package_size, with_auth):
        token = with_auth
        json_request = copy.deepcopy(parcel_calc_multi_with_custom_package_json)
        json_request['parcel']['customPackage'] = custom_package_size

        with allure.step('Выполнить POST /parcels/calc/multi'):
            client = ParcelsApi()
            response = client.get_multi_calculate(json_request, token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_multi_schema)

        with allure.step('Проверка параметров ответа'):
            data_resp = response.json()['data']
            delivery_price_resp = data_resp['actualDeliveryInfo'][0]['deliveryInfo']['price']['value']
            sender_price_base_resp = float(data_resp['senderPrice']['base'][:-1])
            sender_price_total_resp = float(data_resp['senderPrice']['total'][:-1])

            assert delivery_price_resp > 0, f"Ожидалось deliveryInfo.price.value > 0, получено {delivery_price_resp}"
            assert sender_price_base_resp > 0, f"Ожидалось senderPrice.base > 0, получено {sender_price_base_resp}"
            assert sender_price_total_resp > 0, f"Ожидалось senderPrice.total > 0, получено {sender_price_total_resp}"

    @testit.workItemIds(25896)
    @testit.externalId('TestParcelsCalcMulti_25896')
    @testit.displayName('[200] POST /parcels/calc/multi - расчет стоимости отправления с упаковкой ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/calc/multi - расчет стоимости отправления с упаковкой ')
    @allure.testcase(url='https://testit..ru/browse/25896')
    def test_parcels_calc_multi_with_package_bb(self, with_auth):
        token = with_auth
        json_request = copy.deepcopy(parcel_calc_multi_with_package_json)

        with allure.step('Выполнить POST /parcels/calc/multi'):
            client = ParcelsApi()
            response = client.get_multi_calculate(json_request, token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_multi_schema)

        with allure.step('Проверка параметров ответа'):
            data_resp = response.json()['data']
            delivery_price_resp = data_resp['actualDeliveryInfo'][0]['deliveryInfo']['price']['value']
            sender_price_base_resp = float(data_resp['senderPrice']['base'][:-1])
            sender_price_total_resp = float(data_resp['senderPrice']['total'][:-1])

            assert delivery_price_resp > 0, f"Ожидалось deliveryInfo.price.value > 0, получено {delivery_price_resp}"
            assert sender_price_base_resp > 0, f"Ожидалось senderPrice.base > 0, получено {sender_price_base_resp}"
            assert sender_price_total_resp > 0, f"Ожидалось senderPrice.total > 0, получено {sender_price_total_resp}"
