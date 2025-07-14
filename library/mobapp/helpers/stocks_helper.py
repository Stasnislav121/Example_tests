import allure


from library.mobapp.db import MobAppDB
from .common_helper import *


class StocksHelper(CommonHelper):

    @staticmethod
    def insert_stock(data: dict):
        keys = ', '.join(data.keys())
        values = ', '.join(f'{value!r}' for value in data.values())
        mobapp_db = MobAppDB()
        with allure.step(f'Добавить акцию в БД со значениями {data}'):
            result = mobapp_db.sql_write(f"INSERT INTO stocks ({keys}) VALUES ({values})")
            return result

    @staticmethod
    def get_stocks(minutes=1):
        future_time = CommonHelper.get_future_time(minutes=minutes)
        mobapp_db = MobAppDB()
        with allure.step('Получить список акций'):
            result = mobapp_db.sql_read(
                f"SELECT * FROM stocks WHERE expiration_date > '{future_time}' AND personal_url IS NULL")
        return result

    @staticmethod
    def get_stock_by_param(param, value):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить список акций из БД по {param} = {value}'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM stocks WHERE {param} = {value!r}')
        return result

    @staticmethod
    def delete_stock(param, value):
        mobapp_db = MobAppDB()
        with allure.step(f'Удалить акцию из БД по {param} = {value}'):
            result = mobapp_db.sql_write(f"DELETE FROM stocks WHERE {param} = {value!r}")
            return result

    @staticmethod
    def add_stock(data: dict):
        StocksHelper.insert_stock(data)
        return StocksHelper.get_stock_by_param(param='int_id', value=data['int_id'])
