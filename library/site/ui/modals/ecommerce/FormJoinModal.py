import allure

from library.site.ui import BasePage


class FormJoinModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector('#popupPromo')
        self.screenshot('form_join_modal_opened')

    def form_join(self):
        with allure.step('Обращение к форме "Подключитесь к "'):
            from library.site.ui import EcommerceJoinForm
            form = EcommerceJoinForm(self.page).check_element()
            form.set_parent(self)
        return form
