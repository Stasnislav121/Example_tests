from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class InternationalDeliveryMenu(BaseMenu):
    css_map = {
        'eCom solution': 'a[href="/international-delivery/business-solutions"]',
        ' offer': 'a[href="/international-delivery/-offer"]',
        'Guarantees and Insurance': 'a[href="/international-delivery/guarantees-and-insurance"]',
        'Marketplace': 'a[href="/international-delivery/marketplace_solution"]',
        'Returns to ASOS': 'a[href="/international-delivery/international-return-to-asos"]'
    }

    def open_ecom_solution(self):
        self.open_menu_desktop('eCom solution')
        return EComSolutionPage(self.page).check_page()

    def open__offer(self):
        self.open_menu_desktop(' offer')
        return OfferPage(self.page).check_page()

    def open_guarantees_and_insurance(self):
        self.open_menu_desktop('Guarantees and Insurance')
        return GuaranteesAndInsurancePage(self.page).check_page()

    def open_marketplace(self):
        self.open_menu_desktop('Marketplace')
        return MarketplacePage(self.page).check_page()

    def open_returns_to_asos(self):
        self.open_menu_desktop('Returns to ASOS')
        return ReturnsToAsosPage(self.page).check_page()
