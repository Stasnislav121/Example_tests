import allure

from library.site.ui.blocks.map.BaseMap import BaseMap


class PointMap(BaseMap):
    css_map = '.map__container'
    css_map_content = '.ymaps-2-1-79-map'
    css_filter_icon = '.filter-icon'
    css_private_client_tab = '.ui-map-tab'
    css_private_client_filter = '.map-nav__button_submenu'

    def __init__(self, page):
        super().__init__(page)
        self.page.locator(f"css={self.css_map}").scroll_into_view_if_needed()
        self.wait_for_selector(self.css_map_content)
        self.hover(self.css_map)

    def click_any_point(self):
        with allure.step('Кликнуть на иконку любого отделения и обратиться к карточке отделения'):
            self.wait_for_selector(self.css_point_icon)
            self.click(self.css_point_icon)
        from library.site.ui import PointCard
        block_card = PointCard(self.page)
        return block_card

    def ctl_filter_ecommerce(self, filters_displayed=False):
        with allure.step('Обращение к контролу фильтров карты'):
            if self.is_mobile and filters_displayed is False:
                with allure.step('Кликнуть на кнопку "Подбор отделений"'):
                    self.click(f"{self.css_filter_icon}", force=False)
            from library.site.ui import EcommerceMapFilterControl
            control = EcommerceMapFilterControl(self.page)
        return control

    def ctl_filter_private_clients(self):
        with allure.step('Обращение к контролу фильтров карты'):
            self.click(f"{self.css_private_client_filter}", force=False)
            from library.site.ui import PrivateClientsMapFilterControl
            control = PrivateClientsMapFilterControl(self.page)
        return control

    def select_sort_tab(self, tab_text, selector):
        with allure.step(f'Выбрать таб {tab_text}'):
            self.click(f'{selector}:has-text("{tab_text}")', force=False)
            self.expect_to_be_visible(f'{selector}_active:has-text("{tab_text}")')
        return self

    def select_tab_receiving_packages_from_the_sender(self, city_code='68'):
        with allure.step('Выбрать таб "Прием посылок от отправителя"'):
            with self.expect_response(lambda request:
                                      f'/api/v1/odp?cityCode={city_code}&select=id,geo&perPage=1000&receptionLap=1&'
                                      f'page=1' in request.url) as resp_info:
                self.select_sort_tab(tab_text='Прием посылок от отправителя', selector=self.css_private_client_tab)
            resp_info.value.finished()
            self.screenshot('tab_from_the_sender_selected')
        return self

    def select_tab_receiving_packages_by_the_recipient(self, city_code='68'):
        with allure.step('Выбрать таб "Получение посылок получателем"'):
            with self.expect_response(lambda request:
                                      f'/api/v1/odp?cityCode={city_code}&select=id,geo&perPage=1000&deliveryLap=1&'
                                      f'page=1' in request.url) as resp_info:
                self.select_sort_tab(tab_text='Получение посылок получателем', selector=self.css_private_client_tab)
            resp_info.value.finished()
        self.screenshot('tab_by_the_recipient_selected')
        return self


class FindAtOfficesPointMap(PointMap):
    css_map = '.map__container_up'


class CalcPointMap(PointMap):
    css_map = '.calculator-map-content'
