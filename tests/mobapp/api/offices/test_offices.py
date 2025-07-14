import pytest
import allure
import testit
from library.mobapp import *


class TestOffices:
    @testit.workItemIds(17720)
    @testit.externalId('TestOffices_17720')
    @testit.displayName('[200] GET /offices/id - получение детальной информации об отделении')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[200] GET /offices/id - получение детальной информации об отделении')
    @allure.testcase(url='https://testit..ru/browse/17720')
    def test_get_info_about_office_by_code(self):
        code = '00726'

        expect_office = OfficesHelper.get_office_info_by_code_office(code=code)
        expect_office_id = expect_office[0]['code']
        expect_address = expect_office[0]['address']
        expect_country = expect_office[0]['country']
        expect_city_code = expect_office[0]['city_code']
        expect_city_title = 'Москва'
        expect_latitude = expect_office[0]['latitude']
        expect_longitude = expect_office[0]['longitude']

        with allure.step(f'Выполнить GET /offices/{code}'):
            client = OfficesApi()
            response = client.get_information_about_office(code=code)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, info_office_schema)

        with allure.step('Проверка параметров ответа'):
            office = response.json()['data']
            office_id_resp = office['id']
            office_address_resp = office['address']['address']
            office_country_resp = office['address']['country']
            office_city_code_resp = office['address']['city']['code']
            office_city_title_resp = office['address']['city']['title']
            office_latitude_resp = office['address']['latitude']
            office_longitude_resp = office['address']['longitude']

            assert expect_office_id == office_id_resp, f'Ожидалось {expect_office_id}, получено {office_id_resp}'
            assert expect_address == office_address_resp, f'Ожидалось {expect_address}, получено {office_address_resp}'
            assert expect_country == office_country_resp, f'Ожидалось {expect_country}, получено {office_country_resp}'
            assert expect_city_code == office_city_code_resp, \
                f'Ожидалось {expect_city_code}, получено {office_city_code_resp}'
            assert expect_city_title == office_city_title_resp, \
                f'Ожидалось {expect_city_title}, получено {office_city_title_resp}'
            assert expect_latitude == office_latitude_resp, \
                f'Ожидалось {expect_latitude}, получено {office_latitude_resp}'
            assert expect_longitude == office_longitude_resp, \
                f'Ожидалось {expect_longitude}, получено {office_longitude_resp}'

    @testit.workItemIds(17728)
    @testit.externalId('TestOffices_17728')
    @testit.displayName('[200] GET /offices?cityCode - получение списка отделений по коду города')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[200] GET /offices?cityCode - получение списка отделений по коду города')
    @allure.testcase(url='https://testit..ru/browse/17728')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_offices_by_city_code(self, request, get_token):
        city_code = '16'
        token = request.getfixturevalue(get_token)

        expect_offices = OfficesHelper.get_offices_by_city(city_code=city_code)
        expect_len_offices = len(expect_offices)
        expect_office_id = expect_offices[1]['code']
        expect_latitude = expect_offices[1]['latitude']
        expect_longitude = expect_offices[1]['longitude']
        expect_availability = ['sending', 'receiving']

        with allure.step(f'Выполнить GET /offices?cityCode={city_code}'):
            client = OfficesApi()
            response = client.get_offices_by_city_code(token=token, city_code=city_code, offset='0', limit='999')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, offices_schema)

        with allure.step('Проверка параметров ответа'):
            office_data = response.json()['data']
            office_items = office_data['items']
            offices_len_resp = len(office_items)
            office_id_resp = office_items[1]['id']
            office_latitude_resp = office_items[1]['latitude']
            office_longitude_resp = office_items[1]['longitude']
            office_availability_resp = office_items[1]['availability']
            office_total_resp = office_data['total']

            assert expect_len_offices == offices_len_resp, 'Количество записей неравны'
            assert expect_office_id == office_id_resp, f'Ожидалось {expect_office_id}, получено {office_id_resp}'
            assert expect_latitude == office_latitude_resp, \
                f'Ожидалось {expect_latitude}, получено {office_latitude_resp}'
            assert expect_longitude == office_longitude_resp, \
                f'Ожидалось {expect_longitude}, получено {office_longitude_resp}'
            assert expect_availability == office_availability_resp, \
                f'Ожидалось {expect_availability}, получено {office_availability_resp}'
            assert expect_len_offices == office_total_resp, (f'Ожидалось "total: {expect_len_offices}", '
                                                             f' получено {office_total_resp}')

    @testit.workItemIds(35379)
    @testit.externalId('TestOffices_35379')
    @testit.displayName('[200] GET /offices?cityCode - получение списка отделений по несуществующему коду города')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[200] GET /offices?cityCode - получение списка отделений по несуществующему коду города')
    @allure.testcase(url='https://testit..ru/browse/35379')
    def test_get_offices_by_nonexistent_city_code(self):
        city_code = '999999'

        expect_offices = OfficesHelper.get_offices_by_city(city_code=city_code)
        assert expect_offices == [], 'Массив не пустой'

        with allure.step(f'Выполнить GET /offices?cityCode={city_code}'):
            client = OfficesApi()
            response = client.get_offices_by_city_code(city_code=city_code, offset='0', limit='999')

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, offices_empty_schema)

        with allure.step('Проверка параметров ответа'):
            office_data = response.json()['data']
            office_items = office_data['items']
            office_total_resp = office_data['total']

            assert office_items == [], f'Ожидался пустой массив, получено {offices}'
            assert office_total_resp == 0, f'Ожидалось "total: 0", получено {office_total_resp}'

    @testit.workItemIds(17727)
    @testit.externalId('TestOffices_17727')
    @testit.displayName('[201] GET /offices/search - поиск отделений по адресу')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[201] GET /offices/search - поиск отделений по адресу')
    @allure.testcase(url='https://testit..ru/browse/17727')
    def test_get_offices_with_search(self):
        search_request = 'баж'

        expect_offices = OfficesHelper.get_offices_by_address(address=search_request)
        expect_len_offices = len(expect_offices)
        expect_country = expect_offices[0]['country']
        expect_city_code = expect_offices[0]['city_code']
        expect_city_title = CitiesHelper.get_city_by_code(code=expect_city_code)[0]['title']
        expect_address = expect_offices[0]['address']
        expect_latitude = expect_offices[0]['latitude']
        expect_longitude = expect_offices[0]['longitude']
        expect_is_available_for_courier = bool(expect_offices[0]['address_kd'])

        with allure.step(f'Выполнить GET /offices/search?search={search_request}'):
            client = OfficesApi()
            response = client.search_offices(search=search_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, offices_search_schema)

        with allure.step('Проверка параметров ответа'):
            offices_data = response.json()['data']
            offices_len_resp = len(offices_data)
            office_country_resp = offices_data[0]['country']
            office_city_code_resp = offices_data[0]['city']['code']
            office_city_title_resp = offices_data[0]['city']['title']
            office_address_resp = offices_data[0]['address']
            office_latitude_resp = offices_data[0]['latitude']
            office_longitude_resp = offices_data[0]['longitude']
            office_is_available_for_courier_resp = offices_data[0]['isAvailableForCourier']

            assert expect_len_offices == offices_len_resp, 'Количество записей неравны'
            assert expect_country == office_country_resp, \
                f'Ожидалось {expect_country}, получено {office_country_resp}'
            assert expect_city_code == office_city_code_resp, \
                f'Ожидалось {expect_city_code}, получено {office_city_code_resp}'
            assert expect_city_title == office_city_title_resp, \
                f'Ожидалось {expect_city_title}, получено {office_city_title_resp}'
            assert expect_address == office_address_resp, \
                f'Ожидалось {expect_address}, получено {office_address_resp}'
            assert expect_latitude == office_latitude_resp, \
                f'Ожидалось {expect_latitude}, получено {office_latitude_resp}'
            assert expect_longitude == office_longitude_resp, \
                f'Ожидалось {expect_longitude}, получено {office_longitude_resp}'
            assert expect_is_available_for_courier == office_is_available_for_courier_resp, \
                f'Ожидалось {expect_is_available_for_courier}, получено {office_is_available_for_courier_resp}'

    @testit.workItemIds(17724)
    @testit.externalId('TestOffices_17724')
    @testit.displayName('[200] GET /offices/filters - получение списка фильтров для отделений')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[200] GET /offices/filters - получение списка фильтров для отделений')
    @allure.testcase(url='https://testit..ru/browse/17724')
    def test_get_offices_filters(self):
        with allure.step('Выполнить GET /offices/filters'):
            client = OfficesApi()
            response = client.get_offices_filters()

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, office_filters_schema)

    @testit.workItemIds(41524)
    @testit.externalId('TestOffices_41524')
    @testit.displayName('[200] GET /offices/search - поиск отделений по номеру ПВЗ')
    @testit.nameSpace('API')
    @testit.className('Offices')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Offices')
    @allure.title('[200] GET /offices/search - поиск отделений по номеру ПВЗ')
    @allure.testcase(url='https://testit..ru/browse/41524')
    def test_get_offices_by_office_code(self):
        office_code = '02032'

        with allure.step(f'Получить данные по отделению с кодом {office_code} из таблицы "offices"'):
            expect_offices = OfficesHelper().get_offices_by_code_from_db(code=office_code)
            assert expect_offices, f'Данные по отделению {office_code} отсутствуют в БД'
            expect_offices = expect_offices[0]

            expect_office = {
                'postcode': expect_offices['postcode'],
                'country': expect_offices['country'],
                'city': {
                    'code': expect_offices['city_code'],
                    'title': expect_offices['title'],
                    'latitude': expect_offices['city_latitude'],
                    'longitude': expect_offices['city_longitude']
                },
                'address': expect_offices['address'],
                'latitude': expect_offices['latitude'],
                'longitude': expect_offices['longitude'],
                'isAvailableForCourier': expect_offices['address_kd']
        }

        with allure.step(f'Выполнить GET /offices/search?search={office_code}'):
            client = OfficesApi()
            response = client.search_offices(search=office_code)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, offices_search_schema)

        with allure.step('Проверка параметров ответа'):
            actual_office = response.json()['data'][0]

            assert expect_office == actual_office, (f'Ожидалось равенство отделения с {expect_office}, получено'
                                                    f' {actual_office}')
