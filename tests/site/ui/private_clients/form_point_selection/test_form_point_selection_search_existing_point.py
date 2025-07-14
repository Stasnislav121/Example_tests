import testit
import allure

from library.site.ui.pages import *


class TestFormPointSelectionSearchExistingPoint:
    @testit.workItemIds(20010)
    @testit.externalId('TestFormPointSelectionSearchExistingPoint_20010')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма выбора отделения-отправителя / отделения-получателя')
    @testit.displayName('Поиск существующего отделения через фильтр по полному совпадению значения поля поиска с '
                        'названием отделения')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма выбора отделения-отправителя / отделения-получателя')
    @allure.title('Форма выбора отделения-отправителя / отделения-получателя - '
                  'Поиск существующего отделения через фильтр по полному совпадению значения поля поиска с названием '
                  'отделения')
    def test_form_point_selection_search_existing_point_full_match(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        point_address = '620130, Екатеринбург г, 8 Марта ул, д.179'

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            form_point = form_calculator.select_own_package() \
                .fill_country_block(sender_city='Екатеринбург', receiver_city='Екатеринбург') \
                .goto_sender_point_form()

        with allure.step('Выполнить поиск отделения'):
            block_points_list = form_point.block_points()
            block_points_list.search_point(address=point_address)

        with allure.step(f'Проверить, что в списке отобразилось только одно отделение: {point_address}'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Название'] == point_address, f'В списке ожидалось отделения: {point_address}'
            assert not points[0]['Выбрано'], 'Отделение не должно быть выбрано'

        with allure.step('Выбрать отделение'):
            block_points_list.click_point(address=point_address)

        with allure.step('Проверить, что отделение выбрано и присутствует в списке'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Выбрано'], 'Отделение должно быть выбрано'

    @testit.workItemIds(20007)
    @testit.externalId('TestFormPointSelectionSearchExistingPoint_20007')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма выбора отделения-отправителя / отделения-получателя')
    @testit.displayName('Поиск существующего отделения через фильтр по включению значения поля поиска в названии '
                        'отделения')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма выбора отделения-отправителя / отделения-получателя')
    @allure.title('Форма выбора отделения-отправителя / отделения-получателя - '
                  'Поиск существующего отделения через фильтр по включению значения поля поиска в названии отделения')
    def test_form_point_selection_search_existing_point_partial_match(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        partial_address = 'Радищева'
        full_address = '620014, Екатеринбург г, Радищева ул, д.31'

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            form_point = form_calculator.select_own_package() \
                .fill_country_block(sender_city='Екатеринбург', receiver_city='Екатеринбург') \
                .goto_sender_point_form()

        with allure.step('Выполнить поиск отделения'):
            block_points_list = form_point.block_points()
            block_points_list.search_point(address=partial_address)

        with allure.step(f'Проверить, что в списке отобразилось только одно отделение: {full_address}'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Название'] == full_address, f'В списке ожидалось отделения: {full_address}'
            assert not points[0]['Выбрано'], 'Отделение не должно быть выбрано'

        with allure.step('Выбрать отделение'):
            block_points_list.click_point(address=full_address)

        with allure.step('Проверить, что отделение выбрано и присутствует в списке'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Выбрано'], 'Отделение должно быть выбрано'

    @testit.workItemIds(20009)
    @testit.externalId('TestFormPointSelectionSearchExistingPoint_20009')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма выбора отделения-отправителя / отделения-получателя')
    @testit.displayName('Поиск существующего отделения через фильтр при наличии только одного отделения')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма выбора отделения-отправителя / отделения-получателя')
    @allure.title('Форма выбора отделения-отправителя / отделения-получателя - '
                  'Поиск существующего отделения через фильтр при наличии только одного отделения')
    def test_form_point_selection_search_existing_point_single_point(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        point_address = '225215, Белоозерск, ул. Ленина, 50А'

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            form_point = form_calculator.select_own_package() \
                .fill_country_block(sender_country='Беларусь', sender_city='Белоозерск') \
                .set_package_weight() \
                .set_own_package_size() \
                .goto_sender_point_form()

        with allure.step('Выполнить поиск отделения'):
            block_points_list = form_point.block_points()
            block_points_list.set_search_string(point_address) \
                .wait_for_timeout(1)

        with allure.step(f'Проверить, что в списке отобразилось только одно отделение: {point_address}'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Название'] == point_address, f'В списке ожидалось отделения: {point_address}'
            assert not points[0]['Выбрано'], 'Отделение не должно быть выбрано'

        with allure.step('Выбрать отделение'):
            block_points_list.click_point(address=point_address)

        with allure.step('Проверить, что отделение выбрано и присутствует в списке'):
            points = block_points_list.get_data()
            assert len(points) == 1, 'В списке должно быть 1 отделение'
            assert points[0]['Название'] == point_address, f'В списке ожидалось отделения: {point_address}'
            assert points[0]['Выбрано'], 'Отделение должно быть выбрано'
