import pytest
import allure
import testit
import copy

from library.mobapp import *


class TestParcelsDelivery:
    @testit.workItemIds(35158)
    @testit.externalId('TestParcelsDelivery_35158')
    @testit.displayName('[201] POST /parcels/delivery - граничные значения "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - граничные значения "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35158')
    @pytest.mark.parametrize('custom_package_size', [{"width": 1, "length": 1, "height": 1},
                                                     {"width": 120, "length": 80, "height": 50}])
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_with_custom_package_size_boundary_values(self, custom_package_size, api_version):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage'] = custom_package_size
            client = ParcelsApi(version=api_version)
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_two_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']

            assert first_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"

            assert second_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"

    @testit.workItemIds(35161)
    @testit.externalId('TestParcelsDelivery_35161')
    @testit.displayName('[201] POST /parcels/delivery - виды упаковок ')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/delivery - виды упаковок ')
    @allure.testcase(url='https://testit..ru/browse/35161')
    @pytest.mark.parametrize('package_id', ['793', '794', '795', '796', '797',
                                            '798', '799', '800', '801', '802', '803', '804', '808', '813', '978'])
    def test_parcels_delivery_with_package_bb(self, package_id):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_package_json)
            json_request['package'] = package_id
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_with_two_delivery_type_schema)

        with allure.step('Проверка параметров ответа'):
            delivery_type_resp = response.json()['data']['items']
            first_delivery_id_resp = delivery_type_resp[0]['id']
            first_delivery_price_resp = delivery_type_resp[0]['price']['value']
            second_delivery_id_resp = delivery_type_resp[1]['id']
            second_delivery_price_resp = delivery_type_resp[1]['price']['value']

            assert first_delivery_id_resp == OFFICE_TO_DOOR_ID, \
                f"Ожидалось {OFFICE_TO_DOOR_ID},  получено {first_delivery_id_resp}"
            assert first_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {first_delivery_price_resp}"

            assert second_delivery_id_resp == OFFICE_TO_OFFICE_ID, \
                f"Ожидалось {OFFICE_TO_OFFICE_ID}, получено {second_delivery_id_resp}"
            assert second_delivery_price_resp > 0, \
                f"Ожидалось items.price.value > 0, получено {second_delivery_price_resp}"

    @testit.workItemIds(35174)
    @testit.externalId('TestParcelsDelivery_35174')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при отсутствии параметров габаритов '
                        'в "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при отсутствии параметров габаритов '
                  'в "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35174')
    @pytest.mark.parametrize(('error_field', 'error_text'),
                             [('customPackage.width', 'Ширина упаковки обязательна для заполнения'),
                              ('customPackage.length', 'Длина упаковки обязательна для заполнения'),
                              ('customPackage.height', 'Высота упаковки обязательна для заполнения')])
    def test_parcels_delivery_without_custom_package_dimensions(self, error_field, error_text):
        dimension = error_field.split('.')[1]

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage'].pop(dimension)
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35177)
    @testit.externalId('TestParcelsDelivery_35177')
    @testit.displayName('[403] POST /parcels/delivery - получение ошибки при отсутствии параметра "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[403] POST /parcels/delivery - получение ошибки при отсутствии параметра "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35177')
    def test_parcels_delivery_without_custom_package(self):
        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request.pop('customPackage')
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)

        with allure.step('Проверка параметров ответа'):
            assert response.status_code == 403, f"Ожидалось 403, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_err_schema)

    @testit.workItemIds(35178)
    @testit.externalId('TestParcelsDelivery_35178')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при несуществующем "package"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при несуществующем "package"')
    @allure.testcase(url='https://testit..ru/browse/35178')
    def test_parcels_delivery_not_found_package(self):
        error_field = 'package'
        error_text = 'Упаковка не найдена'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_package_json)
            json_request[error_field] = '1000'
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35181)
    @testit.externalId('TestParcelsDelivery_35181')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений '
                        'параметра "customPackage.width"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений параметра '
                  '"customPackage.width"')
    @allure.testcase(url='https://testit..ru/browse/35181')
    @pytest.mark.parametrize(('custom_package_width', 'error_text'), [(0, 'Ширина упаковки обязательна для заполнения'),
                                                                      (121,
                                                                       'Ширина упаковки не может превышать 120 см')])
    def test_parcels_delivery_exceeding_the_boundary_values_custom_package_width(self, custom_package_width,
                                                                                 error_text):
        error_field = 'customPackage.width'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage']['width'] = custom_package_width
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35182)
    @testit.externalId('TestParcelsDelivery_35182')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений '
                        'параметра "customPackage.length"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений '
                  'параметра "customPackage.length"')
    @allure.testcase(url='https://testit..ru/browse/35182')
    @pytest.mark.parametrize(('custom_package_length', 'error_text'), [(0, 'Длина упаковки обязательна для заполнения'),
                                                                       (121,
                                                                        'Длина упаковки не может превышать 120 см')])
    def test_parcels_delivery_exceeding_the_boundary_values_custom_package_length(self, custom_package_length,
                                                                                  error_text):
        error_field = 'customPackage.length'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage']['length'] = custom_package_length
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35183)
    @testit.externalId('TestParcelsDelivery_35183')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений '
                        'параметра "customPackage.height"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при превышении граничных значений '
                  'параметра "customPackage.height"')
    @allure.testcase(url='https://testit..ru/browse/35183')
    @pytest.mark.parametrize(('custom_package_height', 'error_text'),
                             [(0, 'Высота упаковки обязательна для заполнения'),
                              (121, 'Высота упаковки не может превышать 120 см')])
    def test_parcels_delivery_exceeding_the_boundary_values_custom_package_height(self, custom_package_height,
                                                                                  error_text):
        error_field = 'customPackage.height'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage']['height'] = custom_package_height
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"

    @testit.workItemIds(35184)
    @testit.externalId('TestParcelsDelivery_35184')
    @testit.displayName('[422] POST /parcels/delivery - получение ошибки при нарушении пропорции 120х80х50 в '
                        'параметре "customPackage"')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[422] POST /parcels/delivery - получение ошибки при нарушении пропорции 120х80х50 в '
                  'параметре "customPackage"')
    @allure.testcase(url='https://testit..ru/browse/35184')
    def test_parcels_delivery_violation_of_proportion_dimensions_custom_package(self):
        error_field = 'customPackage.height'
        error_text = 'Высота упаковки не может превышать 50 см'

        with allure.step('Выполнить POST /parcels/delivery'):
            json_request = copy.deepcopy(parcel_delivery_with_custom_package_json)
            json_request['customPackage'] = {"width": 120, "length": 65, "height": 65}
            client = ParcelsApi()
            response = client.get_delivery(json_request, token=None, check_error=False)
            assert response.status_code == 422, f"Ожидалось 422, получено {response.status_code}"

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, parcel_delivery_err_schema)

        with allure.step('Проверка параметров ответа'):
            error_field_resp = response.json()['data']['errors'][0]['field']
            error_text_resp = response.json()['data']['errors'][0]['description']
            error_status_resp = response.json()['success']
            assert error_field_resp == error_field, f"Ожидалось {error_field}, получено {error_field_resp}"
            assert error_text_resp == error_text, f"Ожидалось {error_text}, получено {error_text_resp}"
            assert error_status_resp is False, f"Ожидалось False, получено {error_status_resp}"
