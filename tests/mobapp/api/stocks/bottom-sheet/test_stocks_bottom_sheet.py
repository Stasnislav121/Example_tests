import allure
import testit
import copy

from library.mobapp import *


class TestStocks:
    @testit.workItemIds(40467)
    @testit.externalId('TestStocks_40467')
    @testit.displayName('[200] GET /stocks/bottom-sheet - получение информации для нижних шторок')
    @testit.nameSpace('API')
    @testit.className('Stocks')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Stocks')
    @allure.title('[200] GET /stocks/bottom-sheet - получение информации для нижних шторок')
    @allure.testcase(url='https://testit..ru/browse/40467')
    def test_get_stock_for_bottom_sheet(self, request):
        with allure.step('Добавить акцию в таблицу "Stocks"'):
            data = copy.deepcopy(stock_request_json)
            random_int = random.randint(1000, 9999)
            data['hash'] = f'7b08edf3-55d8-{random_int}-90f5-350ce33d4d43'
            data['int_id'] = random_int
            data['title'] = StringHelper().get_random_ru_string()
            data['show_on_main'] = 1
            data['expiration_date'] = CommonHelper.get_future_time(hours=1)
            data['show_interval_days'] = 13
            StocksHelper.insert_stock(data)

        expect_link = f'https://lk..ru/stocks/{data["hash"]}'
        expect_button = 'Подробнее'

        with allure.step('Выполнить GET /stocks/bottom-sheet'):
            client = StocksBottomSheetApi()
            response = client.get_stock_for_bottom_sheet()
            request.addfinalizer(lambda: StocksHelper.delete_stock(param='int_id', value=data['int_id']))

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, stock_for_bottom_sheet_schema)

        with allure.step('Проверка параметров ответа'):
            stock_resp = response.json()['data']

            assert stock_resp['id'] == data['hash'], f"Ожидалось {data['hash']}, получено {stock_resp['id']}"
            assert stock_resp['image'] == data['mobile_img'], \
                f"Ожидалось {data['mobile_img']}, получено {stock_resp['image']}"
            assert stock_resp['showIntervalDays'] == data['show_interval_days'], (
                f"Ожидалоcь {data['show_interval_days']}, получено {stock_resp['showIntervalDays']}")
            assert stock_resp['title'] == data['title'], f"Ожидалоcь {data['title']}, получено {stock_resp['title']}"
            assert stock_resp['description'] == data['description'], \
                f"Ожидалось {data['description']}, получено {stock_resp['description']}"
            assert stock_resp['button']['title'] == expect_button, (f"Ожидался текст 'button.title': {expect_button}, "
                                                                    f"получено {stock_resp['button']['title']}")
            assert stock_resp['button']['link'] == expect_link, (f"Ожидалась ссылка 'button.link': {expect_link}, "
                                                                 f"получено {stock_resp['button']['link']}")
