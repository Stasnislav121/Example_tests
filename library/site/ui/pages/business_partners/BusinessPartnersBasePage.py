from library.site.ui import *
from library.site.ui.pages import *


class BusinessPartnersBasePage(HomePage):
    page_element = '.header__nav'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "Бизнес-партнерам"'):
            from library.site.ui.menus.BusinessPartnersMenu import BusinessPartnersMenu
            return BusinessPartnersMenu(self.page)
