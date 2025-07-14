import allure
import testit

from library.mobapp import *


class TestParcelsIdIm:
    @testit.workItemIds(41174)
    @testit.externalId('TestParcelsIdIm_41174')
    @testit.displayName('[200] GET /parcels/_parcelId_ - получение детальной информации об отправлении авторизованным '
                        'владельцем посылки (ИМ)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ - получение детальной информации об отправлении авторизованным'
                  ' владельцем посылки (ИМ)')
    @allure.testcase(url='https://testit..ru/browse/41174')
    def test_get_data_own_parcel_im(self, with_auth):
        expect_parcel_id = '0000661064859'
        expect_track_number = 'BBR201070991'
        expect_store_track_number = 'autotest_mobile_20250317'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(token=with_auth, parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_im_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_track_number = actual_data['trackNumber']
            actual_store_track_number = actual_data['storeTrackNumber']

            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_track_number == actual_track_number, (
                f'Ожидался "trackNumber": {expect_track_number}, получен {actual_track_number}')
            assert expect_store_track_number == actual_store_track_number, (
                f'Ожидался "storeTrackNumber": {expect_store_track_number}, получен {actual_store_track_number}')

    @testit.workItemIds(41172)
    @testit.externalId('TestParcelsIdIm_41172')
    @testit.displayName('[200] GET /parcels/_parcelId_ - '
                        'получение детальной информации об отправлении неавторизованным пользователем (ИМ)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ - '
                  'получение детальной информации об отправлении неавторизованным пользователем (ИМ)')
    @allure.testcase(url='https://testit..ru/browse/41172')
    def test_get_data_parcel_im_without_auth(self):
        expect_parcel_id = 'BBR201070991'
        expect_store_track_number = 'autotest_mobile_20250317'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_im_not_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_track_number = actual_data['trackNumber']
            actual_store_track_number = actual_data['storeTrackNumber']

            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_parcel_id == actual_track_number, (
                f'Ожидался "trackNumber": {expect_parcel_id}, получен {actual_track_number}')
            assert expect_store_track_number == actual_store_track_number, (
                f'Ожидался "storeTrackNumber": {expect_store_track_number}, получен {actual_store_track_number}')

    @testit.workItemIds(41173)
    @testit.externalId('TestParcelsIdIm_41173')
    @testit.displayName('[200] GET /parcels/_parcelId_ - '
                        'получение детальной информации об отправлении авторизованным пользователем - не владельцем '
                        'посылки (ИМ)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ - '
                  'получение детальной информации об отправлении авторизованным пользователем - не владельцем '
                  'посылки (ИМ)')
    @allure.testcase(url='https://testit..ru/browse/41173')
    def test_get_data_else_parcel_im_with_auth(self, with_auth):
        expect_parcel_id = 'ABO201070890'
        expect_store_track_number = '68107801-0038-1'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(token=with_auth, parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_im_not_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_track_number = actual_data['trackNumber']
            actual_store_track_number = actual_data['storeTrackNumber']

            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_parcel_id == actual_track_number, (
                f'Ожидался "trackNumber": {expect_parcel_id}, получен {actual_track_number}')
            assert expect_store_track_number == actual_store_track_number, (
                f'Ожидался "storeTrackNumber": {expect_store_track_number}, получен {actual_store_track_number}')
