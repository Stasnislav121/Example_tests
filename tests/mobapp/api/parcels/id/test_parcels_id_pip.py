import allure
import testit

from library.mobapp import *


class TestParcelsIdPip:
    @testit.workItemIds(17699)
    @testit.externalId('TestParcelsIdPip_17699')
    @testit.displayName('[200] GET /parcels/_parcelId_ - '
                        'получение детальной информации об отправлении неавторизованным пользователем (ПИП)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ - '
                  'получение детальной информации об отправлении неавторизованным пользователем (ПИП)')
    @allure.testcase(url='https://testit..ru/browse/17699')
    def test_get_data_parcel_pip_without_auth(self):
        expect_parcel_id = '0000200089446'
        expect_title = 'Отправление для Артём'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_pip_not_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_title = actual_data['title']
            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_title == actual_title, (
                f'Ожидался "title": {expect_title}, получен {actual_title}')

    @testit.workItemIds(41165)
    @testit.externalId('TestParcelsIdPip_41165')
    @testit.displayName('[200] GET /parcels/_parcelId_ - получение детальной информации об отправлении авторизованным '
                        'пользователем - не владельцем посылки (ПИП)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ - получение детальной информации об отправлении авторизованным '
                  'пользователем - не владельцем посылки (ПИП)')
    @allure.testcase(url='https://testit..ru/browse/41165')
    def test_get_data_else_parcel_pip_with_auth(self, with_auth):
        expect_parcel_id = '0000200089446'
        expect_title = 'Отправление для Артём'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(token=with_auth, parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_pip_not_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_title = actual_data['title']
            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_title == actual_title, (
                f'Ожидался "title": {expect_title}, получен {actual_title}')

    @testit.workItemIds(41163)
    @testit.externalId('TestParcelsIdPip_41163')
    @testit.displayName('[200] GET /parcels/_parcelId_ -  получение детальной информации об отправлении авторизованным'
                        ' владельцем посылки (ПИП)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/_parcelId_ -  получение детальной информации об отправлении авторизованным '
                  'владельцем посылки (ПИП)')
    @allure.testcase(url='https://testit..ru/browse/41163')
    def test_get_data_own_parcel_pip(self, with_auth, create_parcel_with_autotest_user_sender):
        expect_parcel_id = create_parcel_with_autotest_user_sender
        expect_title = 'Отправление для MOBILE AUTOTEST Получатель'

        client = ParcelsApi()

        with allure.step(f'Выполнить GET /parcels/{expect_parcel_id}'):
            response = client.get_parcel(token=with_auth, parcel_id=expect_parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcels_id_pip_owner_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']

            actual_parcel_id = actual_data['id']
            actual_title = actual_data['title']
            assert expect_parcel_id == actual_parcel_id, (
                f'Ожидался "id": {expect_parcel_id}, получен {actual_parcel_id}')
            assert expect_title == actual_title, (
                f'Ожидался "title": {expect_title}, получен {actual_title}')
