import allure
import testit
import pytest

from library.mobapp import *
from library.mobapp.files.files_path import *


class TestParcelsCustomPackage:
    @testit.workItemIds(25659)
    @testit.externalId('TestParcelsCustomPackage_25659')
    @testit.displayName('[201] POST /parcels/custom-package/file - добавление изображения (форматы)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/custom-package/file - добавление изображения (форматы)')
    @allure.testcase(url='https://testit..ru/browse/25659')
    @pytest.mark.parametrize('file_path', [*PACKAGE_IMAGE.values()])
    def test_custom_package_file_add_valid_formats(self, with_auth, file_path, request):
        client = ParcelsApi()
        expect_image_link = 'https://storage.img.net/mobile-app-common/custom_packages/'

        with allure.step('Выполнить POST /parcels/custom-package/file'):
            response = client.upload_custom_package_image(file_path=file_path, token=with_auth)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, custom_package_file_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_image_id = actual_data['imageId']
            request.addfinalizer(lambda: ParcelsHelper().delete_package_image_from_db(image_id=actual_image_id))
            actual_image_link = actual_data['imageLink']

            assert actual_image_id > 0, f'Ожидался "imageId" > 0, получен {actual_image_id}'
            assert expect_image_link in actual_image_link, \
                f'{expect_image_link} не содержится в "imageLink": {actual_image_link}'
