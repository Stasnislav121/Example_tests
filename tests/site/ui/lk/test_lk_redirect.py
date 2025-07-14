import testit
import allure

from library.site.ui.pages import *


class TestLkRedirect:
    @testit.workItemIds(14904)
    @testit.externalId('TestLkRedirect_14904')
    @testit.nameSpace('Общее')
    @testit.className('Личный кабинет')
    @testit.displayName('Переход по кнопкам')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Личный кабинет')
    @allure.title('Личный кабинет - Переход по кнопкам')
    @allure.testcase(url='https://testit..ru/browse/14904')
    def test_lk_redirect_by_buttons(self, site_main_page):
        menu_lk = site_main_page.menu_lk()

        with allure.step('Нажать по кнопке "Для частных клиентов"'):
            new_page = menu_lk.open_for_private_clients()
            page_url = new_page.get_current_url()
            assert page_url == 'https://lk..ru/auth/?redirectTo=%2F'

        with allure.step('Нажать по кнопке "Мобильное приложение"'):
            new_page = menu_lk.open_mobile_app()
            page_url = new_page.get_current_url()
            if new_page.is_mobile:
                assert page_url == 'https://mobile..ru/qr/?utm_source=mobile_app&utm_medium=special&' \
                                   'utm_campaign=site&utm_term=verhnee_menu'
            else:
                assert page_url == 'https://.ru/castnym-klientam/dostavka/mobil-noe-prilozenie?' \
                                   'utm_source=mobile_app&utm_medium=special&utm_campaign=site&utm_term=verhnee_menu'

        with allure.step('Нажать по кнопке "Для Интернет-магазинов"'):
            new_page = menu_lk.open_for_online_store()
            page_url = new_page.get_current_url()
            assert page_url == 'https://account..ru/'
