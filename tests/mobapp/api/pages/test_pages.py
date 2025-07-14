import pytest
import allure
import testit
from library.mobapp import *


class TestPages:
    @testit.workItemIds(17719)
    @testit.externalId('TestPages_17719')
    @testit.displayName('[200] GET /pages/:page - получение ссылки на информационную страницу')
    @testit.nameSpace('API')
    @testit.className('Pages')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Pages')
    @allure.title('[200] GET /pages/:page - получение ссылки на информационную страницу')
    @allure.testcase(url='https://testit..ru/browse/17719')
    @pytest.mark.parametrize(('page_name', 'page_id'), [('about', 100), ('personalDataAgreement', 101),
                                                        ('userAgreement', 102), ('faq', 200),
                                                        ('personalDataExtended', 103), ('interRefundsAsos', 106)])
    def test_get_pages(self, page_name, page_id):
        expect_page_data = {
            "link": f"https://mobile..ru/html/?id={page_id}"
        }

        with allure.step(f'Выполнить GET /pages/{page_name}'):
            client = PagesApi()
            response = client.get_pages(page_name=page_name)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, page_schema)

        with allure.step('Проверка параметров ответа'):
            actual_page_data = response.json()['data']
            assert expect_page_data == actual_page_data, f'Ожидалось равенство с {expect_page_data}, \
             получено {actual_page_data}'

    @testit.workItemIds(37431)
    @testit.externalId('TestPages_37431')
    @testit.displayName('[422] GET /pages/:page - '
                        ' получение ошибки при запросе ссылки на несуществующую информационную страницу')
    @testit.nameSpace('API')
    @testit.className('Pages')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Pages')
    @allure.title('[422] GET /pages/:page - '
                  ' получение ошибки при запросе ссылки на несуществующую информационную страницу')
    @allure.testcase(url='https://testit..ru/browse/37431')
    def test_get_nonexistent_page(self):
        nonexistent_page = 'abcd'
        expect_err_data = {
            'field': 'page',
            'description': 'Указанная страница не найдена'
        }

        with allure.step(f'Выполнить GET /pages/{nonexistent_page}'):
            client = PagesApi()
            response = client.get_pages(page_name=nonexistent_page, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, page_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_err_data = response.json()['data']['errors'][0]
            assert expect_err_data == actual_err_data, f'Ожидалось равенство с {expect_err_data}, \
                 получено {actual_err_data}'
