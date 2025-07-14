import allure

from library.site.ui.pages.ecommerce import *


class ITSolutionsPluginPage(EcommerceBasePage):
    page_element = '.editor'

    def check_title_is_specific_title(self, expected_title):
        with allure.step(f'Проверить, что заголовок страницы: {expected_title}'):
            title = self.inner_text(f'h1:text("{expected_title}")')
            assert title == expected_title, f'Ожидался заголовок: {expected_title}, но получен: {title}'
        return self

    def check_content_exists(self):
        with allure.step('Проверить, что блок с описанием присутствует на странице'):
            self.wait_for_selector('.editor')
        return self

    def check_document_link_exists(self):
        with allure.step('Проверить, что ссылка на документацию присутствует на странице'):
            self.wait_for_selector('a.docs__item')
        return self

    def check_support_link_exists(self):
        with allure.step('Проверить, что ссылка на связь с тех. поддержкой присутствует на странице'):
            self.wait_for_selector('[href="http://sd..ru/"]:text("портале технической поддержки")')
        return self
