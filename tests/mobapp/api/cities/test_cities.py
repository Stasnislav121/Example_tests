import pytest
import allure
import testit
from library.mobapp import *


class TestCities:
    @testit.workItemIds(17735)
    @testit.externalId('TestCities_17735')
    @testit.displayName('[200] GET /cities - получение списка городов')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities')
    @allure.title('[200] GET /cities - получение списка городов')
    @allure.testcase(url='https://testit..ru/browse/17735')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_cities(self, array_helper, request, get_token):
        expect_city = {
                "code": "68",
                "title": "Москва",
                "latitude": 55.755864,
                "longitude": 37.617698
        }

        expect_cities = CitiesHelper.get_cities_by_country()
        assert len(expect_cities) > 0, f'Ожидалось количество городов больше 0, получено {len(expect_cities)}'

        token = request.getfixturevalue(get_token)

        with allure.step('Выполнить GET /cities'):
            client = CitiesApi()
            response = client.get_cities(token=token, limit='99999')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_schema)

        with allure.step('Проверка параметров ответа'):
            cities_resp = response.json()['data']['items']
            city_resp = cities_resp[0]

            array_helper.assert_arrays(expect_city, city_resp)
            assert len(expect_cities) == len(cities_resp), \
                f'Ожидалось равное количество городов, получено {len(cities_resp)}'

    @testit.workItemIds(35574)
    @testit.externalId('TestCities_35574')
    @testit.displayName('[200] GET /cities - с limit и offset')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities')
    @allure.title('[200] GET /cities - с limit и offset')
    @allure.testcase(url='https://testit..ru/browse/35574')
    def test_get_cities_with_limit_and_offset(self, array_helper):
        expect_city = {
                "code": "116",
                "title": "Санкт-Петербург",
                "latitude": 59.938784,
                "longitude": 30.314997
        }
        expect_len = 1
        limit = '1'
        offset = '1'

        with allure.step(f'Выполнить GET /cities?offset={offset}&limit={limit}'):
            client = CitiesApi()
            response = client.get_cities(limit=limit, offset=offset)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_schema)

        with allure.step('Проверка параметров ответа'):
            cities_resp = response.json()['data']['items']
            city_resp = cities_resp[0]

            array_helper.assert_arrays(expect_city, city_resp)
            assert expect_len == len(cities_resp), \
                f'Ожидалось количество городов = {expect_len}, получено {len(cities_resp)}'

    @testit.workItemIds(35573)
    @testit.externalId('TestCities_35573')
    @testit.displayName('[200] GET /cities?countryCode=BLR&search= - поиск города по стране')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities')
    @allure.title('[200] GET /cities?countryCode=BLR&search= - поиск города по стране')
    @allure.testcase(url='https://testit..ru/browse/35573')
    def test_get_cities_with_search_from_country(self, array_helper):
        expect_city = {
                "code": "Н00163822",
                "title": "Минск",
                "latitude": 53.902284,
                "longitude": 27.561831
        }
        expect_len = 1
        country_code = 'BLR'
        search_value = 'Мин'

        with allure.step(f'Выполнить GET /cities?countryCode={country_code}&search={search_value}'):
            client = CitiesApi()
            response = client.get_cities(country_code=country_code, search=search_value)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_schema)

        with allure.step('Проверка параметров ответа'):
            cities_resp = response.json()['data']['items']
            city_resp = cities_resp[0]

            array_helper.assert_arrays(expect_city, city_resp)
            assert expect_len == len(cities_resp), \
                f'Ожидалось количество городов = {expect_len}, получено {len(cities_resp)}'

    @testit.workItemIds(35572)
    @testit.externalId('TestCities_35572')
    @testit.displayName('[200] GET /cities?search - поиск города по всем странам')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities')
    @allure.title('[200] GET /cities?search - поиск города по всем странам')
    @allure.testcase(url='https://testit..ru/browse/35572')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_cities_with_search_from_all_countries(self, array_helper, request, get_token):
        expect_city = {
                "code": "68",
                "title": "Москва",
                "latitude": 55.755864,
                "longitude": 37.617698
        }
        search_value = 'Моск'

        expect_cities = CitiesHelper.get_city_by_title(title=search_value)
        assert len(expect_cities) > 0, f'Ожидалось количество городов больше 0, получено {len(expect_cities)}'

        token = request.getfixturevalue(get_token)

        with allure.step(f'Выполнить GET /cities?search={search_value}'):
            client = CitiesApi()
            response = client.get_cities(token=token, search=search_value)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_schema)

        with allure.step('Проверка параметров ответа'):
            cities_resp = response.json()['data']['items']
            city_resp = cities_resp[0]

            array_helper.assert_arrays(expect_city, city_resp)
            assert len(expect_cities) == len(cities_resp), \
                f'Ожидалось равное количество городов, получено {len(cities_resp)}'
