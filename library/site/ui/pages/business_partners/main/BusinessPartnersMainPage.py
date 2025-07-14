import allure

from library.site.ui.pages.business_partners import *


class BusinessPartnersMainPage(BusinessPartnersBasePage):
    page_element = '.slide-top__title:text(" — это не только служба доставки")'
    page_route = '/biznes-partneram'

    @staticmethod
    def open(page):
        return BusinessPartnersMainPage(page).open_url('/biznes-partneram').check_page()

    def goto_open_point_page(self):
        with allure.step('Кликнуть на кнопку "Узнать больше" в блоке '
                         '"Партнерский пункт выдачи заказов на базе существующего бизнеса" и перейти на страницу '
                         '"Откройте пункт выдачи заказов в своем городе"'):
            with self.expect_page() as page_info:
                self.click('[href="/biznes-partneram/open-point-pvz"]')
            new_page = page_info.value

        from library.site.ui import OpenPointPage
        return OpenPointPage(new_page)
