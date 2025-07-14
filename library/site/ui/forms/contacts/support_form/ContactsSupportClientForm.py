import allure

from library.site.ui.forms.contacts.support_form.ContactsSupportBaseForm import ContactsSupportBaseForm
from library.site.ui.pages.private_clients.terms.TermsDocumentsPage import TermsDocumentsPage


class ContactsSupportClientForm(ContactsSupportBaseForm):
    def set_parcel_number(self, email='0000123456789'):
        with allure.step(f'Установить в поле "Номер отправления" значение: {email}'):
            self.fill(f"{self.css_parcel_number}", email)
            self.screenshot('parcel_number_set', locator=self.page_element)
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
            with self.expect_page() as page_terms_document:
                self.click(f'{self.css_personal_agreement} a', force=False)
            new_page = page_terms_document.value
        return TermsDocumentsPage(new_page).check_page()
