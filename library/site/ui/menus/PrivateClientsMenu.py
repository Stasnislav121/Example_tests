from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class PrivateClientsMenu(BaseMenu):
    css_map = {
        'Доставка': {
            'Отправить и получить посылку': 'a[href="/castnym-klientam/dostavka/otpravit_posylku"]',
            'Доставка по России': 'a[href="/castnym-klientam/dostavka/dostavka-posylok-rf"]',
            'Доставка посылок с площадок частных объявлений': 'a[href="/castnym-klientam/dostavka/dostavka-s-avito'
                                                              '-uly-vkontakte-armarki-masterov"]',
            'Доставка растений из интернет-магазинов': 'a[href="/castnym-klientam/dostavka/dostavka-rastenij-iz'
                                                       '-internet-magazinov"]',
            'Отследить посылку': 'a[href="/tracking-page"]',
            'Мобильное приложение': 'a[href="/castnym-klientam/dostavka/mobil-noe-prilozenie"]',
        },
        'Условия': {
            'Упаковка писем и посылок': 'a[href="/castnym-klientam/info-klientam/upakovka-pisem-i-posylok"]',
            'Требования к отправке': 'a[href="/castnym-klientam/info-klientam/trebovaniya-k-otpravke"]',
            'Документы': 'a[href="/castnym-klientam/info-klientam/dokumenty"]',
            'Информация о способах оплаты': 'a[href="/castnym-klientam/info-klientam/online_oplata"]',
        },
        'Международная доставка': {
            'Посылки из Казахстана: получайте в отделениях ': 'a[href="/castnym-klientam/mn-dostavka/posylki'
                                                                      '-iz-kazahstana-polucajte-v-otdeleniah-"]',
            'Возврат товаров в магазин ASOS': 'a[href="/castnym-klientam/mn-dostavka/vozvrat-tovarov-v-magazin-asos"]',
            'Таможенные правила для физических лиц': 'a[href="/castnym-klientam/mn-dostavka/tamozhennye-pravila-dlya'
                                                     '-fizicheskih-lic"]',
            'Товары, запрещенные к международной перевозке': 'a[href="/castnym-klientam/mn-dostavka/tovary,'
                                                             '-zapresennye-k-mezdunarodnoj-perevozke"]',
            'Персональные данные': 'a[href="/castnym-klientam/mn-dostavka/personalnye-dannye"]',
            'Оферта Боксберри': 'a[href="/castnym-klientam/mn-dostavka/oferta-"]',
        },
        'FAQ': 'a[href="/faq/chastnym-klientam-voprosy-i-otvety"]'
    }

    def open_delivery_send_package(self):
        self.open_submenu('Доставка', 'Отправить и получить посылку')
        return DeliverySendPackagePage(self.page).check_page()

    def open_delivery_package_in_russia(self):
        self.open_submenu('Доставка', 'Доставка по России')
        return DeliveryPackageInRussiaPage(self.page).check_page()

    def open_delivery_package_from_ad_platforms(self):
        self.open_submenu('Доставка', 'Доставка посылок с площадок частных объявлений')
        return DeliveryPackageFromAdPlatformsPage(self.page).check_page()

    def open_delivery_plants_from_online_store(self):
        self.open_submenu('Доставка', 'Доставка растений из интернет-магазинов')
        return DeliveryPlantsFromOnlineStore(self.page).check_page()

    def open_delivery_mobile_app(self):
        self.open_submenu('Доставка', 'Мобильное приложение')
        return DeliveryMobileAppPage(self.page).check_page()

    def open_delivery_tracking(self):
        self.open_submenu('Доставка', 'Отследить посылку')
        return DeliveryTrackingPage(self.page).check_page()

    def open_terms_packaging(self):
        self.open_submenu('Условия', 'Упаковка писем и посылок')
        return TermsPackagingPage(self.page).check_page()

    def open_terms_delivery(self):
        self.open_submenu('Условия', 'Требования к отправке')
        return TermsDeliveryPage(self.page).check_page()

    def open_terms_documents(self):
        self.open_submenu('Условия', 'Документы')
        return TermsDocumentsPage(self.page).check_page()

    def open_terms_payment_info(self):
        self.open_submenu('Условия', 'Информация о способах оплаты')
        return TermsPaymentInfoPage(self.page).check_page()

    def open_international_delivery_from_kz(self):
        self.open_submenu('Международная доставка', 'Посылки из Казахстана: получайте в отделениях ')
        return InternationalDeliveryFromKzPage(self.page).check_page()

    def open_international_delivery_return_to_asos(self):
        self.open_submenu('Международная доставка', 'Возврат товаров в магазин ASOS')
        return InternationalDeliveryReturnToASOSPage(self.page).check_page()

    def open_international_delivery_custom_rules(self):
        self.open_submenu('Международная доставка', 'Таможенные правила для физических лиц')
        return InternationalDeliveryCustomsRulesPage(self.page).check_page()

    def open_international_delivery_forbidden_goods(self):
        self.open_submenu('Международная доставка', 'Товары, запрещенные к международной перевозке')
        return InternationalDeliveryForbiddenGoodsPage(self.page).check_page()

    def open_international_delivery_personal_data(self):
        self.open_submenu('Международная доставка', 'Персональные данные')
        return InternationalDeliveryPersonalDataPage(self.page).check_page()

    def open_international_delivery_offer(self):
        self.open_submenu('Международная доставка', 'Оферта Боксберри')
        return InternationalDeliveryOfferPage(self.page).check_page()

    def open_faq(self):
        self.open_menu('FAQ')
        return PrivateClientsFaqPage(self.page).check_page()
