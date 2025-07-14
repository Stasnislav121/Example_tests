import allure
import testit

from library.mobapp import *


class TestParcelsDuplicate:
    @testit.workItemIds(41515)
    @testit.externalId('TestParcelsDuplicate_41515')
    @testit.displayName('[200] GET /parcels/duplicate - '
                        'получение данных для создания дубликата отправления c кастомной упаковкой')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/duplicate - '
                  'получение данных для создания дубликата отправления c кастомной упаковкой')
    @allure.testcase(url='https://testit..ru/browse/41515')
    @pytest.mark.parametrize('platform, package_id', (('android', 'null'), ('ios', None)))
    def test_duplicate_parcel_with_custom_package(self, with_auth, request, platform, package_id):
        json_request = ParcelCreateJsonConstructor().parcel_office_to_office_custom_package_json()
        expect_parcel_package = {
            'id': package_id,
            'title': '',
            'image': '',
            '': False,
            'length': json_request['parcelInfo']['customPackage']['length'],
            'width': json_request['parcelInfo']['customPackage']['width'],
            'height': json_request['parcelInfo']['customPackage']['height'],
            'parcelExample': '',
            'isCustom': True
      }

        client = ParcelsApi()
        parcel_id = client.create(json_request).json()['data']['id']
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=parcel_id, token=with_auth))

        with allure.step('Выполнить GET /parcels/duplicate'):
            response = client.get_duplicate_parcel(token=with_auth, platform=platform, parcel_id=parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_duplicate_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_data_package = actual_data['parcelInfo']['package']

            assert expect_parcel_package == actual_data_package, (
                f'Ожидался "package": {expect_parcel_package}, получен {actual_data_package}')

    @testit.workItemIds(41516)
    @testit.externalId('TestParcelsDuplicate_41516')
    @testit.displayName('[200] GET /parcels/duplicate - '
                        'получение данных для создания дубликата отправления c упаковкой ББ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[200] GET /parcels/duplicate - получение данных для создания дубликата отправления c упаковкой ББ')
    @allure.testcase(url='https://testit..ru/browse/41516')
    def test_duplicate_parcel_with_package_bb(self, with_auth, request):
        json_request = ParcelCreateJsonConstructor().parcel_office_to_office_custom_package_json(package_type='799')
        expect_parcel_package = {
                'id': '799',
                'title': 'Короб ХS',
                'image': "https://storage.img.net/mobile-app-images/packs/799.png",
                '': True,
                'length': 15,
                'width': 15,
                'height': 15,
                'parcelExample': "мобильный телефон, украшения, духи",
                'isCustom': False
            }

        client = ParcelsApi()
        parcel_id = client.create(json_request).json()['data']['id']
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=parcel_id, token=with_auth))

        with allure.step('Выполнить GET /parcels/duplicate'):
            response = client.get_duplicate_parcel(token=with_auth, parcel_id=parcel_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_duplicate_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_data_package = actual_data['parcelInfo']['package']

            assert expect_parcel_package == actual_data_package, (
                f'Ожидался "package": {expect_parcel_package}, получен {actual_data_package}')
