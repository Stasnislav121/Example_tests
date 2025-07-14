import allure

from library.site.ui.pages.BasePage import BasePage


class ReceiverAddressForm(BasePage):
    css_title = '.calculator__title:text("Введите адрес получателя")'
    css_continue = '.calculator__button_next-step'
    css_flat = '#recipient-flat'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)

    def set_flat(self, number='1'):
        with allure.step(f'Установить в поле "Квартира" номер: {number}'):
            self.fill(self.css_flat, number)
        return self

    def goto_next_step(self):
        with allure.step('Кликнуть на кнопку "Далее" и перейти к форме "Данные отправителя и получателя"'):
            self.click(f"{self.css_continue}", 'Далее')
            self.screenshot('goto_next_step')

            from library.site.ui import SenderAndReceiverDataForm
            form = SenderAndReceiverDataForm(self.page)
            form.set_parent(self.get_parent())
        return form
