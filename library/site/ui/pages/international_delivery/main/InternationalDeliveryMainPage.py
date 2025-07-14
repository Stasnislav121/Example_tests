from library.site.ui.pages.international_delivery import *


class InternationalDeliveryMainPage(InternationalDeliveryBasePage):
    page_element = ':text("Why ?")'
    page_route = '/international-delivery'

    @staticmethod
    def open(page):
        return InternationalDeliveryMainPage(page).open_url('/international-delivery').check_page()
