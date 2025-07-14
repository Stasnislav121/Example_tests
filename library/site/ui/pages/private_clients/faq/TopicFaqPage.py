import allure

from library.site.ui.pages.private_clients import *


class TopicFaqPage(PrivateClientsBasePage):
    page_element = '.faqItem__content'
    css_title = '.pageTitle__title'
    css_content = '.faqItem__content'
    css_was_useful = ':text("Была ли статья полезна?")'
    css_yes_button = '.faqItem__pollButton_green:text("Да")'
    css_no_button = '.faqItem__pollButton_red:text("Нет")'

    def get_data(self):
        with allure.step('Считать данные на странице топика раздела "FAQ"'):
            data = {
                'Заголовок': self.inner_text(self.css_title),
                'Содержимое': self.inner_text(self.css_content)
            }
        return data

    def check_page(self, screen=True):
        with allure.step('Проверка страницы топика раздела "FAQ"'):
            super().check_page(screen=screen)
            with allure.step('Проверка наличия заголовка'):
                self.wait_for_selector(self.css_title)
            with allure.step('Проверка наличия описания'):
                self.wait_for_selector(self.css_content)
            with allure.step('Проверка блока "Была ли статья полезна?"'):
                self.wait_for_selector(self.css_was_useful)
                self.wait_for_selector(self.css_yes_button)
                self.wait_for_selector(self.css_no_button)

        return self
