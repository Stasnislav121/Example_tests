import allure
import testit
import copy

from library.mobapp import *


class TestParcelsCalcMulti:
    @testit.workItemIds(35925)
    @testit.externalId('TestParcelsCalcMulti_35925')
    @testit.displayName('[200] POST /parcels/calc/multi - c "deliveryType" = "officeToDoor"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/calc/multi - c "deliveryType" = "officeToDoor"')
    @allure.testcase(url='https://testit..ru/browse/35925')
    def test_parcels_calc_multi_with_delivery_office_to_door(self, with_auth):
        delivery_id = 'officeToDoor'
        expect_services = [
            "Доставка отправления между адресатами",
            "Упаковка",
            "Страхование",
            "Отслеживание",
            "Проверка содержимого при получении",
            "Сообщения получателю о поступлении посылки, отправителю – о выдаче посылки (Push/VK/Viber/SMS)",
            "Доставка посылки курьером"
        ]

        token = with_auth
        json_request = copy.deepcopy(parcel_calc_multi_with_cd_json)
        json_request['receivers'][0]['deliveryId'] = delivery_id

        with allure.step('Выполнить POST /parcels/calc/multi'):
            client = ParcelsApi()
            response = client.get_multi_calculate(json_request, token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_multi_schema)

        with allure.step('Проверка параметров ответа'):
            data_resp = response.json()['data']

            delivery_info_resp = data_resp['actualDeliveryInfo'][0]['deliveryInfo']
            delivery_info_id_resp = delivery_info_resp['deliveryId']
            delivery_info_text_resp = delivery_info_resp['deliveryInfo']
            delivery_price_resp = delivery_info_resp['price']['value']

            sender_price_base_resp = float(data_resp['senderPrice']['base'][:-1])
            sender_price_total_resp = float(data_resp['senderPrice']['total'][:-1])

            included_services_resp = data_resp['includedServices']

            assert delivery_info_id_resp == delivery_id, (f'Ожидалось deliveryId = {delivery_id}, '
                                                          f'получено {delivery_info_id_resp}')
            assert delivery_info_text_resp != '', f'Ожидалось {delivery_info_text_resp}, получено ""'
            assert delivery_price_resp > 0, f"Ожидалось deliveryInfo.price.value > 0, получено {delivery_price_resp}"
            assert sender_price_base_resp > 0, f"Ожидалось senderPrice.base > 0, получено {sender_price_base_resp}"
            assert sender_price_total_resp > 0, f"Ожидалось senderPrice.total > 0, получено {sender_price_total_resp}"
            ArrayHelper().assert_lists(expect_services, included_services_resp)

    @testit.workItemIds(35926)
    @testit.externalId('TestParcelsCalcMulti_35926')
    @testit.displayName('[200] POST /parcels/calc/multi - c "deliveryType" = "officeToOffice"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/calc/multi - c "deliveryType" = "officeToOffice"')
    @allure.testcase(url='https://testit..ru/browse/35926')
    def test_parcels_calc_multi_with_delivery_office_to_office(self, with_auth):
        delivery_id = 'officeToOffice'
        expect_services = [
            "Доставка отправления между адресатами",
            "Упаковка",
            "Страхование",
            "Отслеживание",
            "Проверка содержимого при получении",
            "Сообщения получателю о поступлении посылки, отправителю – о выдаче посылки (Push/VK/Viber/SMS)"
        ]

        token = with_auth
        json_request = copy.deepcopy(parcel_calc_multi_with_custom_package_json)
        json_request['receivers'][0]['deliveryId'] = delivery_id

        with allure.step('Выполнить POST /parcels/calc/multi'):
            client = ParcelsApi()
            response = client.get_multi_calculate(json_request, token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_multi_schema)

        with allure.step('Проверка параметров ответа'):
            data_resp = response.json()['data']

            delivery_info_resp = data_resp['actualDeliveryInfo'][0]['deliveryInfo']
            delivery_info_id_resp = delivery_info_resp['deliveryId']
            delivery_info_text_resp = delivery_info_resp['deliveryInfo']
            delivery_price_resp = delivery_info_resp['price']['value']

            sender_price_base_resp = float(data_resp['senderPrice']['base'][:-1])
            sender_price_total_resp = float(data_resp['senderPrice']['total'][:-1])

            included_services_resp = data_resp['includedServices']

            assert delivery_info_id_resp == delivery_id, (f'Ожидалось deliveryId = {delivery_id},'
                                                          f' получено {delivery_info_id_resp}')
            assert delivery_info_text_resp != '', f'Ожидалось {delivery_info_text_resp}, получено ""'
            assert delivery_price_resp > 0, f"Ожидалось deliveryInfo.price.value > 0, получено {delivery_price_resp}"
            assert sender_price_base_resp > 0, f"Ожидалось senderPrice.base > 0, получено {sender_price_base_resp}"
            assert sender_price_total_resp > 0, f"Ожидалось senderPrice.total > 0, получено {sender_price_total_resp}"
            ArrayHelper().assert_lists(expect_services, included_services_resp)
