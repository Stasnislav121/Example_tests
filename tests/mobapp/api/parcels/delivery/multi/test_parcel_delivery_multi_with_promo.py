import allure
import testit
import copy

from library.mobapp import *


class TestParcelsDeliveryMulti:
    @testit.workItemIds(37234)
    @testit.externalId('TestParcelsDeliveryMulti_37234')
    @testit.displayName('[200] POST /parcels/delivery/multi - получить варианты доставки отправления  с промокодом')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/delivery/multi - получить варианты доставки отправления  с промокодом')
    @allure.testcase(url='https://testit..ru/browse/37234')
    def test_parcels_delivery_multi_with_promo(self, with_auth):
        token = with_auth
        json_request = copy.deepcopy(parcel_delivery_multi_with_package_json)
        json_request['promo'] = 'ПИКОДИ'

        with allure.step('Выполнить POST /parcels/delivery/multi'):
            client = ParcelsApi()
            response = client.get_multi_delivery(json_request, token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_multi_schema)

        with allure.step('Проверка параметров ответа'):
            data_resp = response.json()['data']

            to_door_data = data_resp['toDoor']['price']
            to_door_id = to_door_data['delivery']['id']
            to_door_title = to_door_data['delivery']['title']
            to_door_price = to_door_data['delivery']['price']['value']
            to_door_discount_price = to_door_data['discount']['price']['value']
            to_door_final_price = to_door_data['finalPrice']['value']
            result_door_final_price = to_door_price - to_door_discount_price

            to_office_data = data_resp['toOffice']['price']
            to_office_id = to_office_data['delivery']['id']
            to_office_title = to_office_data['delivery']['title']
            to_office_price = to_office_data['delivery']['price']['value']
            to_office_discount_price = to_office_data['discount']['price']['value']
            to_office_final_price = to_office_data['finalPrice']['value']
            result_office_final_price = to_office_price - to_office_discount_price

            assert to_door_id == 'officeToDoor', f'Ожидалось "id: officeToDoor" , получено {to_door_id}'
            assert to_door_title == 'Доставка от отделения до двери', \
                f'Ожидался "title: Доставка от отделения до двери", получено {to_door_title}'
            assert to_door_price > 0, f"Ожидалось toDoor.price.delivery.price.value > 0, получено {to_door_price}"
            assert to_door_discount_price > 0, \
                f"Ожидалось toDoor.price.discount.price.value > 0, получено {to_door_discount_price}"
            assert to_door_final_price == result_door_final_price, \
                f"Ожидалось {result_door_final_price}, получено {to_door_final_price}"

            assert to_office_id == 'officeToOffice', f'Ожидалось "id: officeToOffice" , получено {to_office_id}'
            assert to_office_title == 'Доставка от отделения до отделения', \
                f'Ожидался "title: Доставка от отделения до отделения", получено {to_office_title}'
            assert to_office_price > 0, f"Ожидалось toOffice.price.delivery.price.value > 0, получено {to_office_price}"
            assert to_office_discount_price > 0, \
                f"Ожидалось toOffice.price.discount.price.value > 0, получено {to_office_discount_price}"
            assert to_office_final_price == result_office_final_price, \
                f"Ожидалось {result_office_final_price}, получено {to_office_final_price}"
