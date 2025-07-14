import allure

from library.site.ui.pages import *


class TabMenuHeader(BasePage):
    css_map = {
        'Частным клиентам': 'a[href="/"]',
        'Контакты': 'a[href="/kontakty"]',
        'Бизнесу': 'a[href="/e-commerce"]',
        'Партнерам': 'a[href="/biznes-partneram"]',
        'International delivery': 'a[href="/international-delivery"]',
        'О компании': 'a[href="/o-kompanii"]'
    }

    def open_tab(self, name):
        with allure.step(f"Переключиться в верхнем меню на вкладку [{name}]"):
            if self.is_mobile:
                self.set_scroll_top(0)
                self.click('.header-mobile .dropdown__item_active')
                self.wait_for_selector('.header-mobile .dropdown__item_active')
                self.click(f'.header-mobile {self.css_map[name]}', force=False)
            else:
                self.click(f'.header-desktop {self.css_map[name]}', force=False)
        return self

    def open_private_clients(self):
        self.open_tab('Частным клиентам')
        return ClientsMainPage(self.page).check_page()

    def open_contacts(self):
        self.open_tab('Контакты')
        return ContactsMainPage(self.page).check_page()

    def open_ecommerce(self):
        self.open_tab('Бизнесу')
        return EcommerceMainPage(self.page).check_page()

    def open_business_partners(self):
        self.open_tab('Партнерам')
        return BusinessPartnersMainPage(self.page).check_page()

    def open_international_delivery(self):
        self.open_tab('International delivery')
        return InternationalDeliveryMainPage(self.page).check_page()

    def open_about_company(self):
        self.open_tab('О компании')
        return AboutCompanyMainPage(self.page).check_page()

    def search_on_site(self, value):
        with allure.step(f'Произвести поиск значением: {value}'):
            self.click('.header-search__input')
            self.press_sequentially('.header-search__input', value)
            self.click_locator('.header-search__input')
            self.screenshot('request_value_set')
            self.click('.header-search__button')
            from library.site.ui import SearchPage
            return SearchPage(self.page).check_element()
