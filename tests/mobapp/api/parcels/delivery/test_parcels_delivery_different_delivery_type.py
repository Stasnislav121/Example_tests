import allure
import testit
import copy

from library.mobapp import *


class TestParcelsDelivery:
    @testit.workItemIds(35228)
    @testit.externalId('TestParcelsDelivery_35228')
    @testit.displayName('[201] POST /parcels/delivery - получение 2-х видов доставки')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - получение 2-х видов доставки')
    @allure.testcase(url='https://testit..ru/browse/35228')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_get_two_delivery_type(self, api_version):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_package_json)
            json_request['senderCityCode'] = '68'
            json_request['receiverCityCode'] = '68'
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_two_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']

            days = int(delivery_type_resp[0]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_title_resp = delivery_type_resp[0]['title']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            first_discount_description_resp = delivery_type_resp[0]['deliverySmallDescription']

            assert first_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_title_resp == OFFICE_TO_DOOR_TITLE, \
                f"Ожидалось {OFFICE_TO_DOOR_TITLE}, получено {first_delivery_title_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"
            assert first_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {first_discount_description_resp}"

            days = int(delivery_type_resp[1]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_title_resp = delivery_type_resp[1]['title']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']
            second_discount_description_resp = delivery_type_resp[1]['deliverySmallDescription']

            assert second_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_title_resp == OFFICE_TO_OFFICE_TITLE, \
                f"Ожидалось {OFFICE_TO_OFFICE_TITLE}, получено {second_delivery_title_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"
            assert second_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {second_discount_description_resp}"

    @testit.workItemIds(35229)
    @testit.externalId('TestParcelsDelivery_35229')
    @testit.displayName('[201] POST /parcels/delivery - получение 4-х видов доставки')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - получение 4-х видов доставки')
    @allure.testcase(url='https://testit..ru/browse/35229')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_get_four_delivery_type(self, with_auth, api_version):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_package_json)
            json_request['senderCityCode'] = '16'
            json_request['receiverCityCode'] = '37'
            auth_token = with_auth
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=auth_token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_four_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']

            days = int(delivery_type_resp[0]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_title_resp = delivery_type_resp[0]['title']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            first_discount_description_resp = delivery_type_resp[0]['deliverySmallDescription']

            assert first_delivery_id_resp == DOOR_TO_DOOR_ID, \
                f"Ожидалось {DOOR_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_title_resp == DOOR_TO_DOOR_TITLE, \
                f"Ожидалось {DOOR_TO_DOOR_TITLE}, получено {first_delivery_title_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"
            assert first_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {first_discount_description_resp}"

            days = int(delivery_type_resp[1]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_title_resp = delivery_type_resp[1]['title']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']
            second_discount_description_resp = delivery_type_resp[1]['deliverySmallDescription']

            assert second_delivery_id_resp == DOOR_TO_OFFICE_ID, \
                f"Ожидалось {DOOR_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_title_resp == DOOR_TO_OFFICE_TITLE, \
                f"Ожидалось {DOOR_TO_OFFICE_TITLE}, получено {second_delivery_title_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"
            assert second_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {second_discount_description_resp}"

            days = int(delivery_type_resp[2]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            third_delivery_id_resp = delivery_type_resp[2]['id']
            third_delivery_title_resp = delivery_type_resp[2]['title']
            third_delivery_price_resp = delivery_type_resp[2]['price']['value']
            third_discount_description_resp = delivery_type_resp[2]['deliverySmallDescription']

            assert third_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {third_delivery_id_resp}"
            assert third_delivery_title_resp == OFFICE_TO_DOOR_TITLE, \
                f"Ожидалось {OFFICE_TO_DOOR_TITLE}, получено {third_delivery_title_resp}"
            assert third_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {third_delivery_price_resp}"
            assert third_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {third_discount_description_resp}"

            days = int(delivery_type_resp[3]['footerInfo']['days'])
            assert days > 0, f"Ожидалось footerInfo.days > 0,  получено {days}"
            delivery_time_text = ParcelsResponseHandler.get_string_delivery_small_description(days)
            fourth_delivery_id_resp = delivery_type_resp[3]['id']
            fourth_delivery_title_resp = delivery_type_resp[3]['title']
            fourth_delivery_price_resp = delivery_type_resp[3]['price']['value']
            fourth_discount_description_resp = delivery_type_resp[3]['deliverySmallDescription']

            assert fourth_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {fourth_delivery_id_resp}"
            assert fourth_delivery_title_resp == OFFICE_TO_OFFICE_TITLE, \
                f"Ожидалось {OFFICE_TO_OFFICE_TITLE}, получено {fourth_delivery_title_resp}"
            assert fourth_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {fourth_delivery_price_resp}"
            assert fourth_discount_description_resp == delivery_time_text, \
                f"Ожидалось {delivery_time_text}, получено {fourth_discount_description_resp}"
