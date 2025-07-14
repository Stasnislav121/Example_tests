import allure

from library.site.ui import *
from library.site.ui.pages import *


class ContactsBasePage(HomePage):
    page_element = '.header__nav'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "Контакты"'):
            from library.site.ui.menus.ContactsMenu import ContactsMenu
            return ContactsMenu(self.page)
