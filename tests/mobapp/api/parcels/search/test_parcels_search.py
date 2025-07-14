import allure
import testit
from library.mobapp import *


class TestParcelsSearch:
    @testit.workItemIds(41457)
    @testit.externalId('TestParcelsSearch_41457')
    @testit.displayName('[200] GET /parcels/search?type=parcel&status=active - получение активных отправлений')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/search?type=parcel&status=active - получение активных отправлений')
    @allure.testcase(url='https://testit..ru/browse/41457')
    def test_parcels_search_active_parcel(self, request, with_auth, create_parcel_with_autotest_user_sender):
        expect_parcel_id = create_parcel_with_autotest_user_sender
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=expect_parcel_id, token=with_auth,
                                                                 check_delete=False))
        expect_title = 'Отправление для MOBILE AUTOTEST Получатель'
        expect_barcode_link = f'.ru/api/v1/parcels/get-barcode/{expect_parcel_id}?print=true'

        with allure.step('Выполнить GET parcels/search?type=parcel&status=active'):
            client = ParcelsApi()
            response = client.search_parcel(token=with_auth, type='parcel', status='active', limit=50)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_search_success_schema)

        with allure.step('Проверка параметров ответа'):
            parcels_resp = response.json()['data']['items']
            parcel_resp = [parsel for parsel in parcels_resp if parsel['id'] == expect_parcel_id][0]

            actual_parcel_id = parcel_resp['id']
            actual_type = parcel_resp['type']
            actual_title = parcel_resp['title']
            actual_track_number = parcel_resp['trackNumber']
            actual_barcode_link = parcel_resp['barcodeLink']
            actual_is_owner = parcel_resp['isOwner']

            assert actual_parcel_id == expect_parcel_id, (f"Ожидалось id: {expect_parcel_id}, "
                                                          f"получено {actual_parcel_id}")
            assert actual_type == 'parcel', f"Ожидалось type: 'parcel', получено {actual_type}"
            assert actual_title == expect_title, f"Ожидалось title: {expect_title}, получено {actual_title}"
            assert actual_track_number == expect_parcel_id, (f"Ожидалось trackNumber: {actual_track_number}, "
                                                             f"получено {actual_parcel_id}")
            assert actual_is_owner is True, f"Ожидалось isOwner: true, получено {actual_is_owner}"
            assert expect_barcode_link in actual_barcode_link, (f"Ожидалось вхождение '{expect_barcode_link}', "
                                                                f"получено {actual_barcode_link}")

    @testit.workItemIds(41458)
    @testit.externalId('TestParcelsSearch_41458')
    @testit.displayName('[200] GET /parcels/search?type=receipt&status=active - получение активных получений')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/search?type=receipt&status=active - получение активных получений')
    @allure.testcase(url='https://testit..ru/browse/41458')
    def test_parcels_search_active_receipt(self, request, with_auth, create_parcel_for_autotest_user_receipt):
        expect_parcel_id = create_parcel_for_autotest_user_receipt
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=expect_parcel_id, token=with_auth,
                                                                 check_delete=False))
        expect_title = f'Отправление от {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["name"]}'
        expect_barcode_link = f'.ru/api/v1/parcels/get-barcode/{expect_parcel_id}?print=true'

        with allure.step('Выполнить GET parcels/search?type=receipt&status=active'):
            client = ParcelsApi()
            response = client.search_parcel(token=with_auth, type='receipt', status='active', limit=50)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_search_success_schema)

        with allure.step('Проверка параметров ответа'):
            parcels_resp = response.json()['data']['items']
            parcel_resp = [parsel for parsel in parcels_resp if parsel['id'] == expect_parcel_id][0]

            actual_parcel_id = parcel_resp['id']
            actual_type = parcel_resp['type']
            actual_title = parcel_resp['title']
            actual_track_number = parcel_resp['trackNumber']
            actual_barcode_link = parcel_resp['barcodeLink']
            actual_is_owner = parcel_resp['isOwner']

            assert actual_parcel_id == expect_parcel_id, (f"Ожидалось id: {expect_parcel_id}, "
                                                          f"получено {actual_parcel_id}")
            assert actual_type == 'receipt', f"Ожидалось type: 'receipt', получено {actual_type}"
            assert actual_title == expect_title, f"Ожидалось title: {expect_title}, получено {actual_title}"
            assert actual_track_number == expect_parcel_id, (f"Ожидалось trackNumber: {actual_track_number}, "
                                                             f"получено {actual_parcel_id}")
            assert actual_is_owner is True, f"Ожидалось isOwner: true, получено {actual_is_owner}"
            assert expect_barcode_link in actual_barcode_link, (f"Ожидалось вхождение '{expect_barcode_link}', "
                                                                f"получено {actual_barcode_link}")

    @testit.workItemIds(41459)
    @testit.externalId('TestParcelsSearch_41459')
    @testit.displayName('[200] GET /parcels/search?type=all&status=active - получение всех активных посылок')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/search?type=all&status=active - получение всех активных посылок')
    @allure.testcase(url='https://testit..ru/browse/41459')
    def test_parcels_search_all_active_parcels(self, request, with_auth, create_parcel_with_autotest_user_sender,
                                               create_parcel_for_autotest_user_receipt):
        expect_sender_parcel_id = create_parcel_with_autotest_user_sender
        expect_receipt_parcel_id = create_parcel_for_autotest_user_receipt
        expect_parcels = [expect_sender_parcel_id, expect_receipt_parcel_id]
        request.addfinalizer(
            lambda: [ParcelsHelper.delete_parcel(parcel_id=[p for p in expect_parcels],
                                                 token=with_auth, check_delete=False)])

        with allure.step('Выполнить GET parcels/search?type=all&status=active'):
            client = ParcelsApi()
            response = client.search_parcel(token=with_auth, type='all', status='active', limit=50)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_search_success_schema)

        with allure.step('Проверка параметров ответа'):
            parcels_resp = response.json()['data']['items']
            parcels_resp = [parsel for parsel in parcels_resp if parsel['id'] in expect_parcels]
            assert len(parcels_resp) == 2, f'Ожидалось количество посылок = 2, получено {len(parcels_resp)}'

            actual_sender_parcel_id = parcels_resp[1]['id']
            actual_receipt_parcel_id = parcels_resp[0]['id']

            assert actual_sender_parcel_id == expect_sender_parcel_id, (f"Ожидалось id: {expect_sender_parcel_id}, "
                                                                        f"получено {actual_sender_parcel_id}")
            assert actual_receipt_parcel_id == expect_receipt_parcel_id, (f"Ожидалось id: {expect_receipt_parcel_id}, "
                                                                          f"получено {actual_receipt_parcel_id}")

    @testit.workItemIds(41461)
    @testit.externalId('TestParcelsSearch_41461')
    @testit.displayName('[200] GET /parcels/search?type=parcel&status=active&isFavorite=true - '
                        'получение избранных отправлений')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/search?type=parcel&status=active&isFavorite=true - '
                  'получение избранных отправлений')
    @allure.testcase(url='https://testit..ru/browse/41461')
    def test_parcels_search_favorite_parcel(self, request, with_auth):
        expect_parcel_id = '0000200007265'
        expect_title = f'Отправление от {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["name"]}'
        request.addfinalizer(lambda: client.delete_parcel_favorite(parcel=expect_parcel_id))

        with allure.step(f'Выполнить PUT /parcels/{expect_parcel_id}/favorites'):
            client = ParcelsApi()
            client.add_parcel_favorite(parcel=expect_parcel_id, token=with_auth)

        with allure.step('Выполнить GET parcels/search?type=parcel&status=active&isFavorite=true'):
            response = client.search_parcel(token=with_auth, type='parcel', status='active', favorite='true', limit=1)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_search_favorite_schema)

        with allure.step('Проверка параметров ответа'):
            parcels_resp = response.json()['data']['items'][0]
            actual_parcel_id = parcels_resp['id']
            actual_type = parcels_resp['type']
            actual_title = parcels_resp['title']
            actual_track_number = parcels_resp['trackNumber']
            actual_is_favorite = parcels_resp['isFavorite']

            assert actual_parcel_id == expect_parcel_id, (f"Ожидалось id: {expect_parcel_id}, "
                                                          f"получено {actual_parcel_id}")
            assert actual_type is None, f"Ожидалось type: null, получено {actual_type}"
            assert actual_title == expect_title, f"Ожидалось title: {expect_title}, получено {actual_title}"
            assert actual_track_number == expect_parcel_id, (f"Ожидалось trackNumber: {actual_track_number}, "
                                                             f"получено {actual_parcel_id}")
            assert actual_is_favorite is True, f"Ожидалось isFavorite: true, получено {actual_is_favorite}"

    @testit.workItemIds(41456)
    @testit.externalId('TestParcelsSearch_41456')
    @testit.displayName('[200] GET /parcels/search?status=closed - получение завершенных посылок')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/search?status=closed - получение завершенных посылок')
    @allure.testcase(url='https://testit..ru/browse/41456')
    def test_parcels_search_closed_parcel(self, with_auth):
        expect_parcel_id = '0000200007266'
        expect_title = f'Отправление от {AUTOTEST_USER_LONG_EXPIRATION_TOKEN["name"]}'

        with allure.step('Выполнить GET parcels/search?status=closed'):
            client = ParcelsApi()
            response = client.search_parcel(token=with_auth, type='parcel', status='closed', limit=1)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_search_success_schema)

        with allure.step('Проверка параметров ответа'):
            parcels_resp = response.json()['data']['items'][0]
            actual_parcel_id = parcels_resp['id']
            actual_type = parcels_resp['type']
            actual_title = parcels_resp['title']
            actual_track_number = parcels_resp['trackNumber']
            actual_barcode_link = parcels_resp['barcodeLink']
            actual_is_owner = parcels_resp['isOwner']

            assert actual_parcel_id == expect_parcel_id, (f"Ожидалось id: {expect_parcel_id}, "
                                                          f"получено {actual_parcel_id}")
            assert actual_type == 'parcel', f"Ожидалось type: 'parcel', получено {actual_type}"
            assert actual_title == expect_title, f"Ожидалось title: {expect_title}, получено {actual_title}"
            assert actual_track_number == expect_parcel_id, (f"Ожидалось trackNumber: {actual_track_number}, "
                                                             f"получено {actual_parcel_id}")
            assert actual_is_owner is True, f"Ожидалось isOwner: true, получено {actual_is_owner}"
            assert actual_barcode_link is None, f"Ожидалось barcodeLink: null', получено {actual_barcode_link}"
