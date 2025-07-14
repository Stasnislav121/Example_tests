import re
import pytz
import pytest
import random
import string
import allure

from datetime import datetime
from urllib.parse import unquote


class StringHelper:
    def __init__(self):
        pass

    def get_random_string(self, length=20):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_ru_string(self, length=20):
        letters = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_punctuation_string(self, length=20):
        letters = string.punctuation
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_mixed_string(self, length=20):
        letters = string.printable
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_phone(self, length=10):
        letters = string.digits
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def get_random_email(self):
        result_str = self.get_random_string(7) + '@' + self.get_random_string(10) + '.com'
        return result_str

    def get_substring_by_regexp(self, text, template):
        result = ''
        match = re.search(template, text)
        try:
            if match:
                result = match.group(1)
        except IndexError:
            allure.attach(f'Не удалось извлечь подстроку из строки "{text}" по шаблону "{template}"',
                          name='get_substring_by_regexp_error')
        return result

    @staticmethod
    def get_parameters_from_url(url: str) -> dict:
        with allure.step(f'Считать параметры запроса из URL: {url}'):
            parameters = {}
            request_params = unquote(url).split('?')[1].split('&')
            for param in request_params:
                key = param.split('=')[0]
                value = param.split('=')[1]
                parameters[key] = value
            allure.attach(str(parameters), "PARAMETERS", allure.attachment_type.JSON)

        return parameters


@pytest.fixture
def string_helper():
    return StringHelper()


class DateHelper:
    def __init__(self):
        pass

    def format_date(self, date, current_format, required_format):
        return datetime.strptime(str(date), current_format).strftime(required_format)

    def change_date_timezone(self, date: datetime, timezone: str):
        return pytz.utc.localize(date).astimezone(pytz.timezone(timezone))

    def assert_date_format(self, date, date_format):
        date_is_valid = False
        try:
            datetime.strptime(date, date_format)
            date_is_valid = True
        except ValueError:
            pass
        assert date_is_valid, f'Дата "{date}" не соответствует формату: {date_format}'

    def assert_date_equals(self, actual_date, expected_date):
        assert actual_date == expected_date, f'Даты {actual_date} - {expected_date} не равны'

    def assert_date_in_range(self, actual_date, start_date, end_date):
        assert start_date <= actual_date <= end_date, \
            f'Дата {actual_date} не находится в промежутке между датами: {start_date} - {end_date}'

    def assert_date_string_in_range(self, actual_date_str, start_date_str, end_date_str, date_format):
        actual_date = datetime.strptime(actual_date_str, date_format)
        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_str, date_format)
        self.assert_date_in_range(actual_date, start_date, end_date)

    def assert_date_string_equals(self, actual_date_str, expected_date_str, date_format):
        actual_date = datetime.strptime(actual_date_str, date_format)
        expected_date = datetime.strptime(expected_date_str, date_format)
        self.assert_date_equals(actual_date, expected_date)


@pytest.fixture
def date_helper():
    return DateHelper()


class ArrayHelper:
    def __init__(self):
        pass

    # probably need to add checking of values, search by first property equivalent
    # check test_list_pickup_points:test_list_filter for reference
    def assert_arrays(self, arr, expected_arr):
        assert len(arr) == len(expected_arr)
        for param in expected_arr:
            with allure.step(f"Проверка наличия {param}"):
                assert param in arr, f"{param} не найден"
            if isinstance(expected_arr[param], dict):
                with allure.step(f"Проверка массива {param}"):
                    self.assert_arrays(arr[param], expected_arr[param]), \
                        f"Массивы {param} не равны. Result: " + str(arr) + ' Expected: ' + str(expected_arr)
            else:
                with allure.step(f"Проверка {param} = {expected_arr[param]}"):
                    assert arr[param] == expected_arr[param], \
                        f"{param} не равны. Result: " + str(arr) + ' Expected: ' + str(expected_arr)

    def assert_lists(self, list, expected_list):
        assert len(list) == len(expected_list), 'Длина списков не совпадает'
        list.sort()
        expected_list.sort()
        assert list == expected_list, "Массивы НЕ равны"


@pytest.fixture
def array_helper():
    return ArrayHelper()


class DictHelper:
    @staticmethod
    def delete_keys(dictionary, keys_to_delete):
        if not isinstance(dictionary, dict):
            return dictionary

        keys_set = set(keys_to_delete) if not isinstance(keys_to_delete, set) else keys_to_delete
        result = {}

        for key, value in dictionary.items():
            if key not in keys_set:
                if isinstance(value, dict):
                    result[key] = DictHelper.delete_keys(value, keys_set)
                elif isinstance(value, (list, tuple)):
                    result[key] = [
                        DictHelper.delete_keys(item, keys_set) if isinstance(item, dict) else item for item in value
                    ]
                else:
                    result[key] = value
        return result

    @staticmethod
    def update_keys(dictionary, updates):
        for key, value in updates.items():
            if key in dictionary and isinstance(dictionary[key], dict) and isinstance(value, dict):
                DictHelper.update_keys(dictionary[key], value)
            else:
                dictionary[key] = value
        return dictionary


@pytest.fixture
def dict_helper():
    return DictHelper()
