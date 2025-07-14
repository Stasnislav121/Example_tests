import pytest
from library.mobapp.api.api_const import AUTOTEST_USER_LONG_EXPIRATION_TOKEN


@pytest.fixture
def with_auth():
    return AUTOTEST_USER_LONG_EXPIRATION_TOKEN['token']


@pytest.fixture
def without_auth():
    return None
