import allure

from allure_commons.types import AttachmentType
from library.site.ui import PointMap, BasePage, FindAtOfficesPointMap


class PrivateClientsMapFilterControl(BasePage):
    page_element = '.map-nav__button_submenu'
    css_map = {
        'Международные отправления': '[for="interRefunds"]',
    }

    def check_element(self, screen=False):
        with allure.step("Проверить контрол переключателей фильтров отделений"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что контрол загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('PrivateClientsMapFilterControl_loaded', locator=self.page_element)
        return self

    def switch_point_inter_refunds_filter(self, tab, select, switch_name, city_code='68', check_count=True):
        with allure.step(f'Переключить фильтр: "Прием в отделении" в положение {select}'):
            inter_refunds_param = '&interRefunds=1' if select else ''
            url = f'api/v1/odp?cityCode={city_code}&select=id,geo&perPage=1000&{tab}=1{inter_refunds_param}&page=1'
            with self.expect_response(lambda request:
                                      url in request.url) as resp_info:
                self.__switch_filter(switch_name=switch_name, check_count=check_count)
            resp_info.value.finished()

            self.screenshot(name='point_inter_refunds_filter_switched')
        return self

    def __switch_filter(self, switch_name, check_count=True):
        with allure.step(f'Переключить фильтр: "{switch_name}"'):
            if "find_an_office" in self.page.url:
                page = FindAtOfficesPointMap(self.page)
            else:
                page = PointMap(self.page)
            points_before = page.get_points_cnt()
            allure.attach(str(points_before), 'points_count_before', AttachmentType.TEXT)
            self.click(self.css_map[switch_name], force=False)
            cnt_updated = False
            if check_count:
                for _ in range(10):
                    points_after = page.get_points_cnt()
                    if points_after != points_before:
                        cnt_updated = True
                        break
                    self.wait_for_timeout(1)
                allure.attach(str(points_after), 'points_count_after', AttachmentType.TEXT)
                assert cnt_updated, 'Количество отделений не изменилось после переключения фильтра'

        return self

    def switch_on_point_inter_refunds_filter_in_tab_recipient(self, check_count=False):
        with allure.step('Включить фильтр: "Международные отправления" в табе "Получение посылок получателем"'):
            self.switch_point_inter_refunds_filter(tab='deliveryLap', select=True,
                                                   switch_name='Международные отправления',
                                                   check_count=check_count)
        return self

    def switch_off_point_inter_refunds_filter_in_tab_recipient(self, check_count=False):
        with allure.step('Выключить фильтр: "Международные отправления" в табе "Получение посылок получателем"'):
            self.switch_point_inter_refunds_filter(tab='deliveryLap', select=False,
                                                   switch_name='Международные отправления',
                                                   check_count=check_count)
        return self

    def switch_on_point_inter_refunds_filter_in_tab_sender(self, check_count=False):
        with allure.step('Включить фильтр: "Международные отправления" в табе "Прием посылок от отправителя"'):
            self.switch_point_inter_refunds_filter(tab='receptionLap', select=True,
                                                   switch_name='Международные отправления',
                                                   check_count=check_count)
        return self

    def switch_off_point_inter_refunds_filter_in_tab_sender(self, check_count=False):
        with allure.step('Выключить фильтр: "Международные отправления" в табе "Прием посылок от отправителя"'):
            self.switch_point_inter_refunds_filter(tab='receptionLap', select=False,
                                                   switch_name='Международные отправления',
                                                   check_count=check_count)
        return self
