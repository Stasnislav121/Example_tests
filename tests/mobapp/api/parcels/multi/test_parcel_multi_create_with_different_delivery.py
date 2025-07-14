import allure
import testit
import copy
import pytest

from library.mobapp import *


class TestParcelsMultiCreate:
    @testit.workItemIds(37278)
    @testit.externalId('TestParcelsDeliveryMulti_37278')
    @testit.displayName('[201] POST /parcels/multi/create - создание ЭН ПВЗ-Двери')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('[201] POST /parcels/multi/create - создание ЭН ПВЗ-Двери')
    @allure.testcase(url='https://testit..ru/browse/37278')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_delivery_multi_office_to_door(self, request, with_auth, api_version):
        token = with_auth
        json_request = copy.deepcopy(parcel_multi_create_office_to_door_json())

        expect_client_receiver_id = json_request['receivers'][0]['id']

        with allure.step('Выполнить POST /parcels/multi/create'):
            client = ParcelsApi(version=api_version)
            response = client.multi_create(json_request, token=token)
            parcels_resp = ParcelsResponseHandler.get_parcels_list(response.json()['data']['parcels'])
            request.addfinalizer(
                lambda: [ParcelsHelper.delete_parcel(parcel_id=[p['trackNumber'] for p in parcels_resp],
                                                     token=with_auth, check_delete=False)])

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, multi_create_schema)

        with allure.step('Проверка параметров ответа'):
            parcel_resp = parcels_resp[0]

            client_receiver_id_resp = parcel_resp['clientReceiverId']
            order_number_resp = parcel_resp['trackNumber']
            expect_shared_link = f"https://.ru/tracking-page?id={order_number_resp}&utm_source=new_site&utm_medium=special&utm_campaign=mobile_app_tracking"
            shared_link_resp = parcel_resp['sharedLink']

            assert client_receiver_id_resp == expect_client_receiver_id, \
                f'Ожидалоссь "clientReceiverId" {expect_client_receiver_id}, получено {client_receiver_id_resp}'
            assert len(order_number_resp) == 13, f'Ожидалась длина trackNumber == 13, получено {len(order_number_resp)}'
            assert shared_link_resp == expect_shared_link, (f'Ожидалось {expect_shared_link}, '
                                                            f'получено {shared_link_resp}')
