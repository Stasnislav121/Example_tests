import testit
import allure
from library.site.site_const import *


class TestAvailabilityOfThePayerType:
    @testit.workItemIds(33827)
    @testit.externalId('TestFormCalculator_33827')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма "Выбор отправителя и получателя"')
    @testit.displayName('Доступность вариантов вида плательщика для отделения-получателя в РБ в зависимости от '
                        'признаков')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма "Выбор отправителя и получателя"')
    @allure.title('Доступность вариантов вида плательщика для отделения-получателя в РБ в зависимости от признаков')
    @allure.testcase(url='https://testit..ru/browse/33827')
    def test_availability_of_the_payer_type_for_rf_rb(self, site_main_page):
        point_rb_with_acquiring_only = '220035, Минск, проспект Машерова, 76А-2'
        point_rb_with_cash_payment_only = '223039, Минск, Минский р-н, Ждановичский с/c, 51, р-н д. Дегтяревка'
        point_rb_without_payment = '220113, Минск, ул. Мележа, 5/1'
        form_calculator = site_main_page.form_calculator()

        with allure.step('Выбрать направление РФ-РБ'):
            block_own_package = form_calculator.select_sender_city() \
                .select_receiver_country(country='Беларусь') \
                .select_receiver_city(CREATE_PARCEL_BELARUS_RECEIVER_CITY)

        with allure.step('Дозаполнить данные и дойти до формы "Выбор отделения-получателя"'):
            points_receiver_form = block_own_package.select_own_package() \
                .goto_sender_point_form() \
                .select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step()

        with allure.step(f'Выбрать отделение-получатель {CREATE_PARCEL_BELARUS_RECEIVER_POINT_ADDRESS_WITH_PAYMENT} с '
                         f'признаками acquiring = true И cash_payment = true и перейти на следующий шаг'):
            data_form = points_receiver_form \
                .select_point_from_list(CREATE_PARCEL_BELARUS_RECEIVER_POINT_ADDRESS_WITH_PAYMENT) \
                .goto_next_step()

        with allure.step('Проверить доступность выбора плательщика-получателя'):
            data_form.click_payer_receiver()

        with allure.step(f'Выбрать отделение-получатель {point_rb_with_acquiring_only} с '
                         f'признаками acquiring = true И cash_payment = false и перейти на следующий шаг'):
            data_form = data_form.goto_receiver_point_for_step() \
                .select_point_from_list(point_rb_with_acquiring_only) \
                .goto_next_step()

        with allure.step('Проверить недоступность выбора плательщика-получателя'):
            data_form.click_payer_receiver(force=True).check_payer_sender_selected()

        with allure.step(f'Выбрать отделение-получатель {point_rb_with_cash_payment_only} с '
                         f'признаками acquiring = false И cash_payment = true и перейти на следующий шаг'):
            data_form = data_form.goto_receiver_point_for_step() \
                .select_point_from_list(point_rb_with_cash_payment_only) \
                .goto_next_step()

        with allure.step('Проверить недоступность выбора плательщика-получателя'):
            data_form.click_payer_receiver(force=True).check_payer_sender_selected()

        with allure.step(f'Выбрать отделение-получатель {point_rb_without_payment} с '
                         f'признаками acquiring = false И cash_payment = false и перейти на следующий шаг'):
            data_form = data_form.goto_receiver_point_for_step() \
                .select_point_from_list(point_rb_without_payment) \
                .goto_next_step()

        with allure.step('Проверить недоступность выбора плательщика-получателя'):
            data_form.click_payer_receiver(force=True).check_payer_sender_selected()
