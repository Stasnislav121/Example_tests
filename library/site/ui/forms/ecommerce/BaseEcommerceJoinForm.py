import allure

from library.site.ui.pages.BasePage import BasePage
from library.site.ui.pages.ecommerce.documents import DocumentsConfidentialityAgreementPage
from settings import DOWNLOADS_DIR


class BaseEcommerceJoinForm(BasePage):
    css_legal_entity = '[placeholder="Юридическое лицо*"]'
    css_site = '[placeholder="Адрес вашего сайта"]'
    css_full_name = '[placeholder="ФИО*"]'
    css_email = '[type="email"]'

    def check_element(self, screen=False):
        with allure.step("Подключитесь к '"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('EcommerceJoinForm_loaded', locator=self.page_element)
        return self

    def set_phone(self, phone):
        with allure.step(f'Установить в поле "Ваш номер телефона" значение: {phone}'):
            for digit in phone:
                self.click(self.css_phone)
                self.key_press(digit)
        return self

    def set_email(self, email):
        with allure.step(f'Установить в поле "Адрес электронной почты" значение: {email}'):
            self.fill(self.css_email, email)
        return self

    def set_site(self, site='https://.ru'):
        with allure.step(f'Установить в поле "Адрес вашего сайта" значение: {site}'):
            self.fill(self.css_site, site)
        return self

    def set_legal_entity(self, name='Автотест Юр.лицо'):
        with allure.step(f'Установить в поле "Юридическое лицо" значение: {name}'):
            self.fill(self.css_legal_entity, name)
        return self

    def set_social_link(self, link='https://vk.com/_ru'):
        with allure.step(f'Установить в поле "Ссылка на соц.сети" значение: {link}'):
            self.fill(self.css_social_link, link)
        return self

    def set_fullname(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "ФИО" значение: {name}'):
            self.fill(self.css_full_name, name)
        return self

    def click_subscription(self):
        with allure.step('Кликнуть в чек-бокс "Получение информационной рассылки от "'):
            self.click(self.css_subscription)
        return self

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Я даю согласие на обработку своих персональных данных"'):
            self.click(self.css_personal_agreement, position={'x': 10, 'y': 10}, force=False)
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

    def click_url_in_label(self):
        with allure.step('Кликнуть по ссылке "Я даю согласие на обработку своих персональных данных"'):
            with self.expect_page() as page_conf_agreement:
                self.click(f"{self.css_personal_agreement} a", force=False)
            new_page = page_conf_agreement.value
        return DocumentsConfidentialityAgreementPage(new_page).check_page()

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with allure.step('Проверить, что отправлен запрос к ЛКИМ по адресу account-predprod.task..ru'):
                with self.expect_request(lambda request: 'account-predprod.task..ru' in request.url):
                    self.click(self.css_send_request)
            self.screenshot('send_request_clicked')
        return self

    def click_city(self):
        with allure.step('Кликнуть в поле "Город"'):
            self.click(self.css_city)
        return self

    def select_city(self, city=None):
        self.click_city()
        if city is None:
            city = self.get_cities()[0]
        with allure.step(f'Выбрать в поле "Город" значение: {city}'):
            self.click(f".multiselect__element:has-text('{city}')", force=False)
            self.screenshot('city_selected')
        return self

    def get_cities(self):
        with allure.step('Считать данные из дропдауна поля "Город"'):
            cities = []
            cnt = self.count(".multiselect__element")
            for i in range(cnt):
                city = self.inner_text(f".multiselect__element:nth-child({i + 1})")
                city = city.replace('\n', '')
                cities.append(city)

            allure.attach(str(cities), 'Дропдаун поля "Город"', allure.attachment_type.JSON)

        return cities
