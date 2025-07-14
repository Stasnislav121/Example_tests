import allure
import testit
from library.mobapp import *


class TestSmsCodeVerify:
    @testit.workItemIds(17692)
    @testit.externalId('TestSmsCodeVerify_17692')
    @testit.displayName('[201] POST /sms/code/verify - верификация смс')
    @testit.nameSpace('API')
    @testit.className('Sms')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Sms')
    @allure.title('[201] POST /sms/code/verify - верификация смс')
    @allure.testcase(url='https://testit..ru/browse/17692')
    def test_sms_code_verify_success(self, request_sms):
        data = {
            'phone': request_sms['phone'],
            'code': '9999'
        }
        expect_expiration_time = '21600'

        with allure.step('Выполнить POST /sms/code/verify'):
            client = SmsApi()
            response = client.request_sms_code_verify(json=data)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, sms_code_verify_success_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_verification_token = actual_data['verificationToken']
            actual_expiration_time = actual_data['expirationTime']

            assert actual_verification_token, (f'Ожидался не пустой "verificationToken", '
                                               f'получен {actual_verification_token}')
            assert expect_expiration_time == actual_expiration_time, (
                f'Ожидалось "expirationTime": {expect_expiration_time},получено {actual_expiration_time}')
