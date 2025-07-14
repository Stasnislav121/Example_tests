import allure

from library.site.ui.pages.ecommerce import *


class ServicesBonusesFromPartnersPage(EcommerceBasePage):
    page_element = '.partner-offer-catalog'
    page_route = '/e-commerce/uslugi/partner-offer'
    css_offer = '.partner-offer-catalog .prizes__col'

    @staticmethod
    def open(page):
        return ServicesBonusesFromPartnersPage(page).open_url('/e-commerce/uslugi/partner-offer').check_page()

    def get_offer_catalog(self):
        with allure.step('Считать данные из каталога предложений партнеров'):
            offers = []
            offer_cnt = self.count(self.css_offer)
            for i in range(offer_cnt):
                offer = {
                    'Название': self.get_attribute(f'{self.css_offer}:nth-child({i + 1})', 'alt'),
                    'Текст': self.inner_text(f'{self.css_offer}:nth-child({i + 1}) .partner-offer-card__text'),
                    'Ссылка': self.get_attribute(f'{self.css_offer}:nth-child({i + 1}) a', 'href')
                }
                offers.append(offer)

        return offers

    def goto_offer_detail_page(self):
        with allure.step('Кликнуть на кнопку "Подробнее" напротив первого предложения в каталоге'):
            self.click('a.partner-offer-card__btn')
        from library.site.ui import ServicesPartnerOfferPage
        return ServicesPartnerOfferPage(self.page)
