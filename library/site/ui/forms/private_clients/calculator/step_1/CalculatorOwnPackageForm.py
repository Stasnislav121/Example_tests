import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorOwnPackageForm(BasePage):
    page_element = '.calculator-form__field_sizes'
    css_height = 'input[placeholder="Высота"]'
    css_width = 'input[placeholder="Ширина"]'
    css_length = 'input[placeholder="Длина"]'
    css_validation_error = '.calc__field-error'

    def check_element(self, screen=False):
        with allure.step("Проверить блок заполнения собственной упаковки"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorOwnPackageBlock_loaded', locator=self.page_element)
        return self

    def set_own_package_size(self, height=10, width=10, length=10):
        with allure.step(f'Заполнить свою упаковку параметрами: высота={height}, ширина={width}, длина={length}'):
            self.set_own_package_height(height)
            self.set_own_package_width(width)
            self.set_own_package_length(length)
        return self

    def set_own_package_height(self, height):
        with allure.step(f'Установить в поле "Высота" значение: {height}'):
            self.fill(self.css_height, height)
            self.screenshot('own_package_height_set', locator=self.page_element)
        return self

    def set_own_package_width(self, height):
        with allure.step(f'Установить в поле "Ширина" значение: {height}'):
            self.fill(self.css_width, height)
            self.screenshot('own_package_width_set', locator=self.page_element)
        return self

    def set_own_package_length(self, height):
        with allure.step(f'Установить в поле "Длина" значение: {height}'):
            self.fill(self.css_length, height)
            self.screenshot('own_package_length_set', locator=self.page_element)
        return self

    def get_own_package_size_error(self):
        with allure.step('Считать текст ошибки в блоке'):
            error = self.inner_text(f"{self.page_element} {self.css_validation_error}")
            allure.attach(str(error), 'Текст ошибки', allure.attachment_type.TEXT)
        return error

    def check_own_package_size_error_hidden(self):
        with allure.step('Проверить, что в блоке не отображается ошибка валидации'):
            self.wait_for_selector(f"{self.page_element} {self.css_validation_error}",
                                   state='detached')
        return self
