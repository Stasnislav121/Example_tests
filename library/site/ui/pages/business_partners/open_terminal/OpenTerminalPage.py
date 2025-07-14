import allure

from library.site.ui.pages.business_partners import *
from settings import DOWNLOADS_DIR


class OpenTerminalPage(BusinessPartnersBasePage):
    page_element = ':text("Откройте терминал  в вашем городе")'
    page_route = '/biznes-partneram/open-terminal'
    css_offer_link = 'p:text("Ознакомиться с офертой можете") a:text("здесь")'

    @staticmethod
    def open(page):
        return OpenTerminalPage(page).open_url('/biznes-partneram/open-terminal').check_page()

    def download_offer(self):
        with allure.step('Кликнуть на гиперссылку "здесь" в строке "Ознакомиться с офертой можете здесь" и загрузить '
                         'файл'):
            with self.expect_download() as download_info:
                self.click(self.css_offer_link, force=False)
            download = download_info.value
            file_name = download.suggested_filename
            destination_path = f'{DOWNLOADS_DIR}/{file_name}'
            download.save_as(path=destination_path)
            allure.attach.file(destination_path, file_name)

        return destination_path
