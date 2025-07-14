from library.common.helpers import *
from datetime import timedelta


class CommonHelper:
    @staticmethod
    def get_list_for_key_in_obj(list_obj, key):
        return [i[key] for i in list_obj]

    @staticmethod
    def get_obj_for_key_in_list(list_obj: list, key: str, value) -> dict:
        for i in list_obj:
            if i[key] == value:
                return i

    @staticmethod
    def get_future_time(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
        future_time = (DateHelper().change_date_timezone(datetime.utcnow(), timezone='Europe/Moscow') +
                       timedelta(days=days, seconds=seconds, microseconds=microseconds,
                                 milliseconds=milliseconds, minutes=minutes, hours=hours,
                                 weeks=weeks)).strftime("%Y-%m-%d %H:%M:%S")
        return future_time

    @staticmethod
    def sort_dict_by_value(data, value):
        sorted_data = sorted(data, key=lambda x: x[value])
        return sorted_data
