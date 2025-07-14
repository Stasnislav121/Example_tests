import testit
import allure

from library.site.ui.pages import *


class TestFormCalculatorPayment:
    @testit.workItemIds(15024)
    @testit.externalId('TestFormCalculator_15024')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Перерасчет стоимости при изменениях')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Перерасчет стоимости при изменениях')
    @allure.testcase(url='https://testit..ru/browse/15024')
    def test_form_calculator_payment_recalculation_upon_changes(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Заполнить данные в форме и получить условия доставки'):
            order_info = form_calculator.fill_country_block(sender_city='Екатеринбург', receiver_city='Екатеринбург') \
                .select__package() \
                .scroll_to_bottom_of_form() \
                .check_delivery_price_recalculated(price_before=0) \
                .get_order_delivery_info()
            assert order_info['Стоимость'] > 0
            if site_main_page.is_mobile:
                assert order_info['Срок доставки'] == '1 рабочий день'
            else:
                assert order_info['Срок доставки'] == ('Срок доставки: 1 рабочий день День приема посылки - не '
                                                       'учитывается')

        with allure.step('Внести изменения в поле: Ценность посылки - 100000'):
            form_calculator.set_package_price(100000) \
                .check_delivery_price_recalculated(order_info['Стоимость'])

            new_order_info_1 = form_calculator.get_order_delivery_info()
            assert new_order_info_1['Стоимость'] > order_info['Стоимость']
            assert new_order_info_1['Срок доставки'] == order_info['Срок доставки']

        with allure.step('Внести изменения в размер упаковки: Выбрать короб - TL'):
            form_calculator.select__package(package_name='Короб TL') \
                .check_delivery_price_recalculated(new_order_info_1['Стоимость'])

            new_order_info_2 = form_calculator.get_order_delivery_info()
            assert new_order_info_2['Стоимость'] > new_order_info_1['Стоимость']
            assert new_order_info_2['Срок доставки'] == order_info['Срок доставки']

        with allure.step('Внести изменения в поле: Город получатель - Москва'):
            form_calculator.select_receiver_city('Москва') \
                .check_delivery_price_recalculated(new_order_info_2['Стоимость'])

            new_order_info_3 = form_calculator.get_order_delivery_info()
            assert new_order_info_3['Стоимость'] > new_order_info_2['Стоимость']
            assert new_order_info_3['Срок доставки'] != new_order_info_2['Срок доставки']

    @testit.workItemIds(36240)
    @testit.externalId('TestFormCalculator_36240')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Калькулятор расчета и создания посылки онлайн"')
    @testit.displayName('Наличие текста "Вернем указанную сумму в '
                  'случае утери или повреждения посылки" в калькуляторе у поля "ценность посылки"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Калькулятор расчета и создания посылки онлайн"')
    @allure.title('Форма "Калькулятор расчета и создания посылки онлайн" - Наличие текста "Вернем указанную сумму в '
                  'случае утери или повреждения посылки" в калькуляторе у поля "ценность посылки"')
    @allure.testcase(url='https://testit..ru/browse/36240')
    def test_form_calculator_declared_price_return_money_text(self, site_main_page):
        expect_text = 'Вернем указанную сумму в случае утери или повреждения посылки'
        form_calculator = site_main_page.form_calculator()

        with allure.step('Считать текст под полем "Ценность посылки"'):
            actual_text = form_calculator.get_package_price_text()

        with allure.step('Проверить текст'):
            assert actual_text == expect_text, f'Ожидалось {expect_text}, получено {actual_text}'
