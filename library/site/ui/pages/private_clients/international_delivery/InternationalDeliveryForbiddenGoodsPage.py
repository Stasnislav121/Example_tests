from library.site.ui.pages.private_clients import *
from library.site.ui import *


class InternationalDeliveryForbiddenGoodsPage(PrivateClientsBasePage):
    page_element = ':text("Товары, запрещенные к международной перевозке")'
    page_route = '/castnym-klientam/mn-dostavka/tovary,-zapresennye-k-mezdunarodnoj-perevozke'
