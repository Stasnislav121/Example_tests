import allure

from library.site.ui.pages.BasePage import BasePage
from settings import DOWNLOADS_DIR


class ContactsSupportBaseForm(BasePage):
    page_element = '#form_feedback'
    css_title = '.form__title:text("Связаться со службой поддержки")'
    css_private_client = '.nav li:nth-child(1) button'
    css_eshop = '.nav li:nth-child(2) button'
    css_issue_point = '.nav li:nth-child(3) button'
    css_name = '[placeholder="Ваше имя"]'
    css_email = '[type="email"]'
    css_parcel_number = '#form_feedback [placeholder="Номер отправления"]'
    css_request_text = '#form_feedback textarea'
    css_request_theme = '[placeholder="Тема обращения"] + span'
    css_inn = '[placeholder="ИНН интернет-магазина"]'
    css_city = '[placeholder="Город*"] + span'
    css_personal_agreement = '[for="agreement"]'
    css_subscription = '[for="subscription"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)
        self.screenshot('ContactsSupportBaseForm_loaded', locator=self.page_element)

    def goto_client_form(self):
        with allure.step('Перейти к форме "Частный клиент"'):
            self.click(self.css_private_client, force=False)
            self.wait_for_selector(f"{self.css_private_client}.active")
            from library.site.ui import ContactsSupportClientForm
            form = ContactsSupportClientForm(self.page)
        return form

    def goto_internet_shop_form(self):
        with allure.step('Перейти к форме "Интернет-магазин"'):
            self.click(self.css_eshop, force=False)
            self.wait_for_selector(f"{self.css_eshop}.active")
            from library.site.ui import ContactsSupportInternetShopForm
            form = ContactsSupportInternetShopForm(self.page)
        return form

    def goto_point_form(self):
        with allure.step('Перейти к форме "Пункт выдачи"'):
            self.click(self.css_issue_point, force=False)
            self.wait_for_selector(f"{self.css_issue_point}.active")
            from library.site.ui import ContactsSupportPointForm
            form = ContactsSupportPointForm(self.page)
        return form

    def set_name(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "Ваше имя" значение: {name}'):
            self.fill(self.css_name, name)
        return self

    def set_email(self, email='autotest_site@.ru'):
        with allure.step(f'Установить в поле "Email" значение: {email}'):
            self.fill(self.css_email, email)
        return self

    def set_text_request(self, text='Текст сообщения автотест'):
        with allure.step(f'Установить в поле "Текст сообщения" значение: {text}'):
            self.fill(self.css_request_text, text)
        return self

    def click_request_theme(self):
        with allure.step('Кликнуть в поле "Тема обращения"'):
            self.click(self.css_request_theme)
            self.screenshot('request_theme_clicked', locator=self.page_element)
        return self

    def select_request_theme(self, theme=None):
        self.click_request_theme()
        if theme is None:
            theme = self.get_request_themes()[0]
        with allure.step(f'Выбрать в поле "Тема обращения" значение: {theme}'):
            self.click(f".multiselect--active .multiselect__element:has-text('{theme}')", force=False)
            self.screenshot('request_theme_selected', locator=self.page_element)
        return self

    def get_request_themes(self):
        with allure.step('Считать данные из дропдауна поля "Тема обращения"'):
            themes = []
            cnt = self.count('.multiselect--active .multiselect__element')
            for i in range(cnt):
                theme = self.inner_text(f".multiselect--active .multiselect__element:nth-child({i + 1})")
                theme = theme.replace('\n', '')
                themes.append(theme)

            allure.attach(str(themes), 'Дропдаун поля "Тема обращения"', allure.attachment_type.JSON)

        return themes

    def click_subscription(self):
        with allure.step('Кликнуть в чек-бокс "Получение информационной рассылки от "'):
            self.click(self.css_subscription)
            self.screenshot('subscription_clicked', locator=self.page_element)
        return self

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            self.click(self.css_personal_agreement, position={'x': 10, 'y': 10}, force=False)
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
