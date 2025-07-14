import allure
import testit
import pytest
from library.mobapp import *


class TestSmsCodeVerify:
    @testit.workItemIds(39312)
    @testit.externalId('TestSmsCodeVerify_39312')
    @testit.displayName('[422] POST /sms/code/verify - попытка верификации смс без создания события для верификации')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/verify - попытка верификации смс без создания события для верификации')
    @allure.testcase(url='https://testit..ru/browse/39312')
    def test_sms_code_verify_without_actual_reason(self, string_helper):
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'code': '9999'
        }
        expect_description = 'Неверный код'

        with allure.step('Выполнить POST /sms/code/verify'):
            client = SmsApi()
            response = client.request_sms_code_verify(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_verify_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_description = actual_data['description']

            assert expect_description == actual_description, (
                f'Ожидалось "errors.description": {expect_description},получено {actual_description}')

    @testit.workItemIds(39313)
    @testit.externalId('TestSmsCodeVerify_39313')
    @testit.displayName('[422] POST /sms/code/verify - неверный код для верификации смс')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/verify - неверный код для верификации смс')
    @allure.testcase(url='https://testit..ru/browse/39313')
    def test_sms_code_verify_invalid_verification_code(self, request_sms):
        data = {
            'phone': request_sms['phone'],
            'code': '1234'
        }
        expect_description = 'Неверный код'

        with allure.step('Выполнить POST /sms/code/verify'):
            client = SmsApi()
            response = client.request_sms_code_verify(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_verify_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_description = actual_data['description']

            assert expect_description == actual_description, (
                f'Ожидалось "errors.description": {expect_description},получено {actual_description}')

    @testit.workItemIds(39314)
    @testit.externalId('TestSmsCodeVerify_39314')
    @testit.displayName('[422] POST /sms/code/verify - получение ошибки при запросе без параметров')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/verify - получение ошибки при запросе без параметров')
    @allure.testcase(url='https://testit..ru/browse/39314')
    @pytest.mark.parametrize('param', ['phone', 'code'])
    def test_sms_code_verify_without_params(self, string_helper, param):
        expect_description = 'Параметр отсутствует или не заполнен'
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'code': '1234'
        }
        del data[param]

        with allure.step('Выполнить POST /sms/code/verify'):
            client = SmsApi()
            response = client.request_sms_code_verify(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_verify_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert param == actual_field, f'Ожидалось "field": "{param}", получен "{actual_field}"'
            assert expect_description == actual_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')

    @testit.workItemIds(39315)
    @testit.externalId('TestSmsCodeVerify_39315')
    @testit.displayName('[422] POST /sms/code/verify - получение ошибки при запросе с пустыми параметрами')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/verify - получение ошибки при запросе с пустыми параметрами')
    @allure.testcase(url='https://testit..ru/browse/39315')
    @pytest.mark.parametrize('param', ['phone', 'code'])
    def test_sms_code_verify_empty_params(self, param, string_helper):
        expect_description = 'Параметр отсутствует или не заполнен'
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'code': '1234'
        }
        data[param] = ''

        with allure.step('Выполнить POST /sms/code/verify'):
            client = SmsApi()
            response = client.request_sms_code_verify(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_verify_err_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert param == actual_field, f'Ожидалось "field": "{param}", получен "{actual_field}"'
            assert expect_description == actual_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')
