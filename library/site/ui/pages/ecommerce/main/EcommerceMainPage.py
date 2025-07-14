import allure

from library.site.ui.pages.ecommerce import EcommerceBasePage


class EcommerceMainPage(EcommerceBasePage):
    page_element = '.calculator-im'
    css_banner = '.e-commerce__top__inner'
    css_banner_btn = '.e-commerce__top__btn:text("Узнать тарифы")'
    css_form_calculator = '.calculator-im'
    css_business_header = '.e-commerce__business h2:text("Подходим для бизнеса любого масштаба")'
    css_advantages_header = 'h2:text("Наши преимущества")'
    css_our_services_header = '.e-commerce__our-services h2:text("Услуги  для бизнеса")'
    css_our_map_block = '.ecommerce-map'
    css_our_clients_header = '.e-commerce__our-clients h2:text("Наши клиенты")'
    css_form_join = '#reg-form'
    page_route = '/e-commerce'

    @staticmethod
    def open(page):
        return EcommerceMainPage(page).open_url(url='/e-commerce', timeout=60000).close_modal().check_page()

    def check_page(self, screen=True):
        with allure.step('Проверить главную страницу раздела "Бизнесу"'):
            super().check_page(screen=screen)

            with allure.step('Проверить, что видим форму "Расчёт и отправка посылок для интернет-магазинов"'):
                self.wait_for_selector(self.css_form_calculator)
            with allure.step('Проверить, что видим форму "Подключитесь к "'):
                self.wait_for_selector(self.css_form_join)

            self.screenshot('EcommerceMainPage_loaded')

        return self

    def check_all_blocks(self):
        with allure.step('Проверить наличие всех блоков на главной странице раздела "Бизнесу"'):
            with allure.step('Проверить, что видим банер"'):
                self.expect_to_be_visible(self.css_banner)
            with allure.step('Проверить, что видим кнопку "Узнать тарифы"'):
                self.expect_to_be_visible(self.css_banner_btn)
            with allure.step('Проверить, что видим заголовок "Подходим для бизнеса любого масштаба"'):
                self.expect_to_be_visible(self.css_business_header)
            with allure.step('Проверить, что видим заголовок "Наши преимущества"'):
                self.expect_to_be_visible(self.css_advantages_header)
            with allure.step('Проверить, что видим заголовок "Услуги  для бизнеса"'):
                self.expect_to_be_visible(self.css_our_services_header)
            with allure.step('Проверить, что видим блок карты'):
                self.expect_to_be_visible(self.css_our_map_block)
            with allure.step('Проверить, что видим заголовок "Наши клиенты"'):
                self.expect_to_be_visible(self.css_our_clients_header)
            self.screenshot('EcommerceMainPage_loaded')
        return self

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.map.common.PointMap import PointMap
            block = PointMap(self.page)
            block.set_parent(self)
        return block

    def form_join(self):
        with allure.step('Обращение к форме "Подключитесь к "'):
            from library.site.ui import EcommerceMainJoinForm
            form = EcommerceMainJoinForm(self.page).check_element()
            form.set_parent(self)
        return form

    def form_calculator(self):
        with allure.step('Обращение к форме "Расчёт и отправка посылок для интернет-магазинов"'):
            from library.site.ui import CalculatorEcommerceForm
            form = CalculatorEcommerceForm(self.page).check_element()
            form.set_parent(self)
        return form
