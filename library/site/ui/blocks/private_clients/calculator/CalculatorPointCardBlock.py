import allure

from library.site.ui import *


class CalculatorPointCardBlock(BasePage):
    css_cluster_icon = '.ymaps-2-1-79-svg-icon'
    css_point_icon = '.ymaps-2-1-79-image'
    css_point_card = '.map-card_active'
    css_select_point = 'a:text("Выбрать это отделение")'
    css_cancel = 'a:text("Отмена")'
    css_selected = '.map-schedule__button:text("Выбрано")'
    css_close = '.map-card__close'

    def click_any_point(self):
        with allure.step('Кликнуть на иконку любого отделения'):
            self.click(self.css_point_icon)
            self.wait_for_selector(self.css_point_card)
        return self

    def click_select_point(self):
        with allure.step('Кликнуть на кнопку "Выбрать это отделение"'):
            self.click(self.css_select_point, 'Выбрать это отделение', force=False)
            self.wait_for_selector(self.css_selected)
            self.wait_for_selector(self.css_cancel)
        return self

    def click_close_point(self):
        with allure.step('Кликнуть на иконку закрытия карточки отделения'):
            self.click(self.css_cancel)
            self.wait_for_selector(self.css_point_card, state='detached')
        return self

    def get_point_info(self):
        data = {}
        with allure.step('Считать данные из открытой карточки отделения'):
            data['Адрес'] = self.inner_text(f"{self.css_point_card} .map-card__title")
            data['Телефон'] = self.inner_text(f"{self.css_point_card} .map-card__phone")
            data['Режим работы'] = self.inner_text(f"{self.css_point_card} .map-card__work-time")

        return data
