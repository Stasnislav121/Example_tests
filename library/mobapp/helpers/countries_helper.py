import allure

from library.mobapp.db import MobAppDB


class CountriesHelper:
    @staticmethod
    def get_countries(param, filter):
        mobapp_db = MobAppDB()
        with allure.step('Получить страны из БД'):
            result = mobapp_db.sql_read(
                f"SELECT {param} FROM countries WHERE {filter}")
        return result

    @staticmethod
    def get_countries_with_auth(param='*', filter='export = 0 AND blocked = 0'):
        with allure.step(f'Получить {param} из БД с признаками {filter}'):
            result = CountriesHelper.get_countries(param, filter)
        return result

    @staticmethod
    def get_countries_with_registration(param='*', filter='export = 0 AND blocked = 0 AND code_iso=643'):
        with allure.step(f'Получить {param} из БД с признаками {filter}'):
            result = CountriesHelper.get_countries(param, filter)
        return result

    @staticmethod
    def get_countries_with_checkout(param='*', filter='blocked = 0'):
        with allure.step(f'Получить {param} из БД с признаками {filter}'):
            result = CountriesHelper.get_countries(param, filter)
        return result

    @staticmethod
    def get_countries_with_passport(param='*', filter='blocked = 0'):
        with allure.step(f'Получить {param} из БД с признаками {filter}'):
            result = CountriesHelper.get_countries(param, filter)
        return result

    @staticmethod
    def get_list_countries(list_obj, key):
        result_list = [i[key] for i in list_obj]
        return result_list
