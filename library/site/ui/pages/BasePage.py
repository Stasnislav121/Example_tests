import os
import allure


from library.ui.base_ui2 import BaseUI2


class BasePage(BaseUI2):
    text_to_check = None
    text_to_check_element = None

    def __init__(self, page):
        super().__init__(page)
        page.set_default_timeout(40 * 1000)

        self.is_mobile = os.environ.get('IS_MOBILE')
        if self.is_mobile is None or self.is_mobile == '':
            self.is_mobile = False
        else:
            self.is_mobile = eval(self.is_mobile)

        self.base_url = "https://.ru"

    def check_page(self, screen=True):
        with allure.step(f"Базовая проверка страницы {type(self).__name__}"):
            if self.page_element != '':
                with allure.step(f"Проверка наличия элемента {self.page_element}"):
                    try:
                        self.page.wait_for_selector(self.page_element, state='attached')
                    except Exception as ex:
                        self.screenshot('error_check_page_element')
                        raise Exception(f"Функция check_page не дождалась элемента {self.page_element}: {ex.args}") \
                            from ex

            if self.text_to_check is not None and self.text_to_check_element is not None:
                with allure.step(
                        f"Проверка наличия текста {self.text_to_check} в элементе {self.text_to_check_element}"):
                    text_exist = self.inner_text(self.text_to_check_element)
                    if self.text_to_check not in text_exist:
                        self.screenshot('error_check_page_text')
                        raise Exception(
                            f"Текст не содержит в check_page по "
                            f"селектору {self.text_to_check_element}: {self.text_to_check} нет в {text_exist}")

            if screen:
                self.screenshot(type(self).__name__ + '_opened')

            self.check_error_banner()

        return self

    def open_url(self, url, timeout=None):
        url_to_open = self.base_url + url
        with allure.step(f"Открыть страницу {url_to_open}"):
            if self.page_element != '':
                try:
                    self.page.goto(self.base_url + url, timeout=timeout)
                    self.page.wait_for_selector(self.page_element, state='visible')
                except Exception as ex:
                    self.screenshot('error_open_base_url')
                    raise Exception(
                        f"Невозможно дождаться элемент по селектору {self.page_element} "
                        f"при открытии страницы: {ex.args}") from ex

        return self
