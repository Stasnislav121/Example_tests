import allure

from library.site.ui.pages.ecommerce import *


class ServicesAcceptancePointsPage(EcommerceBasePage):
    page_element = '.pageTitle__title:text("Пункты приема посылок от интернет-магазинов")'
    page_route = '/e-commerce/uslugi/punkty-priema-posylok-ot-internet-magazinov'

    @staticmethod
    def open(page):
        return ServicesAcceptancePointsPage(page).open_url('/e-commerce/uslugi/punkty-priema-posylok-ot-internet'
                                                           '-magazinov').check_page()

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.map.common.PointMap import PointMap
            block = PointMap(self.page)
            block.set_parent(self)
        return block
