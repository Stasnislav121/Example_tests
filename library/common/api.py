import requests
import allure
import urllib3


class ApiClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, json=None, headers=None, log=True, cookies=None, timeout=60,
             files=None):
        url = f"{self.base_address}{path}"

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

        with allure.step(f'DELETE: {url}'):
            if headers is not None:
                allure.attach(str(headers).replace('\n', ''), 'HEADERS', allure.attachment_type.JSON)
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            response = requests.delete(url=url, headers=headers, json=json, verify=False, timeout=timeout)
            if len(response.content) < 1000:
                # too big content make very big artifacts in GitLab and pages are not published
                allure.attach(response.content, 'RESPONSE ' + str(response.status_code), allure.attachment_type.JSON)
            return response
