import allure

from library.site.ui.pages.BasePage import BasePage


class BusinessPartnersAdForm(BasePage):
    page_element = '#form_ecom'
    css_title = '.form__title:text("Оставьте заявку, чтобы узнать наши рекламные возможности и условия")'
    css_city = '#city'
    css_company = '#organization'
    css_full_name = '#name'
    css_phone = '#phone'
    css_email = '#email'
    css_suggestion = '#comment'
    css_personal_agreement = '[for="agreement"]'
    css_subscription = '[for="subscription"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.page_element)
        self.screenshot('BusinessPartnersAdForm_loaded', locator=self.page_element)

    def set_city(self, city):
        with allure.step(f'Установить в поле "Город" значение: {city}'):
            self.fill(self.css_city, city)
            self.screenshot('city_set', locator=self.page_element)
        return self

    def select_city(self, city='Москва'):
        with allure.step(f'Выбрать в поле "Город" значение: {city}'):
            self.set_city(city)
            self.click(f'.suggestions-suggestion:has-text("{city}")')
            self.screenshot('city_selected', locator=self.page_element)
        return self

    def set_phone(self, phone='+7(999)999-99-99'):
        with allure.step(f'Установить в поле "Номер телефона" значение: {phone}'):
            self.fill(self.css_phone, phone)
            self.screenshot('phone_set', locator=self.page_element)
        return self

    def set_email(self, email='autotest_site@.ru'):
        with allure.step(f'Установить в поле "Адрес электронной почты" значение: {email}'):
            self.fill(self.css_email, email)
            self.screenshot('email_set', locator=self.page_element)
        return self

    def set_company(self, name='Автотест Компания'):
        with allure.step(f'Установить в поле "Название компании" значение: {name}'):
            self.fill(self.css_company, name)
            self.screenshot('company_set', locator=self.page_element)
        return self

    def set_fullname(self, name='Автотест Имя'):
        with allure.step(f'Установить в поле "ФИО" значение: {name}'):
            self.fill(self.css_full_name, name)
            self.screenshot('fullname_set', locator=self.page_element)
        return self

    def set_suggestion(self, text='Автотест Предложение'):
        with allure.step(f'Установить в поле "Краткое описание вашего предложения" текст: {text}'):
            self.fill(self.css_suggestion, text)
            self.screenshot('suggestion_set', locator=self.page_element)
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

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with self.expect_request(lambda request: f'{self.base_url}/form/ecom/join' in request.url
                                                     and request.method == 'POST'):
                self.click(self.css_send_request)
            self.screenshot('send_request_clicked')
            self.wait_for_selector('.success-message')
        return self

    def click_city(self):
        with allure.step('Кликнуть в поле "Город"'):
            self.click(self.css_city)
            self.screenshot('city_clicked', locator=self.page_element)
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
