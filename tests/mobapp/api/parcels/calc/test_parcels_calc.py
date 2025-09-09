import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestParcelsCalc:
    @testit.workItemIds(34795)
    @testit.externalId('TestParcelsCalc_34795')
    @testit.displayName('[201] POST parcels/calc - разные виды доставки')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - разные виды доставки')
    @allure.testcase(url='https://testit..ru/browse/34795')
    @pytest.mark.parametrize(('delivery_id', 'delivery_title'),
                             [('officeToOffice', 'Доставка от отделения до отделения'),
                              ('officeToDoor', 'Доставка от отделения до двери'),
                              ('doorToOffice', 'Доставка от двери до отделения'),
                              ('doorToDoor', 'Доставка от двери до двери')])
    @pytest.mark.forci
    def test_parcels_calc_with_different_delivery_id(self, delivery_id, delivery_title):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_package_json)
            json_request['deliveryId'] = delivery_id
            client = ParcelsApi()
            response = client.get_calculate(json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            delivery_id_resp = response.json()['data']['delivery']['id']
            delivery_title_resp = response.json()['data']['delivery']['title']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"
            assert delivery_id_resp == delivery_id, f"Ожидалось {delivery_id}, получено {delivery_id_resp}"
            assert delivery_title_resp == delivery_title, f"Ожидалось {delivery_title}, получено {delivery_title_resp}"

    @testit.workItemIds(35064)
    @testit.externalId('TestParcelsCalc_35064')
    @testit.displayName('[201] POST parcels/calc - виды упаковок ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - виды упаковок ')
    @allure.testcase(url='https://testit..ru/browse/35064')
    @pytest.mark.parametrize('package_id', ['793', '794', '795', '796', '797',
                                            '798', '799', '800', '801', '802', '803', '804', '808', '813', '978'])
    def test_parcels_calc_with_package_bb(self, package_id):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_package_json)
            json_request['package'] = package_id
            client = ParcelsApi()
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"

    @testit.workItemIds(35063)
    @testit.externalId('TestParcelsCalc_35063')
    @testit.displayName('[201] POST parcels/calc - граничные значения "paidByReceiver"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - граничные значения "paidByReceiver"')
    @allure.testcase(url='https://testit..ru/browse/35063')
    @pytest.mark.parametrize('paid_by_receiver', [True, False])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_with_paid_by_receiver_boundary_values(self, paid_by_receiver, api_version):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_package_json)
            json_request['paidByReceiver'] = paid_by_receiver
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"

    @testit.workItemIds(35061)
    @testit.externalId('TestParcelsCalc_35061')
    @testit.displayName('[201] POST parcels/calc - граничные значения "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - граничные значения "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35061')
    @pytest.mark.parametrize('custom_package_size', [{"width": 1, "length": 1, "height": 1},
                                                     {"width": 120, "length": 80, "height": 50}])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_with_custom_package_size_boundary_values(self, custom_package_size, api_version):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['customPackage'] = custom_package_size
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"

    @testit.workItemIds(35059)
    @testit.externalId('TestParcelsCalc_35059')
    @testit.displayName('[201] POST parcels/calc - РФ-РФ, граничные значения "declaredPrice.value"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - РФ-РФ, граничные значения "declaredPrice.value"')
    @allure.testcase(url='https://testit..ru/browse/35059')
    @pytest.mark.parametrize('declared_price', [1000.00, 200000.00])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_with_declared_price_boundary_values(self, declared_price, api_version):
        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['declaredPrice']['value'] = declared_price
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"

    @testit.workItemIds(35062)
    @testit.externalId('TestParcelsCalc_35062')
    @testit.displayName('[201] POST parcels/calc - РФ-СНГ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - РФ-СНГ')
    @allure.testcase(url='https://testit..ru/browse/35062')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_from_rf_to_cis(self, api_version):
        sender_city_code = '03379'
        receiver_city_code = 'Н00163804'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['senderCityCode'] = sender_city_code
            json_request['receiverCityCode'] = receiver_city_code
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"

    @testit.workItemIds(35065)
    @testit.externalId('TestParcelsCalc_35065')
    @testit.displayName('[201] POST parcels/calc - с "promo"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST parcels/calc - с "promo"')
    @allure.testcase(url='https://testit..ru/browse/35065')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_calc_with_promo(self, api_version):
        promo = 'пикоди'
        discount_title = f'Скидка по промокоду {promo}'

        with allure.step('Выполнить POST /parcels/calc'):
            json_request = copy.deepcopy(parcel_calc_with_custom_package_json)
            json_request['promo'] = promo
            client = ParcelsApi(version=api_version)
            response = client.get_calculate(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_calc_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_price_resp = response.json()['data']['delivery']['price']['value']
            discount_title_resp = response.json()['data']['discount']['title']
            discount_price_value_resp = response.json()['data']['discount']['price']['value']
            discount_price_code_resp = response.json()['data']['discount']['price']['code']
            assert delivery_price_resp > 0, f"Ожидалось delivery.price.value > 0, получено {delivery_price_resp}"
            assert discount_title_resp == discount_title, f"Ожидалось {discount_title}, получено {discount_title_resp}"
            assert discount_price_value_resp > 0, (f"Ожидалось discount.price.value > 0, "
                                                   f"получено {discount_price_value_resp}")
            assert discount_price_code_resp == 'RUB', f"Ожидалось 'RUB', получено {discount_price_code_resp}"
