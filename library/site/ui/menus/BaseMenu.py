import allure

from library.site.ui.pages import *


class BaseMenu(BasePage):
    css_map = {}

    def open_menu(self, menu):
        with allure.step(f"Открыть раздел [{menu}]"):
            if self.is_mobile:
                self.click('.mobile-header-tab__burger')
                self.click(f'.mobile-header-tabs {self.css_map[menu]}', force=False)
            else:
                self.click(f'.header-desktop {self.css_map[menu]}', force=False)
        return self

    def open_submenu(self, menu, submenu):
        with allure.step(f"Открыть в верхнем меню [{menu}] раздел [{submenu}]"):
            if self.is_mobile:
                self.click('.mobile-header-tab__burger')
                self.click(f'.mobile-header-tabs .header-dropdown__title:text("{menu}")', force=False)
                self.click(f'.mobile-header-tab__menu {self.css_map[menu][submenu]}', force=False)
            else:
                self.hover(f'.header-desktop .tabs__item_submenu a:text("{menu}")')
                self.click(f'.header-desktop {self.css_map[menu][submenu]}', force=False)

        return self

    def open_menu_desktop(self, menu):
        with allure.step(f"Открыть раздел [{menu}]"):
            if self.is_mobile:
                self.click('.header-desktop .header__hamburger', force=False)
                self.wait_for_selector('.header__hamburger_open')
                self.click(f'.header-desktop .header-dropdown__item {self.css_map[menu]}', force=False)
            else:
                self.wait_for_selector(f'.header__nav .tabs__item a:text("{menu}")')
                self.click(f'.header-desktop {self.css_map[menu]}', force=False)

        return self

    def open_submenu_desktop(self, menu, submenu):
        with allure.step(f"Открыть в верхнем меню [{menu}] раздел [{submenu}]"):
            if self.is_mobile:
                self.click('.header-desktop .header__hamburger', force=False)
                self.wait_for_selector('.header__hamburger_open')
                self.click(f'.header-desktop .header-dropdown__title:text("{menu}")', force=False)
                self.click(f'.header-dropdown__item_active {self.css_map[menu][submenu]}', force=False)
            else:
                self.wait_for_selector(f'.header-desktop .tabs__item_submenu a:text("{menu}")')
                self.hover(f'.header-desktop .tabs__item_submenu a:text("{menu}")')
                self.click(f'.header-desktop {self.css_map[menu][submenu]}', force=False)

        return self
