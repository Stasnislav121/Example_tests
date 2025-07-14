import allure
import pytest

from library.site.ui import *
from tests.site.ui.conftest import *


@pytest.fixture
def site_ecommerce_faq(site_page):
    with allure.step('Открыть на вкладке "Интернет-магазинам" страницу раздела "FAQ"'):
        return ECommerceFaqPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_ecommerce_it_solutions(site_page):
    with allure.step('Открыть на вкладке "Интернет-магазинам" страницу раздела "IT-решения"'):
        return ITSolutionsPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_ecommerce_bonuses_from_partners(site_page):
    with allure.step('Открыть на вкладке "Интернет-магазинам" страницу раздела "Бонусы от партнеров"'):
        return ServicesBonusesFromPartnersPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_ecommerce_services_delivery_to_cis(site_page):
    with allure.step('Открыть на вкладке "Интернет-магазинам" страницу раздела "Доставка в страны СНГ"'):
        return ServicesDeliveryToCISPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_ecommerce_services_acceptance_points(site_page):
    with allure.step('Открыть на вкладке "Интернет-магазинам" страницу раздела "Пункты приема посылок от '
                     'интернет-магазинов"'):
        return ServicesAcceptancePointsPage.open(site_page) \
            .accept_all()
