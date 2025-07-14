import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *


class DeliveryTrackingPage(PrivateClientsBasePage):
    page_element = ':has-text("Отследить посылку")'
    css_track_widget = '.track-widget'
    page_route = '/tracking-page'

    @staticmethod
    def open(page):
        return DeliveryTrackingPage(page).open_url('/tracking-page').check_page()

    def check_page(self, screen=True):
        with allure.step('Проверить страницу "Отследить посылку"'):
            super().check_page(screen=screen)

            with allure.step('Проверить, что видим виджет отслеживания посылки'):
                self.wait_for_selector(self.css_track_widget)

            self.screenshot('DeliveryTrackingPage_loaded')

        return self

    def form_tracking(self):
        with allure.step('Обращение к форме "Отследить отправление"'):
            from library.site.ui import ParcelTrackingForm
            form = ParcelTrackingForm(self.page)
            form.set_parent(self)
        return form
