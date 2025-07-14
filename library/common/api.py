import requests
import allure
import urllib3
import random
import string

from datetime import datetime
from json import dumps, loads
from typing import List, Optional


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None, log=True, cookies=None, timeout=60,
             files=None):
        url = f"{self.base_address}{path}"
        headers = self.add_x_request_id(headers)

        with allure.step(f'POST: {url}'):
            if json is not None and log:
                allure.attach(str(json).replace('\n', ''), 'POST DATA', allure.attachment_type.JSON)
            if data is not None and log:
                allure.attach(str(data).replace('\n', ''), 'POST DATA', allure.attachment_type.JSON)
            if headers is not None and log:
                allure.attach(str(headers).replace('\n', ''), 'HEADERS', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.post(url=url, params=params, data=data, json=json, headers=headers, verify=False,
                                     cookies=cookies, timeout=timeout, files=files)
            if log:
                allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response

    def put(self, path="/", params=None, data=None, json=None, headers=None, timeout=60):
        url = f"{self.base_address}{path}"
        headers = self.add_x_request_id(headers)

        with allure.step(f'PUT: {url}'):
            allure.attach(str(json), 'PUT DATA', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.put(url=url, params=params, data=data, json=json, headers=headers, verify=False,
                                    timeout=timeout)
            allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response

    def get(self, path="/", params=None, headers=None, json=None, cookies=None, print_url=True, data=None,
            timeout=60):
        url = f"{self.base_address}{path}"
        headers = self.add_x_request_id(headers)
        if print_url:
            print(url)

        with allure.step(f'GET: {url}'):
            if params is not None:
                allure.attach(str(params).replace('\n', ''), 'PARAMETERS', allure.attachment_type.JSON)
            if headers is not None:
                allure.attach(str(headers).replace('\n', ''), 'HEADERS', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.get(url=url, params=params, headers=headers, json=json, verify=False, cookies=cookies,
                                    data=data, timeout=timeout)
            allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response

    def patch(self, path="/", params=None, data=None, json=None, headers=None, log=True, cookies=None, timeout=60):
        url = f"{self.base_address}{path}"
        headers = self.add_x_request_id(headers)

        with allure.step(f'PATCH: {url}'):
            if json is not None and log:
                allure.attach(str(json).replace('\n', ''), 'PATCH DATA', allure.attachment_type.JSON)
            if headers is not None and log:
                allure.attach(str(headers).replace('\n', ''), 'HEADERS', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.patch(url=url, params=params, data=data, json=json, headers=headers, verify=False,
                                      cookies=cookies, timeout=timeout)
            if log:
                allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response

    def delete(self, path="/", headers=None, json=None, timeout=60):
        url = f"{self.base_address}{path}"
        headers = self.add_x_request_id(headers)

        with allure.step(f'DELETE: {url}'):
            if headers is not None:
                allure.attach(str(headers).replace('\n', ''), 'HEADERS', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.delete(url=url, headers=headers, json=json, verify=False, timeout=timeout)
            if len(response.content) < 1000:
                # too big content make very big artifacts in GitLab and pages are not published
                allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response

    def add_x_request_id(self, headers):
        if headers is None:
            headers = {}
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(10))
        headers['X-Request-Id'] = 'Autotest-' + current_time + '-' + random_str
        return headers


class ApiAllureHelper:
    def __init__(self):
        pass

    def check_status_code(self, code, expected_code):
        with allure.step(f"Проверка кода ответа {expected_code}"):
            assert code == expected_code, f"Код ответа запроса должен быть {expected_code}, получен {code}"

    def check_response_200(self, response):
        self.check_status_code(response.status_code, 200)

    def check_response_400(self, response):
        self.check_status_code(response.status_code, 400)

    def check_response_200_empty_json(self, response):
        with allure.step('Проверка ответа 200 и пустой JSON'):
            with allure.step(f"Проверка кода ответа {response.status_code} == 200?"):
                assert response.status_code == 200, \
                    f"Код ответа запроса должен быть 200, вернулся {response.status_code}"
            with allure.step("Проверка ответа на пустой JSON"):
                assert response.json() == {}, "Ответ должен быть пустным JSON"

    def check_response_200_not_empty_json(self, response):
        with allure.step('Проверка ответа 200 и не пустой JSON'):
            with allure.step(f"Проверка кода ответа {response.status_code} == 200?"):
                assert response.status_code == 200, \
                    f"Код ответа запроса должен быть 200, пришел {response.status_code}, {response.content}"
            with allure.step("Проверка ответа, что не пустой"):
                assert response.content != '', "Ответ не должен быть пустым"
            with allure.step("Проверка ответа на пустой JSON"):
                assert response.json() != {}, "Ответ должен быть не пустным JSON"

    def check_response_code_and_json(self, response, code, json, replace: Optional[List[tuple or list]] = None):
        with allure.step("Проверка ответа"):
            with allure.step(f"Проверка кода ответа {response.status_code} == {code}?"):
                assert response.status_code == code, \
                    f"Код ответа запроса должен быть {code}, вернулся {response.status_code}"
            with allure.step("Проверка ответа, что не пустой"):
                assert response.content != '', "Ответ не должен быть пустым"

            with allure.step("Проверка JSON ответа"):
                response_json = response.json()
                if replace is not None:
                    json_string = dumps(response_json)
                    for char_to_replace, new_char in replace:
                        json_string = json_string.replace(char_to_replace, new_char)
                    response_json = loads(json_string)

                assert response_json == json, "Ответ " + str(response_json) + f" должен быть равен {str(json)}"

    def check_response_and_return_body(self, response, code):
        with allure.step(f'Проверка статуса ответа на {code}'):
            if code == 200:
                self.check_response_200(response)
            elif code == 400:
                self.check_status_code(code, 400)
            elif code == 401:
                self.check_status_code(code, 401)
            elif code == 403:
                self.check_status_code(code, 403)
            else:
                raise Exception(f'Код {code} не существует или не определён')

        with allure.step('Проверка параметров ответа'):
            response_body = response.json()
        return response_body
