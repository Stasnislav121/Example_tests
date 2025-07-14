import allure
import testit
from library.mobapp import *


class TestAuthRegistration:
    @testit.workItemIds(36847)
    @testit.externalId('TestAuthRegistration_36847')
    @testit.displayName('[201] POST /auth/registration - регистрация нового пользователя')
    @testit.nameSpace('API')
    @testit.className('Auth')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Auth')
    @allure.title('[201] POST /auth/registration - регистрация нового пользователя')
    @allure.testcase(url='https://testit..ru/browse/36847')
    def test_auth_registration_new_user(self, request_and_verify_sms_for_registration):
        sms_data = request_and_verify_sms_for_registration
        user_data_request = copy.deepcopy(auth_registration_json)
        user_data_request.update(sms_data)
        part_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'

        with allure.step('Выполнить POST /auth/registration/'):
            client = AuthApi()
            response = client.registration(json=user_data_request)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, auth_registration_success_schema)

        with allure.step('Проверка параметров ответа'):
            actual_data = response.json()['data']
            actual_user_data = actual_data['user']
            auth_token = actual_data['authToken']
            refresh_token = actual_data['refreshToken']
            user_status = actual_user_data['status']
            user_phone = actual_user_data['phone']
            user_email = actual_user_data['email']
            user_name = actual_user_data['name']

            assert part_token in auth_token, f'Ожидалось вхождение {part_token} в {auth_token}, получено {auth_token}'
            assert part_token in refresh_token, (f'Ожидалось вхождение {part_token} в {refresh_token},'
                                                 f'получено {refresh_token}')
            assert user_status == 'user', f'Ожидалось "status": "user", получен "{user_status}"'
            assert user_phone == user_data_request['phone'], (f'Ожидалось "phone": "{user_data_request["phone"]}", '
                                                              f'получен "{user_phone}"')
            assert user_email == user_data_request['email'], (f'Ожидалось "email": "{user_data_request["email"]}", '
                                                              f'получен "{user_email}"')
            assert user_name == user_data_request['name'], (f'Ожидалось "name": "{user_data_request["name"]}", '
                                                            f'получен "{user_name}"')
