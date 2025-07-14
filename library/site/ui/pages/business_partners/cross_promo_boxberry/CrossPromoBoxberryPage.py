import allure

from library.site.ui.pages.business_partners import *


class CrossPromoPage(BusinessPartnersBasePage):
    page_element = ':text("Что мы предлагаем")'
    page_route = '/biznes-partneram/kross-promo-s-'

    def form_ad(self):
        with allure.step('Обращение к форме "Подключитесь к "'):
            from library.site.ui import BusinessPartnersAdForm
            form = BusinessPartnersAdForm(self.page)
            form.set_parent(self)
        return form
