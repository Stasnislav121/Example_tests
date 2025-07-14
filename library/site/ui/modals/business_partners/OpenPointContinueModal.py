import allure

from library.site.ui import BasePage


class OpenPointContinueModal(BasePage):
    page_element = '.popup-need-more'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.page_element)
        self.screenshot('OpenPointContinueModal_loaded', locator=self.page_element)

    def click_no_complete(self):
        with allure.step('Кликнуть на кнопку "Нет, завершить" и обратиться к модальному окну об успешной отправке'):
            self.click('.popup-need-more__btn:has-text("Нет, завершить")', force=False)
            from library.site.ui import SuccessMessageModal
            modal = SuccessMessageModal(self.page)
        return modal

    def click_yes_continue(self):
        with allure.step('Кликнуть на кнопку "Да, хочу продолжить" и обратиться к форме заполнения заявки РФ'):
            self.click('.btn_green:has-text("Да, хочу продолжить")', force=False)
            from library.site.ui import BusinessPartnersOpenPointLargeForm
            form = BusinessPartnersOpenPointLargeForm(self.page)
        return form
