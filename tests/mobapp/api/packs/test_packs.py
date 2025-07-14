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
    def test_get_packs(self, array_helper, request, get_token):
        expect_packs = {
            "boxes": [
                {
                    "id": "799",
                    "title": "Короб ХS",
                    "image": "https://storage.img.net/mobile-app-images/packs/799.png?v=1",
                    "": True,
                    "length": 15,
                    "width": 15,
                    "height": 15,
                    "parcelExample": "мобильный телефон, украшения, духи"
                },
                {
                    "id": "798",
                    "title": "Короб S",
                    "image": "https://storage.img.net/mobile-app-images/packs/798.png?v=1",
                    "": True,
                    "length": 20,
                    "width": 20,
                    "height": 20,
                    "parcelExample": "книга, платье, канцелярия"
                },
                {
                    "id": "797",
                    "title": "Короб M",
                    "image": "https://storage.img.net/mobile-app-images/packs/797.png?v=1",
                    "": True,
                    "length": 35,
                    "width": 20,
                    "height": 20,
                    "parcelExample": "рюкзак, детские игрушки, джинсы"
                },
                {
                    "id": "804",
                    "title": "Короб TL",
                    "image": "https://storage.img.net/mobile-app-images/packs/804.png?v=1",
                    "": True,
                    "length": 80,
                    "width": 15,
                    "height": 20,
                    "parcelExample": "книга, платье, канцелярия"
                },
                {
                    "id": "801",
                    "title": "Короб L",
                    "image": "https://storage.img.net/mobile-app-images/packs/801.png?v=1",
                    "": True,
                    "length": 35,
                    "width": 30,
                    "height": 25,
                    "parcelExample": "ноутбук, планшет, куртка"
                },
                {
                    "id": "802",
                    "title": "Короб XL",
                    "image": "https://storage.img.net/mobile-app-images/packs/802.png?v=1",
                    "": True,
                    "length": 50,
                    "width": 40,
                    "height": 35,
                    "parcelExample": "принтер, компьютер, мелкая электроника"
                }
            ],
            "packages": [
                {
                    "id": "796",
                    "title": "Пакет с клапаном XS",
                    "image": "https://storage.img.net/mobile-app-images/packs/796.png?v=1",
                    "": True,
                    "length": None,
                    "width": 24,
                    "height": 24,
                    "parcelExample": "книга"
                },
                {
                    "id": "795",
                    "title": "Пакет с клапаном S",
                    "image": "https://storage.img.net/mobile-app-images/packs/795.png?v=1",
                    "": True,
                    "length": None,
                    "width": 24,
                    "height": 32,
                    "parcelExample": "перчатки"
                },
                {
                    "id": "794",
                    "title": "Пакет с клапаном M",
                    "image": "https://storage.img.net/mobile-app-images/packs/794.png?v=1",
                    "": True,
                    "length": None,
                    "width": 30,
                    "height": 40,
                    "parcelExample": "туфли"
                },
                {
                    "id": "793",
                    "title": "Пакет с клапаном L",
                    "image": "https://storage.img.net/mobile-app-images/packs/793.png?v=1",
                    "": True,
                    "length": None,
                    "width": 39,
                    "height": 51,
                    "parcelExample": "костюм"
                },
                {
                    "id": "978",
                    "title": "Пакет с клапаном XL",
                    "image": "https://storage.img.net/mobile-app-images/packs/978.png?v=1",
                    "": True,
                    "length": None,
                    "width": 60,
                    "height": 75,
                    "parcelExample": "детский комбинезон"
                }
            ],
            "envelops": [
                {
                    "id": "800",
                    "title": "Конверт А4",
                    "image": "https://storage.img.net/mobile-app-images/packs/800.png?v=1",
                    "": True,
                    "length": None,
                    "width": 30,
                    "height": 21,
                    "parcelExample": "пакет документов формата а4"
                }
            ]
    }
        token = request.getfixturevalue(get_token)

        with allure.step('Выполнить GET /packs'):
            client = PacksApi()
            response = client.get_packs(token=token)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, packs_schema)

        with allure.step('Проверка параметров ответа'):
            packs_resp = response.json()['data']
            array_helper.assert_arrays(expect_packs, packs_resp)
