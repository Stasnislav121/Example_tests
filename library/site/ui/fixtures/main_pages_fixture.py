import allure
import pytest

from library.site.ui import *
from tests.site.ui.conftest import *


@pytest.fixture
def site_main_page(site_page):
    with allure.step('Открыть главную страницу сайта'):
        return HomePage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_ecommerce_page(site_page):
    with allure.step('Открыть главную страницу раздела "Интернет-магазинам"'):
        return EcommerceMainPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_contacts_page(site_page):
    with allure.step('Открыть главную страницу раздела "Контакты"'):
        return ContactsMainPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_business_partners_page(site_page):
    with allure.step('Открыть главную страницу раздела "Бизнес-партнерам"'):
        return BusinessPartnersMainPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_international_delivery_page(site_page):
    with allure.step('Открыть главную страницу раздела "International delivery"'):
        return InternationalDeliveryMainPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_about_company_page(site_page):
    with allure.step('Открыть главную страницу раздела "О компании"'):
        return AboutCompanyMainPage.open(site_page) \
            .accept_all()


@pytest.fixture
def site_find_an_office(site_page):
    with allure.step('Открыть страницу "Найти отделение в "'):
        return FindOfficePage.open(site_page) \
            .accept_all()
