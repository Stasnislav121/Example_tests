import allure
import testit
from library.mobapp import *


class TestUserLogout:
    @testit.workItemIds(17693)
    @testit.externalId('TestUserLogout_17693')
    @testit.displayName('[200] POST /user/logout - завершение сессии авторизованного пользователя')
    @testit.nameSpace('API')
    @testit.className('User')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: User')
    @allure.title('[200] POST /user/logout - завершение сессии авторизованного пользователя')
    @allure.testcase(url='https://testit..ru/browse/17693')
    def test_user_logout(self):
        device_id = f'{random.randint(10000, 99990)}'
        token = AuthHelper.get_auth_token(phone=AUTOTEST_USER[0], password=AUTOTEST_USER[1], device_id=device_id)

        with allure.step('Проверить наличие записи по пользователю в таблице "users_sessions"'):
            actual_session = UserHelper.get_user_session(username=AUTOTEST_USER[0], device_id=device_id)
            assert actual_session[0]['device_id'] == device_id, 'device_id не равен'

        with allure.step('Выполнить POST /user/logout'):
            client = UserApi()
            response = client.logout_user(token=token, device_id=device_id)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, user_logout_schema)

        with allure.step('Проверка параметров ответа'):
            result_session = UserHelper.get_user_session(username=AUTOTEST_USER[0], device_id=device_id)
            assert result_session == [], f'Ожидалось отсутствие записей в result_session, получено {result_session}'

    @testit.workItemIds(35910)
    @testit.externalId('TestUserLogout_35910')
    @testit.displayName('[418] POST /user/logout - попытка завершение сессии неавторизованного пользователя')
    @testit.nameSpace('API')
    @testit.className('User')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: User')
    @allure.title('[418] POST /user/logout - попытка завершение сессии неавторизованного пользователя')
    @allure.testcase(url='https://testit..ru/browse/35910')
    def test_user_logout_without_auth(self):
        device_id = f'{random.randint(10000, 99990)}'
        token = AuthHelper.get_auth_token(phone=AUTOTEST_USER[0], password=AUTOTEST_USER[1], device_id=device_id)

        with allure.step(f'Выполнить POST /user/logout с токеном {token}'):
            client = UserApi()
            response = client.logout_user(token=token, device_id=device_id)

        with allure.step(f'Выполнить POST /user/logout c токеном {token} '
                         f'после удаления записи сессии в таблице "users_sessions"'):
            response = client.logout_user(token=token, device_id=device_id, check_error=False)

        with allure.step('Проверить код ответа'):
            ResponseHandler.check_response_code_is_418(response)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, user_logout_schema_err)

        with allure.step('Проверка параметров ответа'):
            ResponseHandler.check_response_has_success_is_false(response)
