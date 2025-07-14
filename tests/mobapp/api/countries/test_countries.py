import allure
import testit
from library.mobapp import *


class TestCountries:
    @testit.workItemIds(34979)
    @testit.externalId('TestCountries_34979')
    @testit.displayName('[200] GET /countries?type=auth')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?type=auth')
    @allure.testcase(url='https://testit..ru/browse/34979')
    def test_get_countries_with_auth(self):
        expect_countries = CountriesHelper.get_countries_with_auth(param='title')
        expect_countries_title_list = CountriesHelper.get_list_countries(expect_countries, key='title')

        with allure.step('Выполнить GET /countries?type=auth'):
            client = CountriesApi()
            response = client.get_countries(type='auth')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries_title_list, countries_resp)

    @testit.workItemIds(34980)
    @testit.externalId('TestCountries_34980')
    @testit.displayName('[200] GET /countries?type=registration')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?type=registration')
    @allure.testcase(url='https://testit..ru/browse/34980')
    def test_get_countries_with_registration(self):
        expect_countries = CountriesHelper.get_countries_with_registration(param='title')
        expect_countries_title_list = CountriesHelper.get_list_countries(expect_countries, key='title')

        with allure.step('Выполнить GET /countries?type=registration'):
            client = CountriesApi()
            response = client.get_countries(type='registration')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries_title_list, countries_resp)

    @testit.workItemIds(34981)
    @testit.externalId('TestCountries_34981')
    @testit.displayName('[200] GET /countries?type=checkout')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?type=checkout')
    @allure.testcase(url='https://testit..ru/browse/34981')
    def test_get_countries_with_checkout(self):
        expect_countries = CountriesHelper.get_countries_with_checkout(param='title')
        expect_countries_title_list = CountriesHelper.get_list_countries(expect_countries, key='title')

        with allure.step('Выполнить GET /countries?type=checkout'):
            client = CountriesApi()
            response = client.get_countries(type='checkout', limit='2147483647')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries_title_list, countries_resp)

    @testit.workItemIds(34982)
    @testit.externalId('TestCountries_34982')
    @testit.displayName('[200] GET /countries?type=passport')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?type=passport')
    @allure.testcase(url='https://testit..ru/browse/34982')
    def test_get_countries_with_passport(self):
        expect_countries = CountriesHelper.get_countries_with_passport(param='title')
        expect_countries_title_list = CountriesHelper.get_list_countries(expect_countries, key='title')

        with allure.step('Выполнить GET /countries?type=passport'):
            client = CountriesApi()
            response = client.get_countries(type='checkout', limit='2147483647')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries_title_list, countries_resp)

    @testit.workItemIds(34984)
    @testit.externalId('TestCountries_34984')
    @testit.displayName('[200] GET /countries?type=checkout с limit=2&offset=1')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?type=checkout с limit=2&offset=1')
    @allure.testcase(url='https://testit..ru/browse/34984')
    def test_get_countries_with_limit_and_offset(self):
        expect_countries = ['Казахстан', 'Киргизия']

        with allure.step('Выполнить GET /countries?type=checkout с limit=2&offset=1'):
            client = CountriesApi()
            response = client.get_countries(type='checkout', limit='2', offset='1')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries, countries_resp)

    @testit.workItemIds(34985)
    @testit.externalId('TestCountries_34985')
    @testit.displayName('[200] GET /countries?search=')
    @testit.nameSpace('API')
    @testit.className('Countries')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Countries')
    @allure.title('[200] GET /countries?search=')
    @allure.testcase(url='https://testit..ru/browse/34985')
    def test_get_countries_with_search(self):
        expect_countries = ['Россия']

        with allure.step('Выполнить GET /countries?search=Рос'):
            client = CountriesApi()
            response = client.get_countries(search='Рос')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, countries_schema)

        with allure.step('Проверка параметров ответа'):
            countries_resp = response.json()['data']['countries']
            CountriesResponseHandler.check_countries_in_response(expect_countries, countries_resp)
