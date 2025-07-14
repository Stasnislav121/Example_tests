import testit
import allure


class TestFormEcomCalculatorValidation:
    @testit.workItemIds(14804)
    @testit.externalId('TestFormEcomCalculator_14804')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('Форма калькулятора "Расчёт и отправка посылок для интернет-магазинов"')
    @testit.displayName('Валидация поля "Оценочная стоимость" калькулятора ИМ')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма калькулятора "Расчёт и отправка посылок для интернет-магазинов"')
    @allure.title('Форма калькулятора "Расчёт и отправка посылок для интернет-магазинов" - Валидация поля "Оценочная '
                  'стоимость" калькулятора ИМ')
    @allure.testcase(url='https://testit..ru/browse/14804')
    def test_form_ecom_calculator_validation_package_price(self, site_ecommerce_page):
        form_calculator = site_ecommerce_page.form_calculator()
        expected_error = 'от 5 до 300 000'

        with allure.step('Предварительно заполнить данные в форме'):
            form_calculator.select_sender_city() \
                .select_receiver_city() \
                .select_own_package() \
                .set_package_weight() \
                .check_calculate_button_active()

        with allure.step('В поле "Оценочная стоимость" ввести значение: 0'):
            form_calculator.set_package_price(0) \
                .check_calculate_button_disabled()
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('В поле "Оценочная стоимость" ввести значение: 5'):
            form_calculator.set_package_price(5) \
                .check_calculate_button_active() \
                .check_package_price_error_hidden()

        with allure.step('В поле "Оценочная стоимость" ввести значение: 4.99'):
            form_calculator.set_package_price(4.99) \
                .check_calculate_button_disabled()
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('В поле "Оценочная стоимость" ввести значение: 5.01'):
            form_calculator.set_package_price(5.01) \
                .check_calculate_button_active() \
                .check_package_price_error_hidden()

        with allure.step('В поле "Оценочная стоимость" ввести значение: 299 999.99'):
            form_calculator.set_package_price(299999.99) \
                .check_calculate_button_active() \
                .check_package_price_error_hidden()

        with allure.step('В поле "Оценочная стоимость" ввести значение: 300 000.01'):
            form_calculator.set_package_price(300000.01) \
                .check_calculate_button_disabled()
            error = form_calculator.get_package_price_error()
            assert error == expected_error, f'Ожидалась ошибка: {expected_error}, но получена: {error}'

        with allure.step('В поле "Оценочная стоимость" ввести значение: 300 000'):
            form_calculator.set_package_price(300000) \
                .check_calculate_button_active() \
                .check_package_price_error_hidden()
