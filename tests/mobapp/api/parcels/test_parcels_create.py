import allure
import testit
import copy

from library.mobapp import *


class TestParcelsCreate:
    @testit.workItemIds(31137)
    @testit.externalId('TestParcelsCreate_31137')
    @testit.displayName('parcels/create с упаковкой BB (с авторизацией)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('parcels/create с упаковкой BB (с авторизацией)')
    @allure.testcase(url='https://testit..ru/browse/31137')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_create_with__package_with_auth(self, request, with_auth, api_version):
        json_request = copy.deepcopy(parcel_create_office_to_office_json)
        json_request['parcelInfo']['package'] = _PACKAGE_CODE

        auth_token = with_auth
        client = ParcelsApi(version=api_version)
        response = client.create(json_request, token=auth_token)
        parcel_id = response.json()['data']['id']
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=parcel_id, token=auth_token))
        ResponseHandler.validate_response(response, parcel_create_schema)

    @testit.workItemIds(17708)
    @testit.externalId('TestParcelsCreate_17708')
    @testit.displayName('parcels/create с упаковкой BB (без авторизации)')
    @testit.nameSpace('API')
    @testit.className('Parcels')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Parcels')
    @allure.title('parcels/create с упаковкой BB (без авторизации)')
    @allure.testcase(url='https://testit..ru/browse/17708')
    @pytest.mark.parametrize('api_version', ['v2', 'v3'])
    def test_parcels_create_with__package_no_auth(self, request, api_version, with_auth):
        json_request = copy.deepcopy(parcel_create_office_to_office_json)
        json_request['parcelInfo']['package'] = _PACKAGE_CODE

        client = ParcelsApi(version=api_version)
        response = client.create(json_request)
        parcel_id = response.json()['data']['id']
        request.addfinalizer(lambda: ParcelsHelper.delete_parcel(parcel_id=parcel_id, token=with_auth))
        ResponseHandler.validate_response(response, parcel_create_schema)
