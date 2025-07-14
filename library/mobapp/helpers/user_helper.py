import allure

from library.mobapp.db import MobAppDB


class UserHelper:
    @staticmethod
    def get_user_session(username, device_id):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить запись сессии из БД по username = "{username}", device_id = "{device_id}"'):
            result = mobapp_db.sql_read(
                f'SELECT * FROM users_sessions WHERE username = "{username}" AND device_id = "{device_id}"')
        return result

    @staticmethod
    def insert_session(username, device_id, hash_part, expiration):
        mobapp_db = MobAppDB()
        with allure.step(f'Добавить сессию в БД со значениями username = "{username}", device_id = "{device_id}", '
                         f' hash_part = "{hash_part}", expiration = "{expiration}"'):
            result = mobapp_db.sql_write(f"INSERT INTO users_sessions "
                                         f" (username, device_id, hash_part, expiration, "
                                         f" last_login, ip, os, device, client) "
                                         f" VALUES ('{username}', '{device_id}', "
                                         f" '{hash_part}', '{expiration}', "
                                         f" '2024-10-14 13:52:12', '192.168.11.113', 'other', DEFAULT, 'test')")
        return result

    @staticmethod
    def update_session(expiration, username, device_id, hash_part):
        mobapp_db = MobAppDB()
        with allure.step(f'Обновить сессию в БД со значениями expiration = "{expiration}", username = "{username}", '
                         f' device_id = "{device_id}", hash_part = "{hash_part}"'):
            result = mobapp_db.sql_write(f"UPDATE users_sessions SET expiration = '{expiration}' "
                                         f" WHERE username = '{username}' AND device_id = '{device_id}' "
                                         f" AND hash_part = '{hash_part}'")
            return result
