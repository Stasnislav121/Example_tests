import allure
import testit
from library.mobapp import *


class TestParcelsFavoritesSync:
    @testit.workItemIds(41107)
    @testit.externalId('TestParcelsFavoritesSync_41107')
    @testit.displayName('[201] PUT /parcels/favorites/sync - синхронизация локально сохраненных избранных посылок')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] PUT /parcels/favorites/sync - синхронизация локально сохраненных избранных посылок')
    @allure.testcase(url='https://testit..ru/browse/41107')
    def test_parcels_favorites_sync(self, with_auth, request):
        parcels = {
            'parcelIds': [
                '0000268361002',
                'ABD185901381'
            ]
        }

        with allure.step('Выполнить PUT /parcels/favorites/sync'):
            client = ParcelsApi()
            response = client.sync_favorites_parcels(token=with_auth, json=parcels)
            request.addfinalizer(lambda: client.delete_favorite_parcel(token=with_auth, parcels=parcels['parcelIds'],
                                                                       check_error=False))

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_success_schema)

        with allure.step('Выполнить GET /parcels/search?type=parcel&status=active&isFavorite=true'):
            parcels_resp = client.search_parcel(token=with_auth, type='parcel', status='active',
                                                favorite='true').json()['data']['items']

        with allure.step('Проверка параметров ответа'):
            parcels_track_actual = CommonHelper.get_list_for_key_in_obj(list_obj=parcels_resp, key='trackNumber')
            assert parcels_track_actual == parcels['parcelIds'], (f"Ожидалось {parcels['parcelIds']}, "
                                                                  f"получено {parcels_track_actual}")
