from library.common.helpers import *


class CountriesResponseHandler:
    @staticmethod
    def check_countries_in_response(expect_countries, result_countries):
        with allure.step('Проверить наличие страны в ответе метода /countries'):
            name_result_countries = []
            for i in result_countries:
                name_result_countries.append(i['countryName'])
            ArrayHelper().assert_lists(expect_countries, name_result_countries)
