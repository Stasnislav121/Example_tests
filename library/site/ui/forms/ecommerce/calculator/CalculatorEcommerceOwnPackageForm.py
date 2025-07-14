import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorEcommerceOwnPackageForm(BasePage):
    page_element = '.calculator__item-content .calculator-fields:nth-child(2)'
    css_height = '.field-input__inner[id=calcHeight]'
    css_width = '.field-input__inner[id=calcWidth]'
    css_length = '.field-input__inner[id=calcLength]'

    def check_element(self, screen=False):
        with allure.step("Проверить блок заполнения собственной упаковки"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorEcommerceOwnPackageForm_loaded', locator=self.page_element)
        return self

    def set_own_package_size(self, height=10, width=10, length=10):
        with allure.step(f'Заполнить габариты параметрами: высота={height}, ширина={width}, длина={length}'):
            self.set_own_package_height(height)
            self.set_own_package_width(width)
            self.set_own_package_length(length)
        return self

    def set_own_package_height(self, height):
        with allure.step(f'Установить в поле "Высота" значение: {height}'):
            self.fill(self.css_height, height)
            self.screenshot('own_package_height_set', locator=self.page_element)
        return self

    def set_own_package_width(self, width):
        with allure.step(f'Установить в поле "Высота" значение: {width}'):
            self.fill(self.css_width, width)
            self.screenshot('own_package_width_set', locator=self.page_element)
        return self

    def set_own_package_length(self, length):
        with allure.step(f'Установить в поле "Высота" значение: {length}'):
            self.fill(self.css_length, length)
            self.screenshot('own_package_length_set', locator=self.page_element)
        return self
