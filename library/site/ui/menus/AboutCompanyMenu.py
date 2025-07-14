from library.site.ui import *
from library.site.ui.menus.BaseMenu import BaseMenu


class AboutCompanyMenu(BaseMenu):
    css_map = {
        'Компания': {
            'Наша команда': 'a[href="/o-kompanii/kompania/komanda"]',
            'Ценности и цели': 'a[href="/o-kompanii/kompania/cennosti-i-celi"]',
            'Партнерская программа': 'a[href="/o-kompanii/kompania/partnerskaa-programma"]',
            'История': 'a[href="/o-kompanii/kompania/istoria"]',
            'Юридическая информация': 'a[href="/o-kompanii/kompania/uridiceskaa-informacia"]',
            'Тендер на закупки': 'a[href="/o-kompanii/kompania/ender-na-zakupki"]'
        },
        'Новости и акции': 'a[href="/about_us/news"]',
        ' в СМИ': 'a[href="/o-kompanii/-v-smi"]',
        'Наши вакансии': 'a[href="/ "]'
    }

    def open_our_team(self):
        self.open_submenu_desktop('Компания', 'Наша команда')
        return OurTeamPage(self.page).check_page()

    def open_values_and_goal(self):
        self.open_submenu_desktop('Компания', 'Ценности и цели')
        return ValuesAndGoalPage(self.page).check_page()

    def open_partner_program(self):
        self.open_submenu_desktop('Компания', 'Партнерская программа')
        return PartnerProgramPage(self.page).check_page()

    def open_history(self):
        self.open_submenu_desktop('Компания', 'История')
        return HistoryPage(self.page).check_page()

    def open_legal_information(self):
        self.open_submenu_desktop('Компания', 'Юридическая информация')
        return LegalInformationPage(self.page).check_page()

    def open_tender_procurement(self):
        self.open_submenu_desktop('Компания', 'Тендер на закупки')
        return TenderProcurementPage(self.page).check_page()

    def open_news_and_promotions(self):
        self.open_menu_desktop('Новости и акции')
        return NewsAndPromotionsPage(self.page).check_page()

    def open__in_media(self):
        self.open_menu_desktop(' в СМИ')
        return InMediaPage(self.page).check_page()

    def open_our_vacancies(self):
        self.open_menu_desktop('Наши вакансии')
        return OurVacanciesPage(self.page).check_page()
