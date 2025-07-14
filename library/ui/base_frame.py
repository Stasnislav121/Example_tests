import allure

from library.ui.base_ui2 import BaseUI2


class BaseFrame:
    def __init__(self, frame, page):
        self.frame = frame
        self.page = page

    def fill(self, css, value, el_name=None, click=True):
        mess = f"Заполнить [элемент]=[{value}], css = {css}" if el_name is None \
            else f"Заполнить [{el_name}]=[{value}], css = {css}"
        with allure.step(f"{mess}"):
            try:
                locator = self.frame.locator(f"css={css}").nth(0)
                if click:
                    locator.click()
                locator.fill('')
                locator.fill(value.__str__())
            except Exception as ex:
                BaseUI2(self.page).screenshot('error_frame_fill')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно заполнить элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def click(self, css, force=True, position=None, el_name=None):
        mess = f"Нажать элемент, css = {css}" if el_name is None else f"Нажать [{el_name}], css = {css}"
        with allure.step(f"{mess}"):
            try:
                locator = self.frame.locator(f"css={css}").nth(0)
                locator.click(force=force, position=position)
            except Exception as ex:
                BaseUI2(self.page).screenshot('error_frame_click')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно нажать элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def wait_for_selector(self, css, state='visible'):
        try:
            locator = self.frame.locator(f"css={css}").nth(0)
            locator.wait_for(state=state)
        except Exception as ex:
            BaseUI2(self.page).screenshot('error_frame_wait_for')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно дождаться элемент по селектору = {css}:\n{error_msg}") from ex

        return self
