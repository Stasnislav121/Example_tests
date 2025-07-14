import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *
from settings import DOWNLOADS_DIR


class InternationalDeliveryPersonalDataPage(PrivateClientsBasePage):
    page_element = ':text("Политика  by  в отношении обработки персональных данных")'
    page_route = '/castnym-klientam/mn-dostavka/personalnye-dannye'
    css_policy_link = 'a:text("общедоступным документом")'

    @staticmethod
    def open(page):
        return InternationalDeliveryPersonalDataPage(page).open_url(
            '/castnym-klientam/mn-dostavka/personalnye-dannye').check_page()

    def download_policy(self):
        with allure.step('Кликнуть на гиперссылку "общедоступным документом" и загрузить файл'):
            with self.expect_download() as download_info:
                self.click(self.css_policy_link, force=False)
            download = download_info.value
            file_name = download.suggested_filename
            destination_path = f'{DOWNLOADS_DIR}/{file_name}'
            download.save_as(path=destination_path)
            allure.attach.file(destination_path, file_name)

        return destination_path
