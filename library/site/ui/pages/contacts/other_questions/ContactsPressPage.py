import allure

from library.site.ui.pages.contacts import *
from library.site.ui import *


class ContactsPressPage(ContactsBasePage):
    page_element = '.pageTitle__title:text("Пресс-служба ")'
    page_route = '/kontakty/napisat-pis-mo-v-sluzbu-podderzki/press-sluzba-'

    def form_feedback(self):
        with allure.step('Обращение к форме "Форма обратной связи"'):
            from library.site.ui import ContactsFeedbackForm
            form = ContactsFeedbackForm(self.page)
            form.set_parent(self)
        return form
