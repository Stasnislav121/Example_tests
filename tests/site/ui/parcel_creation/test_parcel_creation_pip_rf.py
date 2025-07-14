import pytest
import testit
import allure

from library.site.site_const import *


class TestParcelCreationPipRF:
    @testit.workItemIds(13870)
    @testit.externalId('TestParcelCreation_13870')
    @testit.nameSpace('Создание посылок')
    @testit.className('РФ-РФ')
    @testit.displayName('Оформление ПиП РФ ПВЗ-ПВЗ упаковка своя')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Создание посылок')
    @allure.title('Создание посылок - Оформление ПиП РФ ПВЗ-ПВЗ упаковка своя')
    @allure.testcase(url='https://testit..ru/browse/13870')
    @pytest.mark.usefixtures("check_creation_rf_from_point_to_point_own_package")
    def test_parcel_creation_pip_rf_from_point_to_point_own_package(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            sender_form = form_calculator.select_sender_city() \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY) \
                .select_own_package() \
                .goto_sender_point_form()

        with allure.step('Выбрать отделение отправителя'):
            receiver_form = sender_form.select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Выбрать отделение получателя'):
            data_form = receiver_form.select_point_from_list(CREATE_PARCEL_RF_RECEIVER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Заполнить данные отправителя и получателя'):
            final_step_form = data_form.fill_form_payer_sender() \
                .goto_next_step()

        with allure.step('Проверить данные на финальном шаге формы'):
            final_step_form.check_parcel_created_from_point_rf()

    @testit.workItemIds(13873)
    @testit.externalId('TestParcelCreation_13873')
    @testit.nameSpace('Создание посылок')
    @testit.className('РФ-РФ')
    @testit.displayName('Оформление ПиП РФ ПВЗ-КД упаковка ББ')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Создание посылок')
    @allure.title('Создание посылок - Оформление ПиП РФ ПВЗ-КД упаковка ББ')
    @allure.testcase(url='https://testit..ru/browse/13873')
    @pytest.mark.usefixtures("check_creation_rf_from_point_to_door__package")
    def test_parcel_creation_pip_rf_from_point_to_door__package(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            sender_form = form_calculator.select_sender_city() \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY) \
                .select__package() \
                .select_from_point_to_door(street=CREATE_PARCEL_RF_COURIER_STREET) \
                .goto_sender_point_form()

        with allure.step('Выбрать отделение отправителя'):
            receiver_form = sender_form.select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step(is_kd=True)

        with allure.step('Заполнить адрес получателя'):
            data_form = receiver_form.set_flat() \
                .goto_next_step()

        with allure.step('Заполнить данные отправителя и получателя'):
            final_step_form = data_form.fill_form_payer_sender() \
                .goto_next_step()

        with allure.step('Проверить данные на финальном шаге формы'):
            final_step_form.check_parcel_created_from_point_rf()

    @testit.workItemIds(13874)
    @testit.externalId('TestParcelCreation_13874')
    @testit.nameSpace('Создание посылок')
    @testit.className('РФ-РФ')
    @testit.displayName('Оформление ПиП РФ КД-ПВЗ упаковка своя')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Создание посылок')
    @allure.title('Создание посылок - Оформление ПиП РФ КД-ПВЗ упаковка своя')
    @allure.testcase(url='https://testit..ru/browse/13874')
    @pytest.mark.usefixtures("check_creation_rf_from_door_to_point_own_package")
    def test_parcel_creation_pip_rf_from_door_to_point_own_package(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            sender_form = form_calculator.select_sender_city(CREATE_PARCEL_RF_SENDER_CITY) \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY) \
                .select_own_package() \
                .select_from_door_to_point(street=CREATE_PARCEL_RF_RETURN_POINT_STREET) \
                .goto_sender_address_form()

        with allure.step('Указать адрес отправителя и выбрать отделение для возврата'):
            receiver_form = sender_form.fill_address(street=CREATE_PARCEL_RF_RETURN_POINT_STREET) \
                .select_point_from_list(CREATE_PARCEL_RF_RETURN_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Выбрать отделение получателя'):
            data_form = receiver_form.select_point_from_list(CREATE_PARCEL_RF_RECEIVER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step('Заполнить данные отправителя и получателя'):
            final_step_form = data_form.fill_form_payer_sender() \
                .goto_next_step()

        with allure.step('Проверить данные на финальном шаге формы'):
            final_step_form.check_parcel_created_from_kd_rf()

    @testit.workItemIds(13877)
    @testit.externalId('TestParcelCreation_13877')
    @testit.nameSpace('Создание посылок')
    @testit.className('РФ-РФ')
    @testit.displayName('Оформление ПиП РФ КД-КД упаковка ББ')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Создание посылок')
    @allure.title('Создание посылок - Оформление ПиП РФ КД-КД упаковка ББ')
    @allure.testcase(url='https://testit..ru/browse/13877')
    @pytest.mark.usefixtures("check_creation_rf_from_door_to_door__package")
    def test_parcel_creation_pip_rf_from_door_to_door__package(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Заполнить данные в форме и перейти на следующий шаг оформления'):
            sender_form = form_calculator.select_sender_city(CREATE_PARCEL_RF_SENDER_CITY) \
                .select_receiver_country() \
                .select_receiver_city(CREATE_PARCEL_RF_RECEIVER_CITY) \
                .select__package() \
                .select_from_door_to_door(from_street=CREATE_PARCEL_RF_RETURN_POINT_STREET,
                                          to_street=CREATE_PARCEL_RF_COURIER_STREET, to_house='д 1') \
                .goto_sender_address_form()

        with allure.step('Заполнить адрес отправителя и выбрать отделение для возврата'):
            receiver_form = sender_form.fill_address(street=CREATE_PARCEL_RF_RETURN_POINT_STREET) \
                .select_point_from_list(CREATE_PARCEL_RF_RETURN_POINT_ADDRESS) \
                .goto_next_step(is_kd=True)

        with allure.step('Заполнить адрес получателя'):
            data_form = receiver_form.set_flat() \
                .goto_next_step()

        with allure.step('Заполнить данные отправителя и получателя'):
            final_step_form = data_form.fill_form_payer_sender() \
                .goto_next_step()

        with allure.step('Проверить данные на финальном шаге формы'):
            final_step_form.check_parcel_created_from_kd_rf()
