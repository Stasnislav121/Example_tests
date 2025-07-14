import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *
from settings import DOWNLOADS_DIR


class TermsPackagingPage(PrivateClientsBasePage):
    page_element = ':text("Правила упаковки писем и посылок")'
    page_route = '/castnym-klientam/info-klientam/upakovka-pisem-i-posylok'
    css_packaging_requirements_link = 'a:has-text("Требования к упаковке и грузу для отправлений физических лиц")'

    @staticmethod
    def open(page):
        return TermsPackagingPage(page).open_url('/castnym-klientam/info-klientam/upakovka-pisem-i-posylok') \
            .check_page()

    def download_packaging_requirements(self):
        with allure.step('Кликнуть на гиперссылку "Требования к упаковке и грузу для отправлений физических лиц" '
                         'и загрузить файл'):
            with self.expect_download() as download_info:
                self.click(self.css_packaging_requirements_link, force=False)
            download = download_info.value
            file_name = download.suggested_filename
            destination_path = f'{DOWNLOADS_DIR}/{file_name}'
            download.save_as(path=destination_path)
            allure.attach.file(destination_path, file_name, allure.attachment_type.PDF, extension='pdf')

        return destination_path
