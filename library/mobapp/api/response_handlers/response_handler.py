import allure
import pytest

from requests import Response
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError


class ResponseHandler:
    @staticmethod
    def validate_response(response: Response, schema):
        with allure.step('Валидация ответа по json-схеме'):
            try:
                allure.attach(str(response.json()), 'RESPONSE', allure.attachment_type.JSON)
                allure.attach(str(schema), 'SCHEMA', allure.attachment_type.JSON)
                validate(instance=response.json(), schema=schema)
            except ValidationError as err:
                pytest.fail(f'Ошибка при валидации ответа:\n{err}')

    @staticmethod
    def check_response_field_value(response: Response, field_path: list or tuple, expected_value):
        if len(field_path) == 0:
            pytest.fail('Параметр field_path не должен быть пустым!')
        text_path = ''
        actual_value = response.json()
        for item in field_path:
            text_path += f'[{item}]'
            actual_value = actual_value[item]
        assert actual_value == expected_value, \
            f'В поле {text_path}, ожидалось значение: {expected_value}, получено: {actual_value}'

    @staticmethod
    def check_status_code(code, expected_code):
        with allure.step(f"Проверка кода ответа {expected_code}"):
            assert code == expected_code, f"Код ответа запроса должен быть {expected_code}, получен {code}"

    @staticmethod
    def check_response_code_is_200(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=200)

    @staticmethod
    def check_response_code_is_201(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=201)

    @staticmethod
    def check_response_has_success_is_true(response: Response):
        ResponseHandler.check_response_field_value(response, field_path=['success'], expected_value=True)

    @staticmethod
    def check_response_has_success_is_false(response: Response):
        ResponseHandler.check_response_field_value(response, field_path=['success'], expected_value=False)

    @staticmethod
    def check_response_code_is_401(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=401)

    @staticmethod
    def check_response_code_is_403(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=403)

    @staticmethod
    def check_response_code_is_418(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=418)

    @staticmethod
    def check_response_code_is_422(response: Response):
        ResponseHandler.check_status_code(code=response.status_code, expected_code=422)
