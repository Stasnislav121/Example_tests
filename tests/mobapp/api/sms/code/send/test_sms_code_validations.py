import allure
import testit
from library.mobapp import *
import pytest


class TestSmsCodeSend:
    @testit.workItemIds(39292)
    @testit.externalId('TestSmsCodeSend_39292')
    @testit.displayName('[422] POST /sms/code/send - получение ошибки при запросе без параметров')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/send - получение ошибки при запросе без параметров')
    @allure.testcase(url='https://testit..ru/browse/39292')
    @pytest.mark.parametrize('param', ['phone', 'reason'])
    def test_sms_code_send_without_params(self, string_helper, param):
        expect_description = 'Параметр отсутствует или не заполнен'
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'reason': 'registration'
        }
        del data[param]

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_err_param_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert actual_field == param, f'Ожидалось "field": "{param}", получен "{actual_field}"'
            assert actual_description == expect_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')

    @testit.workItemIds(39326)
    @testit.externalId('TestSmsCodeSend_39326')
    @testit.displayName('[422] POST /sms/code/send - получение ошибки при запросе с пустыми параметрами')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/send - получение ошибки при запросе с пустыми параметрами')
    @allure.testcase(url='https://testit..ru/browse/39326')
    @pytest.mark.parametrize('param', ['phone', 'reason'])
    def test_sms_code_send_empty_params(self, string_helper, param):
        expect_description = 'Параметр отсутствует или не заполнен'
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'reason': 'registration'
        }
        data[param] = ''

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_err_param_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert actual_field == param, f'Ожидалось "field": "{param}", получен "{actual_field}"'
            assert actual_description == expect_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')

    @testit.workItemIds(39297)
    @testit.externalId('TestSmsCodeSend_39297')
    @testit.displayName('[422] POST /sms/code/send - получение ошибки при запросе смс с несуществующей причиной')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/send - получение ошибки при запросе смс с несуществующей причиной')
    @allure.testcase(url='https://testit..ru/browse/39297')
    def test_sms_code_send_with_nonexistent_reason(self, string_helper):
        expect_description = 'Неверное значение параметра'
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'reason': 'qwerty'
        }

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_err_param_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert actual_field == "reason", f'Ожидалось "field": "reason", получен "{actual_field}"'
            assert actual_description == expect_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')

    @testit.workItemIds(39296)
    @testit.externalId('TestSmsCodeSend_39296')
    @testit.displayName('[422] POST /sms/code/send - получение ошибки при запросе смс с телефоном в неверном формате')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/send - получение ошибки при запросе смс с телефоном в неверном формате')
    @allure.testcase(url='https://testit..ru/browse/39296')
    def test_sms_code_send_with_incorrect_phone_format(self):
        expect_description = 'Неверный формат номера телефона'
        data = {
            'phone': '790000000000',
            'reason': 'registration'
        }

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_err_param_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']['errors'][0]
            actual_field = actual_data['field']
            actual_description = actual_data['description']

            assert actual_field == "phone", f'Ожидалось "field": "phone", получен "{actual_field}"'
            assert actual_description == expect_description, (f'Ожидалось "description": "{expect_description}", '
                                                              f'получен "{actual_description}"')
