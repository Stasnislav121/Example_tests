import pytest
import allure
import testit
from library.mobapp import *


class TestPacks:
    @testit.workItemIds(35397)
    @testit.externalId('TestPacks_35397')
    @testit.displayName('[200] GET /packs - получение списка упаковок')
    @testit.nameSpace('API')
    @testit.className('Packs')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Packs')
    @allure.title('[200] GET /packs - получение списка упаковок')
    @allure.testcase(url='https://testit..ru/browse/35397')
    @pytest.mark.parametrize('get_token', ["without_auth"])
    @pytest.mark.forci
    def test_get_packs(self, array_helper, request, get_token):
        expect_packs = {
                    "id": "799",
                    "title": "Короб ХS",
                    "image": "https://storage.img.net/mobile-app-images/packs/799.png?v=1",
                    "length": 15,
                    "width": 15,
                    "height": 15,
                    "parcelExample": "мобильный телефон, украшения, духи"
        }
        token = request.getfixturevalue(get_token)

        with allure.step('Выполнить GET /packs'):
            client = PacksApi()
            response = client.get_packs(token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, packs_schema)

        with allure.step('Проверка параметров ответа'):
            packs_resp = response.json()['data']['boxes'][0]
            array_helper.assert_arrays(expect_packs, packs_resp)
