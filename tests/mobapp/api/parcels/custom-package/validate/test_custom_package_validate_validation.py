import allure
import testit
import pytest

from library.mobapp import *


class TestParcelsCustomPackageValidateValidation:
    @testit.workItemIds(40405)
    @testit.externalId('TestParcelsCustomPackage_40405')
    @testit.displayName('[422] POST /parcels/custom-package/validate - '
                        'получение ошибки при отсутствии параметров габаритов')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/custom-package/validate - получение ошибки при отсутствии параметров габаритов')
    @allure.testcase(url='https://testit..ru/browse/40405')
    @pytest.mark.parametrize('size_param', ['width', 'length', 'height'])
    def test_custom_package_validate_without_size_params(self, size_param):
        json_request = {'width': 120, 'height': 80, 'length': 50}

        error_field = size_param
        expect_description = 'Параметр отсутствует или не заполнен'

        del json_request[size_param]

        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=json_request, token=None, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_unprocessable_entity_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == expect_description, f"Ожидалось {expect_description}, получено {error_text_resp}"

    @testit.workItemIds(40409)
    @testit.externalId('TestParcelsCustomPackage_40409')
    @testit.displayName('[422] POST /parcels/custom-package/validate - '
                        'получение ошибки при превышении граничных значений параметра "width"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/custom-package/validate - '
                  'получение ошибки при превышении граничных значений параметра "width"')
    @allure.testcase(url='https://testit..ru/browse/40409')
    @pytest.mark.parametrize(('width_value', 'error_text'), [(0, 'Параметр отсутствует или не заполнен'),
                                                             (121, 'Ширина упаковки не может превышать 120 см')])
    def test_custom_package_validate_exceeding_the_boundary_values_width(self, width_value, error_text):
        error_field = 'width'
        expect_description = error_text
        json_request = {'width': width_value, 'length': 80, 'height': 50, }

        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=json_request, token=None, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_unprocessable_entity_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == expect_description, f"Ожидалось {expect_description}, получено {error_text_resp}"

    @testit.workItemIds(40410)
    @testit.externalId('TestParcelsCustomPackage_40410')
    @testit.displayName('[422] POST /parcels/custom-package/validate'
                        ' - получение ошибки при превышении граничных значений параметра "length"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/custom-package/validate'
                  ' - получение ошибки при превышении граничных значений параметра "length"')
    @allure.testcase(url='https://testit..ru/browse/40410')
    @pytest.mark.parametrize(('length_value', 'error_text'), [(0, 'Параметр отсутствует или не заполнен'),
                                                              (81, 'Длина упаковки не может превышать 80 см')])
    def test_custom_package_validate_exceeding_the_boundary_values_length(self, length_value, error_text):
        error_field = 'length'
        expect_description = error_text
        json_request = {'width': 120, 'length': length_value, 'height': 50}

        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=json_request, token=None, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_unprocessable_entity_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == expect_description, f"Ожидалось {expect_description}, получено {error_text_resp}"

    @testit.workItemIds(40411)
    @testit.externalId('TestParcelsCustomPackage_40411')
    @testit.displayName('[422] POST /parcels/custom-package/validate'
                        ' - получение ошибки при превышении граничных значений параметра "height"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/custom-package/validate'
                  ' - получение ошибки при превышении граничных значений параметра "height"')
    @allure.testcase(url='https://testit..ru/browse/40411')
    @pytest.mark.parametrize(('height_value', 'error_text'), [(0, 'Параметр отсутствует или не заполнен'),
                                                              (51, 'Высота упаковки не может превышать 50 см')])
    def test_custom_package_validate_exceeding_the_boundary_values_height(self, height_value, error_text):
        error_field = 'height'
        expect_description = error_text
        json_request = {'width': 120, 'length': 80, 'height': height_value}

        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=json_request, token=None, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_unprocessable_entity_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == expect_description, f"Ожидалось {expect_description}, получено {error_text_resp}"

    @testit.workItemIds(40412)
    @testit.externalId('TestParcelsCustomPackage_40412')
    @testit.displayName('[422] POST /parcels/custom-package/validate'
                        ' - получение ошибки при нарушении пропорции 120х80х50')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/custom-package/validate - получение ошибки при нарушении пропорции 120х80х50')
    @allure.testcase(url='https://testit..ru/browse/40412')
    def test_custom_package_validate_violation_of_proportion_dimensions_package(self):
        error_field = 'height'
        expect_description = 'Высота упаковки не может превышать 50 см'
        json_request = {'width': 120, 'length': 65, 'height': 65}

        with allure.step('Выполнить POST /parcels/custom-package/validate'):
            client = ParcelsApi()
            response = client.validate_package(json=json_request, token=None, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response=response)
            ResponseHandler.check_response_has_success_is_false(response=response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_unprocessable_entity_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == expect_description, f"Ожидалось {expect_description}, получено {error_text_resp}"
