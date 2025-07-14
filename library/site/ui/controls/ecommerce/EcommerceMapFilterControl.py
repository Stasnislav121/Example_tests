import allure

from allure_commons.types import AttachmentType
from library.site.ui import PointMap, BasePage


class EcommerceMapFilterControl(BasePage):
    page_element = '.map-filter'
    css_map = {
        'Прием в отделении': '[for="reception"]',
        'Прием на терминале': '[for="terminalReception"]',
        'Экспресс-прием': '[for="expressReception"]',
    }

    def check_element(self, screen=False):
        with allure.step("Проверить контрол переключателей фильтров отделений"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что контрол загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('EcommerceMapFilterControl_loaded', locator=self.page_element)
        return self

    def switch_point_reception_filter(self):
        with allure.step('Переключить фильтр: "Прием в отделении"'):
            self.__switch_filter('Прием в отделении')
            self.screenshot('point_reception_filter_switched', locator=self.page_element)
        return self

    def switch_terminal_reception_filter(self):
        with allure.step('Переключить фильтр: "Прием на терминале"'):
            self.__switch_filter('Прием на терминале')
            self.screenshot('terminal_reception_filter_switched', locator=self.page_element)
        return self

    def switch_express_reception_filter(self):
        with allure.step('Переключить фильтр: "Экспресс-прием"'):
            self.__switch_filter('Экспресс-прием')
            self.screenshot('express_reception_filter_switched', locator=self.page_element)
        return self

    def switch_all_filters(self):
        with allure.step('Переключить все фильтры'):
            self.switch_point_reception_filter()
            self.switch_terminal_reception_filter()
            self.switch_express_reception_filter()
        return self

    def __switch_filter(self, switch_name):
        with allure.step(f'Переключить фильтр: "{switch_name}"'):
            points_before = PointMap(self.page).get_points_cnt()
            allure.attach(str(points_before), 'points_count_before', AttachmentType.TEXT)
            self.click(self.css_map[switch_name], force=False)
            cnt_updated = False
            for _ in range(10):
                points_after = PointMap(self.page).get_points_cnt()
                if points_after != points_before:
                    cnt_updated = True
                    break
                self.wait_for_timeout(1)
            allure.attach(str(points_after), 'points_count_after', AttachmentType.TEXT)
            assert cnt_updated, 'Количество отделений не изменилось после переключения фильтра'

        return self
