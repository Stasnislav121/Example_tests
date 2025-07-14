import testit
import allure
from library.site.site_const import *
from library.site.ui.pages import *


class TestFormPointSelectionFilterOnMap:
    @testit.workItemIds(39467)
    @testit.externalId('TestFormPointSelectionFilterOnMap_39467')
    @testit.nameSpace('Частным клиентам')
    @testit.className('Форма выбора отделения-отправителя / отделения-получателя')
    @testit.displayName('Отображение доступности фильтра приема оплаты на отделении-получателе')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Форма выбора отделения-отправителя / отделения-получателя')
    @allure.title('Форма выбора отделения-отправителя / отделения-получателя - '
                  'Отображение доступности фильтра приема оплаты на отделении-получателе')
    @allure.testcase(url='https://testit..ru/browse/39467')
    def test_form_point_selection_payer_recipient_accessibility_filter(self, site_main_page):
        form_calculator = site_main_page.form_calculator()

        with allure.step('Выбрать направление РФ-РБ'):
            block_own_package = form_calculator.select_sender_city(CREATE_PARCEL_RF_T0_CIS_SENDER_CITY) \
                .select_receiver_country('Беларусь') \
                .select_receiver_city(CREATE_PARCEL_BELARUS_RECEIVER_CITY)

        with allure.step('Дозаполнить данные и дойти до формы "Выберите отделение получателя"'):
            block_map = block_own_package.select_own_package() \
                .goto_sender_point_form() \
                .select_point_from_list(CREATE_PARCEL_RF_SENDER_POINT_ADDRESS) \
                .goto_next_step() \
                .block_map()

        with allure.step('Включить тумблер "Отделения принимают оплату при получении"'):
            cnt_points_before = block_map.switch_on_payer_recipient_accessibility_filter().get_points_in_calc_cnt()
            assert cnt_points_before > 0, 'На карте должны отображаться отделения'

        with allure.step('Выключить тумблер "Отделения принимают оплату при получении"'):
            cnt_points_after = block_map.switch_off_payer_recipient_accessibility_filter().get_points_in_calc_cnt()
            assert cnt_points_after > 0, 'На карте должны отображаться отделения'
