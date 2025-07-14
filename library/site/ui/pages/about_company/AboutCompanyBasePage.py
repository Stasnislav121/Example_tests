from library.site.ui import *
from library.site.ui.pages import *


class AboutCompanyBasePage(HomePage):
    page_element = '.header__nav'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "О компании"'):
            from library.site.ui.menus.AboutCompanyMenu import AboutCompanyMenu
            return AboutCompanyMenu(self.page)
