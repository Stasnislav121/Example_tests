import allure

from library.site.ui import *
from library.site.ui.pages import *


class PrivateClientsBasePage(HomePage):
    page_element = '.header__nav'
    css_desktop_lk = '.button-accounts_header-desktop'
    css_mobile_lk = '.header-mobile__login'

    def menu_navigation(self):
        with allure.step('Обращение к меню навигации на вкладке "Частным клиентам"'):
            from library.site.ui.menus.PrivateClientsMenu import PrivateClientsMenu
            return PrivateClientsMenu(self.page)

    def menu_lk(self):
        with allure.step('Обратится к меню "Личный кабинет"'):
            if self.is_mobile:
                self.set_scroll_top(0)
                self.click(self.css_mobile_lk, 'Вход', force=False)
                self.wait_for_selector('#personalAccountModal')
            else:
                self.click(self.css_desktop_lk, 'Личный кабинет', force=False)
                self.wait_for_selector('.header-desktop .personal-accounts_open-menu')

            from library.site.ui.menus.LkMenu import LkMenu
            return LkMenu(self.page)
