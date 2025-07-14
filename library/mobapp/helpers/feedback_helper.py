import allure

from library.mobapp.db import MobAppDB
from .common_helper import *


class FeedbackHelper:

    @staticmethod
    def get_feedback_topics_with_show_on_list():
        with allure.step('Получить список тем отзывов из БД'):
            mobapp_db = MobAppDB()
            result = mobapp_db.sql_read(
                'SELECT id, title, alias FROM feedbacks_themes WHERE show_in_list = 1 ORDER BY sort_priority')

        with allure.step('Преобразование "id" к строке'):
            for item in result:
                item['id'] = str(item['id'])
        return result

    @staticmethod
    def get_feedback_from_db_on_param(*, filter_param, filter_value, select_params='*'):
        with allure.step(f'Получить отзыв из БД по {filter_param} = {filter_value}'):
            mobapp_db = MobAppDB()
            sql_request = (f'SELECT {select_params if isinstance(select_params, str) else ", ".join(select_params)} '
                           f'FROM feedbacks LEFT JOIN feedbacks_data on feedbacks.id = feedbacks_data.feedback_id '
                           f'WHERE {filter_param} = {filter_value!r}')
            result = mobapp_db.sql_read(sql_request)
        return result

    @staticmethod
    def delete_feedback(*, filter_param, filter_value):
        with allure.step(f'Удалить акцию из БД по {filter_param} = {filter_value}'):
            mobapp_db = MobAppDB()
            result = {'feedbacks_data': mobapp_db.sql_write(
                f"DELETE FROM feedbacks_data WHERE feedback_id = "
                f"(SELECT id FROM feedbacks WHERE {filter_param} = {filter_value!r})"),
                      'feedbacks': mobapp_db.sql_write(f"DELETE FROM feedbacks WHERE {filter_param} = {filter_value!r}")
                      }
            return result
