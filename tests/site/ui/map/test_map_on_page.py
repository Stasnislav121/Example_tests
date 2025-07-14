import pytest
import testit
import allure

from library.site.site_const import MAP_POINT_ADDRESS
from library.site.ui.pages import *


class TestMapOnPage:
    @testit.workItemIds(13622)
    @testit.externalId('TestPrivateClients_13622')
    @testit.nameSpace('Общее')
    @testit.className('Карта на страницах')
    @testit.displayName('Фильтры по отделениям')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Карта на страницах')
    @allure.title('Карта на страницах - Фильтры по отделениям')
    @allure.testcase(url='https://testit..ru/browse/13622')
    @pytest.mark.parametrize('page_to_check', [
        'Бизнесу',
        'Доставка в страны СНГ',
        'Пункты приема посылок от интернет-магазинов'])
    def test_map_on_page_filter_by_points(self, site_ecommerce_page, page_to_check):
        with allure.step(f'Открыть страницу "{page_to_check}"'):
            if page_to_check == 'Бизнесу':
                ecommerce_page = site_ecommerce_page
            elif page_to_check == 'Доставка в страны СНГ':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_delivery_to_cis()
            elif page_to_check == 'Пункты приема посылок от интернет-магазинов':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_acceptance_points()

        with allure.step('Выключить все тумблеры в фильтре'):
            block_map = ecommerce_page.block_map()
            if page_to_check != 'Бизнесу':
                ctl_filter = block_map.ctl_filter_ecommerce(filters_displayed=False)
            else:
                ctl_filter = block_map.ctl_filter_ecommerce(filters_displayed=True)
            ctl_filter.switch_all_filters()
            cnt = block_map.get_points_cnt()
            assert cnt == 0, 'На карте не должны отображаться отделения'

        with allure.step('Включить тумблер "Прием в отделении"'):
            ctl_filter.switch_point_reception_filter()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Выключить тумблер "Прием в отделении"'):
            ctl_filter.switch_point_reception_filter()
            cnt = block_map.get_points_cnt()
            assert cnt == 0, 'На карте не должны отображаться отделения'

        with allure.step('Включить тумблер "Прием на терминале"'):
            ctl_filter.switch_terminal_reception_filter()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Выключить тумблер "Прием на терминале"'):
            ctl_filter.switch_terminal_reception_filter()
            cnt = block_map.get_points_cnt()
            assert cnt == 0, 'На карте не должны отображаться отделения'

        with allure.step('Включить тумблер "Экспресс-прием"'):
            ctl_filter.switch_express_reception_filter()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

    @testit.workItemIds(35746)
    @testit.externalId('TestPrivateClients_35746')
    @testit.nameSpace('Общее')
    @testit.className('Карта на страницах')
    @testit.displayName('Отображение отделений на карте главной страницы (.ru) '
                        ' и на карте "Найти отделение в" (.ru/find_an_office)')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Карта на страницах')
    @allure.title('Карта на страницах - Отображение отделений на карте главной страницы (.ru) '
                  ' и на карте "Найти отделение в" (.ru/find_an_office)')
    @allure.testcase(url='https://testit..ru/browse/35746')
    @pytest.mark.parametrize('page_to_check', ['site_main_page', 'site_find_an_office'])
    def test_map_on_page_filter_by_point_type(self, site_page, page_to_check, request):
        page_to_check = request.getfixturevalue(page_to_check)

        with allure.step('Пролистать до карты'):
            block_map = page_to_check.block_map()

        with allure.step('Выбрать таб "Получение посылок получателем"'):
            cnt = block_map.select_tab_receiving_packages_by_the_recipient().get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Включить тумблер "Международные отправления"'):
            ctl_filter = block_map.ctl_filter_private_clients()
            ctl_filter.switch_on_point_inter_refunds_filter_in_tab_recipient()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Выключить тумблер "Международные отправления"'):
            ctl_filter.switch_off_point_inter_refunds_filter_in_tab_recipient()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Выбрать таб "Прием посылок от отправителя"'):
            block_map.ctl_filter_private_clients()
            cnt = block_map.select_tab_receiving_packages_from_the_sender().get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Включить тумблер "Международные отправления"'):
            ctl_filter = block_map.ctl_filter_private_clients()
            ctl_filter.switch_on_point_inter_refunds_filter_in_tab_sender()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'

        with allure.step('Выключить тумблер "Международные отправления"'):
            ctl_filter.switch_off_point_inter_refunds_filter_in_tab_sender()
            cnt = block_map.get_points_cnt()
            assert cnt > 0, 'На карте должны отображаться отделения'
