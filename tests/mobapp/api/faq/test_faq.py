import allure
import testit
from library.mobapp import *


class TestFaq:
    @testit.workItemIds(37302)
    @testit.externalId('TestFaq_37302')
    @testit.displayName('[200] GET /faq - получение cписка наиболее часто задаваемых вопросов')
    @testit.nameSpace('API')
    @testit.className('FAQ')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: FAQ')
    @allure.title('[200] GET /faq - получение cписка наиболее часто задаваемых вопросов')
    @allure.testcase(url='https://testit..ru/browse/37302')
    def test_get_faq(self):
        expect_faq_data = {
            "link": "https://mobapp-predprod.task..ru/html/?id=200"
        }

        with allure.step('Выполнить GET /faq'):
            client = FaqApi()
            response = client.get_faq()

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, faq_schema)

        with allure.step('Проверка параметров ответа'):
            actual_faq_data = response.json()['data']
            assert expect_faq_data == actual_faq_data, f'Ожидалось равенство с {expect_faq_data}, \
             получено {actual_faq_data}'
