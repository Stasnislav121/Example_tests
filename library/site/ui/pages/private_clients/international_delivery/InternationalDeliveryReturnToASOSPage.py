from library.site.ui.pages.private_clients import *
from library.site.ui import *


class InternationalDeliveryReturnToASOSPage(PrivateClientsBasePage):
    page_element = ':text("Сейчас интернет-магазин ASOS временно прекратил принимать возвраты")'
    page_route = '/castnym-klientam/mn-dostavka/vozvrat-tovarov-v-magazin-asos'
