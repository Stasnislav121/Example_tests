import testit
import allure

from library.site.ui.pages import *


class TestFormSupportInternetShop:
    @testit.workItemIds(13100)
    @testit.externalId('TestFormSupport_13100')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName('Форма "Связаться со службой поддержки" интернет магазин')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title('Контакты - Форма "Связаться со службой поддержки" интернет магазин')
    @allure.testcase(url='https://testit..ru/browse/13100')
    def test_form_support_internet_shop(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_internet_shop_form()

        with allure.step('Заполнить форму и отправить обращение'):
            form_support.set_name() \
                .set_email() \
                .set_inn() \
                .select_request_theme() \
                .set_text_request() \
                .click_subscription() \
                .click_personal_agreement() \
                .click_send_request()

    @testit.workItemIds(28872)
    @testit.externalId('TestFormSupport_28872')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Связаться со службой поддержки"')
    @testit.displayName(
        'Редирект на страницу "Согласие и политика по обработке персональных данных" по ссылке из текста чекбокса '
        'формы "Связаться со службой поддержки" из вкладки "Интернет-магазин"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title(
        'Контакты - Редирект на страницу "Согласие и политика по обработке персональных данных" по ссылке из текста '
        'чекбокса формы "Связаться со службой поддержки" из вкладки "Интернет-магазин"')
    @allure.testcase(url='https://testit..ru/browse/28872')
    def test_check_open_conf_agreement_page_in_internet_shop_tab(self, site_contacts_page):
        form_support = site_contacts_page.form_support() \
            .goto_internet_shop_form()

        with allure.step('Нажать на гиперссылку '
                         '"Я даю согласие на обработку своих персональных данных и проверить страницу перехода"'):
            confidentiality_agreement_page = form_support.click_url_in_label()
            actual_url = confidentiality_agreement_page.get_current_url()
            expect_url = f'{confidentiality_agreement_page.base_url}{confidentiality_agreement_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

        with allure.step('Проверить наличие документов на странице'):
            documents = confidentiality_agreement_page.get_documents_count()
            assert documents > 0, 'На странице отсутствуют документы'
