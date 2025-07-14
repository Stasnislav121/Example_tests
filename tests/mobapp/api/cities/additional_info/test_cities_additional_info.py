import pytest
import allure
import testit
from library.mobapp import *


class TestCitiesAdditionalInfo:
    @testit.workItemIds(33746)
    @testit.externalId('TestCities_33746')
    @testit.displayName('[200] GET /cities/additional-info - получение плашки с доп. информацией по импорту/экспорту')
    @testit.nameSpace('API')
    @testit.className('Cities')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Cities/additional-info')
    @allure.title('[200] GET /cities/additional-info - получение плашки с доп. информацией по импорту/экспорту')
    @allure.testcase(url='https://testit..ru/browse/33746')
    @pytest.mark.parametrize('get_token', ["with_auth", "without_auth"])
    def test_get_cities_additional_info(self, array_helper, request, get_token):
        expect_additional_info = {
            "additionalInfo": "Предупредите получателя: когда посылка будет проходить таможенное оформление на "
                              "границе с Арменией, ему позвонят для уточнения номера паспорта. Паспорт получателя "
                              "может быть паспортом любой страны мира."
        }
        sender_city_code = '56'
        receiver_city_code = 'Н00703410'

        token = request.getfixturevalue(get_token)

        with allure.step('Выполнить GET /cities/additional-info?senderCityCode=56&receiverCityCode=Н00703410'):
            client = CitiesApi()
            response = client.get_additional_info(token=token, sender_city_code=sender_city_code,
                                                  receiver_city_code=receiver_city_code)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, cities_additional_info_schema)

        with allure.step('Проверка параметров ответа'):
            additional_info_resp = response.json()['data']
            array_helper.assert_arrays(expect_additional_info, additional_info_resp)
