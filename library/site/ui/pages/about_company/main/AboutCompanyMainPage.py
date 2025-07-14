from library.site.ui.pages.about_company import *


class AboutCompanyMainPage(AboutCompanyBasePage):
    page_element = '.pageTitle__title:text("О компании")'
    page_route = '/o-kompanii'

    @staticmethod
    def open(page):
        return AboutCompanyMainPage(page).open_url('/o-kompanii').check_page()
