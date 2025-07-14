# import pytest
# import allure
import testit
from library.mobapp import *


class TestUserChatlist:
    @testit.workItemIds(19506)
    @testit.externalId('TestUserChatlist_19506')
    @testit.displayName('[200] GET /user/chatlist - получение ссылок на чаты ')
    @testit.nameSpace('API')
    @testit.className('User')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: User')
    @allure.title('[200] GET /user/chatlist - получение ссылок на чаты ')
    @allure.testcase(url='https://testit..ru/browse/19506')
    def test_get_chat_list(self):
        expect_additional_info = 'Внимание! Новые правила работы'
        expect_chat_list = [
                {
                    "title": "Webim",
                    "link": "https://api.webim.ru/chat/init"
                },
                {
                    "title": "Telegram",
                    "link": "https://t.me/bot"
                },
                {
                    "title": "Viber",
                    "link": "https://www.viber.com/bot"
                }]

        with allure.step('Выполнить GET /user/chatlist'):
            client = UserApi()
            response = client.get_user_chat_list()

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, user_chat_list_schema)

        with allure.step('Проверка параметров ответа'):
            actual_chat_list_data = response.json()['data']
            actual_additional_info = actual_chat_list_data['additionalInfo']
            actual_chat_list = actual_chat_list_data['links']

            assert expect_additional_info == actual_additional_info, \
                f'Ожидалось "additionalInfo": {expect_additional_info}, получено {actual_additional_info}'
            assert expect_chat_list == actual_chat_list, \
                f'Ожидалось "links": {expect_chat_list}, получено {actual_chat_list}'
