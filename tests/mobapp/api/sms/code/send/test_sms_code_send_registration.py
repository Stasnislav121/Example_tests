import allure
import testit
from library.mobapp import *


class TestSmsCodeSend:
    @testit.workItemIds(17691)
    @testit.externalId('TestSmsCodeSend_17691')
    @testit.displayName('[201] POST /sms/code/send - запрос смс для регистрации')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[201] POST /sms/code/send - запрос смс для регистрации')
    @allure.testcase(url='https://testit..ru/browse/17691')
    def test_sms_code_send_request_registration(self, string_helper):
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'reason': 'registration'
        }

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_success_schema)

        with allure.step('Проверка параметров ответа'):
            timer = response.json()['data']['timer']
            assert timer == 120, f'Ожидалось "data.timer : 120", получен {timer}'

    @testit.workItemIds(39295)
    @testit.externalId('TestSmsCodeSend_39295')
    @testit.displayName('[422] POST /sms/code/send - получение ошибки при запросе смс для регистрации '
                        'для существующего пользователя')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[422] POST /sms/code/send - получение ошибки при запросе смс для регистрации '
                  'для существующего пользователя')
    @allure.testcase(url='https://testit..ru/browse/39295')
    def test_sms_code_send_request_registration_for_exist_user(self):
        expect_text = 'Ошибка регистрации. Дождитесь СМС с информацией'

        data = {
            'phone': '70001696757',
            'reason': 'registration'
        }

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data, check_error=False)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_422(response)
            ResponseHandler.check_response_has_success_is_false(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_err_registration_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()
            actual_name = actual_data['name']
            actual_message = actual_data['message']

            assert expect_text == actual_name, f'Ожидалось "name": "{expect_text}", получен "{actual_name}"'
            assert expect_text == actual_message, (f'Ожидалось "message": "{expect_text}", '
                                                   f'получен "{actual_message}"')
