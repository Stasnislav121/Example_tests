import allure
import testit
from library.mobapp import *


class TestSmsCodeSend:
    @testit.workItemIds(39289)
    @testit.externalId('TestSmsCodeSend_39289')
    @testit.displayName('[201] POST /sms/code/send - запрос смс для смены пароля')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[201] POST /sms/code/send - запрос смс для смены пароля')
    @allure.testcase(url='https://testit..ru/browse/39289')
    def test_sms_code_send_request_password_change(self, string_helper):
        data = {
            'phone': '7000' + string_helper.get_random_phone(length=7),
            'reason': 'passwordChange'
        }

        with allure.step('Выполнить POST /sms/code/send'):
            client = SmsApi()
            response = client.request_sms_code_send(json=data)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_send_success_schema)

        with allure.step('Проверка параметров ответа'):
            timer = response.json()['data']['timer']
            assert timer == 120, f'Ожидалось "data.timer : 120", получен {timer}'
