import allure

from library.site.ui.pages.private_clients import *
from library.site.ui import *


class PrivateClientsMainPage(PrivateClientsBasePage):
    page_element = '.calculator__title'
    css_form_calculator = '.calculator__title'
    css_form_tracking_desktop = '#item-tracking'
    css_form_tracking_mobile = '.formbar-mobile__item_tracking'

    def check_page(self, screen=False):
        with allure.step('Проверить главную страницу системы'):
            super().check_page(screen=screen)

            with allure.step('Проверить, что видим форму "Калькулятор расчета и создания посылки онлайн"'):
                self.wait_for_selector(self.css_form_calculator)

            with allure.step('Проверить, что видим форму "Отследить посылку"'):
                if self.is_mobile:
                    self.wait_for_selector(self.css_form_tracking_mobile)
                else:
                    self.wait_for_selector(self.css_form_tracking_desktop)

            self.screenshot('PrivateClientsMainPage_loaded')

        return self

    def click_close_modal(self):
        with allure.step('Кликнуть иконку закрытия модального окна'):
            self.click('.modal__close')
            self.screenshot('close_modal_clicked')
        return self

    def get_modal_error(self):
        with allure.step('Считать текст ошибки из модального окна'):
            return self.inner_text('.error-message__text')

    def prepare_for_screenshot(self):
        with allure.step('Подготовить страницу для скриншота'):
            with allure.step('Прокрутить страницу вниз частями, чтобы догрузились все элементы'):
                scroll_pause = 0.3
                modify_pause = 1
                page_height = self.get_client_height()
                for i in range(10):
                    height_to_scroll = (page_height / 10) * (i + 1)
                    self.mouse_wheel(0, height_to_scroll)
                    self.wait_for_timeout(scroll_pause)
                self.wait_loaders()

            with allure.step('Поменять название выбранного города'):
                fake_city = 'Fake'
                self.run_js(f'items = document.querySelectorAll(".town__link");'
                            f'items.forEach(element => element.innerHTML = `{fake_city}`);')
                self.wait_for_timeout(0.8)

            with allure.step('Поменять изображение в слайдере и убрать навигатор'):
                fake_image = 'http://placehold.it/120x120&text=image1'
                self.run_js(f'slides = document.querySelectorAll(".slider__image");'
                            f'slides.forEach(element => element.setAttribute("style", '
                            f'"background-image: url(\'{fake_image}\')"));'
                            f'slider_nav = document.querySelectorAll(".slider__nav");'
                            f'slider_nav.forEach(element => element.remove());')
                self.wait_for_timeout(modify_pause)

                fake_head = 'Fake'
                self.run_js(f'items = document.querySelectorAll(".slider__itemInfo");'
                            f'items.forEach(element => element.innerHTML = `{fake_head}`);')
                self.wait_for_timeout(modify_pause)

            with allure.step('Убрать контент карты'):
                map_locator = '#pointsMap > .ymaps-2-1-79-map'
                scroll_height = self.run_js('document.querySelector(".city-show").scrollHeight', need_result=True)
                self.set_scroll_top(scroll_height)
                self.wait_for_selector(map_locator)
                self.run_js(f'document.querySelector("{map_locator}").remove()')
                self.wait_for_timeout(modify_pause)

            with allure.step('Прокрутить страницу наверх'):
                self.set_scroll_top(0)
                self.wait_loaders()
                self.wait_for_timeout(3)

        return self

    # def close_survey_modal(self):
    #     def handler():
    #         self.click('.modal-leave__close')
    #     self.page.add_locator_handler(self.page.get_by_text("Мы заметили, что вы"), handler)

    def form_calculator(self):
        with allure.step('Обращение к форме "Калькулятор расчета и создания посылки онлайн"'):
            from library.site.ui import CalculatorForm
            form = CalculatorForm(self.page).check_element()
            form.set_parent(self)
        return form

    def block_banner(self):
        with allure.step('Обращение к блоку баннеров'):
            from library.site.ui import PrivateClientsBannerBlock
            form = PrivateClientsBannerBlock(self.page)
            form.set_parent(self)
        return form

    def block_form_navigation(self):
        with allure.step('Обращение к навигационному блоку'):
            from library.site.ui import PrivateClientsNavigationBar
            form = PrivateClientsNavigationBar(self.page)
            form.set_parent(self)
        return form

    def block_map(self):
        with allure.step('Обращение к блоку карты отделений'):
            from library.site.ui.blocks.map.common.PointMap import PointMap
            block = PointMap(self.page)
            block.set_parent(self)
        return block
