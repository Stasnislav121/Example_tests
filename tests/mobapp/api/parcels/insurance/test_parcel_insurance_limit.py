import pytest
import allure
import testit

from library.mobapp import *


class TestInsuranceLimit:
    @testit.workItemIds(36136)
    @testit.externalId('TestInsuranceLimit_36136')
    @testit.displayName('[200] POST /parcels/insurance/limit - получение оценочной стоимости РФ-РФ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/insurance/limit - получение оценочной стоимости РФ-РФ')
    @allure.testcase(url='https://testit..ru/browse/36136')
    def test_get_parcels_insurance_limit_for_rf_rf(self):
        rf_cities = ('68', '16')
        expect_limit = {
            "min": 1000,
            "max": 200000,
            "recommended": 1000
        }
        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = rf_cities[0]
        json_request['receiverCities'][0] = rf_cities[1]

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_schema)

        with allure.step('Проверка параметров ответа'):
            actual_limit = response.json()['data']
            assert expect_limit == actual_limit, f'Ожидалось равенство с {expect_limit}, \
             получен {actual_limit}'

    @testit.workItemIds(40416)
    @testit.externalId('TestInsuranceLimit_40416')
    @testit.displayName('[200] POST /parcels/insurance/limit - '
                        'получение оценочной стоимости с несколькими городами-получателями')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/insurance/limit - '
                  'получение оценочной стоимости с несколькими городами-получателями')
    @allure.testcase(url='https://testit..ru/browse/40416')
    def test_get_parcels_insurance_limit_for_several_receiver_cities(self):
        sender_city = '68'
        receiver_cities = ['68', '16']
        expect_limit = {
            "min": 1000,
            "max": 200000,
            "recommended": 1000
        }
        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = sender_city
        json_request['receiverCities'] = receiver_cities

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_schema)

        with allure.step('Проверка параметров ответа'):
            actual_limit = response.json()['data']
            assert expect_limit == actual_limit, f'Ожидалось равенство с {expect_limit}, \
             получен {actual_limit}'

    @testit.workItemIds(36140)
    @testit.externalId('TestInsuranceLimit_36140')
    @testit.displayName('[200] POST /parcels/insurance/limit - получение оценочной стоимости СНГ-РФ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/insurance/limit - получение оценочной стоимости СНГ-РФ')
    @allure.testcase(url='https://testit..ru/browse/36140')
    @pytest.mark.parametrize(('sender_city', 'receiver_city'), [('Н00163804', '68'), ('Н00195824', '68'),
                                                                ('Н00195808', '68'), ('Н00704663', '68')])
    def test_get_parcels_insurance_limit_for_cis_rf(self, sender_city, receiver_city):
        expect_limit = {
            "min": 1000,
            "max": 200000,
            "recommended": 1000
        }

        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = sender_city
        json_request['receiverCities'][0] = receiver_city

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_schema)

        with allure.step('Проверка параметров ответа'):
            actual_limit = response.json()['data']
            assert expect_limit == actual_limit, f'Ожидалось равенство с {expect_limit}, \
             получен {actual_limit}'

    @testit.workItemIds(36138)
    @testit.externalId('TestInsuranceLimit_36138')
    @testit.displayName('[200] POST /parcels/insurance/limit - получение оценочной стоимости РФ-СНГ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/insurance/limit - получение оценочной стоимости РФ-СНГ')
    @allure.testcase(url='https://testit..ru/browse/36138')
    @pytest.mark.parametrize(('sender_city', 'receiver_city'), [('16', 'Н00163804'), ('16', 'Н00195824'),
                                                                ('16', 'Н00195808'), ('16', 'Н00704663')])
    def test_get_parcels_insurance_limit_for_rf_cis(self, sender_city, receiver_city):
        expect_limit = {
            "min": 1000,
            "max": 100000,
            "recommended": 1000
        }

        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = sender_city
        json_request['receiverCities'][0] = receiver_city

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_schema)

        with allure.step('Проверка параметров ответа'):
            actual_limit = response.json()['data']
            assert expect_limit == actual_limit, f'Ожидалось равенство с {expect_limit}, \
             получен {actual_limit}'

    @testit.workItemIds(36142)
    @testit.externalId('TestInsuranceLimit_36142')
    @testit.displayName('[200] POST /parcels/insurance/limit - получение оценочной стоимости СНГ-СНГ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] POST /parcels/insurance/limit - получение оценочной стоимости СНГ-СНГ')
    @allure.testcase(url='https://testit..ru/browse/36142')
    @pytest.mark.parametrize(('sender_city', 'receiver_city'), [('Н00704663', 'Н00163804'), ('Н00163804', 'Н00195824'),
                                                                ('Н00195824', 'Н00195808'), ('Н00195808', 'Н00704663')])
    def test_get_parcels_insurance_limit_for_cis_cis(self, sender_city, receiver_city):
        expect_limit = {
            "min": 1000,
            "max": 100000,
            "recommended": 1000
        }

        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = sender_city
        json_request['receiverCities'][0] = receiver_city

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_schema)

        with allure.step('Проверка параметров ответа'):
            actual_limit = response.json()['data']
            assert expect_limit == actual_limit, f'Ожидалось равенство с {expect_limit}, \
             получен {actual_limit}'

    @testit.workItemIds(37034)
    @testit.externalId('TestInsuranceLimit_37034')
    @testit.displayName('[422] POST /parcels/insurance/limit - получение ошибки в случае отсутствия города')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/insurance/limit - получение ошибки в случае отсутствия города')
    @allure.testcase(url='https://testit..ru/browse/37034')
    @pytest.mark.parametrize(('nonexistent_cities', 'expect_error_text'),
                             [(('68', '12345'), 'Город получателя не найден'),
                              (('12345', '68'), 'Город отправителя не найден')])
    def test_get_parcels_insurance_limit_for_nonexistent_cities(self, nonexistent_cities, expect_error_text):
        json_request = copy.deepcopy(parcel_insurance_limit_json)
        json_request['senderCity'] = nonexistent_cities[0]
        json_request['receiverCities'][0] = nonexistent_cities[1]

        with allure.step('Выполнить POST /parcels/insurance/limit'):
            client = ParcelsInsuranceLimit()
            response = client.get_insurance_limit(json=json_request, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_insurance_limit_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_error_text = response.json()['data']['errors'][0]['description']
            assert expect_error_text == actual_error_text, f'Ожидался текст ошибки {expect_error_text}, \
             получен {actual_error_text}'
