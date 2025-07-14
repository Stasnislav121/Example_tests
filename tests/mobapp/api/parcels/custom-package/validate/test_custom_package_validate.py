import allure
import testit
import pytest

from library.mobapp import *


class TestParcelsCustomPackageValidate:
    @testit.workItemIds(40404)
    @testit.externalId('TestParcelsCustomPackage_40404')
    @testit.displayName('[201] POST /parcels/custom-package/validate - валидация полей своей упаковки')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/custom-package/validate - валидация полей своей упаковки')
    @allure.testcase(url='https://testit..ru/browse/40404')
    @pytest.mark.parametrize('package_size', [{'width': 1, 'length': 1, 'height': 1},
                                              {'width': 120, 'length': 80, 'height': 50}])
    def test_custom_package_validate_size_boundary_values(self, package_size):
        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=package_size, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_success_schema)
