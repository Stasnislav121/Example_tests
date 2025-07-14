import testit
import allure

from library.site.ui.pages import *


class TestFormSupportPoint:
    @testit.workItemIds(13101)
    @testit.externalId('TestFormSupport_13101')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName('Форма "Связаться со службой поддержки" пункт выдачи')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title('Контакты - Форма "Связаться со службой поддержки" пункт выдачи')
    @allure.testcase(url='https://testit..ru/browse/13101')
    def test_form_support_point(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_point_form()

        with allure.step('Заполнить форму и отправить обращение'):
            form_support.set_name() \
                .set_email() \
                .select_city() \
                .select_request_theme() \
                .set_text_request() \
                .click_subscription() \
                .click_personal_agreement() \
                .click_send_request()

    @testit.workItemIds(28873)
    @testit.externalId('TestFormSupportPoint_28873')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName(
        'Редирект на страницу "Согласие и политика по обработке персональных данных" '
        'по ссылке из текста чекбокса формы "Связаться со службой поддержки" из вкладки "Пункт выдачи"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title(
        'Контакты - Редирект на страницу "Согласие и политика по обработке персональных данных" '
        'по ссылке из текста чекбокса формы "Связаться со службой поддержки" из вкладки "Пункт выдачи"')
    @allure.testcase(url='https://testit..ru/browse/28873')
    def test_check_open_conf_agreement_page_in_point_tab(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_point_form()

        with allure.step('Нажать на гиперссылку "Я даю согласие на обработку'
                         ' своих персональных данных и проверить страницу перехода"'):
            confidentiality_agreement_page = form_support.click_url_in_label()
            actual_url = confidentiality_agreement_page.get_current_url()
            expect_url = f'{confidentiality_agreement_page.base_url}{confidentiality_agreement_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

        with allure.step('Проверить наличие документов на странице'):
            documents = confidentiality_agreement_page.get_documents_count()
            assert documents > 0, 'На странице отсутствуют документы'
