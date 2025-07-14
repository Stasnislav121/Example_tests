import allure

from library.site.ui import *


class CalculatorPointListBlock(BasePage):
    page_element = '.calc-points-list'
    css_point = '.calc-radio-wrap'
    css_point_name = '.calc-radio-btn__name'
    css_point_phone = '.calc-radio-btn__size'
    css_point_schedule = '.calc-radio-btn__desc'
    css_search = '[placeholder="Поиск отделения"]'
    css_tab_list = '.nav__item:text("Список")'

    def check_element(self, screen=False):
        with allure.step("Проверить блок списка отделений"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorPointListBlock_loaded', locator=self.page_element)

        return self

    def get_data(self):
        with allure.step('Считать данные в блоке списка отделений'):
            points = []
            point_cnt = self.count(self.css_point)
            for i in range(point_cnt):
                point = {}
                locator = f'{self.css_point}:nth-child({i + 1})'
                point['Название'] = self.inner_text(f'{locator} {self.css_point_name}')
                point_selected = self.is_visible(f'{locator} .active')
                if point_selected:
                    point['Выбрано'] = True
                else:
                    point['Выбрано'] = False

                points.append(point)

        return points

    def click_any_point(self):
        with allure.step('Кликнуть в любое отделение'):
            self.wait_for_selector(self.css_point)
            self.wait_for_timeout(1)
            with self.expect_response(lambda request: '/api/v1/odp' in request.url):
                self.click(self.css_point, force=False)
            self.screenshot('any_point_clicked', locator=self.page_element)
        return self

    def click_point(self, address):
        with allure.step(f'Кликнуть в отделение с адресом: {address}'):
            point_locator = f"{self.css_point}:has-text('{address}')"
            self.wait_for_selector(point_locator)
            self.wait_for_timeout(1)
            with self.expect_response(lambda request: '/api/v1/odp' in request.url):
                self.click(point_locator, force=False)
            self.screenshot('point_clicked', locator=self.page_element)
        return self

    def set_search_string(self, value):
        with allure.step(f'Установить в поисковой строке значение: {value}'):
            self.wait_for_selector(self.css_search)
            self.fill(self.css_search, value, 'Поиск отделения')
            self.screenshot('search_string_set', locator=self.page_element)
        return self

    def search_point(self, address):
        with allure.step(f'Найти отделения по адресу: {address}'):
            cnt_before = self.get_point_count()
            self.set_search_string(address)
            if cnt_before > 1:
                self._check_point_count_updated(cnt_before)

        return self

    def select_point(self, address):
        with allure.step(f'Выбрать отделение по адресу: {address}'):
            self.search_point(address)
            self.click_point(address)
            self.screenshot('point_selected', locator=self.page_element)
        return self

    def get_point_count(self):
        with allure.step('Считать количество отделений в списке'):
            return self.count(self.css_point)

    def _check_point_count_updated(self, cnt_before):
        with allure.step('Проверить, что количество отделений изменилось'):
            allure.attach(str(cnt_before), 'points_count_before', AttachmentType.TEXT)
            cnt_updated = False
            for _ in range(5):
                cnt_after = self.get_point_count()
                if cnt_after != cnt_before:
                    cnt_updated = True
                    break
                self.wait_for_timeout(1)
            allure.attach(str(cnt_after), 'points_count_after', AttachmentType.TEXT)
            assert cnt_updated, 'Количество отделений не изменилось при поиске'

        return self
