import allure

from library.site.ui.pages.ecommerce import *


class DocumentsConfidentialityAgreementPage(EcommerceBasePage):
    page_element = ':text("Согласие и политика по обработке персональных данных")'
    page_route = '/e-commerce/dokumenty/soglasenie-o-konfidencial-nosti-informacii-boksberri-soft'
    css_document_title = '.docs__item'

    def get_documents_count(self):
        with allure.step('Посчитать количество документов на странице'):
            elm_cnt = self.count(self.css_document_title)
        return elm_cnt
