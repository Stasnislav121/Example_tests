from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class ContactsMenu(BaseMenu):
    css_map = {
        'Связаться по другим вопросам': {
            'Вопросы по курьерской доставке по г. Москва':
                'a[href="/kontakty/napisat-pis-mo-v-sluzbu-podderzki/voprosy-po-kur-erskoj-dostavke-po-g-moskva-i-gorodam-sputnikam"]',
            'Пресс-служба ': 'a[href="/kontakty/napisat-pis-mo-v-sluzbu-podderzki/press-sluzba-"]'
        }
    }

    def open_press_service(self):
        self.open_submenu_desktop('Связаться по другим вопросам', 'Пресс-служба ')
        return ContactsPressPage(self.page).check_page()
