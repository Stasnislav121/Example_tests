import allure

from datetime import datetime, timedelta
from library.site.ui.pages.BasePage import BasePage


class ContactsFeedbackForm(BasePage):
    page_element = '.form'
    css_title = '.form__title:text("Форма обратной связи")'
    css_name = '.form #name'
    css_press = '.form #pressName'
    css_phone = '.form #phone'
    css_email = '.form #email'
    css_deadline = '.form #deadline'
    css_request_text = '.form #textRequest'
    css_personal_agreement = '[for="agreement"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)
        self.screenshot('ContactsFeedbackForm_loaded', locator=self.page_element)

    def set_name(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "Ваше имя" значение: {name}'):
            self.fill(self.css_name, name)
            self.screenshot('name_set', locator=self.page_element)
        return self

    def set_press_name(self, name='Автотест СМИ'):
        with allure.step(f'Установить в поле "СМИ" значение: {name}'):
            self.fill(self.css_press, name)
            self.screenshot('press_name_set', locator=self.page_element)
        return self

    def set_phone(self, phone='+7(999)999-99-99'):
        with allure.step(f'Установить в поле "Ваш номер телефона" значение: {phone}'):
            self.fill(self.css_phone, phone)
            self.screenshot('phone_set', locator=self.page_element)
        return self

    def set_email(self, email='autotest_site@.ru'):
        with allure.step(f'Установить в поле "Адрес электронной почты" значение: {email}'):
            self.fill(self.css_email, email)
            self.screenshot('email_set', locator=self.page_element)
        return self

    def set_deadline(self, date=None):
        if date is None:
            date = (datetime.today() + timedelta(days=30)).strftime("%d.%m.%Y")
        with allure.step(f'Установить в поле "Дедлайн (дата, время)" значение: {date}'):
            self.fill(self.css_deadline, str(date))
            self.screenshot('deadline_set', locator=self.page_element)
        return self

    def set_text_request(self, text='Текст запроса автотест'):
        with allure.step(f'Установить в поле "Текст запроса" значение: {text}'):
            self.fill(self.css_request_text, text)
            self.screenshot('text_request_set', locator=self.page_element)
        return self

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            self.click(self.css_personal_agreement)
            self.screenshot('personal_agreement_clicked', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with self.expect_request(lambda request: f'{self.base_url}/form/press' in request.url
                                                     and request.method == 'POST'):
                self.click(self.css_send_request)
            self.screenshot('send_request_clicked')
            self.wait_for_selector('.success-message')
        return self
