import os
import allure
import pytest

from _mysql_connector import MySQLInterfaceError
from library.common import mysql_db


class MobAppDB:
    db = None
    db_name = None
    db_connection = None
    host_name = ''
    default_port = 33003
    port = default_port
    user_name = 'root'
    user_password = ''

    def __init__(self):
        self.init_db()
        self.connect_to_db()

    def __del__(self):
        self.close_connection()

    def init_db(self):
        self.db_name = "mobile"
        self.port = self.default_port

    @classmethod
    def connect(cls):
        return MobAppDB()

    def connect_to_db(self):
        with allure.step(f'Подключение к БД с параметрами: host_name={self.host_name}, user_name={self.user_name},'
                         f'db_name={self.db_name}, port={self.port}'):
            self.db = mysql_db.MySqlDb(host_name=self.host_name,
                                       user_name=self.user_name,
                                       user_password=self.user_password,
                                       db_name=self.db_name,
                                       port=self.port)
            self.db_connection = self.db.create_connection()

    def close_connection(self):
        try:
            self.db_connection.close()
        except MySQLInterfaceError as e:
            print(f"The error '{e}' occurred during closing connection")

    def sql_write(self, sql):
        with allure.step("Выполнить SQL запрос"):
            allure.attach(str(sql), 'SQL', allure.attachment_type.TEXT)
            self.db.execute_write_query(self.db_connection, sql)

    def sql_read(self, sql):
        with allure.step("Выполнить SQL запрос"):
            allure.attach(str(sql), 'SQL', allure.attachment_type.TEXT)
            result = self.db.execute_read_query(self.db_connection, sql, dictionary=True)
            allure.attach(str(result), 'query_result', allure.attachment_type.TEXT)
        return result


@pytest.fixture
def mobapp_db():
    db = MobAppDB()
    try:
        yield db
    finally:
        db.close_connection()
