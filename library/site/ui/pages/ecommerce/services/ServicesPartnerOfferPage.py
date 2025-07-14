import allure

from library.site.ui.pages.ecommerce import *


class ServicesPartnerOfferPage(EcommerceBasePage):
    page_element = '[href="/e-commerce/uslugi/partner-offer"]'
    css_join_button = '.btn_red:text("Подключиться к  и получить бонус")'

    def open_form_join_modal(self):
        with allure.step('Кликнуть на кнопку "Подключиться к  и получить бонус" и обратиться к модальному окну '
                         '"Подключитесь к "'):
            # self.wait_for_load_state(state='networkidle')
            self.wait_for_timeout(5)
            self.click(self.css_join_button, force=False)
            from library.site.ui import FormJoinModal
            form = FormJoinModal(self.page)
            form.set_parent(self)
        return form
