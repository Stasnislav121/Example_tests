import allure

from library.site.site_const import *
from library.site.ui.pages.BasePage import BasePage
from library.site.ui.pages import TermsDocumentsPage


class SenderAndReceiverDataForm(BasePage):
    page_element = '.calc__content'
    css_title = '.calculator__title:text("Данные отправителя и получателя")'
    css_sender_name = '[placeholder="ФИО отправителя"]'
    css_sender_phone = '.calculator__col:nth-child(1) [type="phone"]'
    css_sender_passport = 'input[placeholder="Номер паспорта"]'
    css_sender_email = '#sender-email'
    css_recipient_name = '[placeholder="ФИО получателя"]'
    css_recipient_phone = '.calculator__col:nth-child(2) [type="phone"]'
    css_personal_agreement = '[for="personal_agreement"]'
    css_prohibited_goods = '[for="document_agreement"]'
    css_payer_sender = '.calc-radio-btn__name:text("Отправитель")'
    css_payer_receiver = '.calc-radio-btn__name:text("Получатель")'
    css_continue = '.calculator__button_next-step'
    css_back = '.calculator__button_back-step'
    css_all_right = '.receiver-accept__btn'
    css_agreed = '.warning__btn'
    css_attachment_description = '.multiselect'

    def __init__(self, page):
        super().__init__(page)
        self.wait_for_selector(self.css_title)
        self.screenshot('SenderAndReceiverDataForm_loaded', locator=self.page_element)
        self.wait_for_timeout(1)

    def click_personal_agreement(self):
        with allure.step('Кликнуть в чек-бокс "Ознакомлен с политикой персональных данных"'):
            self.wait_for_selector(self.css_personal_agreement)
            self.click(self.css_personal_agreement, position={'x': 10, 'y': 10}, force=False)
            self.screenshot('personal_agreement_clicked', locator=self.page_element)
        return self

    def click_prohibited_goods(self):
        with allure.step('Кликнуть в чек-бокс "Ознакомлен со списком запрещенных к перевозке грузов"'):
            self.wait_for_selector(self.css_prohibited_goods)
            self.click(self.css_prohibited_goods, position={'x': 10, 'y': 10}, force=False)
            self.screenshot('prohibited_goods_clicked', locator=self.page_element)
        return self

    def click_payer_sender(self):
        with allure.step('Кликнуть в блоке "Кто платит за доставку" в чек-бокс "Отправитель"'):
            self.wait_for_selector(self.css_payer_sender)
            self.click(self.css_payer_sender, force=False)
            self.screenshot('payer_sender_clicked', locator=self.page_element)
        return self

    def click_payer_receiver(self, force=False):
        with allure.step('Кликнуть в блоке "Кто платит за доставку" в чек-бокс "Получатель"'):
            self.wait_for_selector(self.css_payer_receiver)
            self.page.locator(self.css_payer_receiver).click(force=force)
            self.screenshot('payer_receiver_clicked', locator=self.page_element)
        return self

    def check_payer_sender_selected(self):
        with allure.step('Проверить, что выбран плательщик-отправитель'):
            return self.expect_to_be_visible(f'.active:has({self.css_payer_sender})')

    def check_payer_receiver_selected(self):
        with allure.step('Проверить, что выбран плательщик-получатель'):
            return self.expect_to_be_visible(f'.active:has({self.css_payer_receiver})')

    def click_next(self):
        with allure.step('Кликнуть на кнопку "Далее"'):
            self.click(f"{self.css_continue}", 'Далее', force=False)
        return self

    def click_back(self):
        with allure.step('Кликнуть на кнопку "Назад"'):
            self.click(f"{self.css_back}", 'Назад', force=False)
        return self

    def set_sender_data(self, name=SENDER_NAME_RU, phone='99999999999', email='autotest_site@.ru'):
        with allure.step(f'Заполнить данные отправителя значениями: ФИО = {name}, телефон = {phone}, email = {email}'):
            self.set_sender_name(name) \
                .set_sender_phone(phone) \
                .set_sender_email(email)
        return self

    def set_sender_data_cis(self, name=SENDER_NAME_RU, phone='99999999999', email='autotest_site@.ru',
                            passport='12345678'):
        with allure.step(f'Заполнить данные отправителя значениями: ФИО = {name}, телефон = {phone}, email = {email}'):
            self.set_sender_name(name) \
                .set_sender_phone(phone) \
                .set_sender_email(email) \
                .set_sender_passport(passport)
        return self

    def set_sender_name(self, name):
        with allure.step(f'Заполнить поле "ФИО отправителя" значением: {name}'):
            self.fill(self.css_sender_name, name)
            self.screenshot('sender_name_set', locator=self.page_element)
        return self

    def set_sender_phone(self, phone):
        with allure.step(f'Заполнить поле "Телефон отправителя" значением: {phone}'):
            self.click(self.css_sender_phone)
            for letter in phone:
                self.key_press(letter)
            self.screenshot('sender_phone_set', locator=self.page_element)
        return self

    def set_sender_email(self, email):
        with allure.step(f'Заполнить поле "Эл. почта" значением: {email}'):
            self.fill(self.css_sender_email, email)
            self.screenshot('sender_email_set', locator=self.page_element)
        return self

    def set_sender_passport(self, number):
        with allure.step(f'Заполнить поле "Паспортные данные отправителя" значением: {number}'):
            self.fill(self.css_sender_passport, number)
            self.screenshot('sender_passport_set', locator=self.page_element)
        return self

    def set_receiver_data(self, name=RECEIVER_NAME_RU, phone='99999999999'):
        with allure.step(f'Заполнить данные получателя значениями: ФИО = {name}, телефон = {phone}'):
            self.set_receiver_name(name) \
                .set_receiver_phone(phone)
        return self

    def set_receiver_name(self, name):
        with allure.step(f'Заполнить поле "ФИО получателя" значением: {name}'):
            self.fill(self.css_recipient_name, name)
            self.screenshot('receiver_name_set', locator=self.page_element)
        return self

    def set_receiver_phone(self, phone):
        with allure.step(f'Заполнить поле "Телефон получателя" значением: {phone}'):
            self.click(self.css_recipient_phone)
            for letter in phone:
                self.key_press(letter)
            self.screenshot('receiver_phone_set', locator=self.page_element)
        return self

    def select_attachments(self, categories=None):
        if categories is None:
            categories = ['Медикаменты и БАДы']
        with allure.step(f'Выбрать в поле "Описание вложения" категории: {categories}'):
            self.click(self.css_attachment_description, force=False)
            for category in categories:
                self.click(f'.multiselect__element span:text("{category}")', force=False)
            self.key_press('Escape')
            self.screenshot('attachments_selected', locator=self.page_element)
        return self

    def fill_form_payer_sender(self):
        with allure.step('Заполнить форму с плательщиком отправителем'):
            self.set_sender_data() \
                .set_receiver_data() \
                .click_payer_sender() \
                .click_personal_agreement() \
                .click_prohibited_goods()

        return self

    def fill_form_payer_receiver(self):
        with allure.step('Заполнить форму с плательщиком получателем'):
            self.set_sender_data() \
                .set_receiver_data() \
                .click_payer_receiver() \
                .click_personal_agreement() \
                .click_prohibited_goods()
        return self

    def fill_form_payer_receiver_cis(self):
        with allure.step('Заполнить форму с плательщиком получателем с отправкой из страны СНГ'):
            self.set_sender_data_cis() \
                .set_receiver_data() \
                .click_payer_receiver() \
                .click_personal_agreement() \
                .select_attachments()
            return self

    def fill_form_without_payer_cis(self):
        with allure.step('Заполнить форму из страны СНГ в страну СНГ без выбора плательщика'):
            self.set_sender_data_cis() \
                .set_receiver_data() \
                .click_personal_agreement() \
                .select_attachments()
            return self

    def fill_form_payer_sender_cis(self):
        with allure.step('Заполнить форму с плательщиком отправителем с отправкой из страны СНГ'):
            self.set_sender_data_cis() \
                .set_receiver_data() \
                .click_payer_sender() \
                .click_personal_agreement() \
                .select_attachments()
            return self

    def fill_form_payer_sender_custom(self):
        with allure.step('Заполнить форму с плательщиком отправителем для страны-получателя с таможней'):
            self.set_sender_data(name=SENDER_NAME_EN) \
                .set_receiver_data(name=RECEIVER_NAME_EN) \
                .click_payer_sender() \
                .click_personal_agreement() \
                .click_prohibited_goods()
        return self

    def click_url_in_label_personal_agreement(self):
        with allure.step('Кликнуть по словам "Я согласен на обработку персональных данных и с Офертой Боксберри"'):
            with self.expect_page() as document_page:
                self.click(f'{self.css_personal_agreement} '
                           f' a:text("Я согласен на обработку персональных данных и с Офертой Боксберри")', force=False)
            new_page = document_page.value
        return TermsDocumentsPage(new_page).check_page()

    def click_url_in_label_prohibited_goods(self):
        with allure.step('Кликнуть по словам "запрещенных к перевозке грузов"'):
            with self.expect_page() as document_page:
                self.click(f'{self.css_prohibited_goods} '
                           f' a:text("запрещенных к перевозке грузов")', force=False)
            new_page = document_page.value
        return TermsDocumentsPage(new_page).check_page()

    def goto_next_step(self, confirm_name=False, confirm_warning=False, to_custom=False, cis_sender_payer=False):
        with allure.step('Перейти к следующему шагу формы'):
            self.click_next()

            if confirm_name:
                self.click(f"{self.css_all_right}", 'Все правильно', force=False)
            if confirm_warning:
                self.click(f"{self.css_agreed}", 'Договорились', force=False)

            self.screenshot('goto_next_step')

            if to_custom:
                from library.site.ui import ParcelCreatingCustomForm
                form = ParcelCreatingCustomForm(self.page).check_element()
            elif cis_sender_payer:
                from library.site.ui import PaymentSelectionCisForm
                form = PaymentSelectionCisForm(self.page).check_element()
            else:
                from library.site.ui import ParcelCreatedForm
                form = ParcelCreatedForm(self.page).check_element()

        return form

    def goto_receiver_point_for_step(self):
        with allure.step('Кликнуть на кнопку "Далее" и перейти к форме выбора получателя'):
            self.click_back()
            from library.site.ui import ReceiverPointForm
            form = ReceiverPointForm(self.page)
            form.set_parent(self.get_parent())

        return form
