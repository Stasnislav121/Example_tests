import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestStocks:
    @testit.workItemIds(35871)
    @testit.externalId('TestStocks_35871')
    @testit.displayName('[200] GET /stocks - получение списка неперсональных акций')
    @testit.nameSpace('API')
    @testit.className('Stocks')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Stocks')
    @allure.title('[200] GET /stocks - получение списка неперсональных акций')
    @allure.testcase(url='https://testit..ru/browse/35871')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_non_personal_stocks(self, request, get_token):
        token = request.getfixturevalue(get_token)
        data = copy.deepcopy(stock_request_json)
        random_int = random.randint(1000, 9999)
        data['hash'] = f'7b08edf3-55d8-{random_int}-90f5-350ce33d4d43'
        data['int_id'] = random_int
        data['title'] = StringHelper().get_random_ru_string()
        StocksHelper.insert_stock(data)
        expect_stocks = StocksHelper.get_stocks()

        with allure.step('Выполнить GET /stocks'):
            client = StocksApi()
            response = client.get_stocks(token=token)
            request.addfinalizer(lambda: StocksHelper.delete_stock(param='int_id', value=data['int_id']))

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, stocks_schema)

        with allure.step('Проверка параметров ответа'):
            stocks_resp = response.json()['data']['items']
            stock_resp = StocksHelper.get_obj_for_key_in_list(list_obj=stocks_resp, key='title', value=data['title'])

            assert len(stocks_resp) == len(expect_stocks), 'Количество записей не равно'
            assert stock_resp['id'] == data['hash'], f"Ожидалось {data['hash']}, получено {stock_resp['id']}"
            assert stock_resp['title'] == data['title'], f"Ожидалоcь {data['title']}, получено {stock_resp['title']}"
            assert stock_resp['description'] == data['image_text'], \
                f"Ожидалось {data['image_text']}, получено {stock_resp['description']}"
            assert stock_resp['image'] == data['mobile_img'], \
                f"Ожидалось {data['mobile_img']}, получено {stock_resp['image']}"

    @testit.workItemIds(35872)
    @testit.externalId('TestStocks_35872')
    @testit.displayName('[200] GET /stocks/id - получение детальной информации об акции')
    @testit.nameSpace('API')
    @testit.className('Stocks')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Stocks')
    @allure.title('[200] GET /stocks/id - получение детальной информации об акции')
    @allure.testcase(url='https://testit..ru/browse/35872')
    def test_get_info_about_non_personal_stock(self, request, with_auth):
        token = with_auth
        data = copy.deepcopy(stock_request_json)
        random_int = random.randint(1000, 9999)
        data['hash'] = f'7b08edf3-55d8-{random_int}-90f5-350ce33d4d43'
        data['int_id'] = random_int
        data['title'] = StringHelper().get_random_ru_string()
        expect_discount = f"-{data['discount']}%"
        expect_expiration_date = DateHelper().format_date(date=data['expiration_date'],
                                                          current_format="%Y-%m-%d %H:%M:%S",
                                                          required_format="%Y-%m-%dT%H:%M:%S") + "+0300"

        StocksHelper.insert_stock(data)
        expect_stocks = StocksHelper.get_stock_by_param(param='int_id', value=data['int_id'])
        assert len(expect_stocks) > 0, f'Ожидалось количество акций в БД > 0, получено {len(expect_stocks)}'

        with allure.step(f'Выполнить GET /stocks/{data["hash"]}'):
            client = StocksApi()
            response = client.get_stock_by_id(token=token, id=data["hash"])
            request.addfinalizer(lambda: StocksHelper.delete_stock(param='int_id', value=data['int_id']))

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, stock_schema)

        with allure.step('Проверка параметров ответа'):
            stock_resp = response.json()['data']

            assert stock_resp['id'] == data['hash'], f"Ожидалось {data['hash']}, получено {stock_resp['id']}"
            assert stock_resp['title'] == data['title'], f"Ожидалось {data['title']}, получено {stock_resp['title']}"
            assert stock_resp['description'] == data['description'], \
                f"Ожидалось {data['description']}, получено {stock_resp['description']}"
            assert stock_resp['image'] == data['mobile_img'], \
                f"Ожидалось {data['mobile_img']}, получено {stock_resp['image']}"
            assert stock_resp['expirationDate'] == expect_expiration_date, \
                f"Ожидалось {expect_expiration_date}, получено {stock_resp['expirationDate']}"
            assert stock_resp['promocode'] == data['promocode'], \
                f"Ожидалось {data['promocode']}, получено {stock_resp['promocode']}"
            assert stock_resp['discount'] == expect_discount, \
                f"Ожидалось {expect_discount}, получено {stock_resp['discount']}"
            assert stock_resp['imageText'] == data['image_text'], \
                f"Ожидалось {data['image_text']}, получено {stock_resp['imageText']}"

    @testit.workItemIds(35953)
    @testit.externalId('TestStocks_35953')
    @testit.displayName('[200] GET /stocks - отсутствие персональной акции в списке неперсональных акций')
    @testit.nameSpace('API')
    @testit.className('Stocks')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Stocks')
    @allure.title('[200] GET /stocks - отсутствие персональной акции в списке неперсональных акций')
    @allure.testcase(url='https://testit..ru/browse/35953')
    @pytest.mark.usefixtures('add_random_non_personal_stock')
    def test_absence_personal_stock_in_stocks_list(self, request):
        expect_stocks = StocksHelper.get_stocks()
        assert len(expect_stocks) > 0, (f'Ожидалось количество неперсональных акций в БД > 0, получено'
                                        f' {len(expect_stocks)}')

        data = copy.deepcopy(stock_request_json)
        random_int = random.randint(1000, 9999)
        data['hash'] = f'7b08edf3-55d8-{random_int}-90f5-350ce33d4d43'
        data['int_id'] = random_int
        data['personal_url'] = '123'
        data['title'] = StringHelper().get_random_ru_string()
        StocksHelper.insert_stock(data)

        with allure.step('Выполнить GET /stocks'):
            client = StocksApi()
            response = client.get_stocks()
            request.addfinalizer(lambda: StocksHelper.delete_stock(param='int_id', value=data['int_id']))

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, stocks_schema)

        with allure.step('Проверка параметров ответа'):
            stocks_resp = response.json()['data']['items']
            stocks_list_resp = StocksHelper.get_list_for_key_in_obj(list_obj=stocks_resp, key='title')
            assert data['title'] not in stocks_list_resp, \
                f"Ожидалось отсутствие {data['title']} в {stocks_list_resp}, получено {stocks_list_resp}"

    @testit.workItemIds(35873)
    @testit.externalId('TestStocks_35873')
    @testit.displayName('[403] GET /stocks/id - попытка получения детальной информации об несуществующей акции')
    @testit.nameSpace('API')
    @testit.className('Stocks')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Stocks')
    @allure.title('[403] GET /stocks/id - попытка получения детальной информации об несуществующей акции')
    @allure.testcase(url='https://testit..ru/browse/35873')
    def test_attempt_get_info_about_non_existent_non_personal_stock(self):
        hash = 'a81eeb63-9123-9999-9999-a578d81adda8'
        error_text = 'Упс...акция уже завершилась'

        with allure.step(f'Выполнить GET /stocks/{hash}'):
            client = StocksApi()
            response = client.get_stock_by_id(id=hash, check_error=False)
            ResponseHandler.check_response_code_is_403(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, stock_schema_err)

        with allure.step('Проверка параметров ответа'):
            stock_resp = response.json()
            assert stock_resp['name'] == error_text, f"Ожидалось {error_text}, получено {stock_resp['name']}"
