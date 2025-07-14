import pytest
from library.mobapp.helpers.sms_helper import *


@pytest.fixture
def request_sms():
    return SmsHelper.request_sms(reason='registration', check_error=True)


@pytest.fixture
def request_and_verify_sms_for_registration():
    phone = SmsHelper.request_sms(reason='registration', check_error=True)['phone']
    verification_token = SmsHelper.verify_sms(phone=phone, code='999').json()['data']['verificationToken']
    return dict(phone=phone, verificationToken=verification_token)
