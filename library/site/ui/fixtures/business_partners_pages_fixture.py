import allure
import pytest

from library.site.ui import *
from tests.site.ui.conftest import *


@pytest.fixture
def site_business_partners_open_terminal(site_page):
    with allure.step('Открыть на вкладке "Бизнес-партнерам" страницу раздела "Открыть терминал"'):
        return OpenTerminalPage.open(site_page) \
            .accept_all()
