import allure

from library.site.ui.forms.business_partners.open_point_form.BusinessPartnersOpenPointBaseForm \
    import BusinessPartnersOpenPointBaseForm


class BusinessPartnersOpenPointRussiaForm(BusinessPartnersOpenPointBaseForm):
    def __init__(self, page):
        super().__init__(page)

    def set_city(self, city):
        with allure.step(f'Установить в поле "Город" значение: {city}'):
            self.fill(self.css_city, city)
            self.screenshot('city_set', locator=self.page_element)
        return self

    def set_address(self, address):
        with allure.step(f'Установить в поле "Адрес предполагаемого отделения " значение: {address}'):
            self.fill(self.css_address, address)
            self.screenshot('address_set', locator=self.page_element)
        return self

    def select_city(self, city='Москва'):
        with allure.step(f'Выбрать в поле "Город" значение: {city}'):
            self.set_city(city)
            self.click(f'.suggestions-suggestion:has-text("{city}")')
            self.screenshot('city_selected', locator=self.page_element)
        return self

    def select_address(self, city='г Москва, Алтуфьевское шоссе'):
        with allure.step('Выбрать в поле "Город" блок'):
            self.set_address(city)
            self.click(f'.suggestions-suggestion:has-text("{city}")')
            self.screenshot('address_selected', locator=self.page_element)
        return self
