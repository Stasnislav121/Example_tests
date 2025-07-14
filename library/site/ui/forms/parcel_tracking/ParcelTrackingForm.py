import allure

from library.site.ui.pages.BasePage import BasePage


class ParcelTrackingForm(BasePage):
    page_element = '.track-widget'
    css_delivery_number = 'input#box'
    css_track = '.formbar-field_search > a'
    css_load = '.track-widget-list__loading'
    css_arrow = '.track-item-arrow'
    css_empty_search_title = '.empty-search-result__title'
    css_empty_search_reason_wrap = '.empty-search-result__col'
    css_empty_search_reason_title = '.empty-search-result__col-title'
    css_comment_text = '.calc-comment__text_text-big'
    css_gift_banner = '.gift-tracking-card'

    def check_element(self, screen=False):
        with allure.step("Проверить форму трекинга"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что форма загрузилась"):
                self.wait_for_selector(self.page_element)
                self.screenshot('ParcelTrackingForm_loaded', locator=self.page_element)
        return self

    def check_parcel_not_found(self):
        with (allure.step('Проверить, что заказ не найден')):
            self.wait_for_selector('.empty-search-result')
            self.screenshot('parcel_not_found')

            with allure.step('Отображается заголовок'):
                title = self.inner_text(self.css_empty_search_title)
                allure.attach(title, 'Заголовок', allure.attachment_type.TEXT)
                expected_title = 'Номер заказа не найден по нескольким причинам:'
                assert title == expected_title, f'Ожидался заголовок: {expected_title}, получен: {title}'

            with allure.step('Отображается причина: "Скоро станет доступен"'):
                title = self.inner_text(
                    f'{self.css_empty_search_reason_wrap}:nth-child(1) {self.css_empty_search_reason_title}')
                allure.attach(title, 'Причина', allure.attachment_type.TEXT)
                expected_title = 'Скоро станет доступен'
                assert title == expected_title, f'Ожидалась причина 1: {expected_title}, получена: {title}'

            with allure.step('Отображается причина: "Попробуйте еще раз"'):
                title = self.inner_text(
                    f'{self.css_empty_search_reason_wrap}:nth-child(2) {self.css_empty_search_reason_title}')
                allure.attach(title, 'Причина', allure.attachment_type.TEXT)
                expected_title = 'Попробуйте еще раз'
                assert title == expected_title, f'Ожидалась причина 2: {expected_title}, получена: {title}'

            with allure.step('Отображается причина: "Чтобы увидеть свои отправления, авторизуйтесь в мобильном '
                             'приложении  или в личном кабинете"'):
                title = self.inner_text(self.css_comment_text) \
                    .replace('\n', '').strip()  # для webkit
                allure.attach(title, 'Причина', allure.attachment_type.TEXT)
                expected_title = ('Чтобы увидеть свои отправления, авторизуйтесь в мобильном приложении  '
                                  'или в личном кабинете')
                assert title == expected_title, f'Ожидалась причина: {expected_title}, получена: {title}'

        return self

    def get_data(self):
        with allure.step('Считать данные в форме отслеживания посылки'):
            data = {
                'Посылки': []
            }
            self.wait_for_selector('.track-widget__content')
            parcel_cnt = self.count('.track-widget-list__item')
            for i in range(parcel_cnt):
                parcel = {}
                parcel_locator = f'.track-widget-list__item:nth-child({i + 1})'
                parcel['Строка №'] = i + 1

                is_sender_visible = self.is_visible(f'{parcel_locator} .track-item__sender')
                if is_sender_visible:
                    parcel['Отправитель'] = self.inner_text(f'{parcel_locator} .track-item__sender')
                else:
                    parcel['Отправитель'] = ''

                parcel['Номер ИМ'] = self.inner_text(f'{parcel_locator} .track-item__number-store')
                parcel['Номер заказа'] = self.inner_text(f'{parcel_locator} .track-item__number-bb')

                is_details_visible = self.is_visible(f'{parcel_locator} .track-details')
                is_status_visible = self.is_visible(f'{parcel_locator} .track-details__status')
                if is_details_visible:
                    details_cnt = self.count('.track-details-item__title')
                    for i in range(1, details_cnt):
                        detail = f'.track-details-item:nth-child({i})'
                        title = self.inner_text(f'{detail} .track-details-item__title').replace(':', '')
                        value = self.inner_text(f'{detail} .track-details-item__body').replace('\n', '').strip() \
                            # replace и strip добавлены из-за браузера Webkit
                        parcel[title] = value
                    if is_status_visible:
                        parcel['Статусы отправления'] = []
                        status_cnt = self.count('.history-step__item')
                        for i in range(status_cnt):
                            item_locator = f'.history-step__item:nth-child({i + 1})'
                            status = {
                                'Название RU': self.inner_text(f'{item_locator} .history-step__name_lang-ru'),
                                # 'Название EN': self.inner_text(f'{item_locator} .history-step__name_lang-en'),
                                'Дата': self.inner_text(f'{item_locator} .history-step__date'),
                                'Город': self.inner_text(f'{item_locator} .history-step__location')
                            }
                            parcel['Статусы отправления'].append(status)

                data['Посылки'].append(parcel)

            allure.attach(str(data), "Данные поиска", allure.attachment_type.JSON)

        return data

    def set_parcel_number(self, number):
        with allure.step(f'Установить в поле "Введите номер отправления" значение: {number}'):
            self.fill(self.css_delivery_number, number)
            self.screenshot('parcel_number_set', locator=self.page_element)
        return self

    def click_track(self):
        with allure.step('Кликнуть на кнопку "Отследить"'):
            with self.expect_response(
                    lambda request: '/api/v1/tracking/order/get?searchId=' in request.url) as resp_info:
                self.click(self.css_track, 'Отследить', force=False)
            resp_info.value.finished()
        return self

    def click_arrow(self, parcel_num=None):
        with allure.step('Кликнуть на иконку стрелки напротив ' +
                         f'{parcel_num}-й посылки в списке' if parcel_num is not None else 'любой посылки в списке'):
            if parcel_num is not None:
                self.click(f".track-widget-list__item:nth-child({parcel_num}) {self.css_arrow}", force=False)
                self.wait_for_selector(f".track-widget-list__item:nth-child({parcel_num}) .track-details_active")
            else:
                self.click(self.css_arrow, force=False)
                self.wait_for_selector(".track-details_active")

            self.screenshot('arrow_clicked', locator=self.page_element)

        return self

    def track_parcel(self, number):
        with allure.step(f'Отследить посылку: {number}'):
            self.set_parcel_number(number)
            self.click_track()
        return self

    def check_parcel_card_expanded(self):
        with allure.step('Проверить, что карточка заказа развернута'):
            self.wait_for_selector('.track-widget-list__item.active')
        return self

    def check_about_order_block_point_delivery(self):
        with allure.step('Проверить блок "О заказе"'):
            with allure.step('Отображается название блока'):
                self.wait_for_selector('.track-details__title:text("О заказе")')
            with allure.step('Отображается кнопка "Показать на карте"'):
                self.wait_for_selector('.track-details-item__map-link:has-text("Показать на карте")')

        return self

    def check_about_order_block_courier_delivery(self):
        with allure.step('Проверить блок "О заказе"'):
            with allure.step('Отображается название блока'):
                self.wait_for_selector('.track-details__title:text("О заказе")')
            with allure.step('Отображается поле "Статус заказа"'):
                self.wait_for_selector('.track-details-item__title:text("Статус заказа:")')
            with allure.step('Отображается поле "Плановая дата доставки"'):
                self.wait_for_selector('.track-details-item__title:text("Плановая дата доставки:")')
            with allure.step('Отображается поле "К оплате"'):
                self.wait_for_selector('.track-details-item__title:text("К оплате:")')
            with allure.step('Отображается поле "Способы оплаты"'):
                self.wait_for_selector('.track-details-item__title:text("Способы оплаты:")')
            with allure.step('Отображается поле "Адрес доставки"'):
                self.wait_for_selector('.track-details-item__title:text("Адрес доставки:")')

        return self

    def check_statuses_block(self):
        with allure.step('Проверить блок "Статусы отправления"'):
            with allure.step('Отображается название блока'):
                self.wait_for_selector('.track-details__title:text("Статусы отправления")')
            with allure.step('Отображается хотя бы 1 статус'):
                self.wait_for_selector('.history-step__item')
            with allure.step('У статуса отображается иконка в виде круга'):
                self.wait_for_selector('.history-step__circle')
            with allure.step('У статуса отображаются описания на русском и английском языках'):
                self.wait_for_selector('.history-step__name_lang-ru')
                # self.wait_for_selector('.history-step__name_lang-en')
            with allure.step('У статуса отображается дата'):
                self.wait_for_selector('.history-step__date')
            with allure.step('У статуса отображается город'):
                self.wait_for_selector('.history-step__location')

        return self

    def check_delivery_point_block(self):
        with allure.step('Проверить блок "Время работы отделения"'):
            with allure.step('Отображается название блока'):
                self.wait_for_selector('.map-schedule__title:has-text("Время работы отделения")')
            with allure.step('Отображается календарь'):
                self.wait_for_selector('.map-schedule__calendar')

        return self

    def check_gift_banner(self):
        with allure.step('Проверить отображение банера "Выберите подарок от нашего партнера"'):
            self.wait_for_selector(self.css_gift_banner)
        return self

    def go_to_gift_page(self):
        with allure.step('Нажать на кнопку "Выбрать подарок"'):
            with self.expect_page() as gift_page:
                self.click('.gift-tracking-card__btn', force=False)
            url = gift_page.value.url
        return url
