import allure
import testit
from library.mobapp import *


class TestUser:
    @testit.workItemIds(35405)
    @testit.externalId('TestUser_35405')
    @testit.displayName('[200] GET /user - получение данных профиля пользователя')
    @testit.nameSpace('API')
    @testit.className('User')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: User')
    @allure.title('[200] GET /user - получение данных профиля пользователя')
    @allure.testcase(url='https://testit..ru/browse/35405')
    def test_get_user_info_with_auth(self, array_helper, with_auth):
        expect_info = {
            "id": "28488724",
            "status": "user",
            "phone": AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            "email": "mobile@autotest.com",
            "sex": "male",
            "birthday": "2016-09-09",
            "passportDataFilled": False,
            "name": "MOBILE AUTOTEST Отправитель",
            "passportSeries": None,
            "passportNumber": None
        }

        token = with_auth

        with allure.step('Выполнить GET /user'):
            client = UserApi()
            response = client.get_user_info(token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, user_info_schema)

        with allure.step('Проверка параметров ответа'):
            info_resp = response.json()['data']
            array_helper.assert_arrays(expect_info, info_resp)

    @testit.workItemIds(35406)
    @testit.externalId('TestUser_35406')
    @testit.displayName('[401] GET /user - получение ошибки при запросе данных профиля неавторизованного пользователя')
    @testit.nameSpace('API')
    @testit.className('User')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: User')
    @allure.title('[401] GET /user - получение ошибки при запросе данных профиля неавторизованного пользователя')
    @allure.testcase(url='https://testit..ru/browse/35406')
    def test_get_user_info_without_auth(self):
        with allure.step('Выполнить GET /user'):
            client = UserApi()
            response = client.get_user_info(check_error=False)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_err_schema)

        with allure.step('Проверка кода ответа'):
            ResponseHandler.check_response_code_is_401(response)
