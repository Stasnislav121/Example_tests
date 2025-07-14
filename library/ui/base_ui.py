import io
import os
import time

import allure
from allure_commons.types import AttachmentType
from PIL import Image


class BaseUI:
    page_element = ""
    base_url = ""
    img_index = 1

    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url
        page.set_default_timeout(30 * 1000)

    def goto(self, url, timeout=None):
        with allure.step(f"Открыть урл: {url}"):
            self.page.goto(url, timeout=timeout)

        return self

    def goto_relative(self, url, timeout=None):
        self.goto(f'{self.base_url}{url}', timeout=timeout)
        return self

    def go_back(self):
        self.page.go_back()
        return self

    def run_js(self, js, need_result=False):
        with allure.step('Execute JS'):
            allure.attach(js, 'JS', AttachmentType.TEXT)
            result = self.page.evaluate(js)
            if need_result:
                return result

        return self

    def open(self):
        with allure.step(f"Открыть страницу {self.base_url}"):
            self.page.set_viewport_size({"width": 2000, "height": 1500})
            print(f"open url {self.base_url}")
            self.page.goto(self.base_url)

            if self.page_element != '':
                try:
                    self.page.wait_for_selector(self.page_element, state='visible')
                except:
                    print(f"Unable to wait selector = {self.page_element}, state = visible")
                    raise

        return self

    def wait_for_selector(self, css, state='visible', el_name=None, timeout=None):
        mess = f"Ожидаем css = {css}, state = {state}" if el_name is None \
            else f"Ожидаем {el_name}, css = {css}, state = {state}"
        with allure.step(mess):
            try:
                self.page.wait_for_selector(css, state=state, timeout=timeout)
            except Exception:
                print(f"Unable to wait selector = {css}, state = {state}")
                self.screenshot('error_waitForSelector')
                raise

        return self

    def click(self, css, el_name=None, force=True):
        mess = f"Нажать элемент, css = {css}" if el_name is None else f"Нажать [{el_name}], css = {css}"
        with allure.step(mess):
            if not force:
                self.wait_for_selector(css)
            try:
                self.page.click(css, force=force)
            except:
                print(f"Unable to click selector = {css}, force = {force}")
                self.screenshot('error_click')
                raise

        return self

    def url(self):
        return self.page.url

    def wait_for_timeout(self, seconds):
        with allure.step(f'Подождать {seconds} секунд'):
            self.page.wait_for_timeout(seconds * 1000)
        return self

    def wait_for_url(self, url, timeout=None):
        return self.page.wait_for_url(url, timeout=timeout)

    def accept_dialog(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
        return self

    def fill(self, css, value, el_name=None):
        mess = f"Заполнить [элемент]=[{value}], css = {css}" if el_name is None \
            else f"Заполнить [{el_name}]=[{value}], css = {css}"
        with allure.step(mess):
            try:
                self.page.fill(css, value)
            except:
                print(f"Unable to fill selector = {css}")
                self.screenshot('error_fill')
                raise

            return self

    def press_enter(self):
        with allure.step("Нажать Enter"):
            self.page.keyboard.press('Enter')
        return self

    def select_option(self, selector, value):
        with allure.step(f"Выбрать в поле со списоком {selector} значение {value}"):
            self.page.select_option(selector, value)
        return self

    def set_input_file(self, element, file_name):
        self.page.set_input_files(element, file_name)

    def expect_download(self):
        return self.page.expect_download()

    def get_value(self, css, name='value', wait=True):
        try:
            if wait:
                self.wait_for_selector(css)
            value = self.page.get_attribute(css, name)
        except Exception:
            print(f"Unable to fill selector = {css}")
            self.screenshot('error_fill')
            raise

        return value

    def input_value(self, css):
        return self.page.evaluate(f"() => document.querySelector('{css}').value")

    def get_value_frame(self, frame, css, name='value'):
        return self.page.frame_locator(frame).locator(css).get_attribute(name)

    def get_inner_text_frame(self, frame, css):
        return self.page.frame_locator(frame).locator(css).inner_text()

    def click_frame(self, frame, css):
        return self.page.frame_locator(frame).locator(css).click()

    def type_text(self, text):
        self.page.keyboard.type(text)

    def is_checked(self, element):
        return self.page.is_checked(element)

    def inner_text(self, css):
        self.wait_for_selector(css)
        return self.page.inner_text(css)

    def count(self, css):
        return self.page.evaluate(f"() => document.querySelectorAll('{css}').length")

    def is_visible(self, css):
        return self.page.is_visible(css)

    def set_cookies(self, cookies):
        with allure.step('Установить список cookies в текущий контекст браузера'):
            allure.attach(str(cookies), 'cookies_to_set', AttachmentType.TEXT)
            self.page.context.add_cookies(cookies)
        return self

    def reload(self):
        self.page.reload()
        return self

    def logout(self):
        with allure.step('Разлогиниться'):
            self.goto_relative('/site/logout')
        return self

    def blur(self, locator):
        with allure.step(f'Снять фокус с локатора {locator}'):
            self.page.locator(locator).blur()
        return self

    def screenshot(self, name=None, full_page=False, locator=None):
        if name is None:
            test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
            path = f"images/{BaseUI.img_index.__str__()}_img_{test_name}.png"
        else:
            path = f"images/{BaseUI.img_index}_img_{name}.png"

        if locator is None:
            try:
                img = self.page.screenshot(path=path, full_page=full_page)
            except Exception:
                time.sleep(1)
                img = self.page.screenshot(path=path, full_page=full_page)
        else:
            try:
                img = self.page.locator(locator).screenshot(path=path)
            except Exception as ex:
                self.screenshot('error_locator_screenshot')
                raise Exception(f'Невозможно создать скриншот элемента с локатором "{locator}": {ex.args}') from ex

        with open(path, "wb") as fh:
            fh.write(img)

        img_tmp = Image.open(path)
        basewidth = 1000
        if (int(img_tmp.size[0]) > int(basewidth)):
            wpercent = (basewidth / float(img_tmp.size[0]))
            hsize = int(float(img_tmp.size[1]) * float(wpercent))
            img_tmp = img_tmp.resize((basewidth, hsize), Image.ANTIALIAS)
            img_tmp.save(path)

        bytes_io = io.BytesIO()
        img_tmp.save(bytes_io, format='PNG')
        img = bytes_io.getvalue()

        allure.attach(img, path, attachment_type=AttachmentType.PNG)
        BaseUI.img_index = BaseUI.img_index + 1
        return path
