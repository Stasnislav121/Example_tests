import copy

import pytest
from library.mobapp.helpers.stocks_helper import *
from library.mobapp.api.json_requests import stock_request_json


@pytest.fixture
def add_random_non_personal_stock():
    data = copy.deepcopy(stock_request_json)
    random_int = random.randint(1000, 9999)
    data['hash'] = f'7b08edf3-55d8-{random_int}-90f5-350ce33d4d43'
    data['int_id'] = random_int
    data['title'] = StringHelper().get_random_ru_string()
    client = StocksHelper()
    response = client.insert_stock(data=data)
    yield response
    client.delete_stock(param='int_id', value=data['int_id'])
