import allure

from library.site.ui.pages.BasePage import BasePage


class ParcelCreatingCustomForm(BasePage):
    page_element = '[name="calculator_pip"]'
    css_title = '.calc-pay__title'
    css_delivery_number = '.calculator__item_active [placeholder="Номер отправления"]'
    css_create_invoice_button = '.calculator__button_red'
    css_calculator_table = '.calculator-table'
    css_field_label = '.calculator-field__label'
    css_delivery_price_desktop = '.calculator-total__info__cost'
    css_delivery_price_mobile = '.calc-fixed__cost'
    css_delivery_time_desktop = '.calculator-total__desc span'
    css_delivery_time_mobile = '.calc-fixed__days'
    css_offer_agreement = '.payment-info__checkbox-label'
    css_total_block = '.calculator__col_total'
    css_calc_item = '.calc-pay__item'
    css_package_content_block = '.accordion__item:has-text("Состав посылки")'
    css_services_block = '.accordion__item:has-text("Включенные услуги")'

    def check_element(self, screen=False):
        with allure.step('Проверить форму "Создание посылки"'):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.wait_for_selector(self.page_element)
                self.screenshot('ParcelCreatingCustomForm_loaded', locator=self.page_element)

            with allure.step('Проверить отображение основного контента формы'):
                with allure.step('Отображается заголовок: "Ваше отправление"'):
                    self.wait_for_selector(f'{self.css_title}:text("Ваше отправление")')

        return self

    def get_order_data(self):
        data = {}
        with allure.step('Считать данные о заказе'):
            item_cnt = self.count(self.css_calc_item)
            for i in range(item_cnt):
                locator = f'{self.css_calc_item}:nth-child({i + 2})'
                title = self.inner_text(f'{locator} .calc-pay__item__title').strip()
                value = self.inner_text(f'{locator} .calc-pay__item__text').strip()
                data[title] = value

            allure.attach(str(data), 'Данные заказа', allure.attachment_type.JSON)

        return data

    def get_delivery_cost_data(self):
        data = {}
        with allure.step('Считать данные в блоке "Стоимость доставки"'):
            if self.is_mobile:
                cost = self.inner_text(self.css_delivery_price_mobile)
                period = self.inner_text(self.css_delivery_time_mobile)
            else:
                cost = self.inner_text(self.css_delivery_price_desktop)
                period = self.inner_text(self.css_delivery_time_desktop)

            data['Стоимость'] = float(cost.strip().split()[0])
            data['Срок доставки'] = period.strip().split()[0]

        allure.attach(str(data), 'Данные блока "Стоимость доставки"', allure.attachment_type.JSON)

        return data

    def get_package_content(self):
        items = []
        with allure.step('Считать данные в блоке "Состав посылки"'):
            locator = '.accordion-customs__li'
            item_cnt = self.count(locator)
            for i in range(item_cnt):
                item = {
                    'Название': self.inner_text(f'{locator}:nth-child({i + 1}) .accordion-customs__li__title').strip(),
                    'Описание': self.inner_text(f'{locator}:nth-child({i + 1}) .accordion-customs__li__text').strip()
                }
                items.append(item)

            allure.attach(str(items), 'Данные блока "Состав доставки"', allure.attachment_type.JSON)

        return items

    def get_services(self):
        services = []
        with allure.step('Считать данные в блоке "Включенные услуги"'):
            locator = '.accordion__list-item'
            item_cnt = self.count(locator)
            for i in range(item_cnt):
                service = self.inner_text(f'{locator}:nth-child({i + 1})').strip()
                services.append(service)

            allure.attach(str(services), 'Данные блока "Включенные услуги"', allure.attachment_type.JSON)

        return services

    def click_package_content(self):
        with allure.step('Кликнуть в блок "Состав посылки"'):
            self.click(f"{self.css_package_content_block}", 'Состав посылки', force=False)
        return self

    def click_services(self):
        with allure.step('Кликнуть в блок "Включенные услуги"'):
            self.click(f"{self.css_services_block}", 'Включенные услуги', force=False)
        return self

    def click_create_invoice(self):
        with allure.step('Кликнуть на кнопку "Создать Электронную накладную"'):
            self.click(f"{self.css_create_invoice_button}", 'Создать Электронную накладную', force=False)
        return self

    def click_offer_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Нажимая “Оплатить” вы соглашаетесь c условиями оферты"'):
            self.click(self.css_offer_agreement, force=False)
            self.screenshot('offer_agreement_clicked', locator=self.page_element)
        return self

    def goto_next_step(self):
        with allure.step('Перейти к следующему шагу формы'):
            self.click_create_invoice()
            self.screenshot('goto_next_step')
            from library.site.ui import ParcelCreatedForm
            form = ParcelCreatedForm(self.page).check_element()

        return form
