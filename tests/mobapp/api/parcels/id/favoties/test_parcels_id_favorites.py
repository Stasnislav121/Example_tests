import allure
import testit

from library.mobapp import *


class TestParcelsIdFavorites:
    @testit.workItemIds(38993)
    @testit.externalId('TestParcelsIdFavorites_38993')
    @testit.displayName('[200] PUT /parcels/_parcelId_/favorites - Добавление посылки в избранное')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] PUT /parcels/_parcelId_/favorites - Добавление посылки в избранное')
    @allure.testcase(url='https://testit..ru/browse/38993')
    def test_add_parcel_in_favorites_success(self, with_auth, request):
        expect_parcel_number = '0000102573944'
        expect_user_id = 28488724

        client = ParcelsApi()
        request.addfinalizer(lambda: client.delete_parcel_favorite(parcel=expect_parcel_number))

        with allure.step(f'Выполнить PUT /parcels/{expect_parcel_number}/favorites'):
            response = client.add_parcel_favorite(parcel=expect_parcel_number, token=with_auth)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_id_favorites_schema)

        with allure.step(f'Проверка запиcи по {expect_parcel_number} в таблице "users_parcels"'):
            favorite_parcel_data = ParcelsHelper.get_favorite_parcel(parcel=expect_parcel_number)[0]
            actual_user_id = favorite_parcel_data['user_id']
            actual_parcel_number = favorite_parcel_data['track_num']
            assert expect_user_id == actual_user_id, f'Ожидался "user_id" == {expect_user_id}, получен {actual_user_id}'
            assert expect_parcel_number == actual_parcel_number, (f'Ожидался "track_num" == {expect_parcel_number},'
                                                                  f' получен {actual_parcel_number}')

    @testit.workItemIds(38994)
    @testit.externalId('TestParcelsIdFavorites_38994')
    @testit.displayName('[403] PUT /parcels/_parcelId_/favorites - Добавление несуществующей посылки в избранное')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[403] PUT /parcels/_parcelId_/favorites - Добавление несуществующей посылки в избранное')
    @allure.testcase(url='https://testit..ru/browse/38994')
    def test_add_nonexistent_parcel_in_favorites(self, with_auth):
        expect_parcel_number = '999999999999'
        expect_error_text = 'Данную посылку нельзя добавить в избранное'

        client = ParcelsApi()

        with allure.step(f'Выполнить PUT /parcels/{expect_parcel_number}/favorites'):
            response = client.add_parcel_favorite(parcel=expect_parcel_number, token=with_auth, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_403(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_id_favorites_schema)

        with allure.step(f'Проверка запиcи по {expect_parcel_number} в таблице "users_parcels"'):
            favorite_parcel_data = ParcelsHelper.get_favorite_parcel(parcel=expect_parcel_number)
            actual_error_text = response.json()['message']

            assert len(favorite_parcel_data) == 0, f'Ожидался пустой список,получен {favorite_parcel_data}'
            assert expect_error_text == actual_error_text, (f'Ожидался текст ошибки {expect_error_text}, '
                                                            f'получен {actual_error_text}')

    @testit.workItemIds(38995)
    @testit.externalId('TestParcelsIdFavorites_38995')
    @testit.displayName('[401] PUT /parcels/_parcelId_/favorites - Добавление посылки в избранное неавторизованным '
                        'пользователем')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[401] PUT /parcels/_parcelId_/favorites - Добавление посылки в избранное неавторизованным '
                  'пользователем')
    @allure.testcase(url='https://testit..ru/browse/38995')
    def test_add_parcel_in_favorites_without_auth(self, without_auth):
        expect_parcel_number = '0000102573944'
        expect_error_text = 'Попробуйте обновить страницу'

        client = ParcelsApi()

        with allure.step(f'Выполнить PUT /parcels/{expect_parcel_number}/favorites'):
            response = client.add_parcel_favorite(parcel=expect_parcel_number, token=without_auth, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_401(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_id_favorites_schema)

        with allure.step(f'Проверка запиcи по {expect_parcel_number} в таблице "users_parcels"'):
            favorite_parcel_data = ParcelsHelper.get_favorite_parcel(parcel=expect_parcel_number)
            actual_error_text = response.json()['message']

            assert len(favorite_parcel_data) == 0, f'Ожидался пустой список,получен {favorite_parcel_data}'
            assert expect_error_text == actual_error_text, (f'Ожидался текст ошибки {expect_error_text}, '
                                                            f'получен {actual_error_text}')

    @testit.workItemIds(39005)
    @testit.externalId('TestParcelsIdFavorites_39005')
    @testit.displayName('[200] DELETE /parcels/_parcelId_/favorites - Удаление посылки из избранного')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] DELETE /parcels/_parcelId_/favorites - Удаление посылки из избранного')
    @allure.testcase(url='https://testit..ru/browse/39005')
    def test_delete_parcel_in_favorites_success(self, with_auth):
        expect_parcel_number = '0000102576189'

        client = ParcelsApi()

        with allure.step(f'Выполнить PUT /parcels/{expect_parcel_number}/favorites'):
            client.add_parcel_favorite(parcel=expect_parcel_number, token=with_auth)
            favorite_parcel_data_before = ParcelsHelper.get_favorite_parcel(parcel=expect_parcel_number)[0]['track_num']
            assert expect_parcel_number == favorite_parcel_data_before, (
                f'Ожидался "track_num" == {expect_parcel_number},получен {favorite_parcel_data_before}')

        with allure.step(f'Выполнить DELETE /parcels/{expect_parcel_number}/favorites'):
            response = client.delete_parcel_favorite(parcel=expect_parcel_number, token=with_auth)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_id_favorites_schema)

        with allure.step(f'Проверка запиcи по {expect_parcel_number} в таблице "users_parcels"'):
            favorite_parcel_data_after = ParcelsHelper.get_favorite_parcel(parcel=expect_parcel_number)

            assert len(favorite_parcel_data_after) == 0, f'Ожидался пустой список,получен {favorite_parcel_data_after}'
