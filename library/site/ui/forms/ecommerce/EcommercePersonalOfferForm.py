import allure

from library.site.ui.pages.BasePage import BasePage
from settings import DOWNLOADS_DIR


class EcommercePersonalOfferForm(BasePage):
    page_element = '.form'
    css_title = '.form__title:text("Получите персональное предложение")',
    css_company = '#organization',
    css_phone = '#phone',
    css_site = '#site',
    css_name = '#name',
    css_email = '[type="email"]'
    css_personal_agreement = '[for="agreement"]'
    css_subscription = '[for="subscription"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)
        self.screenshot('EcommercePersonalOfferForm_loaded', locator=self.page_element)

    def set_name(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "Имя" значение: {name}'):
            self.fill(self.css_name, name)
            self.screenshot('name_set', locator=self.page_element)
        return self

    def set_phone(self, phone):
        with allure.step(f'Установить в поле "Ваш номер телефона" значение: {phone}'):
            self.fill(self.css_phone, phone)
            self.screenshot('phone_set', locator=self.page_element)
        return self

    def set_email(self, email):
        with allure.step(f'Установить в поле "Адрес электронной почты" значение: {email}'):
            self.fill(self.css_email, email)
            self.screenshot('email_set', locator=self.page_element)
        return self

    def set_site(self, site='https://.ru'):
        with allure.step(f'Установить в поле "Адрес вашего сайта" значение: {site}'):
            self.fill(self.css_site, site)
            self.screenshot('site_set', locator=self.page_element)
        return self

    def set_company(self, name='Автотест Компания'):
        with allure.step(f'Установить в поле "Ваша компания*" значение: {name}'):
            self.fill(self.css_company, name)
            self.screenshot('company_set', locator=self.page_element)
        return self

    def click_subscription(self):
        with allure.step('Кликнуть в чек-бокс "Получение информационной рассылки от "'):
            self.click(self.css_subscription)
            self.screenshot('subscription_clicked', locator=self.page_element)
        return self

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            self.click(self.css_personal_agreement)
            self.screenshot('personal_agreement_clicked', locator=self.page_element)
        return self

    def download_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            with self.expect_download() as download_info:
                self.click(f"{self.css_personal_agreement} a", force=False)
            download = download_info.value
            file_name = download.suggested_filename
            destination_path = f'{DOWNLOADS_DIR}/{file_name}'
            download.save_as(path=destination_path)
            allure.attach.file(destination_path, file_name, allure.attachment_type.PDF, extension='pdf')

        return destination_path

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with self.expect_request(lambda request: f'{self.base_url}/form/joinEn' in request.url
                                                     and request.method == 'POST'):
                self.click(self.css_send_request, force=False)
            self.screenshot('send_request_clicked')
            self.wait_for_selector('.success-message')
        return self
