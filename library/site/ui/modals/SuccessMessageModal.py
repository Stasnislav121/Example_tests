import allure

from library.site.ui import BasePage


class SuccessMessageModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector('.success-message')

    def close_modal(self):
        with allure.step('Кликнуть на иконку закрытия модального окна'):
            self.click('.modal__close')
            self.wait_for_selector('.success-message', state='detached')
        return self

    def get_modal_text(self) -> str:
        with allure.step('Считать текст из модального окна'):
            return self.inner_text('.success-message__text')
