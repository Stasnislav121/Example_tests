import allure

from library.common.helpers import StringHelper
from library.mobapp.api.services import SmsApi


class SmsHelper:
    @staticmethod
    def request_sms(phone=None, reason='registration', check_error=True):
        data = {'phone': phone, 'reason': reason}
        if phone is None:
            data['phone'] = '7000' + StringHelper().get_random_phone(length=7)
        with allure.step(f'Запросить смс для пользователя {phone} с событием {reason}'):
            client = SmsApi()
            client.request_sms_code_send(check_error=check_error, json=data)
        return data

    @staticmethod
    def verify_sms(phone=None, code='9999', check_error=True):
        data = {'phone': phone, 'code': code}
        if phone is None:
            data['phone'] = '7000' + StringHelper().get_random_phone(length=7)
        with allure.step(f'Верифицировать смс для пользователя {phone} с кодом {code}'):
            client = SmsApi()
            response = client.request_sms_code_verify(check_error=check_error, json=data)
        return response
