import allure
import testit
from library.mobapp import *


class TestPagesDocuments:
    @testit.workItemIds(40719)
    @testit.externalId('TestPagesDocuments_40719')
    @testit.displayName('[200] GET  /pages/documents - получение ссылок на документы')
    @testit.nameSpace('API')
    @testit.className('Pages')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Pages')
    @allure.title('[200] GET  /pages/documents - получение ссылок на документы')
    @allure.testcase(url='https://testit..ru/browse/40719')
    def test_get_pages(self, request):
        with allure.step('Получить список документов из таблицы "FAQ" с признаком "show_in_profile=1"'):
            pages_helper = PagesHelper()
            data = {'title': StringHelper().get_random_ru_string(),
                    'link': 'https://mobile..ru/html/?id=999',
                    'sort_priority': 999,
                    'text': 'abcd',
                    'page_id': 999,
                    'show_on_profile': 1}
            pages_helper.add_pages_documents_in_db(data=data)
            request.addfinalizer(lambda: pages_helper.delete_pages_documents_in_db(data=data))
            expect_documents_data = pages_helper.get_pages_documents_from_db()
            assert len(expect_documents_data) > 0, (f'Ожидалось количество документов в таблице "FAQ" > 0,'
                                                    f' {len(expect_documents_data)}')

        with allure.step('Выполнить GET /pages/documents'):
            client = PagesDocumentsApi()
            response = client.get_documents()

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, page_documents_schema)

        with allure.step('Проверка параметров ответа'):
            actual_documents_data = response.json()['data']['items']
            assert expect_documents_data == actual_documents_data, f'Ожидалось равенство с {expect_documents_data}, \
             получено {actual_documents_data}'
