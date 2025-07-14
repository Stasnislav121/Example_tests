import allure
import mysql.connector

from mysql.connector import Error


class MySqlDb:
    def __init__(self, host_name=None, user_name=None, user_password=None, db_name=None, port='3306', use_pure=False):
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        self.db_name = db_name
        self.port = port
        self.use_pure = use_pure

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.user_password,
                database=self.db_name,
                port=self.port,
                use_pure=self.use_pure
            )
        except Error as e:
            print(f"The error '{e}' occurred")
            allure.attach(f"The error '{e}' occurred during create connection", 'Error create connection')

        return connection

    def execute_write_query(self, connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
        except Error as e:
            print(f"The error '{e}' occurred")
            allure.attach(f"The error '{e}' occurred during execute write query", 'Error execute write query')

    def execute_read_query(self, connection, query, dictionary=False):
        cursor = connection.cursor(dictionary=dictionary)
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            allure.attach(f"The error '{e}' occurred during execute read query", 'Error execute read query')
