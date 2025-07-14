import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorEcommerceCityForm(BasePage):
    page_element = '.calculator__item-content .calculator-fields:nth-child(1)'
    css_sender_city = '.calculator-field:has(input[placeholder="Город-отправитель"])'
    css_receiver_city = '.calculator-field:has(input[placeholder="Город-получатель"])'

    def check_element(self, screen=False):
        with allure.step("Проверить блок выбора городов"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorEcommerceCityForm_loaded', locator=self.page_element)
        return self

    def click_sender_city(self):
        with allure.step('Кликнуть по полю "Город-отправитель"'):
            self.click(self.css_sender_city, 'Город-отправитель', force=False)
        return self

    def click_receiver_city(self):
        with allure.step('Кликнуть по полю "Город-получатель"'):
            self.click(self.css_receiver_city, 'Город-получатель', force=False)
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
