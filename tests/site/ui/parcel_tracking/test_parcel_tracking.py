import testit
import allure
import pytest

from library.site.helpers import *


class TestParcelTracking:
    @testit.workItemIds(13052)
    @testit.externalId('TestPrivateClients_13052')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Поиск не существующей посылки')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Поиск не существующей посылки')
    @allure.testcase(url='https://testit..ru/browse/13052')
    def test_parcel_tracking_not_existing_parcel(self, site_private_clients_delivery_tracking):
        tracking_page = site_private_clients_delivery_tracking

        with allure.step('Проверить наличие блоков в форме поиска отправления'):
            tracking_page.form_tracking() \
                .track_parcel('9999999999999') \
                .check_parcel_not_found()

    @testit.workItemIds(13054)
    @testit.externalId('TestPrivateClients_13054')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Отображение отслеживания посылки, если найдена только одна посылка')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Отображение отслеживания посылки, если найдена только одна посылка')
    @allure.testcase(url='https://testit..ru/browse/13054')
    def test_parcel_tracking_single_parcel(self, site_private_clients_delivery_tracking, auth_service_predprod_api,
                                           aggregator_service_predprod_api, date_helper):
        tracking_id = 'AUTO000007434'
        sender_name = 'Сфера'
        TrackingHelper.insert_shop(name=sender_name, code='BRR0654873')
        with allure.step(f'Запросить данные о посылке {tracking_id} в ПС'):
            auth_service_predprod_api.add_token('token-get-parcels', 'parcels')
            auth_service_predprod_api.get_access_token(auth_service_predprod_api.lastToken)
            response = aggregator_service_predprod_api.find_parcels_with_statuses(
                {'searchParameters.numberParcels': tracking_id},
                client=auth_service_predprod_api.lastToken
            )
            assert response.status_code == 200, f"Ожидался код ответа: 200, получен: {response.status_code}"
            ml_data = response.json()['parcels'][0]
            order_number = ml_data['orderNumber']
            track_number = ml_data['trackNumber']
            order_status = 'Доступен к получению в Пункте выдачи'
            store_date = date_helper.format_date(date=ml_data['storeDate'], current_format='%Y-%m-%d',
                                                          required_format='%d.%m.%Y')
            store_date = f'{store_date} (включительно)'
            point_address = ml_data['deliveryAddress']
            to_pay = ml_data['amountPay']
            to_pay_format = to_pay / 100
            payment_type = 'Наличный расчет при получении'
            statuses = [{'Название RU': 'Получена информация о заказе. Отправление еще не передано на доставку в '
                                        '', 'Дата': '27.05.2024 (08:21)', 'Город': 'Россия, Москва'},
                        {'Название RU': 'Заказ передан на доставку', 'Дата': '27.05.2024 (08:21)',
                                        'Город': 'Россия, Москва'},
                        {'Название RU': 'Ожидает отправки в город Получателя', 'Дата': '27.05.2024 (08:21)',
                                        'Город': 'Россия, Москва'},
                        {'Название RU': 'В городе Получателя. Ожидайте поступления в Пункт выдачи',
                         'Дата': '27.05.2024 (08:21)', 'Город': 'Россия, Москва'},
                        {'Название RU': 'Доступен к получению в Пункте выдачи', 'Дата': '27.05.2024 (08:21)',
                                        'Город': 'Россия, Москва'}]

        tracking_page = site_private_clients_delivery_tracking
        form_tracking = tracking_page.form_tracking()
        form_tracking.track_parcel(tracking_id) \
            .check_parcel_card_expanded() \
            .check_about_order_block_point_delivery() \
            .check_statuses_block()

        with allure.step('Проверить данные посылки'):
            data = form_tracking.get_data()['Посылки'][0]
            assert len(data) == 10, \
                f"Количество строк данных, ожидалось: 10, получено: {len(data)}"
            assert data['Отправитель'] == sender_name, \
                f"Отправитель, ожидался: {sender_name}, получен: {data['Отправитель']}"
            assert data['Номер ИМ'] == order_number, \
                f"Номер ИМ, ожидался: {order_number}, получен: {data['Номер ИМ']}"
            assert data['Номер заказа'] == track_number, \
                f"Номер заказа, ожидался: {track_number}, получен: {data['Номер заказа']}"
            assert data['Статус заказа'] == order_status, \
                f"Статус заказа, ожидался: {order_status}, получен: {data['Статус заказа']}"
            assert data['Срок хранения'] == store_date, \
                f"Срок хранения, ожидался: {store_date}, получен: {data['Срок хранения']}"
            assert data['К оплате'] == str(to_pay_format), \
                f"К оплате, ожидалось: {to_pay_format}, получен: {data['К оплате']}"
            assert data['Способы оплаты'] == payment_type, \
                f"Способы оплаты, ожидалось: {payment_type}, получен: {data['Способы оплаты']}"
            assert data['Пункт выдачи'] == point_address, \
                f"Пункт выдачи, ожидалось: {point_address}, получен: {data['Пункт выдачи']}"
            assert data['Статусы отправления'] == statuses, \
                f"Статусы отправления, ожидалось: {statuses}, получен: {data['Статусы отправления']}"

    @testit.workItemIds(16972)
    @testit.externalId('TestPrivateClients_16972')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Отображение отслеживания посылки, если найдено несколько посылок')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Отображение отслеживания посылки, если найдено несколько посылок')
    @allure.testcase(url='https://testit..ru/browse/16972')
    def test_parcel_tracking_multiple_parcel(self, site_private_clients_delivery_tracking):
        tracking_page = site_private_clients_delivery_tracking

        form_tracking = tracking_page.form_tracking()
        form_tracking.track_parcel('12345') \
            .click_arrow() \
            .check_parcel_card_expanded()

    @testit.workItemIds(33941)
    @testit.externalId('TestPrivateClients_33941')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Отображение отслеживания посылки в модальном окне, если найдено несколько посылок')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Отображение отслеживания посылки в модальном окне, если найдено несколько '
                  'посылок')
    @allure.testcase(url='https://testit..ru/browse/33941')
    def test_parcel_tracking_multiple_parcel_from_modal(self, site_main_page):
        site_main = site_main_page

        with allure.step('Произвести поиск посылки на главной странице'):
            modal_tracking = site_main.block_form_navigation() \
                .track_parcel('12345')

        with allure.step('Проверить карточку посылки в модальном окне трекинга посылки'):
            modal_tracking.parcels_list() \
                .click_arrow() \
                .check_parcel_card_expanded() \
                .check_about_order_block_point_delivery() \
                .check_delivery_point_block()

    @testit.workItemIds(33939)
    @testit.externalId('TestPrivateClients_33939')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Переход на страницу выбора подарка из банера в карточке посылки со страницы "Отследить '
                        'посылку"')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Переход на страницу выбора подарка из банера в карточке посылки со страницы '
                  '"Отследить посылку"')
    @allure.testcase(url='https://testit..ru/browse/33939')
    def test_go_to_gift_page_from_banner_inside_parcel_card_on_tracking_page(self,
                                                                             site_private_clients_delivery_tracking):
        tracking_page = site_private_clients_delivery_tracking
        expect_url = 'https://get4click.ru/'

        with allure.step('Открыть карточку найденной посылки'):
            parcel_card = tracking_page.form_tracking() \
                .track_parcel('12345') \
                .click_arrow() \
                .check_parcel_card_expanded() \

        with allure.step('В банере "Выберите подарок от нашего партнера" нажать на "Выбрать подарок"'):
            actual_url = parcel_card.check_gift_banner() \
                .go_to_gift_page()
            assert expect_url in actual_url, f'Ожидался {expect_url}, получен {actual_url}'

    @testit.workItemIds(34488)
    @testit.externalId('TestPrivateClients_34488')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Отображение 0 к оплате для посылок с плательщиком-отправителем при поиске через ПС')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отследить посылку - Отображение 0 к оплате для посылок с плательщиком-отправителем '
                  'при поиске через ПС')
    @allure.testcase(url='https://testit..ru/browse/34488')
    def test_parcel_tracking_payer_sender_parcel(self, site_private_clients_delivery_tracking,
                                                 auth_service_predprod_api, aggregator_service_predprod_api,
                                                 date_helper):
        tracking_id = '0000999992751'
        sender_name = 'Доставка писем и посылок'
        TrackingHelper.insert_shop(name=sender_name, code='0000000018')
        with allure.step(f'Запросить данные о посылке {tracking_id} в ПС'):
            auth_service_predprod_api.add_token('token-get-parcels', 'parcels')
            auth_service_predprod_api.get_access_token(auth_service_predprod_api.lastToken)
            response = aggregator_service_predprod_api.find_parcels_with_statuses(
                {'searchParameters.numberParcels': tracking_id},
                client=auth_service_predprod_api.lastToken
            )
            assert response.status_code == 200, f"Ожидался код ответа: 200, получен: {response.status_code}"
            ml_data = response.json()['parcels'][0]
            order_number = ml_data['orderNumber']
            track_number = ml_data['trackNumber']
            delivery_date = date_helper.format_date(date=ml_data['deliveryDate'], current_format='%Y-%m-%d',
                                                          required_format='%d.%m.%Y')
            issue_condition = 'Код из смс'
            point_address = ml_data['deliveryAddress']
            to_pay = ml_data['amountPay']
            assert to_pay > 0, f'amountPay, ожидалось больше 0, получен: {to_pay}'

        tracking_page = site_private_clients_delivery_tracking
        form_tracking = tracking_page.form_tracking()
        form_tracking.track_parcel(tracking_id) \
            .check_parcel_card_expanded() \
            .check_about_order_block_point_delivery()

        with allure.step('Проверить данные посылки'):
            data = form_tracking.get_data()['Посылки'][0]
            assert len(data) == 8, \
                f"Количество строк данных, ожидалось: 8, получено: {len(data)}"
            assert data['Отправитель'] == sender_name, \
                f"Отправитель, ожидался: {sender_name}, получен: {data['Отправитель']}"
            assert data['Номер ИМ'] == order_number, \
                f"Номер ИМ, ожидался: {order_number}, получен: {data['Номер ИМ']}"
            assert data['Номер заказа'] == track_number, \
                f"Номер заказа, ожидался: {track_number}, получен: {data['Номер заказа']}"
            assert data['Плановая дата доставки'] == delivery_date, \
                f"Плановая дата доставки, ожидалось: {delivery_date}, получен: {data['Плановая дата доставки']}"
            assert data['Для получения'] == issue_condition, \
                f"Для получения, ожидалось: {issue_condition}, получен: {data['Для получения']}"
            assert data['К оплате'] == '0.00', \
                f"К оплате, ожидалось: 0.00, получен: {data['К оплате']}"
            assert 'Способы оплаты' not in data, \
                f"Способы оплаты, ожидалось отсутствие, получен: {data['Способы оплаты']}"
            assert data['Пункт выдачи'] == point_address, \
                f"Пункт выдачи, ожидалось: {point_address}, получен: {data['Пункт выдачи']}"

    @testit.workItemIds(37430)
    @testit.externalId('TestPrivateClients_37430')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Отследить посылку')
    @testit.displayName('Отображение отслеживания посылки АВИТО')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Отследить посылку')
    @allure.title('Отображение отслеживания посылки АВИТО')
    @allure.testcase(url='https://testit..ru/browse/37430')
    @pytest.mark.parametrize(('tracking_id', 'issue_condition'), [('0000123429107', 'код авито'),
                                                              ('S-P000152536360', 'код авито'),
                                                              ('S-P000152802503', 'Паспорт или доверенность')])
    def test_parcel_tracking_avito_issue_condition_text(self, site_private_clients_delivery_tracking,
                                                        tracking_id, issue_condition):
        tracking_page = site_private_clients_delivery_tracking
        form_tracking = tracking_page.form_tracking()
        form_tracking.track_parcel(tracking_id) \
            .check_parcel_card_expanded() \
            .check_about_order_block_point_delivery()

        with allure.step('Проверить данные посылки'):
            data = form_tracking.get_data()['Посылки'][0]
            assert data['Для получения'] == issue_condition, \
                f"Для получения, ожидалось: {issue_condition}, получен: {data['Для получения']}"
