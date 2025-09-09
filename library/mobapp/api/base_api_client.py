import os

from library.common.api import ApiClient
# from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.api_const import DEVICE_ID


class BaseApiClient(ApiClient):
    access_token = '2e2df55176160cabaa35729df3f32c85'
    device_id = DEVICE_ID

    def __init__(self, service, version='v2'):
        self.version = version
        self.base_address = f"http://127.0.0.1:8000/{service}"
        self.headers = {
            'X-Access-Token': self.access_token,
            'Device-Id': self.device_id
        }

        super().__init__(base_address=self.base_address)
