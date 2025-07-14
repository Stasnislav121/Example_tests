import allure

from library.site.ui.pages.BasePage import BasePage


class SenderPointForm(BasePage):
    css_title = '.calculator__title:text("Выберите отделение отправителя")'
    css_continue = '.calculator__button_next-step'
    css_tab_list_mobile = '.nav__item:text("Список")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui import CalculatorPointMap
            block = CalculatorPointMap(self.page)
            block.set_parent(self)
        return block

    def block_points(self):
        with allure.step('Обращение к блоку списка отделений'):
            self.switch_to_point_list()
            from library.site.ui import CalculatorPointListBlock
            block = CalculatorPointListBlock(self.page)
            block.set_parent(self)
        return block

    def select_any_point(self):
        self.block_map().click_any_point()
        return self

    def select_point_from_list(self, address=None):
        if address is not None:
            self.block_points().select_point(address)
        else:
            self.block_points().click_any_point()
        return self

    def switch_to_point_list(self):
        if self.is_mobile:
            with allure.step('Переключиться на вкладку "Список" (в мобильной версии)'):
                self.click(self.css_tab_list_mobile, force=False)
                self.wait_for_selector(f"{self.css_tab_list_mobile}.active")
        return self

    def goto_next_step(self, is_kd=False):
        with allure.step('Кликнуть на кнопку "Далее" и перейти к форме выбора отправителя'):
            self.click(f"{self.css_continue}", 'Далее', force=False)
            self.screenshot('goto_next_step')

            if is_kd:
                from library.site.ui import ReceiverAddressForm
                form = ReceiverAddressForm(self.page)
                form.set_parent(self.get_parent())
            else:
                from library.site.ui import ReceiverPointForm
                form = ReceiverPointForm(self.page)
                form.set_parent(self.get_parent())

        return form
