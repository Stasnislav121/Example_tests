import allure
import urllib.parse
from allure_commons.types import AttachmentType

from library.site.ui.blocks.map import BaseMap, CalcPointMap


class CalculatorPointMap(BaseMap):
    page_element = '.calculator-map-content'
    css_map = '.calculator-map-content'
    css_map_content = '.ymaps-2-1-79-map'
    css_address_icon = '.ymaps-2-1-79-islets_icon-with-caption .ymaps-2-1-79-svg-icon'
    css_point_card = '.map-card_active'
    css_select_point = 'a:text("Выбрать это отделение")'
    css_cancel = 'a:text("Отмена")'
    css_selected = '.map-schedule__button:text("Выбрано")'
    css_close = '.map-card__close'
    css_address_input = '[name="calculator_pip"] .ymaps-2-1-79-searchbox-input__input'
    css_search = '[name="calculator_pip"] .ymaps-2-1-79-searchbox-button-text'
    css_close_address = '[name="calculator_pip"] .ymaps-2-1-79-balloon__close-button'
    css_search_suggest = '.ymaps-2-1-79-suggest-item'
    css_search_option = '.ymaps-2-1-79-islets_serp-item'
    css_map_filters = {
        'Отделения принимают оплату при получении': '.ui-switcher__text'
    }

    def check_element(self, screen=False):
        with allure.step("Проверить блок карты отделений"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
            with allure.step("Проверить, что контект карты загрузился"):
                self.wait_for_selector(self.css_map_content)
            self.screenshot('CalculatorPointMap_loaded', locator=self.page_element)
        return self

    def open_any_point(self):
        with allure.step('Выбрать любое отделение на карте'):
            block_card = self.click_any_point()
            block_card.click_select_point()
        return self

    def search_point(self, address='117420, Москва г, Профсоюзная ул, д.47'):
        with allure.step(f'Поиск отделения по адресу: {address}'):
            self.set_search_address(address)
            self.click_search()
            self.wait_for_timeout(0.5)

            if self.is_visible(self.css_search_suggest):
                self.click(f"{self.css_search_suggest}:nth-child(1)")
                self.wait_for_timeout(0.5)

            if self.is_visible(self.css_search_option):
                self.click(f"{self.css_search_option}:nth-child(1)")

            self.wait_for_selector('[name="calculator_pip"] .ymaps-2-1-79-islets_card')
            self.remove_address_card()
        return self

    def click_any_point(self):
        with allure.step('Кликнуть на иконку любого отделения и обратиться к карточке отделения'):
            points_cnt = self.count(self.css_point_icon)
            for _ in range(3):
                if points_cnt > 1:
                    self.click(self.css_map)
                    self.click('.ymaps-2-1-79-zoom__plus')
                    self.wait_for_timeout(1)
                    self.wait_for_selector(self.css_point_icon)
                    points_cnt = self.count(self.css_point_icon)
                else:
                    break
            self.click(self.css_point_icon)
            self.wait_for_selector(self.css_point_icon)

        from library.site.ui import CalculatorPointCardBlock
        block_card = CalculatorPointCardBlock(self.page)
        return block_card

    def __switch_filter(self, switch_name, check_count=True):
        with allure.step(f'Переключить фильтр: "{switch_name}"'):
            point_map = CalcPointMap(self.page)
            points_before = point_map.get_points_in_calc_cnt()
            allure.attach(str(points_before), 'points_count_before', AttachmentType.TEXT)
            self.click(self.css_map_filters[switch_name], force=False)
            cnt_updated = False
            if check_count:
                for _ in range(10):
                    points_after = point_map.get_points_in_calc_cnt()
                    if points_after != points_before:
                        cnt_updated = True
                        break
                    self.wait_for_timeout(1)
                allure.attach(str(points_after), 'points_count_after', AttachmentType.TEXT)
                assert cnt_updated, 'Количество отделений не изменилось после переключения фильтра'

        return self

    def switch_payer_recipient_accessibility_filter(self, select, city_code='Н00163822',
                                                    country_code='', check_count=True):
        with allure.step(f'Переключить фильтр: "Отделения принимают оплату при получении" в положение {select}'):
            country_code = f'&receiverCountryCode={country_code}' if country_code else ''
            accept_payments_param = '&acceptPayments=1' if select else ''
            if any(char.isalpha() for char in city_code):
                city_code = urllib.parse.quote(city_code)
            url = (f'api/v1/odp?cityCode={city_code}&select=title,address,id,workTime,scheduleShort,phone,'
                   f'geo&deliveryLap=1{accept_payments_param}{country_code}&perPage=10000')
            with self.expect_response(lambda request:
                                      url in request.url) as resp_info:
                self.__switch_filter(switch_name='Отделения принимают оплату при получении', check_count=check_count)
            resp_info.value.finished()

            self.screenshot(name='point_payer_recipient_accessibility_filter_switched')
        return self

    def switch_on_payer_recipient_accessibility_filter(self, check_count=True, city_code='Н00163822',
                                                       country_code='112'):
        with allure.step('Включить фильтр: "Отделения принимают оплату при получении"'):
            self.switch_payer_recipient_accessibility_filter(select=True,
                                                             check_count=check_count,
                                                             city_code=city_code,
                                                             country_code=country_code)
        return self

    def switch_off_payer_recipient_accessibility_filter(self, check_count=True, city_code='Н00163822'):
        with allure.step('Выключить фильтр: "Отделения принимают оплату при получении"'):
            self.switch_payer_recipient_accessibility_filter(select=False,
                                                             check_count=check_count,
                                                             city_code=city_code)
        return self
