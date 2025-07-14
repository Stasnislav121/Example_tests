from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class BusinessPartnersMenu(BaseMenu):
    css_map = {
        'Франшиза': 'a[href="/fr..ru/?utm_source=site&utm_medium=free&utm_campaign=partneram_up"]',
        'Открыть терминал': 'a[href="/biznes-partneram/open-terminal"]',
        'Кросс-промо с ': 'a[href="/biznes-partneram/kross-promo-s-"]'
    }

    def open_open_terminal(self):
        self.open_menu_desktop('Открыть терминал')
        return OpenTerminalPage(self.page).check_page()

    def open_cross_promo_(self):
        self.open_menu_desktop('Кросс-промо с ')
        return CrossPromoPage(self.page).check_page()
