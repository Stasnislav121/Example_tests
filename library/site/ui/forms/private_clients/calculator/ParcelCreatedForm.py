import allure

from library.site.ui.pages.BasePage import BasePage


class ParcelCreatedForm(BasePage):
    page_element = '[name="calculator_pip"]'
    css_title = '.calculator__title_active'
    css_comment = '.calc-comment__text'
    css_comment_title = '.calc-comment__title'
    css_map_preview = '#calculatorMapPreview'
    css_delivery_number = '.calculator__item_active [placeholder="Номер отправления"]'
    css_point_block = '.calc-6th__odp-desc'
    css_map = '#calculatorMapPreview'
    css_to_lk_button = '.calculator__button_to-lk'
    css_another_parcel_button = '.calculator__button_back-step'
    css_field_label = '.calculator-field__label'

    def check_element(self, screen=False):
        with allure.step('Проверить форму "Отправление сформировано!"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.wait_for_selector(self.page_element)
                self.screenshot('ParcelCreatedForm_loaded', locator=self.page_element)
        return self

    def get_parcel_number(self):
        with allure.step('Считать номер отправления'):
            number = self.input_value(self.css_delivery_number).strip()
            allure.attach(str(number), 'Номер отправления', allure.attachment_type.TEXT)
        return number

    def check_parcel_created_from_point_rf(self):
        with allure.step('Проверить, что отправление от ПВЗ из РФ сформировано'):
            with allure.step('Отображается комментарий: "Отправка происходит при наличии паспорта"'):
                self.wait_for_selector(f'{self.css_comment}:text("Отправка происходит при наличии паспорта")')
            with allure.step('Отображается блок с данными отделения'):
                self.wait_for_selector(self.css_point_block)
            with allure.step('Отображается блок с картой'):
                self.wait_for_selector(self.css_map)
            with allure.step('Отображается кнопка "Войти в личный кабинет"'):
                self.wait_for_selector(self.css_to_lk_button)
            with allure.step('Отображается кнопка "Оформить еще одну посылку"'):
                self.wait_for_selector(self.css_another_parcel_button)
            with allure.step('Проверить номер отправления'):
                number = self.get_parcel_number()
                assert len(number) == 13, 'Длина номера отправления должна составлять 13 символов'

        return self

    def check_parcel_created_from_kd_rf(self):
        with allure.step('Проверить, что отправление от КД из РФ сформировано'):

            with allure.step('Отображается комментарий: "Вызовите курьера..."'):
                self.wait_for_selector(f'{self.css_comment}:has-text("Вызовите курьера на удобный для вас адрес и '
                                       f'передайте ему посылку. Инструкция по курьерскому забору")')
            with allure.step('Отображается кнопка "Войти в личный кабинет"'):
                self.wait_for_selector(self.css_to_lk_button)
            with allure.step('Отображается кнопка "Оформить еще одну посылку"'):
                self.wait_for_selector(self.css_another_parcel_button)
            with allure.step('Проверить номер отправления'):
                number = self.get_parcel_number()
                assert len(number) == 13, 'Длина номера отправления должна составлять 13 символов'

        return self

    def check_parcel_created_from_point_cis(self):
        with allure.step('Проверить, что отправление от ПВЗ из СНГ сформировано'):
            with allure.step('Отображается комментарий: "Отправка происходит при наличии паспорта"'):
                self.wait_for_selector(f'{self.css_comment}:text("Отправка происходит при наличии паспорта")')
            with allure.step('Отображается блок с данными отделения'):
                self.wait_for_selector(self.css_point_block)
            with allure.step('Отображается блок с картой'):
                self.wait_for_selector(self.css_map)
            with allure.step('Отображается кнопка "Войти в личный кабинет"'):
                self.wait_for_selector(self.css_to_lk_button)
            with allure.step('Отображается кнопка "Оформить еще одну посылку"'):
                self.wait_for_selector(self.css_another_parcel_button)
            with allure.step('Проверить номер отправления'):
                number = self.get_parcel_number()
                assert len(number) == 17, 'Длина номера отправления должна составлять 17 символов'
                number.startswith('BBU'), 'Номер отправления должен начинаться с кода "BBU"'

        return self

    def check_parcel_created_to_custom(self):
        with allure.step('Проверить, что отправление в страну с таможней сформировано'):
            with allure.step('Отображается комментарий: "Отправление сформировано!"'):
                self.wait_for_selector(f'{self.css_title}:text("Отправление сформировано!")')
            with allure.step('Отображается плашка: "Отправка происходит при наличии паспорта"'):
                self.wait_for_selector(f'{self.css_comment}:text("Отправка происходит при наличии паспорта")')
            with allure.step('Отображается блок с данными отделения'):
                self.wait_for_selector(self.css_point_block)
            with allure.step('Отображается текст: "Номер вашего отправления, покажите его в отделении:"'):
                self.wait_for_selector(f'{self.css_field_label}:text("Номер вашего отправления, покажите его в '
                                       f'отделении:")')
            with allure.step('Отображается текст: "Отнесите посылку в отделение  по адресу:"'):
                self.wait_for_selector(f'{self.css_field_label}:text("Отнесите посылку в отделение  '
                                       f'по адресу:")')
            with allure.step('Отображается блок с картой'):
                self.wait_for_selector(self.css_map)
            with allure.step('Отображается кнопка "Войти в личный кабинет"'):
                self.wait_for_selector(self.css_to_lk_button)
            with allure.step('Отображается кнопка "Оформить еще одну посылку"'):
                self.wait_for_selector(self.css_another_parcel_button)
            with allure.step('Отображается плашка: "Удобнее и быстрее оформить в личном кабинете"'):
                self.wait_for_selector(f'{self.css_comment_title}:text("Удобнее и быстрее оформить в личном кабинете")')
            with allure.step('Проверить номер отправления'):
                number = self.get_parcel_number()
                assert len(number) == 13, 'Длина номера отправления должна составлять 13 символов'

        return self
