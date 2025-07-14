import allure

from library.mobapp.db import MobAppDB
from .db_helper import *


class OfficesHelper:
    def __init__(self):
        self.mobapp_db = DBHelper()

    @staticmethod
    def get_offices_by_city(city_code):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить отделения из БД по city_code = "{city_code}'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM offices WHERE city_code = "{city_code}"')
        return result

    @staticmethod
    def get_office_info_by_code_office(code):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить информацию по отделению из БД по code = {code}'):
            result = mobapp_db.sql_read(
                f"SELECT * FROM offices WHERE code = {code}")
        return result

    @staticmethod
    def get_offices_by_address(address):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить отделения из БД по address LIKE "{address}"'):
            result = mobapp_db.sql_read(
                f"SELECT * FROM offices WHERE address LIKE '%{address}%'")
        return result

    def get_offices_by_code_from_db(self, code):
        with allure.step(f'Получить информацию по отделению из таблицы "offices" с признаком "code" = {code}'):
            return self.mobapp_db.read_row_with_left_join(left_table='offices',
                                                          right_table='geo_city',
                                                          on_key='offices.city_code = geo_city.code',
                                                          select_column=('offices.zip as postcode, offices.country, '
                                                                         'offices.city_code, geo_city.title, '
                                                                         'geo_city.latitude as city_latitude, '
                                                                         'geo_city.longitude as city_longitude, '
                                                                         'offices.address, offices.latitude, '
                                                                         'offices.longitude, offices.address_kd'),
                                                          where_request={'offices.code': code})
