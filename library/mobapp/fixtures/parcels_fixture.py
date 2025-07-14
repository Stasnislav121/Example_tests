import pytest
from library.mobapp.helpers.parcels_helper import *


@pytest.fixture
def create_parcel_with_autotest_user_sender():
    json_request_data = copy.deepcopy(parcel_create_office_to_office_json)
    json_request_data['senderInfo']['personalUserInfo']['name'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['name']
    json_request_data['senderInfo']['personalUserInfo']['phone'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone']
    json_request_data['senderInfo']['personalUserInfo']['email'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['email']
    json_request_data['receiverInfo']['personalUserInfo']['phone'] = '79000009901'
    return ParcelsHelper.create_parcel(request_with_auth=True, token=AUTOTEST_USER_LONG_EXPIRATION_TOKEN['token'],
                                       json_request_data=json_request_data)


@pytest.fixture
def create_parcel_for_autotest_user_receipt():
    json_request_data = copy.deepcopy(parcel_create_office_to_office_json)
    json_request_data['senderInfo']['personalUserInfo']['phone'] = '79000009901'
    json_request_data['receiverInfo']['personalUserInfo']['name'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['name']
    json_request_data['receiverInfo']['personalUserInfo']['phone'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone']
    json_request_data['receiverInfo']['personalUserInfo']['email'] = AUTOTEST_USER_LONG_EXPIRATION_TOKEN['email']
    return ParcelsHelper.create_parcel(request_with_auth=False, json_request_data=json_request_data)


@pytest.fixture
def upload_package_image():
    return ParcelsHelper.upload_package_image()
