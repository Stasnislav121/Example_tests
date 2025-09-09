# import allure
#
#
# from library.site.db import SiteDB
#
#
# class TrackingHelper:
#
#     @staticmethod
#     def insert_shop(name, code):
#         with allure.step(f"Добавить контрагента в таблицу 'pk_shop' со значениями name = '{name}', code = '{code}'"):
#             site_db = SiteDB()
#             sql_query = (f"INSERT INTO pk_shop (name, code) SELECT '{name}', '{code}' "
#                          f"WHERE NOT EXISTS (SELECT 1 FROM pk_shop WHERE name = '{name}' AND code = '{code}')")
#             result = site_db.sql_write(sql_query)
#             return result
