import testit
import allure
from library.site.site_const import *


class TestFormCalculatorRedirectToDocumentPage:
    @testit.workItemIds(28964)
    @testit.externalId('TestFormCalculator_28964')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Выбор отправителя и получателя"')
    @testit.displayName('Переход по ссылке "Я согласен на обработку персональных данных и с Офертой Боксберри" из '
                        'формы "Данные отправителя и получателя"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Выбор отправителя и получателя"')
    @allure.title('Переход по ссылке "Я согласен на обработку персональных данных и с Офертой Боксберри" из формы '
                  '"Данные отправителя и получателя"')
    @allure.testcase(url='https://testit..ru/browse/28964')
    def test_redirect_to_documents_page_by_url_in_label_on_data_form(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Выбрать направление РФ-РФ'):
            block_own_package = form_calculator.select_sender_city() \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY)

        with allure.step('Дозаполнить данные и дойти до формы "Данные отправителя и получателя"'):
            data_form = block_own_package.select_own_package() \
                .goto_sender_point_form() \
                .select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step() \
                .select_point_from_list(CREATE_PARCEL_RF_RECEIVER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Нажать на гиперссылку "Я согласен на обработку персональных данных и с Офертой Боксберри"'):
            document_page = data_form.click_url_in_label_personal_agreement()
            actual_url = document_page.get_current_url()
            expect_url = f'{document_page.base_url}{document_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

    @testit.workItemIds(31318)
    @testit.externalId('TestFormCalculator_31318')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Выбор отправителя и получателя"')
    @testit.displayName('Переход по ссылке "Нажимая “Оплатить” вы соглашаетесь c условиями оферты" из формы'
                        ' "Оплата" СНГ-РФ, плательщик = Отправитель')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Оплата"')
    @allure.title('Переход по ссылке "Нажимая “Оплатить” вы соглашаетесь c условиями оферты" из формы "Оплата" СНГ-РФ,'
                  ' плательщик = Отправитель')
    @allure.testcase(url='https://testit..ru/browse/31318')
    def test_redirect_to_documents_page_by_url_in_label_on_payment_selection_form(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Выбрать направление СНГ-РФ'):
            block_own_package = form_calculator.select_sender_country('Беларусь') \
                .select_sender_city(CREATE_PARCEL_BELARUS_SENDER_CITY) \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_FROM_CIS_RECEIVER_CITY)

        with allure.step('Дозаполнить данные и дойти до формы "Данные отправителя и получателя"'):
            data_form = block_own_package.set_package_weight() \
                .set_own_package_size() \
                .goto_sender_point_form() \
                .select_point_from_list(CREATE_PARCEL_BELARUS_SENDER_POINT_ADDRESS) \
                .goto_next_step() \
                .select_point_from_list(CREATE_PARCEL_RF_RECEIVER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Заполнить форму "Данные отправителя и получателя" и выбрать Плательщик = Отправитель'):
            payment_selection_form = data_form.fill_form_payer_sender_cis() \
                .goto_next_step(cis_sender_payer=True)

        with allure.step('Нажать на гиперссылку "Нажимая “Оплатить” вы соглашаетесь c условиями оферты"'):
            document_page = payment_selection_form.click_url_in_label_personal_agreement()
            actual_url = document_page.get_current_url()
            expect_url = f'{document_page.base_url}{document_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'

    @testit.workItemIds(36238)
    @testit.externalId('TestFormCalculator_36238')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Выбор отправителя и получателя"')
    @testit.displayName('Переход по ссылке в "Ознакомлен со списком запрещенных к перевозке грузов" из '
                        'формы "Данные отправителя и получателя"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Выбор отправителя и получателя"')
    @allure.title('Переход по ссылке в "Ознакомлен со списком запрещенных к перевозке грузов" из формы '
                  '"Данные отправителя и получателя"')
    @allure.testcase(url='https://testit..ru/browse/36238')
    def test_redirect_to_prohibited_goods_page_by_url_in_label_on_data_form(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Выбрать направление РФ-РФ'):
            block_own_package = form_calculator.select_sender_city() \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY)

        with allure.step('Дозаполнить данные и дойти до формы "Данные отправителя и получателя"'):
            data_form = block_own_package.select_own_package() \
                .goto_sender_point_form() \
                .select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step() \
                .select_point_from_list(CREATE_PARCEL_RF_RECEIVER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Нажать на гиперссылку "запрещенных к перевозке грузов" в тексте "Ознакомлен со списком '
                         'запрещенных к перевозке грузов"'):
            document_page = data_form.click_url_in_label_prohibited_goods()
            actual_url = document_page.get_current_url()
            expect_url = f'{document_page.base_url}{document_page.page_route}'
            assert actual_url == expect_url, f'Ожидалась страница {expect_url}, а открыта {actual_url}'
