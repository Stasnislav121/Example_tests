from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class EcommerceClientsMenu(BaseMenu):
    css_map = {
        'Услуги': {
            'Доставка из США, Европы и Азии для интернет-магазинов': 'a[href="/e-commerce/uslugi/dostavka-iz-ssa'
                                                                     '-evropy-i-azii-dla-internet-magazinov"]',
            'Доставка в страны СНГ': 'a[href="/e-commerce/uslugi/dostavka-v-kazahstan-i-belarus"]',
            'Курьерская служба для интернет-магазинов': 'a[href="/e-commerce/uslugi/kur-erskaa-sluzba-dla-internet'
                                                        '-magazinov"]',
            'Пункты приема посылок от интернет-магазинов': 'a[href="/e-commerce/uslugi/punkty-priema-posylok-ot'
                                                           '-internet-magazinov"]',
            'Экспресс-доставка для интернет-магазинов': 'a[href="/e-commerce/uslugi/ekspress-dostavka-dla-internet'
                                                        '-magazinov"]',
            'Страхование отправлений': 'a[href="/e-commerce/uslugi/strahovanie-otpravlenij"]',
            'Служба доставки для интернет-магазинов': 'a[href="/e-commerce/uslugi/sluzba-dostavki-dla-internet'
                                                      '-magazinov"]',
            'Логистика интернет-магазинов': 'a[href="/e-commerce/uslugi/logistika-internet-magazinov"]',
            'Бонусы от партнеров': 'a[href="/e-commerce/uslugi/partner-offer"]',
        },
        'Документы': {
            'Вложения, запрещенные к отправке внутри России': 'a[href="/e-commerce/dokumenty/vlozenia-zapresennye-k'
                                                              '-otpravke-i-specialnyi-rezhim-dostavki"]',
            'Документы и тарифы': 'a[href="/e-commerce/dokumenty/dokumenty-i-tarify"]',
            'Лицензионное соглашение на все Программы для БОКСБЕРРИ СОФТ': 'a[href="/e-commerce/dokumenty'
                                                                           '/licenzionnoe-soglasenie-na-vse-programmy-dla-boksberri-soft"]',
            'Соглашение о конфиденциальности информации БОКСБЕРРИ СОФТ': 'a[href="/e-commerce/dokumenty/soglasenie-o'
                                                                         '-konfidencial-nosti-informacii-boksberri-soft"]',
        },
        'IT-Решения': 'a[href="/e-commerce/it-resenia"]',
        'Контакты': 'a[href="/kontakty/napisat-pis-mo-v-sluzbu-podderzki/svazat-sa-s-otdelom-prodaz"]',
        'FAQ': 'a[href="/faq/internet-magazinam-voprosy-i-otvety"]'
    }

    def open_services_delivery_from_usa(self):
        self.open_submenu('Услуги', 'Доставка из США, Европы и Азии для интернет-магазинов')
        return ServicesDeliveryFromUSAPage(self.page).check_page()

    def open_services_delivery_to_cis(self):
        self.open_submenu('Услуги', 'Доставка в страны СНГ')
        return ServicesDeliveryToCISPage(self.page).check_page()

    def open_services_courier_for_online_stores(self):
        self.open_submenu('Услуги', 'Курьерская служба для интернет-магазинов')
        return ServicesCourierForOnlineStoresPage(self.page).check_page()

    def open_services_acceptance_points(self):
        self.open_submenu('Услуги', 'Пункты приема посылок от интернет-магазинов')
        return ServicesAcceptancePointsPage(self.page).check_page()

    def open_services_express_delivery_for_stores(self):
        self.open_submenu('Услуги', 'Экспресс-доставка для интернет-магазинов')
        return ServicesExpressDeliveryForStoresPage(self.page).check_page()

    def open_services_insurance_points(self):
        self.open_submenu('Услуги', 'Страхование отправлений')
        return ServicesInsurancePointsPage(self.page).check_page()

    def open_services_unified_delivery_stores(self):
        self.open_submenu('Услуги', 'Служба доставки для интернет-магазинов')
        return ServicesUnifiedDeliveryStoresPage(self.page).check_page()

    def open_services_logistics_online_stores(self):
        self.open_submenu('Услуги', 'Логистика интернет-магазинов')
        return ServicesLogisticsOnlineStoresPage(self.page).check_page()

    def open_services_bonuses_from_partners(self):
        self.open_submenu('Услуги', 'Бонусы от партнеров')
        return ServicesBonusesFromPartnersPage(self.page).check_page()

    def open_documents_attachments_prohibited(self):
        self.open_submenu('Документы', 'Вложения, запрещенные к отправке внутри России')
        return DocumentsAttachmentsProhibitedPage(self.page).check_page()

    def open_documents_documents_and_tariffs(self):
        self.open_submenu('Документы', 'Документы и тарифы')
        return DocumentsDocumentsAndTariffsPage(self.page).check_page()

    def open_documents_license_agreement(self):
        self.open_submenu('Документы', 'Лицензионное соглашение на все Программы для БОКСБЕРРИ СОФТ')
        return DocumentsLicenseAgreementPage(self.page).check_page()

    def open_documents_confidentiality_agreement(self):
        self.open_submenu('Документы', 'Соглашение о конфиденциальности информации БОКСБЕРРИ СОФТ')
        return DocumentsConfidentialityAgreementPage(self.page).check_page()

    def open_it_solutions(self):
        self.open_menu('IT-Решения')
        return ITSolutionsPage(self.page).check_page()

    def open_contacts(self):
        self.open_menu('Контакты')
        return ContactsMainPage(self.page).check_page()

    def open_faq(self):
        self.open_menu('FAQ')
        return ECommerceFaqPage(self.page).check_page()
