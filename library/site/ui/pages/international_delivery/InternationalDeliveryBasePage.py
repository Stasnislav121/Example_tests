from library.site.ui import *
from library.site.ui.pages import *


class InternationalDeliveryBasePage(HomePage):
    page_element = '.header__nav'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "International delivery"'):
            from library.site.ui.menus.InternationalDeliveryMenu import InternationalDeliveryMenu
            return InternationalDeliveryMenu(self.page)
