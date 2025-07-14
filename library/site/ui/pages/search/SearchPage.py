import allure
from library.site.ui import *
from library.site.ui.pages import *


class SearchPage(HomePage):
    page_element = '.pageTitle__title:text("Результаты поиска")'
    page_route = '/search'
    css_go_to_tracking_page = '.results a:has-text("нажмите здесь")'

    @staticmethod
    def open(page):
        return ContactsMainPage(page).open_url('/search').check_page()

    def check_result_not_found_text(self):
        with allure.step('Проверить наличие текста "По вашему запросу ничего не найдено. Попробуйте изменить запрос"'):
            self.expect_to_be_visible('.results:has-text("По вашему запросу ничего не найдено. Попробуйте изменить '
                                      'запрос")')
            self.expect_to_be_visible('.results:has-text("Чтобы отследить статус вашей посылки")')
            self.expect_to_be_visible(self.css_go_to_tracking_page)
            self.screenshot('text_visible')
        return self

    def click_press_here(self):
        with allure.step('Кликнуть по словам "нажмите здесь" в тексте '
                         '"Чтобы отследить статус вашей посылки нажмите здесь"'):
            self.click(f'{self.css_go_to_tracking_page}', force=False)
        with allure.step('Обращение к списку посылок на странице /tracking-page"'):
            from library.site.ui import ParcelTrackingForm
            return ParcelTrackingForm(self.page).check_element()
