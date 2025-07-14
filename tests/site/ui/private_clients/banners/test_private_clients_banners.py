import testit
import allure

from library.site.ui.pages import *


class TestPrivateClientsBanner:
    @testit.workItemIds(12941)
    @testit.externalId('TestPrivateClients_12941')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Баннеры')
    @testit.displayName('Ручная смена банера')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Частным клиентам')
    @allure.title('Частным клиентам - Ручная смена банера')
    @allure.testcase(url='https://testit..ru/browse/12941')
    def test_private_clients_banner_manual_change(self, site_main_page):
        block_banner = site_main_page.block_banner()

        with allure.step('Дождаться доступности ручного переключения банера'):
            banner = block_banner.wait_for_timeout(10)

        with allure.step('Переключить на первый банер'):
            num_before = banner.click_while_change_blocked(1).get_active_banner_number()

        with allure.step('Получить заголовок первого банера'):
            title_before = banner.get_active_banner_title()

        with allure.step('Переключить на третий банер'):
            num_after = banner.click_while_change_blocked(3).get_active_banner_number()

        with allure.step('Получить заголовок третьего банера'):
            title_after = banner.get_active_banner_title()

        with allure.step('Проверить успешность переключения'):
            assert num_before != num_after, \
                f'Номер баннера до переключения ({num_before}) не должен быть = номеру после переключения ({num_after})'
            assert title_before != title_after, \
                f'Заголовок баннера до переключения ({title_before}) не должен быть = номеру после переключения ' \
                f'({title_after})'

    @testit.workItemIds(39278)
    @testit.externalId('TestPrivateClients_39278')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Страница /find_an_office')
    @testit.displayName('Переход на страницу выбора подарка из банера со страницы /find_an_office')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Страница /find_an_office')
    @allure.title('Переход на страницу выбора подарка из банера со страницы /find_an_office')
    @allure.testcase(url='https://testit..ru/browse/39278')
    def test_go_to_gift_page_from_banner_inside_find_an_office_page(self, site_find_an_office):
        expect_url = 'https://get4click.ru/'

        with allure.step('В банере "Выберите подарок от нашего партнера" нажать на "Выбрать подарок"'):
            actual_url = site_find_an_office.check_gift_banner() \
                .go_to_gift_page()

            assert expect_url in actual_url, f'Ожидался {expect_url}, получен {actual_url}'
