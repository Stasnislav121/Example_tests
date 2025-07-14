import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *
from settings import DOWNLOADS_DIR


class TermsDocumentsPage(PrivateClientsBasePage):
    page_element = ':text("Документы и юридические материалы")'
    page_route = '/castnym-klientam/info-klientam/dokumenty'
    css_document_title = '.docs__item-title'

    @staticmethod
    def open(page):
        return TermsDocumentsPage(page).open_url(
            '/castnym-klientam/info-klientam/dokumenty').check_page()

    def download_document(self, doc_name):
        with allure.step(f'Кликнуть на название документа "{doc_name}" и загрузить файл'):
            with self.expect_download() as download_info:
                self.click(f'{self.css_document_title}:text("{doc_name}")', force=False)
            download = download_info.value
            file_name = download.suggested_filename
            destination_path = f'{DOWNLOADS_DIR}/{file_name}'
            download.save_as(path=destination_path)
            allure.attach.file(destination_path, file_name)

        return destination_path

    def get_documents_count(self):
        with allure.step('Посчитать количество документов на странице'):
            elm_cnt = self.count(self.css_document_title)
        return elm_cnt
