import allure

from library.site.ui.pages.contacts import *
from library.site.ui import *


class ContactsMainPage(ContactsBasePage):
    page_element = '.pageTitle__title:text("Контакты")'
    page_route = '/kontakty'

    @staticmethod
    def open(page):
        return ContactsMainPage(page).open_url('/kontakty').check_page()

    def form_support(self):
        with allure.step('Обращение к форме "Связаться со службой поддержки" - "Частный клиент"'):
            from library.site.ui import ContactsSupportClientForm
            form = ContactsSupportClientForm(self.page)
            form.set_parent(self)
        return form
