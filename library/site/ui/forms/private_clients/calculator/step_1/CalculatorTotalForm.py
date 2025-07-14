import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorTotalForm(BasePage):
    css_delivery_price_desktop = '.calculator-total__info__cost'
    css_delivery_price_mobile = '.calc-fixed__cost'
    css_delivery_time_desktop = '.calculator-total__desc'
    css_delivery_time_mobile = '.calc-fixed__days'
    css_register_delivery_desktop = '.calculator__button:text("Оформить доставку")'
    css_register_delivery_mobile = '.calc-fixed .calculator__button:text("Оформить доставку")'

    def __init__(self, page):
        super().__init__(page)
        if self.is_mobile:
            self.page_element = '.calc-fixed'
        else:
            self.page_element = '.calculator-total-wrap'

    def check_element(self, screen=False):
        with allure.step('Проверить блок "Стоимость доставки"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorTotalBlock_loaded', locator=self.page_element)
        return self

    def check_delivery_price_recalculated(self, price_before: float, max_retries=10):
        with allure.step('Проверить, что стоимость доставки пересчитана'):
            price_recalculated = False
            for _ in range(max_retries):
                price_after = self.get_order_delivery_info()['Стоимость']
                if price_after != price_before:
                    price_recalculated = True
                    break
                self.wait_for_timeout(1)
            assert price_recalculated, \
                f'Стоимость не пересчитана, начальная стоимость: {price_after}, текущая стоимость: {price_after}'
            self.screenshot('delivery_price_recalculated', locator=self.page_element)

        return self

    def check_register_button_status(self, disabled=False):
        with allure.step('Проверить, что кнопка "Оформить доставку" ' +
                         ('неактивна' if disabled else 'активна')):
            if self.is_mobile:
                if disabled:
                    self.wait_for_selector(
                        f"{self.css_register_delivery_mobile}.calculator__button_disabled")
                else:
                    self.wait_for_selector(self.css_register_delivery_mobile)
            else:
                if disabled:
                    self.wait_for_selector(f"{self.css_register_delivery_desktop}.calculator__button_disabled")
                else:
                    self.wait_for_selector(self.css_register_delivery_desktop)

        return self

    def get_order_delivery_info(self):
        info = {}
        with allure.step('Считать данные о заказе'):
            if self.is_mobile:
                cost = self.inner_text(self.css_delivery_price_mobile)
                period = self.inner_text(self.css_delivery_time_mobile)
            else:
                cost = self.inner_text(self.css_delivery_price_desktop)
                period = self.inner_text(self.css_delivery_time_desktop)

            info['Стоимость'] = float(cost.strip().split()[0])
            info['Срок доставки'] = ' '.join(period.replace('\n', ' ').split())
            allure.attach(str(info), 'Информация о доставке', allure.attachment_type.JSON)
        return info

    def click_next_step(self):
        with allure.step('Кликнуть на кнопку "Оформить доставку" '):
            if self.is_mobile:
                self.wait_for_selector(self.css_register_delivery_mobile)
                self.click(self.css_register_delivery_mobile, force=False)
            else:
                self.wait_for_selector(self.css_register_delivery_desktop)
                self.click(self.css_register_delivery_desktop, force=False)
            self.screenshot('next_step_clicked')

        return self

    def goto_sender_point_form(self):
        with allure.step('Кликнуть на кнопку "Оформить доставку" и перейти к форме выбора отделения отправителя'):
            with self.expect_response(lambda request: '/api/v1/odp' in request.url):
                self.wait_for_timeout(1)
                self.click_next_step()
            from library.site.ui import SenderPointForm
            form = SenderPointForm(self.page)
            form.set_parent(self.get_parent())

        return form

    def goto_sender_address_form(self):
        with allure.step('Кликнуть на кнопку "Оформить доставку" и перейти к форме выбора адреса отправителя'):
            with self.expect_response(lambda request: '/api/v1/odp' in request.url):
                self.wait_for_timeout(1)
                self.click_next_step()
            from library.site.ui import SenderAddressForm
            form = SenderAddressForm(self.page)
            form.set_parent(self.get_parent())
        return form

    def goto_attachment_form(self):
        with allure.step('Кликнуть на кнопку "Оформить доставку" и перейти к форме заполнения данных о посылке'):
            self.wait_for_timeout(1)
            self.click_next_step()
            from library.site.ui import AttachmentForm
            form = AttachmentForm(self.page)
            form.set_parent(self.get_parent())

        return form
