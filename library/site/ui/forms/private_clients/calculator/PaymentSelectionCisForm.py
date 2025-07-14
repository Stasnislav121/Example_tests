import allure

from library.site.ui.pages.BasePage import BasePage
from library.site.ui.pages import TermsDocumentsPage


class PaymentSelectionCisForm(BasePage):
    page_element = '[name="calculator_pip"]'
    css_title = '.calc-pay__title'
    css_offer_agreement = '.payment-info__checkbox-label'

    def check_element(self, screen=False):
        with allure.step('Проверить форму "Создание посылки"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.wait_for_selector(self.page_element)
                self.screenshot('PaymentSelectionCisForm_loaded', locator=self.page_element)

            with allure.step('Проверить отображение основного контента формы'):
                with allure.step('Отображается заголовок: "Ваше отправление"'):
                    self.wait_for_selector(f'{self.css_title}:text("Ваше отправление")')
        return self

    def click_url_in_label_personal_agreement(self):
        with allure.step(
                'Кликнуть по словам "условиями оферты" в тексте "Нажимая “Оплатить” вы соглашаетесь c условиями оферты"'
        ):
            with self.expect_page() as document_page:
                self.click(f'{self.css_offer_agreement} a', force=False)
            new_page = document_page.value
        return TermsDocumentsPage(new_page).check_page()
