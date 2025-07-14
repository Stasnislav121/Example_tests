import allure

from library.site.ui.pages.BasePage import BasePage


class BasePackageForm(BasePage):
    page_element = '.calc-package-select'
    css_package_item = '.calc-package-select__item'
    css_package_type = '.calc-package-select__nav .nav__item'
    css_package_image = '.calc-package-select__right img'

    def check_element(self, screen=False):
        with allure.step("Проверить блок выбора упаковки "):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorPackageBlock_loaded', locator=self.page_element)
        return self

    def select_package(self, package_type='Короб', package_name='Короб S'):
        with allure.step(f'Выбрать "{package_type}": {package_name}'):
            self.click_package_type(package_type)
            self.click_package(package_name)
            self.screenshot('package_selected', locator=self.page_element)
        return self

    def click_package(self, package_name):
        with allure.step(f'Кликнуть на упаковку: {package_name}'):
            self.click(f'{self.css_package_item}:has-text("{package_name}")', force=False)
            self.wait_for_selector(f'{self.css_package_item}:has-text("{package_name}").active')
            self.screenshot('package_clicked', locator=self.page_element)
        return self

    def click_package_type(self, package_type):
        with allure.step(f'Кликнуть в выбор типа упаковки: {package_type}'):
            self.click(f'{self.css_package_type}:text("{package_type}")', force=False)
            self.wait_for_selector(f'{self.css_package_type}:has-text("{package_type}").active')
            self.screenshot('package_type_clicked', locator=self.page_element)
        return self

    def switch_to_box(self):
        with allure.step('Переключиться на тип упаковки: Короб'):
            self.click_package_type('Короб')
            from library.site.ui import PackageBoxForm
            block = PackageBoxForm(self.page)
        return block

    def switch_to_packet(self):
        with allure.step('Переключиться на тип упаковки: Пакет'):
            self.click_package_type('Пакет')
            from library.site.ui import PackagePacketForm
            block = PackagePacketForm(self.page)
        return block

    def switch_to_envelope(self):
        with allure.step('Переключиться на тип упаковки: Конверт'):
            self.click_package_type('Конверт')
            from library.site.ui import PackageEnvelopeForm
            block = PackageEnvelopeForm(self.page)
        return block

    def get_selected_package_image_link(self):
        with allure.step('Считать ссылку на изображение текущей выбранной упаковки'):
            link = self.get_attribute(self.css_package_image, 'src')
            allure.attach(str(link), 'Ссылка выбранного изображения', allure.attachment_type.TEXT)
        return link
