import allure
import pytest

from library.site.ui import *
from tests.site.ui.conftest import *


@pytest.fixture
def site_private_clients_faq(site_page):
    with allure.step('Открыть на вкладке "Частным клиентам" страницу раздела "FAQ"'):
        return PrivateClientsFaqPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_private_clients_delivery_tracking(site_page):
    with allure.step('Открыть на вкладке "Частным клиентам" в разделе "Доставка" подраздел "Отследить посылку"'):
        return DeliveryTrackingPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_private_clients_terms_packaging(site_page):
    with allure.step('Открыть на вкладке "Частным клиентам" в разделе "Условия" подраздел "Отправить и получить '
                     'посылку"'):
        return TermsPackagingPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_private_clients_terms_documents(site_page):
    with allure.step('Открыть на вкладке "Частным клиентам" в разделе "Условия" подраздел "Документы"'):
        return TermsDocumentsPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_private_clients_international_delivery_personal_data(site_page):
    with allure.step('Открыть на вкладке "Частным клиентам" в разделе "Международная доставка" подраздел '
                     '"Персональные данные"'):
        return InternationalDeliveryPersonalDataPage.open(site_page) \
            .accept_all()
