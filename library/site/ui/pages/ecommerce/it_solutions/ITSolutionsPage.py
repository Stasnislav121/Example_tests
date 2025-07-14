import allure

from library.site.ui.pages.ecommerce import *


class ITSolutionsPage(EcommerceBasePage):
    page_element = ':has-text("IT-Решения")'
    page_route = '/e-commerce/it-resenia'
    css_plugin = '.tile'

    @staticmethod
    def open(page):
        return ITSolutionsPage(page).open_url('/e-commerce/it-resenia').check_page()

    def goto_plugin_link(self, link):
        with allure.step(f'Выполнить переход по гиперссылке: {link} и обратиться к странице плагина'):
            self.click(f'[href="{link}"]')
        from library.site.ui import ITSolutionsPluginPage
        return ITSolutionsPluginPage(self.page)

    def get_data(self):
        data = {
            'Плагины': []
        }
        with allure.step('Считать данные на странице "IT-Решения"'):
            plugin_cnt = self.count(self.css_plugin)
            for i in range(plugin_cnt):
                plugin_locator = f'{self.css_plugin}:nth-child({i + 1})'

                if self.is_visible(f'{plugin_locator} .tile__info'):
                    info = self.inner_text(f'{plugin_locator} .tile__info')
                else:
                    info = self.inner_text(f'{plugin_locator} .tile__title')

                plugin = {
                    'Ссылка': self.get_attribute(f'{plugin_locator} .tile__inner', 'href'),
                    'Иконка': self.get_attribute(f'{plugin_locator} .tile__icon', 'src'),
                    'Название': info,
                }
                data['Плагины'].append(plugin)

            allure.attach(str(data), f'Данные страницы "IT-Решения": {data}', allure.attachment_type.JSON)

        return data
