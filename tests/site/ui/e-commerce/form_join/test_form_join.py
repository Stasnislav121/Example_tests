import random
import pytest
import testit
import allure

from library.site.ui.pages import *


class TestFormJoin:
    @testit.workItemIds(13808)
    @testit.externalId('TestFormJoin_13808')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('Форма "Подключитесь к "')
    @testit.displayName('Форма "Подключитесь к "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Интернет-магазинам')
    @allure.title('Форма "Подключитесь к "')
    @allure.testcase(url='https://testit..ru/browse/13808')
    @pytest.mark.parametrize('page_to_check', [
        'Бизнесу',
        'Доставка в страны СНГ'
    ])
    def test_form_join_send_request(self, site_ecommerce_page, string_helper, page_to_check):
        with allure.step(f'Открыть страницу "{page_to_check}"'):
            if page_to_check == 'Бизнесу':
                ecommerce_page = site_ecommerce_page
            elif page_to_check == 'Доставка в страны СНГ':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_delivery_to_cis()

        phone = f'999{random.randint(10000000, 99999999)}'
        email = string_helper.get_random_email()

        with allure.step('Заполнить и отправить форму'):
            form_join = ecommerce_page.form_join()
            form_join.set_legal_entity() \
                .set_phone(phone) \
                .set_site() \
                .set_social_link() \
                .set_fullname() \
                .set_email(email) \
                .select_city('Москва') \
                .click_subscription() \
                .click_personal_agreement() \
                .click_send_request()


    @testit.workItemIds(13809)
    @testit.externalId('TestFormJoin_13809')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('Форма "Подключитесь к "')
    @testit.displayName('Проверка редиректа на страницу "Согласие и политика по обработке персональных данных" '
                        'по ссылке из текста чекбокса формы "Подключитесь к " /e-commerce/"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Интернет-магазинам')
    @allure.title('Форма "Подключитесь к " - Проверка редиректа на страницу "Согласие и политика '
                  'по обработке персональных данных" по ссылке из текста чекбокса')
    @allure.testcase(url='https://testit..ru/browse/13809')
    @pytest.mark.parametrize('page_to_check', [
        'Бизнесу',
        'Доставка в страны СНГ'
    ])
    def test_check_open_conf_agreement_page_with_checkbox_label(self, site_ecommerce_page, page_to_check):
        with allure.step(f'Открыть страницу "{page_to_check}"'):
            if page_to_check == 'Бизнесу':
                ecommerce_page = site_ecommerce_page
            elif page_to_check == 'Доставка в страны СНГ':
                ecommerce_page = site_ecommerce_page.menu_navigation() \
                    .open_services_delivery_to_cis()

        with allure.step('Нажать на гиперссылку '
                         '"Я даю согласие на обработку своих персональных данных и проверить страницу перехода"'):
            confidentiality_agreement_page = ecommerce_page.form_join() \
                .click_url_in_label()
            actual_url = confidentiality_agreement_page.get_current_url()
            expect_url = f'{confidentiality_agreement_page.base_url}{confidentiality_agreement_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

        with allure.step('Проверить наличие документов на странице'):
            documents = confidentiality_agreement_page.get_documents_count()
            assert documents > 0, 'На странице отсутствуют документы'
