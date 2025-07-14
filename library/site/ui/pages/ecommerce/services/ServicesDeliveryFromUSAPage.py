import allure

from library.site.ui.pages.ecommerce import *
from library.site.ui import *


class ServicesDeliveryFromUSAPage(EcommerceBasePage):
    page_element = ':text("Доставка в Россию из США, Европы и Азии")'
    page_route = '/e-commerce/uslugi/dostavka-iz-ssa-evropy-i-azii-dla-internet-magazinov'

    def form_personal_offer(self):
        with allure.step('Обращение к форме "Получите персональное предложение"'):
            from library.site.ui import EcommercePersonalOfferForm
            form = EcommercePersonalOfferForm(self.page)
            form.set_parent(self)
        return form
