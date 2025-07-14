import testit
import allure

from library.site.ui.pages import *


class TestFormOpenPoint:
    @testit.workItemIds(14863)
    @testit.externalId('TestFormOpenPoint_14863')
    @testit.nameSpace('Бизнес-партнерам')
    @testit.className('Форма "Заявка на открытие пункта выдачи "')
    @testit.displayName('Малая форма РФ "Заявка на открытие пункта выдачи "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Бизнес-партнерам')
    @allure.title('Бизнес-партнерам - Малая форма РФ "Заявка на открытие пункта выдачи "')
    @allure.testcase(url='https://testit..ru/browse/14863')
    def test_form_open_point_russia_small(self, site_business_partners_page):
        form_open_point = site_business_partners_page.goto_open_point_page() \
            .form_open_point()

        with allure.step('Заполнить форму и отправить обращение'):
            success_modal = form_open_point.set_fullname() \
                .set_phone() \
                .set_email() \
                .select_city() \
                .select_address() \
                .click_personal_agreement() \
                .click_send_request() \
                .click_no_complete()

        with allure.step('Проверить текст сообщения в модальном окне'):
            text = success_modal.get_modal_text()
            text = text.replace('\n\n', '\n')  # в браузерах по-разному считываются пробелы, приводим к одному виду
            assert text == 'Ваша заявка отправлена!\n' \
                           'Наш менеджер свяжется с Вами в течение 3-х рабочих дней\n' \
                           'На указанную Вами электронную почту направлено письмо с условиями сотрудничества.'

    @testit.workItemIds(14982)
    @testit.externalId('TestFormOpenPoint_14982')
    @testit.nameSpace('Бизнес-партнерам')
    @testit.className('Форма "Заявка на открытие пункта выдачи "')
    @testit.displayName('Малая форма РК "Заявка на открытие пункта выдачи "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Бизнес-партнерам')
    @allure.title('Бизнес-партнерам - Малая форма РК "Заявка на открытие пункта выдачи "')
    @allure.testcase(url='https://testit..ru/browse/14982')
    def test_form_open_point_kz_small(self, site_business_partners_page):
        form_open_point = site_business_partners_page.goto_open_point_page() \
            .form_open_point() \
            .goto_kz_form()

        with allure.step('Заполнить форму и отправить обращение'):
            success_modal = form_open_point.set_fullname() \
                .set_phone() \
                .set_email() \
                .select_city() \
                .set_address() \
                .click_personal_agreement() \
                .click_send_request()

        with allure.step('Проверить текст сообщения в модальном окне'):
            text = success_modal.get_modal_text()
            text = text.replace('\n\n', '\n')  # в браузерах по-разному считываются пробелы, приводим к одному виду
            assert text == 'Спасибо, Ваша заявка принята\n'\
                           'На указанную Вами электронную почту направлено письмо с условиями сотрудничества.\n' \
                           'Наш менеджер свяжется с Вами в течение 3-х рабочих дней. ' \
                           'Благодарим за интерес к компании '

    @testit.workItemIds(14864)
    @testit.externalId('TestFormOpenPoint_14864')
    @testit.nameSpace('Бизнес-партнерам')
    @testit.className('Форма "Заявка на открытие пункта выдачи "')
    @testit.displayName('Большая форма РФ "Заявка на открытие пункта выдачи "')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Бизнес-партнерам')
    @allure.title('Бизнес-партнерам - Большая форма РФ "Заявка на открытие пункта выдачи "')
    @allure.testcase(url='https://testit..ru/browse/14864')
    def test_form_open_point_russia_large(self, site_business_partners_page):
        form_open_point = site_business_partners_page.goto_open_point_page() \
            .form_open_point()

        with allure.step('Заполнить малую форму'):
            large_form = form_open_point.set_fullname() \
                .set_phone() \
                .set_email() \
                .select_city() \
                .select_address() \
                .click_personal_agreement() \
                .click_send_request() \
                .click_yes_continue()

        with allure.step('Заполнить большую форму и отправить обращение'):
            large_form.select_legal_form() \
                .set_legal_name() \
                .set_legal_registration_date() \
                .set_legal_inn() \
                .select_legal_type_activity() \
                .select_taxation_system() \
                .select_cash_availability() \
                .select_acquiring_availability() \
                .select_security_availability() \
                .select_video_availability() \
                .click_send_request()
