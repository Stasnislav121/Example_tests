import testit
import allure

from library.site.ui.pages import *


class TestFormSupportPrivateClient:
    @testit.workItemIds(13099)
    @testit.externalId('TestPrivateClients_13099')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName('Форма "Связаться со службой поддержки" частный клиент')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title('Контакты - Форма "Связаться со службой поддержки" частный клиент')
    @allure.testcase(url='https://testit..ru/browse/13099')
    def test_form_support_private_client(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_client_form()

        with allure.step('Заполнить форму и отправить обращение'):
            form_support.set_name() \
                .set_email() \
                .set_parcel_number() \
                .select_request_theme() \
                .set_text_request() \
                .click_subscription() \
                .click_personal_agreement() \
                .click_send_request()


    @testit.workItemIds(13102)
    @testit.externalId('TestPrivateClients_13102')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName('Редирект на страницу "Документы и юридические материалы" по ссылке из текста '
                        'чекбокса формы "Связаться со службой поддержки" из вкладки "Частный клиент"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title('Контакты - Редирект на страницу "Документы и юридические материалы" по ссылке '
                  'из текста чекбокса формы "Связаться со службой поддержки" из вкладки "Частный клиент"')
    @allure.testcase(url='https://testit..ru/browse/13102')
    def test_check_open_terms_documents_in_private_client_tab(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_client_form()

        with allure.step('Нажать на гиперссылку '
                         '"Я даю согласие на обработку своих персональных данных и проверить страницу перехода"'):
            terms_document_page = form_support.click_url_in_label()
            actual_url = terms_document_page.get_current_url()
            expect_url = f'{terms_document_page.base_url}{terms_document_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

        with allure.step('Проверить наличие документов на странице'):
            documents = terms_document_page.get_documents_count()
            assert documents > 0, 'На странице отсутствуют документы'
