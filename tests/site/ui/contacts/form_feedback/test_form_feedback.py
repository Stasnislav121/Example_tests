import testit
import allure

from library.site.ui.pages import *


class TestFormFeedback:
    @testit.workItemIds(13103)
    @testit.externalId('TestPrivateClients_13103')
    @testit.nameSpace('Контакты')
    @testit.className('Форма "Форма обратной связи"')
    @testit.displayName('Форма "Форма обратной связи"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Контакты')
    @allure.title('Контакты - Форма "Форма обратной связи"')
    @allure.testcase(url='https://testit..ru/browse/13103')
    def test_form_feedback(self, site_contacts_page):
        form_feedback = site_contacts_page.menu_navigation() \
            .open_press_service() \
            .form_feedback()

        with allure.step('Заполнить форму и отправить обращение'):
            form_feedback.set_name() \
                .set_press_name() \
                .set_phone() \
                .set_email() \
                .set_deadline() \
                .set_text_request() \
                .click_personal_agreement() \
                .click_send_request()
