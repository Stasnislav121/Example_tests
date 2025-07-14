import allure

from library.site.ui.forms.contacts.support_form.ContactsSupportBaseForm import ContactsSupportBaseForm
from library.site.ui.pages.ecommerce.documents.DocumentsConfidentialityAgreementPage \
    import DocumentsConfidentialityAgreementPage


class ContactsSupportInternetShopForm(ContactsSupportBaseForm):
    def set_inn(self, inn='0123456789'):
        with allure.step(f'Установить в поле "ИНН интернет-магазина" значение: {inn}'):
            self.fill(self.css_inn, inn)
            self.screenshot('inn_set', locator=self.page_element)
        return self

    def click_send_request(self):
        with allure.step('Кликнуть на кнопку "Отправить заявку"'):
            with self.expect_request(lambda request: f'{self.base_url}/form/support-legal' in request.url
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
