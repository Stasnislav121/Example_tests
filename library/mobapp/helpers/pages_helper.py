import allure

from .common_helper import *
from .db_helper import *


class PagesHelper(CommonHelper):
    def __init__(self):
        self.mobapp_db = DBHelper()

    def get_pages_documents_from_db(self, show_on_profile=1):
        with allure.step(f'Получить список документов из таблицы "FAQ"'
                         f' с признаком "show_on_profile"={show_on_profile}'):
            return self.mobapp_db.read_row(table_name='faq',
                                           select_column=['title', 'link'],
                                           where_request={'show_on_profile': show_on_profile})

    def add_pages_documents_in_db(self, data):
        with allure.step(f'Добавить документ в таблицу "FAQ" с данными {data}'):
            self.mobapp_db.insert_row(table_name='faq', data=data)

    def delete_pages_documents_in_db(self, data):
        with allure.step(f'Удалить документ из таблицы "FAQ" с данными {data}'):
            self.mobapp_db.delete_row(table_name='faq', where_request=data)
