import allure

from library.site.ui.pages.ecommerce import *


class ECommerceFaqPage(EcommerceBasePage):
    page_element = ':text("Интернет-магазинам. Вопросы и ответы")'
    page_route = '/faq/internet-magazinam-voprosy-i-otvety'
    css_group = '.faq__group'

    @staticmethod
    def open(page):
        return ECommerceFaqPage(page).open_url('/faq/internet-magazinam-voprosy-i-otvety').check_page()

    def goto_faq_link(self, link):
        with allure.step(f'Выполнить переход по гиперссылке: {link} и обратиться к странице темы вопроса'):
            self.click(f'[href="{link}"]')
        from library.site.ui import TopicFaqPage
        return TopicFaqPage(self.page)

    def get_data(self):
        data = []
        with allure.step('Считать данные на странице "FAQ"'):
            grp_cnt = self.count(self.css_group)
            for i in range(grp_cnt):
                grp_locator = f'{self.css_group}:nth-child({i + 1})'
                items = []
                items_cnt = self.count(f'{grp_locator} .faq__groupItem')
                for n in range(items_cnt):
                    item_locator = f'{grp_locator} .faq__groupItem:nth-child({n + 1})'
                    item = {
                        'Название': self.inner_text(f'{item_locator} .faq__groupLink'),
                        'Ссылка': self.get_attribute(f'{item_locator} .faq__groupLink', 'href')
                    }
                    items.append(item)

                group = {
                    'Название': self.inner_text(f'{grp_locator} .faq__groupTitle'),
                    'Ссылки': items
                }
                data.append(group)

        return data
