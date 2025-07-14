import allure

from library.site.ui import *


class PointCard(BasePage):
    page_element = '.map-card__active'
    css_point_card = '.map-card__active'
    css_build_route = '.map-schedule__button:text("Построить маршрут")'
    css_point_page = '.map-schedule__button:text("Страница отделения")'
    css_close = '.map-card__close'
    css_lens = '.slick-gallery__btn-full-window'
    css_calendar = '.calendar'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_point_card)
        self.screenshot('PointCard_loaded', locator=self.page_element)

    def click_close_point(self):
        with allure.step('Кликнуть на иконку закрытия карточки отделения'):
            self.click(self.css_close)
            self.wait_for_selector(self.css_point_card, state='detached')
            self.screenshot('close_point_clicked', locator=self.page_element)
        return self

    def click_build_route(self):
        with allure.step('Кликнуть на кнопку "Построить маршрут"'):
            self.click(self.css_build_route, 'Построить маршрут', force=False)
            self.wait_for_selector('.ymaps-2-1-79-routerRoutes-pane canvas')
            self.screenshot('build_route_clicked', locator=self.page_element)
        return self

    def get_point_info(self):
        data = {}
        with allure.step('Считать данные из открытой карточки отделения'):
            if self.is_mobile:
                data['Адрес'] = self.inner_text(f"{self.css_point_card} .map-card__address_mobile", timeout=1000)
            else:
                data['Адрес'] = self.inner_text(f"{self.css_point_card} .map-card__address", timeout=1000)

            data['Название'] = self.inner_text(f"{self.css_point_card} .map-card__title", timeout=1000)
            data['Фото'] = self.get_attribute(f"{self.css_point_card} .slick-current img", 'src')
            data['Расписание'] = self.inner_text(f"{self.css_point_card} .map-schedule", timeout=1000)

            services = []
            services_cnt = self.count(f"{self.css_point_card} .map-card__tag")
            for i in range(services_cnt):
                service = {
                    'Название': self.inner_text(
                        f"{self.css_point_card} .map-card__tag:nth-child({i + 1}) .map-card__tag-text", timeout=1000),
                    'Иконка': self.get_attribute(f"{self.css_point_card} .map-card__tag:nth-child({i + 1}) img", 'src')
                }
                services.append(service)
            data['Услуги'] = services

            allure.attach(str(data), f'Данные карточки отделения: {data}', allure.attachment_type.JSON)

        return data

    def open_calendar(self):
        with allure.step('Кликнуть на дату и открыть блок с календарем '):
            self.click(self.css_calendar, 'Календарь', force=False)
            from library.site.ui.blocks.map.common.PointCalendar import PointCalendar
            block = PointCalendar(self.page)
            block.set_parent(self)
        return block

    def open_point_page(self):
        with allure.step('Кликнуть на кнопку "Страница отделения" и открыть страницу отделения'):
            self.click(self.css_point_page, 'Страница отделения', force=False)
            from library.site.ui import FindOfficePage
            page = FindOfficePage(self.page)
        return page
