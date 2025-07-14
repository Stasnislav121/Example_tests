from library.site.ui.pages.ecommerce import *


class DocumentsAttachmentsProhibitedPage(EcommerceBasePage):
    page_element = (':text("Вложения, запрещенные к отправке для интернет-магазинов и специальный режим доставки '
                    'внутри России")')
    page_route = '/e-commerce/dokumenty/vlozenia-zapresennye-k-otpravke-i-specialnyi-rezhim-dostavki'
