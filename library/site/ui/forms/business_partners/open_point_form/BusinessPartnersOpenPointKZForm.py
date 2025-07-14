import allure

from library.site.ui.forms.business_partners.open_point_form.BusinessPartnersOpenPointBaseForm \
    import BusinessPartnersOpenPointBaseForm


class BusinessPartnersOpenPointKZForm(BusinessPartnersOpenPointBaseForm):
    def __init__(self, page):
        super().__init__(page)

    def set_city(self, city):
        with allure.step(f'Установить в поле "Город" значение: {city}'):
            self.fill(f".form-kz {self.css_city}", city)
            self.screenshot('city_set', locator=self.page_element)
        return self

    def click_city(self):
        with allure.step('Кликнуть в поле "Город"'):
            self.click(".form-kz .multiselect_city")
            self.screenshot('city_clicked', locator=self.page_element)
        return self

    def select_city(self, city='Астана'):
        with allure.step(f'Выбрать в поле "Город" значение: {city}'):
            self.click_city()
            self.set_city(city)
            self.click(f'.form-kz .multiselect__element:has-text("{city}")')
            self.screenshot('city_selected', locator=self.page_element)
        return self

    def set_address(self, address='улица Астана'):
        with allure.step(f'Установить в поле "Адрес предполагаемого отделения " значение: {address}'):
            self.fill(f".form-kz {self.css_address}", address)
            self.screenshot('address_set', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку" и обратиться к модальному окну'
                         ' о продолжении заполнения'):
            self.click(self.css_send_request, force=False)
            self.screenshot('send_request_clicked')
            from library.site.ui import SuccessMessageModal
            modal = SuccessMessageModal(self.page)
            modal.set_parent(self)
        return modal
