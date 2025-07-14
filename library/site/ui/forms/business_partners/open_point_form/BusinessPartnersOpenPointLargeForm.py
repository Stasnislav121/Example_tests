import allure

from datetime import datetime
from library.site.ui import BasePage


class BusinessPartnersOpenPointLargeForm(BasePage):
    page_element = '.form'
    css_legal_form = '[placeholder="Форма осуществления предпринимательской деятельности*"]'
    css_legal_name = '[placeholder="Юридическое название организации*"]'
    css_registration_date = '[placeholder="Дата регистрации Юридического лица*"]'
    css_inn = '[placeholder="ИНН организации*"]'
    css_type_activity = '[placeholder="Вид деятельности организации*"]'
    css_taxation_system = '[placeholder="Система налогообложения*"]'
    css_cash_availability = '[placeholder="Наличие кассового аппарата*"]'
    css_acquiring_availability = '[placeholder="Наличие терминала эквайринга*"]'
    css_security_availability = '[placeholder="Наличие охранной системы*"]'
    css__video_availability = '[placeholder="Наличие системы видеонаблюдения*"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def set_legal_name(self, name='ИП Автотест'):
        with allure.step(f'Установить в поле "Юридическое название организации" значение: {name}'):
            self.fill(self.css_legal_name, name)
            self.screenshot('legal_name_set', locator=self.page_element)
        return self

    def set_legal_inn(self, inn='1234567890'):
        with allure.step(f'Установить в поле "ИНН организации" значение: {inn}'):
            self.fill(self.css_inn, inn)
            self.screenshot('legal_inn_set', locator=self.page_element)
        return self

    def set_legal_registration_date(self, reg_date=None):
        if reg_date is None:
            reg_date = datetime.now().strftime('%d.%m.%Y')
        with allure.step(f'Установить в поле "Дата регистрации Юридического лица" значение: {reg_date}'):
            self.fill(self.css_registration_date, reg_date)
            self.key_press('Escape')  # закрыть календарь
            self.screenshot('legal_registration_date_set', locator=self.page_element)
        return self

    def select_legal_form(self, form='Индивидуальный предприниматель'):
        with allure.step(f'Выбрать в поле "Форма осуществления предпринимательской деятельности" значение: {form}'):
            self.click(f"{self.css_legal_form} + span", force=False)
            self.click(f'.multiselect__element:has-text("{form}")', force=False)
            self.screenshot('legal_form_selected', locator=self.page_element)
        return self

    def select_legal_type_activity(self, type_activity='Торговля'):
        with allure.step(f'Выбрать в поле "Вид деятельности организации" значение: {type_activity}'):
            self.click(f"{self.css_type_activity} + span", force=False)
            self.click(f'.multiselect__element:has-text("{type_activity}")', force=False)
            self.screenshot('legal_type_activity_selected', locator=self.page_element)
        return self

    def select_taxation_system(self, type_activity='УСН'):
        with allure.step(f'Выбрать в поле "Система налогообложения" значение: {type_activity}'):
            self.click(f"{self.css_taxation_system} + span", force=False)
            self.click(f'.multiselect__element:has-text("{type_activity}")', force=False)
            self.screenshot('taxation_system_selected', locator=self.page_element)
        return self

    def select_cash_availability(self, value='да'):
        with allure.step(f'Выбрать в поле "Наличие кассового аппарата" значение: {value}'):
            self.click(f"{self.css_cash_availability} + span", force=False)
            self.click(f'.form__fields li:nth-child(12) .multiselect__element:has-text("{value}")', force=False)
            self.screenshot('cash_availability_selected', locator=self.page_element)
        return self

    def select_acquiring_availability(self, value='да'):
        with allure.step(f'Выбрать в поле "Наличие терминала эквайринга" значение: {value}'):
            self.click(f"{self.css_acquiring_availability} + span", force=False)
            self.click(f'.form__fields li:nth-child(13) .multiselect__element:has-text("{value}")', force=False)
            self.screenshot('acquiring_availability_selected', locator=self.page_element)
        return self

    def select_security_availability(self, value='да'):
        with allure.step(f'Выбрать в поле "Наличие охранной системы" значение: {value}'):
            self.click(f"{self.css_security_availability} + span", force=False)
            self.click(f'.form__fields li:nth-child(14) .multiselect__element:has-text("{value}")', force=False)
            self.screenshot('security_availability_selected', locator=self.page_element)
        return self

    def select_video_availability(self, value='да'):
        with allure.step(f'Выбрать в поле "Наличие системы видеонаблюдения" значение: {value}'):
            self.click(f"{self.css__video_availability} + span", force=False)
            self.click(f'.form__fields li:nth-child(15) .multiselect__element:has-text("{value}")', force=False)
            self.screenshot('video_availability_selected', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку" и обратиться к модальному окну успешной отправки '
                         'запроса'):
            self.accept_dialog_on()
            self.click(self.css_send_request, force=False)
            self.screenshot('send_request_clicked', locator=self.page_element)
            from library.site.ui import SuccessMessageModal
            modal = SuccessMessageModal(self.page)
            modal.set_parent(self)
        return modal
