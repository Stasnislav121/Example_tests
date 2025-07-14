import allure

from allure_commons.types import AttachmentType
from library.site.ui.pages.BasePage import BasePage


class AttachmentForm(BasePage):
    page_element = '.calculator-form-customs'
    сss_locator_input = '.accordion_calc .accordion__items > div'
    css_description_ru = '[placeholder="Описание вложения на русском"]'
    css_description_en = '[placeholder="Описание вложения на английском"]'
    css_manufacturer = '[placeholder="Производитель"]'
    css_price = '[placeholder="Цена"]'
    css_count = '[placeholder="Количество"]'
    css_full_price = '[placeholder="Полная стоимость"]'
    css_link = '[placeholder="Ссылка на товар в магазине или фото"]'
    css_ru_attachment_price = 'span:nth-child(1) input[placeholder="Цена"][disabled="disabled"]'
    css_eu_attachment_price = 'span:nth-child(2) input[placeholder="Цена"][disabled="disabled"]'
    css_ru_attachments_price = '.calculator-form-customs .field-full:nth-child(1) input'
    css_eu_attachments_price = '.calculator-form-customs .field-full:nth-child(2) input'
    css_add_attachment = '.calculator-form-customs__btn-add'
    css_continue = '.calculator__button_next-step'

    def __init__(self, page, index=1):
        super().__init__(page)
        self.cnt_attachments = index

    def check_element(self, screen=False):
        with allure.step("Проверить блок выбора стран и городов"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorCountryBlock_loaded', locator=self.page_element)
        return self

    def switch_attachment(self, value):
        with allure.step(f'Переключиться на вложение {value}'):
            self.cnt_attachments = value
        return AttachmentForm(self.page, index=value)

    def set_description_ru(self, value='Автотест Описание'):
        with allure.step(f'Заполнить поле "Описание вложения на русском" значением: {value} {self.cnt_attachments}'):
            self.fill(f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_description_ru}',
                      f"{value} {self.cnt_attachments}")
            self.screenshot('description_ru_set', locator=self.page_element)
        return self

    def set_manufacturer(self, value='Автотест Производитель'):
        with allure.step(f'Заполнить поле "Производитель" значением: {value} {self.cnt_attachments}'):
            self.fill(f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_manufacturer}',
                      f"{value} {self.cnt_attachments}")
            self.screenshot('manufacturer_set', locator=self.page_element)
        return self

    def set_price(self, value='999'):
        with allure.step(f'Заполнить поле "Цена" значением: {self.cnt_attachments}{value}'):
            self.fill(f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_price}',
                      f"{self.cnt_attachments}{value}")
            self.screenshot('price_set', locator=self.page_element)
        return self

    def set_count(self, value='1'):
        with allure.step(f'Заполнить поле "Количество" значением: {value}'):
            self.fill(f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_count}', value)
            self.screenshot('count_set', locator=self.page_element)
        return self

    def set_link(self, value='.ru'):
        with allure.step(f'Заполнить поле "Ссылка на товар в магазине или фото"" значением: {value}'):
            self.fill(f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_link}', value)
            self.screenshot('link_set', locator=self.page_element)
        return self

    def get_attachment_eu_full_price(self):
        with allure.step('Считать цену в евро из блока "Полная стоимость"'):
            locator = f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_eu_attachment_price}'
            self.wait_for_selector(locator)
            value = self.input_value(locator)
            allure.attach(str(value), 'Цена, €', AttachmentType.TEXT)
        return value

    def check_translate_description(self, value='Autotest Description'):
        with allure.step(f'Проверить наличие перевода значением: {value} {self.cnt_attachments}'):
            locator = f'{self.сss_locator_input}:nth-child({self.cnt_attachments}) {self.css_description_en}'
            self.wait_for_selector(locator)
            actual_value = self.input_value(locator)
            assert len(actual_value) > 0, f'Ожидался перевод {value} {self.cnt_attachments}, a получено' \
                                            f' {actual_value}'
        return self

    def get_attachment_eu_total_price(self):
        with allure.step('Считать цену в евро из блока "Стоимость вложений"'):
            self.wait_for_selector(self.css_eu_attachments_price)
            value = self.input_value(self.css_eu_attachments_price)
            allure.attach(str(value), 'Стоимость вложений, €', AttachmentType.TEXT)
        return value

    def fill_attachment_form(self):
        with allure.step('Заполнить форму описания вложений'):
            self.set_description_ru()
            self.set_manufacturer()
            self.set_price()
            self.set_count()
            self.set_link()
        return self

    def add_attachment(self):
        with allure.step('Нажать на кнопку "Добавить вложение"'):
            self.click(f"{self.css_add_attachment}", 'Добавить вложение', force=False)
        return self

    def goto_next_step(self):
        with allure.step('Кликнуть на кнопку "Оформить" и перейти к форме выбора отделения получателя'):
            self.click(f"{self.css_continue}", 'Оформить', force=False)
            self.screenshot('goto_next_step')

            from library.site.ui import SenderPointForm
            form = SenderPointForm(self.page)
            form.set_parent(self.get_parent())
        return form
