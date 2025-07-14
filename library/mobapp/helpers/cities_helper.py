import allure

from library.mobapp.db import MobAppDB


class CitiesHelper:
    @staticmethod
    def get_city_by_code(code):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить город из БД по code = {code}'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM geo_city WHERE code = "{code}"')
        return result

    @staticmethod
    def get_cities_by_country(country_code='643'):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить список городов по country_code = {country_code}'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM geo_city WHERE country_code = {country_code}')
        return result

    @staticmethod
    def get_city_by_title(title):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить список городов по title LIKE {title}'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM geo_city WHERE title LIKE "%{title}%"')
        return result
