import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorForm(BasePage):
    page_element = '[name="calculator_pip"]'
    css_price = '.price-input'
    css_weight = '.calculator-field_size input'
    css_validation_error = '.calc__field-error'
    css_price_block = '.calculator-field_cost-bar'
    css_price_block_text = f'{css_price_block} .field__notice'
    css__package = '[for="package-type-"]'
    css_own_package = '[for="package-type-user"]'

    def check_element(self, screen=False):
        with allure.step('Проверить форму "Калькулятор расчета и создания посылки онлайн"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.hover('.b-check')
                self.wait_for_selector(self.page_element)
                # self.screenshot('CalculatorForm_loaded', locator=self.page_element)
        return self

    def fill_country_block(self, sender_country=None, receiver_country='Россия',
                           sender_city='Москва', receiver_city='Екатеринбург'):
        self.block_country().fill_country_block(sender_country=sender_country,
                                                receiver_country=receiver_country,
                                                sender_city=sender_city,
                                                receiver_city=receiver_city)
        return self

    def select_sender_country(self, country='Россия'):
        self.block_country().select_sender_country(country)
        return self

    def select_receiver_country(self, country='Россия'):
        self.block_country().select_receiver_country(country)
        return self

    def select_sender_city(self, city='Москва'):
        self.block_country().select_sender_city(city)
        return self

    def select_receiver_city(self, city='Екатеринбург'):
        self.block_country().select_receiver_city(city)
        return self

    def click_sender_country(self):
        self.block_country().click_sender_country()
        return self

    def click_receiver_country(self):
        self.block_country().click_receiver_country()
        return self

    def click_sender_city(self):
        self.block_country().click_sender_city()
        return self

    def click_receiver_city(self):
        self.block_country().click_receiver_city()
        return self

    def click__package(self):
        with allure.step('Кликнуть в чек-бокс "Упаковка "'):
            self.click(self.css__package, force=False)
        return self

    def click_own_package(self):
        with allure.step('Кликнуть в чек-бокс "Упаковка "'):
            self.click(self.css_own_package, force=False)
        return self

    def select__package(self, package_type='Короб', package_name='Короб XS'):
        self.click__package() \
            .block__package() \
            .select_package(package_type=package_type, package_name=package_name)
        return self

    def select_own_package(self, height=10, width=10, length=10):
        self.click_own_package() \
            .block_own_package() \
            .set_own_package_size(height=height, width=width, length=length)
        return self

    def set_sender_city(self, value):
        self.block_country().set_sender_city(value)
        return self

    def set_receiver_city(self, value):
        self.block_country().set_receiver_city(value)
        return self

    def set_package_price(self, value='1000'):
        with allure.step(f'Установить в поле "Ценность посылки" значение: {value}'):
            self.fill(self.css_price, value)
            self.screenshot('package_price_set', locator=self.page_element)
        return self

    def set_package_weight(self, value='14'):
        with allure.step(f'Установить в поле "Вес посылки" значение: {value}'):
            self.fill(self.css_weight, value)
            self.screenshot('package_weight_set', locator=self.page_element)
        return self

    def set_own_package_size(self, height=10, width=10, length=10):
        self.block_own_package().set_own_package_size(height=height, width=width, length=length)
        return self

    def set_own_package_height(self, height):
        self.block_own_package().set_own_package_height(height)
        return self

    def set_own_package_width(self, width):
        self.block_own_package().set_own_package_width(width)
        return self

    def set_own_package_length(self, length):
        self.block_own_package().set_own_package_length(length)
        return self

    def select_from_point_to_door(self, street='ул Алая', house='д 1'):
        self.block_options().select_from_point_to_door(street=street, house=house)
        return self

    def select_from_door_to_point(self, street='ул Алая', house='д 1'):
        self.block_options().select_from_door_to_point(street=street, house=house)
        return self

    def select_from_door_to_door(self, from_street='ул Алая', from_house='д 1', to_street='Алабяна', to_house='д 11'):
        self.block_options().select_from_door_to_door(from_street=from_street, from_house=from_house,
                                                      to_street=to_street, to_house=to_house)
        return self

    def scroll_to_bottom_of_form(self):
        if self.is_mobile:
            with allure.step('Прокрутить скролл к концу формы (в мобильной версии)'):
                self.mouse_wheel(0, 1000)
                self.wait_for_timeout(0.5)
                self.mouse_wheel(0, 1000)
                self.screenshot('to_bottom_scrolled', locator=self.page_element)
        return self

    def get_package_price_text(self):
        with allure.step('Считать текст в блоке "Ценность посылки"'):
            text = self.inner_text(self.css_price_block_text)
            self.screenshot('package_price_text', locator=self.page_element)
            allure.attach(str(text), 'Текст про возврат денег', allure.attachment_type.TEXT)
        return text

    def get_package_price_error(self):
        with allure.step('Считать текст ошибки в блоке "Ценность посылки"'):
            error = self.inner_text(f"{self.css_price_block} {self.css_validation_error}")
            allure.attach(str(error), 'Текст ошибки', allure.attachment_type.TEXT)
        return error

    def get_own_package_size_error(self):
        return self.block_own_package().get_own_package_size_error()

    def get_input_sender_city(self):
        return self.block_country().get_input_sender_city()

    def get_input_receiver_city(self):
        return self.block_country().get_input_receiver_city()

    def get_dropdown_sender_country(self):
        return self.block_country().get_dropdown_sender_country()

    def get_dropdown_receiver_country(self):
        return self.block_country().get_dropdown_receiver_country()

    def get_dropdown_sender_city(self):
        return self.block_country().get_dropdown_sender_city()

    def get_dropdown_receiver_city(self):
        return self.block_country().get_dropdown_receiver_city()

    def get_courier_warning(self):
        with allure.step('Считать текст уведомления о курьерской доставке'):
            text = self.inner_text('.calculator__warning .calc-comment__text')
            link = self.get_attribute('.calculator__warning a', 'href')
            text = f'{text} ({link})'.replace('\n', '')
            allure.attach(str(text), 'Текст уведомления', allure.attachment_type.TEXT)
        return text

    def get_calculator_warning(self):
        with allure.step('Считать текст уведомления калькулятора'):
            text = self.inner_text('.calculator__warning').rstrip()
            allure.attach(str(text), 'Текст уведомления', allure.attachment_type.TEXT)
        return text

    def get_order_delivery_info(self):
        return self.block_total().get_order_delivery_info()

    def apply_promo_code(self, value='test'):
        self.block_options().apply_promo_code(value)
        return self

    def check_package_price_error_hidden(self):
        self.block_own_package().check_own_package_size_error_hidden()
        return self

    def check_own_package_size_error_hidden(self):
        self.block_own_package().check_own_package_size_error_hidden()
        return self

    def check_register_button_status(self, disabled=False):
        self.block_total().check_register_button_status(disabled)
        return self

    def check_delivery_price_recalculated(self, price_before: float, max_retries=10):
        self.block_total().check_delivery_price_recalculated(price_before=price_before, max_retries=max_retries)
        return self

    def goto_sender_point_form(self):
        self.scroll_to_bottom_of_form()
        form = self.block_total().goto_sender_point_form()
        return form

    def goto_sender_address_form(self):
        self.scroll_to_bottom_of_form()
        form = self.block_total().goto_sender_address_form()
        return form

    def goto_attachment_form(self):
        self.scroll_to_bottom_of_form()
        form = self.block_total().goto_attachment_form()
        return form

    def block__package(self):
        with allure.step('Обратиться к блоку выбора упаковки '):
            from library.site.ui import PackageBoxForm
            block = PackageBoxForm(self.page).check_element()
            block.set_parent(self)
        return block

    def block_own_package(self):
        with allure.step('Обратиться к блоку заполнения собственной упаковки'):
            from library.site.ui import CalculatorOwnPackageForm
            block = CalculatorOwnPackageForm(self.page).check_element()
            block.set_parent(self)
        return block

    def block_options(self):
        with allure.step('Обратиться к блоку опций доставки'):
            from library.site.ui import CalculatorOptionsForm
            block = CalculatorOptionsForm(self.page).check_element()
            block.set_parent(self)
        return block

    def block_total(self):
        with allure.step('Обратиться к блоку "Стоимость доставки"'):
            from library.site.ui import CalculatorTotalForm
            block = CalculatorTotalForm(self.page).check_element()
            block.set_parent(self)
        return block

    def block_country(self):
        with allure.step('Обратиться к блоку выбора стран и городов'):
            from library.site.ui import CalculatorCountryForm
            block = CalculatorCountryForm(self.page).check_element()
            block.set_parent(self)
        return block
