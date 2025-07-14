import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorCountryForm(BasePage):
    page_element = '.calculator-fields_country'
    css_sender_country = '.calculator-field_country-wrap:nth-child(1) .calculator-field_country'
    css_sender_city = '.calculator-field_country-wrap:nth-child(1) .calculator-field_city'
    css_receiver_country = '.calculator-field_country-wrap:nth-child(2) .calculator-field_country'
    css_receiver_city = '.calculator-field_country-wrap:nth-child(2) .calculator-field_city'
    css_dropdown = '.multiselect__content-wrapper'
    css_input = '.multiselect__single'
    css_map = {
        'Страна отправителя': css_sender_country,
        'Город-отправитель': css_sender_city,
        'Страна получателя': css_receiver_country,
        'Город-получатель': css_receiver_city
    }

    def check_element(self, screen=False):
        with allure.step("Проверить блок выбора стран и городов"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorCountryBlock_loaded', locator=self.page_element)
        return self

    def fill_country_block(self, sender_country, receiver_country, sender_city, receiver_city):
        if sender_country is not None:
            self.select_sender_country(sender_country)
        self.select_sender_city(sender_city)
        self.select_receiver_country(receiver_country)
        self.select_receiver_city(receiver_city)
        return self

    def select_sender_country(self, country='Россия'):
        with allure.step(f'Выбрать в поле "Страна" отправителя страну: {country}'):
            self.click_sender_country()
            self.click(f"{self.css_sender_country} :text('{country}')", force=False)
            self.screenshot('sender_country_selected', locator=self.page_element)
        return self

    def select_receiver_country(self, country='Россия'):
        with allure.step(f'Выбрать в поле "Страна" получателя страну: {country}'):
            self.click_receiver_country()
            self.click(f"{self.css_receiver_country} :text('{country}')", force=False)
            self.screenshot('receiver_country_selected', locator=self.page_element)
        return self

    def select_sender_city(self, city='Москва'):
        with allure.step(f'Выбрать в поле "Город-отправитель" город: {city}'):
            self.click_sender_city()
            self.click(f"{self.css_sender_city} .input-city__city:text('{city}')", force=False)
            self.screenshot('sender_city_selected', locator=self.page_element)
        return self

    def select_receiver_city(self, city='Екатеринбург'):
        with allure.step(f'Выбрать в поле "Город-получатель" город: {city}'):
            self.click_receiver_city()
            self.click(f"{self.css_receiver_city} .input-city__city:text('{city}')", force=False)
            self.screenshot('receiver_city_selected', locator=self.page_element)
        return self

    def click_sender_country(self):
        with allure.step('Кликнуть по полю "Страна" отправителя'):
            self.click(self.css_sender_country, 'Страна', force=False)
        return self

    def click_receiver_country(self):
        with allure.step('Кликнуть по полю "Страна" получателя'):
            self.click(self.css_receiver_country, 'Страна', force=False)
        return self

    def click_sender_city(self):
        with allure.step('Кликнуть по полю "Город-отправитель"'):
            self.click(self.css_sender_city, 'Город-отправитель', force=False)
        return self

    def click_receiver_city(self):
        with allure.step('Кликнуть по полю "Город-получатель"'):
            self.click(self.css_receiver_city, 'Город-получатель', force=False)
        return self

    def set_sender_city(self, value):
        with allure.step(f'Установить в поле "Город-отправитель" значение: {value}'):
            self.key_press('Escape')
            self.click_sender_city()
            self.fill(f"{self.css_sender_city} input", value)
            self.screenshot('sender_city_set', locator=self.page_element)
        return self

    def set_receiver_city(self, value):
        with allure.step(f'Установить в поле "Город-получатель" значение: {value}'):
            self.key_press('Escape')
            self.click_receiver_city()
            self.fill(f"{self.css_receiver_city} input", value)
            self.screenshot('receiver_city_set', locator=self.page_element)
        return self

    def get_input_sender_city(self):
        return self.get_input_city_or_country('Город-отправитель')

    def get_input_receiver_city(self):
        return self.get_input_city_or_country('Город-получатель')

    def get_dropdown_sender_country(self):
        return self.get_dropdown_countries('Страна отправителя')

    def get_dropdown_receiver_country(self):
        return self.get_dropdown_countries('Страна получателя')

    def get_dropdown_sender_city(self):
        return self.get_dropdown_cities('Город-отправитель')

    def get_dropdown_receiver_city(self):
        return self.get_dropdown_cities('Город-получатель')

    def get_input_city_or_country(self, field):
        with allure.step(f'Считать данные из инпута: {field}'):
            locator = f"{self.css_map[field]} {self.css_input}:not([style*='display: none'])"
            city = self.inner_text(locator)
        return city

    def get_dropdown_countries(self, field):
        with allure.step(f'Считать данные из дропдауна стран: {field}'):
            locator = f"{self.css_map[field]} {self.css_dropdown}:not([style*='display: none'])"
            self.wait_for_selector(locator, state='visible')
            self.wait_for_timeout(1)
            countries = self.inner_text(locator).split('\n')
            if '' in countries:
                countries.remove('')
            allure.attach(str(countries), f'Страны поля: {field}', allure.attachment_type.JSON)
            self.key_press('Escape')  # закрыть дропдаун после считывания данных
            self.wait_for_selector(locator, state='detached')
        return countries

    def get_dropdown_cities(self, field):
        with allure.step(f'Считать данные из дропдауна городов: {field}'):
            locator = f"{self.css_map[field]} {self.css_dropdown}:not([style*='display: none'])"
            self.wait_for_selector(locator, state='visible')
            self.wait_for_timeout(1)
            cities = self.inner_text(locator).split('\n')
            if '' in cities:
                cities.remove('')
            cities_with_region = []
            for city, region in zip(cities[::2], cities[1::2]):
                val = f'{city}\n{region}'
                cities_with_region.append(val)
            allure.attach(str(cities_with_region), f'Города поля: {field}', allure.attachment_type.JSON)
            self.key_press('Escape')  # закрыть дропдаун после считывания данных
            self.wait_for_selector(locator, state='detached')
        return cities_with_region
