import pytest
import testit
import allure

from library.site.ui.pages import *


class TestFormCalculatorValidation:
    @testit.workItemIds(13967)
    @testit.externalId('TestFormCalculator_13967')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Валидация поля "Оценочная стоимость"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Валидация поля "Оценочная стоимость"')
    @allure.testcase(url='https://testit..ru/browse/13967')
    def test_form_calculator_validation_package_price(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        expected_error = 'от 1000 до 200 000'

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.fill_country_block() \
                .select_own_package()
            block_total = form_calculator.scroll_to_bottom_of_form() \
                .block_total()
            block_total.check_register_button_status()

        with allure.step('Выбрано пустое значение'):
            form_calculator.set_package_price('')
            block_total.check_register_button_status(disabled=True)
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('Выбрано значение: 999'):
            form_calculator.set_package_price(999)
            block_total.check_register_button_status(disabled=True)
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('Выбрано значение: 1000'):
            form_calculator.set_package_price(1000)
            block_total.check_register_button_status()
            form_calculator.check_package_price_error_hidden()

        with allure.step('Выбрано значение: 200 001'):
            form_calculator.set_package_price(200001)
            block_total.check_register_button_status(disabled=True)
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('Выбрано значение: 200 000'):
            form_calculator.set_package_price(200000)
            block_total.check_register_button_status()
            form_calculator.check_package_price_error_hidden()

    @testit.workItemIds(13968)
    @testit.externalId('TestFormCalculator_13968')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Длина наибольшей стороны более 120 см')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Длина наибольшей стороны более 120 см')
    @allure.testcase(url='https://testit..ru/browse/13968')
    def test_form_calculator_validation_length_of_largest_side(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        expected_error = 'Одно измерение должно быть не более 120 см'
        large_size = 121
        small_size = 10

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.fill_country_block() \
                .select_own_package() \
                .scroll_to_bottom_of_form() \
                .check_register_button_status()

        with allure.step(f'В поле "Высота" выбрано значение: {large_size} см'):
            error = form_calculator.set_own_package_height(large_size) \
                .check_register_button_status(disabled=True) \
                .get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step(f'В поле "Высота" выбрано значение: {small_size} см'):
            form_calculator.set_own_package_height(small_size) \
                .check_register_button_status() \
                .check_own_package_size_error_hidden()

        with allure.step(f'В поле "Ширина" выбрано значение: {large_size} см'):
            error = form_calculator.set_own_package_width(large_size) \
                .check_register_button_status(disabled=True) \
                .get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step(f'В поле "Ширина" выбрано значение: {small_size} см'):
            form_calculator.set_own_package_width(small_size) \
                .check_register_button_status() \
                .check_own_package_size_error_hidden()

        with allure.step(f'В поле "Длина" выбрано значение: {large_size} см'):
            error = form_calculator.set_own_package_length(large_size) \
                .check_register_button_status(disabled=True) \
                .get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step(f'В поле "Длина" выбрано значение: {small_size} см'):
            form_calculator.set_own_package_length(small_size) \
                .check_register_button_status() \
                .check_own_package_size_error_hidden()

    @testit.workItemIds(13969)
    @testit.externalId('TestFormCalculator_13969')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Сумма длин всех сторон – более 250 см')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Сумма длин всех сторон – более 250 см')
    @allure.testcase(url='https://testit..ru/browse/13969')
    def test_form_calculator_validation_max_length(self, site_main_page):
        form_calculator = site_main_page.form_calculator()
        expected_error = 'Сумма всех сторон не должна превышать 250см'

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.fill_country_block() \
                .select_own_package() \
                .scroll_to_bottom_of_form() \
                .check_register_button_status()

        with allure.step('Сумма длин всех сторон более 250 см'):
            form_calculator.select_own_package(height=100, width=90, length=61)
            error = form_calculator.check_register_button_status(disabled=True) \
                .get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('Сумма длин всех сторон менее 250 см'):
            form_calculator.select_own_package(height=100, width=80, length=50) \
                .check_register_button_status() \
                .check_own_package_size_error_hidden()

    @testit.workItemIds(16558)
    @testit.externalId('TestFormCalculator_16558')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Соответствие условию 120x80x50 для всех сторон')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Соответствие условию 120x80x50 для всех '
                  'сторон')
    @allure.testcase(url='https://testit..ru/browse/16558')
    @pytest.mark.parametrize(('height', 'width', 'length'), [
        (119, 81, 50),
        (119, 81, 49),
        (120, 79, 51),
        (119, 79, 51),
    ])
    def test_form_calculator_validation_all_sides(self, site_main_page, height, width, length):
        form_calculator = site_main_page.form_calculator()
        expected_error = 'Размеры сторон отправления не должны превышать 120см*80см*50см'

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.fill_country_block()

        with allure.step('Заполнить поля габаритов валидными значениями: 120*80*50'):
            block_own_package = form_calculator.click_own_package() \
                .block_own_package()
            block_own_package.set_own_package_size(height=120, width=80, length=50)
            form_calculator.scroll_to_bottom_of_form() \
                .check_register_button_status()

        with allure.step(f'Заполнить поля габаритов невалидными значениями: {height}*{width}*{length}'):
            block_own_package.set_own_package_size(height=height, width=width, length=length)
            form_calculator.check_register_button_status(disabled=True)
            error = block_own_package.get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('Заполнить поля габаритов валидными значениями: 120*80*50'):
            block_own_package.set_own_package_size(height=120, width=80, length=50)
            form_calculator.check_register_button_status()
            block_own_package.check_own_package_size_error_hidden()

    @testit.workItemIds(30054)
    @testit.externalId('TestFormCalculator_30054')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Соответствие габаритов условию "10см*10см*1см" для отправлений из Беларуси')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Соответствие габаритов условию '
                  '"10см*10см*1см" для отправлений из Беларуси')
    @allure.testcase(url='https://testit..ru/browse/30054')
    @pytest.mark.parametrize(('height', 'width', 'length'), [
        (1, 1, 1),
        (10, 1, 1),
        (1, 10, 1),
        (1, 1, 10),
    ])
    def test_form_calculator_validation_for_sender_belarus(self, site_main_page, height, width, length):
        form_calculator = site_main_page.form_calculator()
        expected_error = 'Минимальные габариты отправления 10см*10см*1см'

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.fill_country_block(sender_country='Беларусь', sender_city='Минск') \
                .scroll_to_bottom_of_form()

        with allure.step('Заполнить поля габаритов валидными значениями: 10см*10см*1см'):
            block_own_package = form_calculator.set_package_weight() \
                .set_own_package_size(10, 10, 1) \
                .check_own_package_size_error_hidden()
            form_calculator.check_register_button_status()

        with allure.step(f'Заполнить поля габаритов невалидными значениями: {height}*{width}*{length}'):
            error = block_own_package.set_own_package_size(height, width, length) \
                .get_own_package_size_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'
            form_calculator.check_register_button_status(disabled=True)

        with allure.step('Заполнить поля габаритов валидными значениями: 120*80*50'):
            block_own_package.set_own_package_size(height=120, width=80, length=50)
            form_calculator.check_register_button_status()
            block_own_package.check_own_package_size_error_hidden()
