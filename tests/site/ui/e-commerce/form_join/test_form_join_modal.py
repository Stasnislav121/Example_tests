import random
import testit
import allure

from library.site.ui.pages import *
from datetime import datetime


class TestFormJoinModal:
    @testit.workItemIds(13810)
    @testit.externalId('TestFormJoinModal_13810')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('Форма "Подключитесь к "')
    @testit.displayName('Модальная форма "Подключитесь к "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Интернет-магазинам')
    @allure.title('Модальная форма "Подключитесь к "')
    @allure.testcase(url='https://testit..ru/browse/13810')
    def test_form_join_modal_send_request(self, site_ecommerce_page):
        form_join = site_ecommerce_page.menu_navigation() \
            .open_services_bonuses_from_partners() \
            .goto_offer_detail_page() \
            .open_form_join_modal() \
            .form_join()

        phone = f'999{random.randint(1000000, 9999999)}'
        email = f'site_autotest_{int(datetime.now().timestamp())}@.ru'

        with allure.step('Заполнить и отправить форму'):
            form_join.set_legal_entity() \
                .set_phone(phone) \
                .set_site() \
                .set_social_link() \
                .set_fullname() \
                .set_email(email) \
                .select_city('Москва') \
                .click_subscription() \
                .click_personal_agreement() \
                .wait_for_timeout(2) \
                .click_send_request()


    @testit.workItemIds(13811)
    @testit.externalId('TestFormJoinModal_13811')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('Форма "Подключитесь к "')
    @testit.displayName('Модальная форма "Подключитесь к "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Интернет-магазинам')
    @allure.title('Модальная форма "Подключитесь к " - Проверка редиректа на страницу'
                  ' "Согласие и политика по обработке персональных данных" по ссылке из текста чекбокса')
    @allure.testcase(url='https://testit..ru/browse/13811')
    def test_check_open_conf_agreement_page_with_modal_checkbox_label(self, site_ecommerce_page):
        form_join = site_ecommerce_page.menu_navigation() \
            .open_services_bonuses_from_partners() \
            .goto_offer_detail_page() \
            .open_form_join_modal() \
            .form_join()

        with allure.step('Нажать на гиперссылку "Я даю согласие на обработку своих персональных данных'
                         ' и проверить страницу перехода"'):
            confidentiality_agreement_page = form_join.click_url_in_label()
            actual_url = confidentiality_agreement_page.get_current_url()
            expect_url = f'{confidentiality_agreement_page.base_url}{confidentiality_agreement_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

        with allure.step('Проверить наличие документов на странице'):
            documents = confidentiality_agreement_page.get_documents_count()
            assert documents > 0, 'На странице отсутствуют документы'
