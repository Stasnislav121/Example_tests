import os

import testit
import allure


class TestOpenTerminalPage:
    @testit.workItemIds(12578)
    @testit.externalId('TestBusinessPartners_12578')
    @testit.nameSpace('Бизнес-партнерам')
    @testit.className('Открыть терминал')
    @testit.displayName('Загрузка файла "оферты"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Бизнес-партнерам')
    @allure.title('Открыть терминал - Загрузка файла "оферты"')
    @allure.testcase(url='https://testit..ru/browse/12578')
    def test_open_terminal_download_offer(self, site_business_partners_open_terminal, request):
        open_terminal_page = site_business_partners_open_terminal

        file = open_terminal_page.download_offer()
        file_name = os.path.basename(file)
        request.addfinalizer(lambda: os.remove(file))
        assert 'Oferta_dlya_terminalov' in file_name, 'Проверка названия файла'
        assert file_name.endswith('.pdf'), 'Проверка, что разрешение файла == pdf'
