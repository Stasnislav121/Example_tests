import allure
import pytest

from library.mobapp.helpers import AuthHelper
from library.mobapp.api.services import ParcelsApi
from library.mobapp.api.api_const import AUTOTEST_USER_LONG_EXPIRATION_TOKEN
from library.mobapp.api.json_requests.parcels import *
import copy
from library.mobapp.db import MobAppDB
from library.mobapp.files.files_path import *


class ParcelsHelper:
    @staticmethod
    def delete_parcel(parcel_id: [str, list], user_phone: str = None, user_password: str = None,
                      request_with_auth: bool = True, token: str = None, check_delete: bool = False):
        with allure.step(f'Удалить посылку: {parcel_id} '
                         f'{f"под пользователем: {user_phone}" if request_with_auth else "неавторизованным"}'):
            if request_with_auth and token is None:
                if user_phone is None or user_password is None:
                    raise ValueError('Аргументы user_phone и user_password не могут быть None для авторизации')
                token = AuthHelper.get_auth_token(phone=user_phone, password=user_password)
            if isinstance(parcel_id, str):
                parcel_id = [parcel_id]
            client = ParcelsApi()
            client.delete_parcels(parcel_ids=parcel_id, token=token)
            if check_delete:
                response = client.get_parcel(parcel_id, check_error=False)
                assert response.json()['message'] == 'Отправление не найдено', 'Посылка не должна быть найдена'

    @staticmethod
    def create_parcel(request_with_auth: bool = True, token: str = None, user_phone: str = None,
                      user_password: str = None, json_request_data=None):
        if request_with_auth and token is None:
            if user_phone is None or user_password is None:
                raise ValueError('Аргументы user_phone и user_password не могут быть None для авторизации')
            token = AuthHelper.get_auth_token(phone=user_phone, password=user_password)
        if json_request_data is None:
            json_request_data = copy.deepcopy(parcel_create_office_to_office_json)
        with allure.step(f'Создать посылку '
                         f'{f"под пользователем: {user_phone}" if request_with_auth else "неавторизованным"}'):
            client = ParcelsApi()
            response = client.create(json_request_data, token=token)
            parcel_id = response.json()['data']['id']
        return parcel_id

    @staticmethod
    def get_favorite_parcel(parcel):
        mobapp_db = MobAppDB()
        with allure.step(f'Получить запись по посылке {parcel} БД в таблице "users_parcels" по "track_num" ='
                         f' {parcel}'):
            result = mobapp_db.sql_read(
                f"SELECT * FROM users_parcels WHERE track_num = {parcel}")
        return result

    @staticmethod
    def delete_package_image_from_db(image_id):
        with allure.step(f'Удалить запись в таблице "uploaded_images" по "id" == {image_id}'):
            MobAppDB().sql_write(f"DELETE FROM uploaded_images WHERE id = {image_id}")

    @staticmethod
    def upload_package_image(image_path=PACKAGE_IMAGE['IMAGE_JPG']):
        with allure.step(f'Загрузить изображение шаблона упаковки по пути {image_path}'):
            client = ParcelsApi()
            response = client.upload_custom_package_image(file_path=image_path,
                                                          token=AUTOTEST_USER_LONG_EXPIRATION_TOKEN['token'])
            image_id = response.json()['data']['imageId']
            return image_id


@pytest.fixture
def parcel_helper():
    return ParcelsHelper()
