import pytest
import testit
import allure

from library.site.site_const import MAP_POINT_ADDRESS
from library.site.ui.pages import *


class TestMapPointCard:
    @testit.workItemIds(13623)
    @testit.externalId('TestPrivateClients_13623')
    @testit.nameSpace('Общее')
    @testit.className('Карта на страницах')
    @testit.displayName('Открытие карточки отделения')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Карта на страницах')
    @allure.title('Карта на страницах - Открытие карточки отделения')
    @allure.testcase(url='https://testit..ru/browse/13623')
    @pytest.mark.parametrize('page_to_check', [
        'Бизнесу',
        'Доставка в страны СНГ',
        'Пункты приема посылок от интернет-магазинов'])
    def test_map_point_card_open(self, site_ecommerce_page, page_to_check):
        with allure.step(f'Открыть страницу "{page_to_check}"'):
            if page_to_check == 'Бизнесу':
                ecommerce_page = site_ecommerce_page
            elif page_to_check == 'Доставка в страны СНГ':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_delivery_to_cis()
            elif page_to_check == 'Пункты приема посылок от интернет-магазинов':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_acceptance_points()

        with allure.step('Открыть карточку отделения'):
            ecommerce_page.block_map() \
                .search_point(MAP_POINT_ADDRESS) \
                .click_any_point()

    @testit.workItemIds(13624)
    @testit.externalId('TestPrivateClients_13624')
    @testit.nameSpace('Общее')
    @testit.className('Карта на страницах')
    @testit.displayName('Содержание карточки отделения')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Карта на страницах')
    @allure.title('Карта на страницах - Содержание карточки отделения')
    @allure.testcase(url='https://testit..ru/browse/13624')
    @pytest.mark.parametrize('page_to_check', [
        'Бизнесу',
        'Доставка в страны СНГ',
        'Пункты приема посылок от интернет-магазинов'])
    def test_map_point_card_content(self, site_ecommerce_page, page_to_check):
        with allure.step(f'Открыть страницу "{page_to_check}"'):
            if page_to_check == 'Бизнесу':
                ecommerce_page = site_ecommerce_page
            elif page_to_check == 'Доставка в страны СНГ':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_delivery_to_cis()
            elif page_to_check == 'Пункты приема посылок от интернет-магазинов':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_acceptance_points()

        with allure.step('Проверить содержание карточки отделения'):
            block_card = ecommerce_page.block_map() \
                .search_point(MAP_POINT_ADDRESS) \
                .click_any_point()

            point_info = block_card.get_point_info()

            assert len(point_info['Адрес']) > 0, 'Наличие адреса отделения'
            assert len(point_info['Название']) > 0, 'Наличие названия и кода отделения'
            assert len(point_info['Фото']) > 0, 'Наличие фото отделения'
            assert len(point_info['Расписание']) > 0, 'Наличие расписания отделения'
            assert len(point_info['Услуги']) > 0, 'Наличие услуг отделения'

            for service in point_info['Услуги']:
                assert len(service) > 0, 'Наличие названия услуги'
                assert len(service) > 0, 'Наличие иконки услуги'

            assert block_card.is_visible(block_card.css_build_route), 'Наличие кнопки "Построить маршрут"'
            assert block_card.is_visible(block_card.css_point_page), 'Наличие кнопки "Страница отделения"'
            if not ecommerce_page.is_mobile:
                assert block_card.is_visible(block_card.css_lens), 'Наличие иконки "Лупа"'
