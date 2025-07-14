import pytest
import testit
import allure

from library.site.ui.pages import *


class TestFaqPage:
    @testit.workItemIds(34413)
    @testit.externalId('TestSearchOnSite_34413')
    @testit.nameSpace('Поиск на сайте')
    @testit.className('Страница поиска')
    @testit.displayName('Страница поиска - Редирект по гиперссылкам')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Поиск на сайте')
    @allure.title('Страница поиска - Редирект по гиперссылкам')
    @allure.testcase(url='https://testit..ru/browse/34413')
    def test_go_to_tracking_page_from_search_page(self, browser_mode, site_main_page):
        if browser_mode == 'mobile':
            pytest.skip('Отсутствует поиск в мобильной версии')
        main_page = site_main_page
        find_value = '55555'
        with (allure.step(f'Произвести поиск на сайте значением {find_value}')):
            search_page = main_page.menu_tabs() \
                .search_on_site(find_value) \
                .check_result_not_found_text()

        with (allure.step('Выполнить переход по ссылке "Нажмите здесь"')):
            search_page.click_press_here()
