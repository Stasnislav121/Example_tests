import allure

from library.site.ui.pages.BasePage import BasePage


class BusinessPartnersOpenPointBaseForm(BasePage):
    page_element = '.form'
    css_title = '.form__title:text("Заявка на открытие пункта выдачи ")'
    css_navigation_rf = '.nav li:nth-child(1) button'
    css_navigation_kz = '.nav li:nth-child(2) button'
    css_full_name = '[placeholder="ФИО*"]'
    css_phone = '[type="phone"]'
    css_email = '[type="email"]'
    css_city = '[placeholder="Город, где планируется открытие отделения*"]'
    css_address = '[placeholder="Адрес предполагаемого отделения *"]'
    css_personal_agreement = '[for="agreement"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)
        self.screenshot('BusinessPartnersOpenPointBaseForm_loaded', locator=self.page_element)

    def goto_russia_form(self):
        with allure.step('Перейти к форме "Россия"'):
            self.click(self.css_navigation_rf, force=False)
            self.wait_for_selector(f"{self.css_navigation_rf}.active")
            from library.site.ui import BusinessPartnersOpenPointRussiaForm
            form = BusinessPartnersOpenPointRussiaForm(self.page)
        return form

    def goto_kz_form(self):
        with allure.step('Перейти к форме "Казахстан"'):
            self.wait_for_selector(self.css_navigation_kz)
            self.hover(self.css_navigation_kz)
            self.click(self.css_navigation_kz, force=False)
            self.wait_for_selector(f"{self.css_navigation_kz}.active")
            from library.site.ui import BusinessPartnersOpenPointKZForm
            form = BusinessPartnersOpenPointKZForm(self.page)
        return form

    def set_fullname(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "ФИО" значение: {name}'):
            self.fill(self.css_full_name, name)
            self.screenshot('fullname_set', locator=self.page_element)
        return self

    def set_phone(self, phone='9999999999'):
        with allure.step(f'Установить в поле "Номер телефона" значение: {phone}'):
            self.click(self.css_phone)
            for letter in phone:
                self.key_press(letter)
            self.screenshot('phone_set', locator=self.page_element)
        return self

    def set_email(self, email='autotest_site@.ru'):
        with allure.step(f'Установить в поле "Адрес электронной почты" значение: {email}'):
            self.fill(self.css_email, email)
            self.screenshot('email_set', locator=self.page_element)
        return self

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            self.click(self.css_personal_agreement, position={'x': 10, 'y': 10}, force=False)
            self.screenshot('personal_agreement_clicked', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку" и обратиться к модальному окну о '
                         'продолжении заполнения'):
            self.click(self.css_send_request, force=False)
            self.screenshot('send_request_clicked')
            from library.site.ui import OpenPointContinueModal
            modal = OpenPointContinueModal(self.page)
            modal.set_parent(self)
        return modal
