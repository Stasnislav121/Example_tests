import allure
from library.site.ui.pages.BasePage import BasePage


class CalculatorEcommerceForm(BasePage):
    page_element = '.calculator-im[id=calculator]'
    css_price = '.field-input__inner[id=calcCost]'
    css_weight = '.field-input__inner[id=calcWeight]'
    css_price_error = f'.calculator-field:has({css_price}) .field__error'
    css_calculate_button = '.calculator__button:text("Рассчитать"):visible'
    css_calculate_button_disabled = '.calculator__button_disabled'

    def check_element(self, screen=False):
        with allure.step('Проверить форму "Расчёт и отправка посылок для интернет-магазинов"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.wait_for_selector(self.page_element)
        return self

    def block_city(self):
        with allure.step('Обратиться к блоку выбора городов'):
            from library.site.ui import CalculatorEcommerceCityForm
            block = CalculatorEcommerceCityForm(self.page).check_element()
            block.set_parent(self)
        return block

    def select_sender_city(self, city='Москва'):
        self.block_city().select_sender_city(city)
        return self

    def select_receiver_city(self, city='Екатеринбург'):
        self.block_city().select_receiver_city(city)
        return self

    def set_package_price(self, value='5'):
        with allure.step(f'Установить в поле "Оценочная стоимость" значение: {value}'):
            self.fill(self.css_price, value)
            self.screenshot('package_price_set', locator=self.page_element)
        return self

    def block_own_package(self):
        with allure.step('Обратиться к блоку заполнения собственной упаковки'):
            from library.site.ui import CalculatorEcommerceOwnPackageForm
            block = CalculatorEcommerceOwnPackageForm(self.page).check_element()
            block.set_parent(self)
        return block

    def select_own_package(self, height=10, width=10, length=10):
        self.block_own_package() \
            .set_own_package_size(height=height, width=width, length=length)
        return self

    def set_package_weight(self, value='14'):
        with allure.step(f'Установить в поле "Вес" значение: {value}'):
            self.fill(self.css_weight, value)
            self.screenshot('package_weight_set', locator=self.page_element)
        return self

    def get_package_price_error(self):
        with allure.step('Считать текст ошибки в блоке "Оценочная стоимость"'):
            error = self.inner_text(f"{self.css_price_error}")
            allure.attach(str(error), 'Текст ошибки', allure.attachment_type.TEXT)
        return error

    def check_package_price_error_hidden(self):
        with allure.step('Проверить отсутствие ошибки в блоке "Оценочная стоимость"'):
            self.wait_for_selector(f"{self.css_price_error}", state='detached')
        return self

    def check_calculate_button_active(self):
        with allure.step('Проверить, что кнопка "Рассчитать" активна'):
            self.wait_for_selector(f'{self.css_calculate_button}:not({self.css_calculate_button_disabled})')
        return self

    def check_calculate_button_disabled(self):
        with allure.step('Проверить, что кнопка "Рассчитать" неактивна'):
            self.wait_for_selector(f'{self.css_calculate_button}{self.css_calculate_button_disabled}')
        return self
