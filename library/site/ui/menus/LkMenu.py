import allure

from library.site.ui.pages import *


class LkMenu(BasePage):
    css_map = {
        'Для частных клиентов': '.personal-accounts__link_private-clients',
        'Мобильное приложение': '.personal-accounts__link_online-store:has-text("Мобильное приложение")',
        'Для интернет-магазинов': '.personal-accounts__link_online-store:has-text("Для интернет-магазинов")',
    }

    def open_link(self, name):
        with allure.step(f'Открыть в меню "Личный кабинет" ссылку [{name}]'):
            with self.expect_page() as page_info:
                if self.is_mobile:
                    self.click(f'#personalAccountModal {self.css_map[name]}', force=False)
                else:
                    self.click(f'.header-desktop {self.css_map[name]}', force=False)
            new_page = page_info.value

        return new_page

    def open_for_private_clients(self):
        new_page = self.open_link('Для частных клиентов')
        return BasePage(new_page)  # здесь выполняется переход на страницу другой системы

    def open_mobile_app(self):
        new_page = self.open_link('Мобильное приложение')
        return DeliveryMobileAppPage(new_page)

    def open_for_online_store(self):
        new_page = self.open_link('Для интернет-магазинов')
        return BasePage(new_page)  # здесь выполняется переход на страницу другой системы
