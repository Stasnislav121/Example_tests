import allure

from library.site.ui.pages.BasePage import BasePage


class ParcelTrackingModal(BasePage):
    page_element = '#trackWidget___BV_modal_body_'

    def check_element(self, screen=False):
        with allure.step("Проверить модальное окно трекинга"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что модальное окно загрузилось"):
                self.wait_for_selector(self.page_element)
                self.screenshot('ParcelTrackingForm_loaded', locator=self.page_element)
        return self

    def parcels_list(self):
        with allure.step('Обращение к списку посылок"'):
            from library.site.ui import ParcelTrackingForm
            return ParcelTrackingForm(self.page).check_element()
