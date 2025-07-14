import allure

from library.site.ui.pages.private_clients import *


class OpenPointPage(PrivateClientsBasePage):
    page_element = ':has-text("Откройте пункт выдачи заказов в своем городе")'
    page_route = '/biznes-partneram/open-point-pvz'

    def form_open_point(self):
        with allure.step('Обращение к форме "Заявка на открытие пункта выдачи "'):
            from library.site.ui import BusinessPartnersOpenPointRussiaForm
            form = BusinessPartnersOpenPointRussiaForm(self.page)
            form.set_parent(self)
        return form
