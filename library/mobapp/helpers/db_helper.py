from typing import Union
import allure
import pytest
from library.mobapp.db import MobAppDB


class DBHelper:
    def __init__(self):
        self.mobapp_db = MobAppDB()

    def insert_row(self, *, table_name: str, data: dict):
        if not isinstance(data, dict):
            raise TypeError(f'Ожидался словарь, получен {type(data).__name__}')
        keys = ', '.join(data.keys())
        values = ', '.join(f"{value!r}" for value in data.values())
        with allure.step(f'Добавить запись в таблицу "{table_name}" с данными {data}'):
            query = f'INSERT INTO {table_name} ({keys}) VALUES ({values})'
            self.mobapp_db.sql_write(query)

    def read_row(self, *, table_name: str, select_column: Union[list, tuple, set, str] = '*',
                 where_request: dict = None) -> list:
        where_request_row = ''
        if isinstance(select_column, (list, tuple, set)):
            select_column = ', '.join(str(item) for item in select_column)
        if isinstance(where_request, dict):
            where_request_row = ' WHERE ' + ' AND '.join(f"{key} = {value!r}" for key, value in where_request.items())
        with allure.step(f'Получить запись из таблицы "{table_name}" по признакам {where_request}'):
            query = f'SELECT {select_column} FROM {table_name}{where_request_row}'
            result = self.mobapp_db.sql_read(query)
        return result

    def read_row_with_left_join(self, *, left_table: str, right_table: str, on_key: str,
                                select_column: Union[list, tuple, set, str] = '*', where_request: dict = None) -> list:
        where_request_row = ''
        if isinstance(select_column, (list, tuple, set)):
            select_column = ', '.join(str(item) for item in select_column)
        if isinstance(where_request, dict):
            where_request_row = ' WHERE ' + ' AND '.join(f"{key} = {value!r}" for key, value in where_request.items())
        with allure.step(f'Получить запись из таблицы "{left_table}" с LEFT JOIN таблицы "{right_table}" '
                         f'по ключу "{on_key}" с признаками {where_request}'):
            query = f'SELECT {select_column} FROM {left_table} LEFT JOIN {right_table} ON {on_key}{where_request_row}'
            result = self.mobapp_db.sql_read(query)
        return result

    def update_row(self, *, table_name: str, data: dict, where_request: dict):
        if not isinstance(data, dict):
            raise TypeError(f'Ожидался словарь, получен {type(data).__name__}')
        if not isinstance(where_request, dict):
            raise TypeError(f'Ожидался словарь, получен {type(where_request).__name__}')
        set_clause = ', '.join(f"{key} = {value!r}" for key, value in data.items())
        where_request_row = ' AND '.join(f"{key} = {value!r}" for key, value in where_request.items())
        with allure.step(f'Обновить запись в таблице "{table_name}"  с признаками {where_request_row} значениями'
                         f' {data}'):
            query = f'UPDATE {table_name} SET {set_clause} WHERE {where_request_row}'
            self.mobapp_db.sql_write(query)

    def delete_row(self, *, table_name: str, where_request: dict):
        if not isinstance(where_request, dict):
            raise TypeError(f'Ожидался словарь, получен {type(where_request).__name__}')
        where_request_row = ' AND '.join(f"{key} = {value!r}" for key, value in where_request.items())
        with allure.step(f'Удалить запись из таблицы "{table_name}" с признаками {where_request}'):
            query = f'DELETE FROM {table_name} WHERE {where_request_row}'
            self.mobapp_db.sql_write(query)


@pytest.fixture
def mobapp_db():
    return DBHelper()
