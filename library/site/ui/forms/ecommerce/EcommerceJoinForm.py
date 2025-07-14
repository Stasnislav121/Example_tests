import allure

from .BaseEcommerceJoinForm import BaseEcommerceJoinForm


class EcommerceJoinForm(BaseEcommerceJoinForm):
    page_element = '#form_ecom'
    css_title = '.form__title:text("Подключитесь к ")'
    css_phone = '[type="phone"]'
    css_social_link = '[placeholder="Ссылка на соц.сети"]'
    css_city = '.form_join .multiselect_city'
    css_personal_agreement = '[for="agreement"]'
    css_subscription = '[for="subscription"]'
    css_send_request = '.form__button:text("Отправить заявку")'

    def check_element(self, screen=False):
        with allure.step("Подключитесь к '"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('EcommerceJoinForm_loaded', locator=self.page_element)
        return self
