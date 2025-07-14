import allure

from library.site.ui.pages.BasePage import BasePage


class CalculatorOptionsForm(BasePage):
    page_element = '.calculator-options'
    css_package_item = '.calc-package-select__item'
    css_package_type = '.calc-package-select__nav .nav__item'
    css_from_point_to_door = '.calc-radio-btn__name:text("От отделения до двери")'
    css_from_door_to_point = '.calc-radio-btn__name:text("От двери до отделения")'
    css_from_door_to_door = '.calc-radio-btn__name:text("От двери до двери")'
    css_from_point_to_point = '.calc-radio-btn__name:text("От отделения до отделения")'
    css_delivery_type = '.calc-radio-wrap'
    css_street = '[placeholder="Улица"]'
    css_house = '[placeholder="Дом"]'
    css_calculate = ':text("Рассчитать")'
    css_promo_code_field = '#promocode'
    css_apply_promo_code = '.calculator__promocode-content a:has-text("Применить")'
    css_expand_promo_code = '.calculator-field__label:text("Промокод")'
    css_service_item = '.accordion__list-item'
    css_expand_services = '.calculator-field__label:text("Включенные услуги")'
    css_map_address_block = {
        'От отделения до двери': '.form-address-wrap[data-qa-id="3"]',
        'От двери до отделения': '.form-address-wrap[data-qa-id="2"]',
        'От двери до двери': '.form-address-wrap[data-qa-id="1"]'
    }

    def check_element(self, screen=False):
        with allure.step("Проверить блок опций доставки"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('CalculatorOptionsBlock_loaded', locator=self.page_element)
        return self

    def apply_promo_code(self, value='test'):
        with allure.step(f'Применить промокод: {value}'):
            self.click(self.css_expand_promo_code, 'Промокод', force=False)
            self.fill(self.css_promo_code_field, value)
            self.click(self.css_apply_promo_code, 'Применить', force=False)
            self.screenshot('promo_code_applied', locator=self.page_element)
        return self

    def click_from_point_to_point(self):
        with allure.step('Кликнуть в чек-бокс "От отделения до отделения"'):
            self.click(self.css_from_point_to_point, 'От отделения до отделения', force=False)
            self.wait_for_selector(f".calc-radio-btn.active {self.css_from_point_to_point}")
            self.screenshot('from_point_to_point_clicked', locator=self.page_element)
        return self

    def click_from_point_to_door(self):
        with allure.step('Кликнуть в чек-бокс "От отделения до двери"'):
            self.click(self.css_from_point_to_door, 'От отделения до двери', force=False)
            self.wait_for_selector(f".calc-radio-btn.active {self.css_from_point_to_door}")
            self.screenshot('from_point_to_door_clicked', locator=self.page_element)
        return self

    def click_from_door_to_point(self):
        with allure.step('Кликнуть в чек-бокс "От двери до отделения"'):
            self.click(self.css_from_door_to_point, 'От отделения до двери', force=False)
            self.wait_for_selector(f".calc-radio-btn.active {self.css_from_door_to_point}")
            self.screenshot('from_door_to_point_clicked', locator=self.page_element)
        return self

    def click_from_door_to_door(self):
        with allure.step('Кликнуть в чек-бокс "От двери до двери"'):
            self.click(self.css_from_door_to_door, 'От двери до двери', force=False)
            self.wait_for_selector(f".calc-radio-btn.active {self.css_from_door_to_door}")
            self.screenshot('from_door_to_door_clicked', locator=self.page_element)
        return self

    def click_expand_services(self):
        with allure.step('Кликнуть в раскрытие поля "Включенные услуги"'):
            self.wait_for_selector(self.css_expand_services)
            self.click(self.css_expand_services, 'Включенные услуги')
            self.screenshot('expand_services_clicked', locator=self.page_element)
        return self

    def click_calculate(self, delivery_option):
        with allure.step(f'Кликнуть на кнопку "Рассчитать" блока "{delivery_option}"'):
            address_block = self.css_map_address_block[delivery_option]
            self.click(f"{address_block} {self.css_calculate}", 'Рассчитать', force=False)
            self.screenshot('calculate_clicked', locator=self.page_element)
        return self

    def set_street(self, street, delivery_option, destination):  # destination = [получателя, отправителя]
        with allure.step(f'Установить в поле "Улица" блока "{delivery_option}" значение: {street}'):
            address_block = self.css_map_address_block[delivery_option]
            self.fill(f"{address_block} .form-address:has-text('Адрес {destination}') {self.css_street}", street)
            self.screenshot('street_set', locator=self.page_element)
        return self

    def set_house(self, house, delivery_option, destination):  # destination = [получателя, отправителя]
        with allure.step(f'Установить в поле "Дом" блока "{delivery_option}" значение: {house}'):
            address_block = self.css_map_address_block[delivery_option]
            locator = f"{address_block} .form-address:has-text('Адрес {destination}') {self.css_house}"
            self.wait_for_selector(locator)
            self.click(locator)
            self.wait_for_timeout(0.5)
            self.fill(locator, house)
            self.screenshot('house_set', locator=self.page_element)
        return self

    def select_street(self, street, delivery_option, destination):
        with allure.step(f'Выбрать в поле "Улица" блока "{delivery_option}" значение: {street}'):
            self.set_street(street, delivery_option, destination)
            self.click(f'.suggestions-suggestion:has-text("{street}")')
            self.screenshot('street_selected', locator=self.page_element)
        return self

    def select_house(self, house, delivery_option, destination):
        with allure.step(f'Выбрать в поле "Дом" блока "{delivery_option}" значение: {house}'):
            self.set_house(house, delivery_option, destination)
            self.click(f'.suggestions-suggestion:has-text("{house}")')
            self.screenshot('house_selected', locator=self.page_element)
        return self

    def select_from_point_to_door(self, street='ул Алая', house='д 1'):
        with allure.step(f'Выбрать опцию доставки "От отделения до двери" и заполнить адрес получателя: '
                         f'улица = {street}, дом = {house}'):
            self.wait_for_timeout(2)
            self.click_from_point_to_door()
            self.select_street(street, delivery_option="От отделения до двери", destination='получателя')
            self.select_house(house, delivery_option="От отделения до двери", destination='получателя')
            self.click_calculate(delivery_option="От отделения до двери")
            self.check_delivery_option_price_calculated('От отделения до двери')
            self.screenshot('from_point_to_door_selected', locator=self.page_element)
        return self

    def select_from_door_to_point(self, street='ул Алая', house='д 1'):
        with allure.step(f'Выбрать опцию доставки "От двери до отделения" и заполнить адрес отправителя: '
                         f'улица = {street}, дом = {house}'):
            self.wait_for_timeout(2)
            self.click_from_door_to_point()
            self.select_street(street, delivery_option="От двери до отделения", destination='отправителя')
            self.select_house(house, delivery_option="От двери до отделения", destination='отправителя')
            self.click_calculate(delivery_option="От двери до отделения")
            self.check_delivery_option_price_calculated('От двери до отделения')
            self.screenshot('from_door_to_point_selected', locator=self.page_element)
        return self

    def select_from_door_to_door(self, from_street='ул Алая', from_house='д 1', to_street='Алабяна', to_house='д 11'):
        with allure.step(f'Выбрать опцию доставки "От двери до двери" и заполнить адрес отправителя: '
                         f'улица = {from_street}, дом = {from_house} и получателя: '
                         f'улица = {to_street}, дом = {to_house}'):
            self.wait_for_timeout(2)
            self.click_from_door_to_door()
            self.select_street(from_street, delivery_option="От двери до двери", destination='отправителя')
            self.select_house(from_house, delivery_option="От двери до двери", destination='отправителя')
            self.select_street(to_street, delivery_option="От двери до двери", destination='получателя')
            self.select_house(to_house, delivery_option="От двери до двери", destination='получателя')
            self.click_calculate(delivery_option="От двери до двери")
            self.check_delivery_option_price_calculated('От двери до двери')
            self.screenshot('from_door_to_door_selected', locator=self.page_element)
        return self

    def check_delivery_option_price_calculated(self, delivery_option):
        with allure.step(f'Проверить, что стоимость доставки варианта "{delivery_option}" рассчитана'):
            price, n = None, 0
            while n < 5 and price in [None, '-']:
                delivery_options = self.get_delivery_options()
                for option in delivery_options:
                    if option['Название'] == delivery_option:
                        price = option['Стоимость']
                n += 1
                self.wait_for_timeout(1)

            assert price, f'Стоимость доставки варианта: "{delivery_option}" не найдена'
            assert price != '', f'Стоимость доставки варианта: "{delivery_option}" не рассчитана'

    def get_services(self):
        with allure.step('Считать данные поля "Включенные услуги"'):
            services = []
            self.wait_for_selector(self.css_service_item)
            cnt = self.count(self.css_service_item)
            for i in range(cnt):
                service_name = self.inner_text(f"{self.css_service_item}:nth-child({i + 1})")
                services.append(service_name)

            allure.attach(str(services), 'Включенные услуги', allure.attachment_type.JSON)
        return services

    def get_delivery_options(self):
        with allure.step('Считать данные поля "Выберите вариант доставки"'):
            delivery_options = []
            self.wait_for_selector(self.css_delivery_type)
            cnt = self.count(self.css_delivery_type)

            for i in range(cnt):
                if self.is_mobile:
                    i *= 2

                option = {}
                option_locator = f"{self.css_delivery_type}:nth-child({i + 1})"
                option['Название'] = self.inner_text(f"{option_locator} .calc-radio-btn__name").replace('\xa0', ' ')
                option['Срок'] = self.inner_text(f"{option_locator} .calc-radio-btn__days")
                option['Стоимость'] = self.inner_text(f"{option_locator} .calculator-options__cost")
                delivery_options.append(option)

            allure.attach(str(delivery_options), 'Варианты доставки', allure.attachment_type.JSON)
        return delivery_options
