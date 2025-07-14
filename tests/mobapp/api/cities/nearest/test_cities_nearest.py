import pytest
import allure
import testit
from library.mobapp import *


class TestCitiesNearest:
    @testit.workItemIds(17734)
    @testit.externalId('TestCities_17734')
    @testit.displayName('[200] GET /cities/nearest - получение ближайшего города по координатам')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities/nearest')
    @allure.title('[200] GET /cities/nearest - получение ближайшего города по координатам')
    @allure.testcase(url='https://testit..ru/browse/17734')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_city_nearest_by_coordinates(self, array_helper, request, get_token):
        expect_city = {
            "code": "02429",
            "title": "Жуков (Калужская обл)",
            "latitude": 55.030627,
            "longitude": 36.747895
        }
        lat = '55.0000'
        lng = '37.0000'

        token = request.getfixturevalue(get_token)

        with allure.step(f'Выполнить GET /cities/nearest?lat={lat}&lng={lng}'):
            client = CitiesApi()
            response = client.get_cities_nearest(token=token, lat=lat, lng=lng)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_nearest_schema)

        with allure.step('Проверка параметров ответа'):
            city_resp = response.json()['data']

            array_helper.assert_arrays(arr=city_resp, expected_arr=expect_city)

    @testit.workItemIds(35575)
    @testit.externalId('TestCities_35575')
    @testit.displayName('[422] GET /cities/nearest - получение ошибки при отсутствии параметра "lat"')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities/nearest')
    @allure.title('[422] GET /cities/nearest - получение ошибки при отсутствии параметра "lat"')
    @allure.testcase(url='https://testit..ru/browse/35575')
    def test_get_city_nearest_by_coordinates_without_lat(self):
        lng = '37.0000'
        error_field = 'lat'
        error_description = 'Параметр отсутствует или не заполнен'

        with allure.step(f'Выполнить GET /cities/nearest?lng={lng}'):
            client = CitiesApi()
            response = client.get_cities_nearest(lng=lng, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_nearest_schema_err)

        with allure.step('Проверка параметров ответа'):
            error_arr_resp = response.json()['data']['errors'][0]
            error_field_resp = error_arr_resp['field']
            error_description_resp = error_arr_resp['description']

        assert error_field == error_field_resp, f"Ожидалось {error_field}, получено {error_field_resp}"
        assert error_description == error_description_resp, (f"Ожидалось {error_description}, "
                                                             f" получено {error_description_resp}")

    @testit.workItemIds(35576)
    @testit.externalId('TestCities_35576')
    @testit.displayName('[422] GET /cities/nearest - получение ошибки при отсутствии параметра "lng"')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities/nearest')
    @allure.title('[422] GET /cities/nearest - получение ошибки при отсутствии параметра "lng"')
    @allure.testcase(url='https://testit..ru/browse/35576')
    def test_get_city_nearest_by_coordinates_without_lng(self):
        lat = '55.0000'
        error_field = 'lng'
        error_description = 'Параметр отсутствует или не заполнен'

        with allure.step(f'Выполнить GET /cities/nearest?lat={lat}'):
            client = CitiesApi()
            response = client.get_cities_nearest(lat=lat, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_nearest_schema_err)

        with allure.step('Проверка параметров ответа'):
            error_arr_resp = response.json()['data']['errors'][0]
            error_field_resp = error_arr_resp['field']
            error_description_resp = error_arr_resp['description']

        assert error_field == error_field_resp, f"Ожидалось {error_field}, получено {error_field_resp}"
        assert error_description == error_description_resp, (f"Ожидалось {error_description},"
                                                             f" получено {error_description_resp}")
