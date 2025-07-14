import allure
import testit
import copy

from library.mobapp import *


class TestParcelsDelivery:
    @testit.workItemIds(35162)
    @testit.externalId('TestParcelsDelivery_35162')
    @testit.displayName('[201] POST /parcels/delivery - с "promo"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - с "promo"')
    @allure.testcase(url='https://testit..ru/browse/35162')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_with_promo(self, api_version):
        promo = 'пикоди'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['promo'] = promo
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_two_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            first_discount_price_resp = delivery_type_resp[0]['promoDiscount']['value']
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']
            second_discount_price_resp = delivery_type_resp[1]['promoDiscount']['value']

            assert first_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"
            assert first_discount_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_discount_price_resp}"

            assert second_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"
            assert second_discount_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_discount_price_resp}"
