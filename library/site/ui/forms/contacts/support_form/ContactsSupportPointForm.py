import allure

from library.site.ui.forms.contacts.support_form.ContactsSupportBaseForm import ContactsSupportBaseForm
from library.site.ui.pages.ecommerce.documents.DocumentsConfidentialityAgreementPage \
    import DocumentsConfidentialityAgreementPage


class ContactsSupportPointForm(ContactsSupportBaseForm):
    def click_city(self):
        with allure.step('Кликнуть в поле "Город"'):
            self.click(self.css_city, force=False)
            self.screenshot('city_clicked', locator=self.page_element)
        return self

    def select_city(self, city='Москва'):
        self.click_city()
        with allure.step(f'Выбрать в поле "Город" значение: {city}'):
            self.click(f".multiselect__element:has-text('{city}')", force=False)
            self.screenshot('city_selected', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with self.expect_request(lambda request: f'{self.base_url}/form/support' in request.url
                                                     and request.method == 'POST'):
                self.click(self.css_send_request)
            self.screenshot('send_request_clicked')
            self.wait_for_selector('.success-message')
        return self

    def click_url_in_label(self):
        with allure.step('Кликнуть по ссылке "Я даю согласие на обработку своих персональных данных"'):
            with self.expect_page() as page_conf_agreement:
                self.click(f'{self.css_personal_agreement} a', force=False)
            new_page = page_conf_agreement.value
        return DocumentsConfidentialityAgreementPage(new_page).check_page()
