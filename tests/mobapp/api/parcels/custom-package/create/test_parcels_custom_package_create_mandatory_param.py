import copy

import allure
import testit

from library.mobapp import *


class TestParcelsCustomPackage:
    @testit.workItemIds(25343)
    @testit.externalId('TestParcelsCustomPackage_25343')
    @testit.displayName('[201] POST /parcels/custom-package/create - cоздание шаблона посылки (только обязательные '
                        'параметры)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/custom-package/create - cоздание шаблона посылки '
                  '(только обязательные параметры)')
    @allure.testcase(url='https://testit..ru/browse/25343')
    def test_parcels_custom_package_create_min_params(self, with_auth, request):
        data = copy.deepcopy(custom_package_request_min_params_json)
        client = ParcelsApi()

        with allure.step('Выполнить POST /parcels/custom-package/create'):
            response = client.create_custom_package(json=data, token=with_auth)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, custom_package_create_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_box_id = actual_data['boxId']
            request.addfinalizer(lambda: client.delete_custom_package(id_package=actual_box_id, token=with_auth))
            actual_description = actual_data['description']
            actual_image_id = actual_data['imageId']
            actual_image_link = actual_data['imageLink']

        assert actual_box_id > 0, f'Ожидался "boxId" > 0, получен {actual_box_id}'
        assert data.items() <= actual_data.items(), f'Ожидалось равенство параметров с {data}, получено {actual_data}'
        assert actual_description is None, f'Ожидался "description": null, получено {actual_description}'
        assert actual_image_id is None, f'Ожидался "imageId": null, получено {actual_image_id}'
        assert actual_image_link is None, f'Ожидался "imageLink": null, получено {actual_image_link}'

    @testit.workItemIds(25344)
    @testit.externalId('TestParcelsCustomPackage_25344')
    @testit.displayName('[201] POST /parcels/custom-package/create - создание шаблона посылки (все параметры)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/custom-package/create - создание шаблона посылки (все параметры)')
    @allure.testcase(url='https://testit..ru/browse/25344')
    def test_parcels_custom_package_create_max_params(self, with_auth, request, upload_package_image):
        expect_image_link = 'https://storage.img.net/mobile-app-common/custom_packages/'
        data = copy.deepcopy(custom_package_request_max_params_json)
        except_image_id = upload_package_image
        data['imageId'] = except_image_id
        client = ParcelsApi()

        with allure.step('Выполнить POST /parcels/custom-package/create'):
            response = client.create_custom_package(json=data, token=with_auth)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, custom_package_create_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_box_id = actual_data['boxId']
            actual_image_id = actual_data['imageId']
            request.addfinalizer(lambda: client.delete_custom_package(id_package=actual_box_id, token=with_auth))
            request.addfinalizer(lambda: ParcelsHelper().delete_package_image_from_db(image_id=except_image_id))
            actual_image_link = actual_data['imageLink']

        assert actual_box_id > 0, f'Ожидался "boxId" > 0, получен {actual_box_id}'
        assert data.items() <= actual_data.items(), f'Ожидалось равенство параметров с {data}, получено {actual_data}'
        assert except_image_id == actual_image_id, f'Ожидался "imageId":{except_image_id}, получен {actual_image_id}'
        assert expect_image_link in actual_image_link, \
            f'{expect_image_link} не содержится в "imageLink": {actual_image_link}'
