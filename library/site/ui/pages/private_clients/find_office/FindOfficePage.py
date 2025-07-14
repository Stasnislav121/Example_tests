import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *


class FindOfficePage(PrivateClientsBasePage):
    page_element = '.map__container'
    page_route = '/find_an_office'
    css_point_name = '.map-card__name'
    css_point_address = '.map-card__info-text'
    css_gift_banner = '.tracking-gift__wrap'

    @staticmethod
    def open(page):
        return FindOfficePage(page).open_url('/find_an_office').check_page()

    def get_data(self):
        data = {}
        with allure.step('Считать данные на странице отделения'):
            self.wait_for_selector(self.css_point_name)
            self.wait_for_selector(self.css_point_address)
            data['Название'] = self.inner_text(f"{self.css_point_name}", timeout=1000)
            data['Адрес'] = self.inner_text(f"{self.css_point_address}", timeout=1000)
            allure.attach(str(data), f'Данные отделения: {data}', allure.attachment_type.JSON)

        return data

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.map.common.PointMap import FindAtOfficesPointMap
            block = FindAtOfficesPointMap(self.page)
            block.set_parent(self)
        return block

    def check_gift_banner(self):
        with allure.step('Проверить отображение банера "Выберите подарок"'):
            self.page.locator(f'css={self.css_gift_banner}').scroll_into_view_if_needed()
            self.screenshot('find_an_offices_gift_banner', locator=self.css_gift_banner)
        return self

    def go_to_gift_page(self):
        with allure.step('Нажать на текст "Выберите подарок"'):
            with self.expect_page() as gift_page:
                self.click(self.css_gift_banner, force=False)
            url = gift_page.value.url
        return url
