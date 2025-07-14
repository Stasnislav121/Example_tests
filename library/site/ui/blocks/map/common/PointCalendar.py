import allure

from library.site.ui.pages.BasePage import BasePage


class PointCalendar(BasePage):
    page_element = '.vdpInnerWrap'
    css_calendar = '.vdpInnerWrap'
    css_date_cell = '[data-id]:not(.outOfRange)'
    css_next_month = '[title="Next month"]'
    css_current_month = '.vdpPeriodControl:nth-child(1) .vdpPrevDirection'
    css_current_year = '.vdpPeriodControl:nth-child(2) .vdpPrevDirection'
    css_current_day = '.today'
    css_select_month = '.vdpPeriodControl:nth-child(1) select'
    css_select_year = '.vdpPeriodControl:nth-child(2) select'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_calendar)
        self.screenshot('PointCalendar_loaded', locator=self.page_element)

    def get_selectable_dates_cnt(self):
        with allure.step('Получить количество доступных для выбора дат в текущем месяце'):
            cnt = self.count(f"{self.css_date_cell}.selectable")
            allure.attach(str(cnt), f'Количество доступных для выбора дат: {cnt}', allure.attachment_type.JSON)
        return cnt

    def click_next_month(self):
        with allure.step('Кликнуть на иконку перехода к следующему месяцу: >'):
            self.click(self.css_next_month, force=False)
            self.wait_for_selector('.vdpNextDirection')
            self.screenshot('next_month_clicked', locator=self.page_element)
        return self

    def get_current_date(self):
        with allure.step('Получить текущую выбранную дату'):
            date = {
                'Месяц': self.inner_text(self.css_current_month),
                'Год': self.inner_text(self.css_current_year),
                'День': self.inner_text(self.css_current_day)
            }
            allure.attach(str(date), f'Текущая дата: {date}', allure.attachment_type.JSON)
        return date
