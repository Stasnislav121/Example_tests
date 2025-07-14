import allure

from library.site.ui.pages.ecommerce import *


class ServicesDeliveryToCISPage(EcommerceBasePage):
    page_element = ':text("Как начать продавать в страны СНГ")'
    page_route = '/e-commerce/uslugi/dostavka-v-kazahstan-i-belarus'

    @staticmethod
    def open(page):
        return ServicesDeliveryToCISPage(page).open_url('/e-commerce/uslugi/dostavka-v-kazahstan-i-belarus') \
            .check_page()

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.map.common.PointMap import PointMap
            block = PointMap(self.page)
            block.set_parent(self)
        return block

    def form_join(self):
        with allure.step('Обращение к форме "Подключитесь к "'):
            from library.site.ui import EcommerceJoinForm
            form = EcommerceJoinForm(self.page).check_element()
            form.set_parent(self)
        return form
