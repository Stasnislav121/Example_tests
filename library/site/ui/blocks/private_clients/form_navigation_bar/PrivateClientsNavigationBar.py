import allure

from library.site.ui.pages.BasePage import BasePage


class PrivateClientsNavigationBar(BasePage):
    css_calculate_button = '.function-button_calc:text("Оформить доставку")'
    css_our_point_button = '.function-button_branch:text("Наши отделения")'
    css_delivery_number_desktop = 'li#item-tracking input'
    css_delivery_number_mobile = '.input-tracking'
    css_delivery_search_button_desktop = 'li#item-tracking button'
    css_delivery_search_button_mobile = '.formbar-mobile__item_tracking .icon-wrapper'

    def set_parcel_number(self, number):
        with allure.step(f'Установить в поле "Номер отправления" значение: {number}'):
            if self.is_mobile:
                self.fill(self.css_delivery_number_mobile, number)
            else:
                self.fill(self.css_delivery_number_desktop, number)
            self.screenshot('parcel_number_set')
        return self

    def click_track(self):
        with allure.step('Кликнуть на кнопку поиска'):
            if self.is_mobile:
                self.click(self.css_delivery_search_button_mobile, force=False)
            else:
                self.click(self.css_delivery_search_button_desktop, force=False)
        return self

    def track_parcel(self, number):
        with allure.step(f'Отследить посылку: {number}'):
            self.set_parcel_number(number)
            self.click_track()
            from library.site.ui import ParcelTrackingModal
            return ParcelTrackingModal(self.page).check_element()
