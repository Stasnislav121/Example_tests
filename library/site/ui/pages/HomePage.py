import allure

from library.site.ui.pages import *


class HomePage(BasePage):
    page_element = ".header__row"
    css_loader = '.loader-overlay'
    css_cookie_accept = '.cookie-info__btn'
    css_city_confirm_desktop = '.header-desktop .city-submit[style="opacity: 1;"] .button_green'
    css_city_confirm_mobile = '.header-mobile city-submit[style="opacity: 1;"] .button_green'
    css_mobile_app_close = '.mobile-store-upper__btn-close'
    css_modal = '.modal'
    css_modal_close = '.modal [class*="icon-close"]'
    # css_modal_close = '.modal-survey-form__close'
    city_confirmed = False
    cookies_accepted = False
    mobile_app_closed = False
    modal_closed = False

    @staticmethod
    def open(page):
        from library.site.ui.pages.private_clients.main.PrivateClientsMainPage import PrivateClientsMainPage
        return PrivateClientsMainPage(page).open_url('').check_page()

    def menu_tabs(self):
        with allure.step("Обращение к верхнему меню переключения вкладок"):
            from library.site.ui.menus.TabMenuHeader import TabMenuHeader
            return TabMenuHeader(self.page)

    def block_mobile_app(self):
        with allure.step("Обращение к блоку раздела мобильного приложения "):
            from library.site.ui.blocks.mobile_app.MobileAppBlock import MobileAppBlock
            return MobileAppBlock(self.page).check_element(screen=False)

    def wait_loaders(self):
        try:
            for _ in range(10):
                self.wait_for_selector(self.css_loader, state='detached')
        except Exception as ex:
            self.screenshot('error_loader_not_disappear')
            raise Exception(f"Функция wait_loader не дождалась исчезновения элемента '{self.css_loader}': {ex.args}") \
                from ex
        return self

    def accept_all(self):
        with allure.step("Принять / закрыть все всплывающие окна, если они еще не были приняты / закрыты"):
            if not self.modal_closed:
                self.close_modal()
            self.mouse_wheel(0, 10)  # scroll нужен для появления всплывающих окон
            if not self.cookies_accepted:
                self.accept_cookies_if_exists()
            if not self.city_confirmed:
                self.confirm_city_if_exists()
            if self.is_mobile and not self.mobile_app_closed:
                self.close_mobile_app_if_exists()
        return self

    def close_mobile_app_if_exists(self):
        with allure.step("Закрыть окно с загрузкой мобильного приложения"):
            for _ in range(100):
                hint_visible = self.is_visible(self.css_mobile_app_close)
                if hint_visible:
                    self.click(self.css_mobile_app_close, force=False)
                    self.mobile_app_closed = True
                    break
        return self

    def close_modal(self):
        with allure.step("Закрыть модальное окно"):
            for _ in range(100):
                modal_visible = self.is_visible(self.css_modal)
                if modal_visible:
                    self.click(self.css_modal_close, force=False)
                    self.modal_closed = True
                    break
        return self

    def accept_cookies_if_exists(self):
        with allure.step("Принять cookies, если окно с запросом отображается"):
            for _ in range(100):
                cookie_visible = self.is_visible(self.css_cookie_accept)
                if cookie_visible:
                    self.accept_cookies()
                    self.cookies_accepted = True
                    break
        return self

    def confirm_city_if_exists(self):
        with allure.step("Подтвердить свой город, если окно с запросом отображается"):
            locators = [self.css_city_confirm_desktop, self.css_city_confirm_mobile]
            for locator in locators:
                for _ in range(100):
                    is_visible = self.is_visible(locator)
                    if is_visible:
                        self.click(locator, 'Да', force=False)
                        self.city_confirmed = True
                        return self
        return self

    def accept_cookies(self):
        with allure.step("Принять cookies"):
            if self.is_mobile:
                # self.run_js(f"document.querySelector('{self.css_cookie_accept}').click()")
                self.click(self.css_cookie_accept, 'Согласен', force=False)
            else:
                self.click(self.css_cookie_accept, 'Согласен', force=False)
        return self
