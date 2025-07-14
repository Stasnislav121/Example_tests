import allure

from library.site.ui import *
from library.site.ui.pages import *


class EcommerceBasePage(HomePage):
    page_element = '.header__nav'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "Интернет-магазинам"'):
            from library.site.ui.menus.EcommerceClientsMenu import EcommerceClientsMenu
            return EcommerceClientsMenu(self.page)
