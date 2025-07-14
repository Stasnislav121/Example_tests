import allure

from library.site.ui.pages.BasePage import BasePage


class SenderAddressForm(BasePage):
    css_title = '.calculator__title:text("Введите адрес отправителя")'
    css_continue = '.calculator__button_next-step'
    css_street = '#recipient-street'
    css_house = '#recipient-home'
    css_flat = '#recipient-flat'
    css_return_point = '.calculator__btn-return-point'
    css_tab_list_mobile = '.nav__item:text("Список")'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)

    def click_return_point(self):
        with allure.step('Кликнуть на кнопку "Указать адрес отделения"'):
            self.click(self.css_return_point, 'Указать адрес отделения', force=False)
        return self

    def select_street(self, street):
        with allure.step(f'Выбрать в поле "Улица" значение: {street}'):
            self.set_street("")
            self.wait_for_timeout(0.5)
            self.set_street(street)
            self.wait_for_selector(f'.suggestions-suggestion:has-text("{street}")')
            self.click(f'.suggestions-suggestion:has-text("{street}")', force=False)
        return self

    def select_house(self, house='д 1'):
        with allure.step(f'Выбрать в поле "Дом" значение: {house}'):
            self.set_house(house)
            self.click(f'.suggestions-suggestion:has-text("{house}")')
        return self

    def fill_address(self, street, house='д 1', flat='1'):
        self.select_street(street)
        self.select_house(house)
        self.set_flat(flat)
        return self

    def set_flat(self, number='1'):
        with allure.step(f'Установить в поле "Квартира" номер: {number}'):
            self.wait_for_selector(self.css_flat)
            self.fill(self.css_flat, number)
        return self

    def set_street(self, street):
        with allure.step(f'Установить в поле "Улица" значение: {street}'):
            self.wait_for_selector(self.css_street)
            self.fill(self.css_street, street)
            self.click(self.css_street, force=False)
        return self

    def set_house(self, house):
        with allure.step(f'Установить в поле "Дом" значение: {house}'):
            self.wait_for_selector(self.css_house)
            self.fill(self.css_house, house)
        return self

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.private_clients.calculator.CalculatorPointMap import CalculatorPointMap
            block = CalculatorPointMap(self.page)
            block.set_parent(self)
        return block

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
        with allure.step('Кликнуть на кнопку "Далее" и перейти к форме выбора получателя'):
            self.click(f"{self.css_continue}", 'Далее', force=False)

            if is_kd:
                from library.site.ui import ReceiverAddressForm
                form = ReceiverAddressForm(self.page)
                form.set_parent(self.get_parent())
            else:
                from library.site.ui import ReceiverPointForm
                form = ReceiverPointForm(self.page)
                form.set_parent(self.get_parent())

        return form

    def block_points(self):
        with allure.step('Обращение к блоку списка отделений'):
            self.switch_to_point_list()
            from library.site.ui import CalculatorPointListBlock
            block = CalculatorPointListBlock(self.page)
            block.set_parent(self)
        return block
