import allure

from .BaseEcommerceJoinForm import BaseEcommerceJoinForm


class EcommerceMainJoinForm(BaseEcommerceJoinForm):
    page_element = '#reg-form'
    css_title = '.legend:text("Регистрация")'
    css_phone = '[type="tel"]'
    css_social_link = '[placeholder="Ссылка на соцсети"]'
    css_city = f'{page_element} .multiselect_city'
    css_personal_agreement = '[for="reg-form_agreement"]'
    css_subscription = '[for="reg-form_subscription"]'
    css_send_request = '.reg-form__btn:text("Зарегистрироваться ")'

    def check_element(self, screen=False):
        with allure.step("Проверить блок 'Регистрация'"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('EcommerceMainJoinForm_loaded', locator=self.page_element)
        return self
