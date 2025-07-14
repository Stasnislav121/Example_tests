import os
import allure
import io
import time
import re as re
import testit as testit

from playwright.sync_api import expect
from PIL import Image
from allure_commons.types import AttachmentType


class BaseUI2:
    page_element = ""  # Уникальный элемент на странице (css селектор), который присутствует на ней и только на ней
    img_index = 1
    parent_element = None  # Родительский элемент, содержащий данный (пример: страница заказов для формы поиска)
    base_url = 'http://192.168.2.30:3000'
    data_state = None
    state_field = None

    def __init__(self, page):
        self.page = page

    @staticmethod
    def format_error(exception):
        if len(str(exception)) > 1800:
            error_msg = f"{str(exception)[:1200]}...\n{'- ' * 40}\n...{str(exception)[-600:]}"
        else:
            error_msg = str(exception)
        return error_msg

    def set_parent(self, parent):
        self.parent_element = parent
        return self

    def check_element(self, screen=True):
        with allure.step(f"Базовая проверка элемента {type(self).__name__}"):
            if self.page_element != '':
                with allure.step(f"Проверка наличия элемента {self.page_element}"):
                    try:
                        self.page.wait_for_selector(self.page_element, state='attached')
                    except Exception as ex:
                        self.screenshot('error_check_page_element')
                        error_msg = BaseUI2.format_error(ex)
                        raise Exception(
                            f"Функция check_element недождалась элемента {self.page_element}:\n{error_msg}") from ex

            if screen:
                self.screenshot(type(self).__name__ + '_opened')

            self.check_error_banner()

        return self

    def get_parent(self):
        if self.parent_element is not None:
            return self.parent_element

        raise Exception("parent элемент не назначен. Устраните ошибку в коде тестов!")

    def goto(self, url):
        with allure.step(f"Открыть урл: {url}"):
            self.page.goto(url)

        return self

    def go_back(self):
        self.page.go_back()
        return self

    def open_url(self, url):
        url_to_open = self.base_url + url
        with allure.step(f"Открыть страницу {url_to_open}"):
            self.page.set_viewport_size({"width": 2000, "height": 1000})
            if self.page_element != '':
                try:
                    self.page.goto(self.base_url + url)
                    self.page.wait_for_selector(self.page_element, state='visible')
                except Exception as ex:
                    self.screenshot('error_open_base_url')
                    error_msg = BaseUI2.format_error(ex)
                    raise Exception(f"Невозможно дождаться элемент по селектору {self.page_element} "
                                    f"при открытии страницы: {error_msg}") from ex

        return self

    def wait_for_selector(self, css, state='visible', timeout=None):
        try:
            self.page.wait_for_selector(css, state=state, timeout=timeout)
        except Exception as ex:
            self.screenshot('error_wait_for_selector')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно дождаться элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def wait_for_load_state(self, state='load'):
        try:
            self.page.wait_for_load_state(state=state)
        except Exception as ex:
            self.screenshot('error_wait_for_load_state')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно дождаться состояния загрузки страницы = {state}:\n{error_msg}") from ex

        return self

    def wait_for_timeout(self, seconds):
        with allure.step(f'Подождать {seconds} секунд'):
            self.page.wait_for_timeout(seconds * 1000)
        return self

    def wait_for_event(self, event: str):
        with allure.step(f'Подождать срабатывание события: {event}'):
            try:
                self.page.wait_for_event(event)
            except Exception as ex:
                self.screenshot('error_wait_for_event')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно дождаться срабатывания события = {event}:\n{error_msg}") from ex
        return self

    def click(self, css, el_name=None, force=True, position=None, button='left'):
        mess = f"Нажать элемент, css = {css}" if el_name is None else f"Нажать [{el_name}], css = {css}"
        with allure.step(mess):
            if not force:
                self.wait_for_selector(css)
            try:
                self.page.click(css, force=force, position=position, button=button)
            except Exception as ex:
                self.screenshot('error_click')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно нажать элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def click_locator(self, css, force=False, position=None, el_name=None):
        mess = f"Нажать элемент, css = {css}" if el_name is None else f"Нажать [{el_name}], css = {css}"
        with allure.step(f"{mess}"):
            try:
                self.page.locator(f"css={css}").click(force=force, position=position)
            except Exception as ex:
                BaseUI2(self.page).screenshot('error_click_locator')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно нажать элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def is_editable(self, css):
        mess = f"Ожидаем что элемент, css = {css} доступен для редактирования"
        with allure.step(mess):
            try:
                value = self.page.is_editable(css)
            except Exception as ex:
                self.screenshot('error_wait_for_editable')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Ошибка при поиске элемента css = {css} :\n{error_msg}") from ex
        return value

    def double_click(self, css, el_name=None, force=True):
        mess = f"Выполнить двойной клик по элементу, css = {css}" if el_name is None \
            else f"Выполнить двойной клик [{el_name}], css = {css}"
        with allure.step(mess):
            if not force:
                self.wait_for_selector(css)
            try:
                self.page.dblclick(css, force=force)
            except Exception as ex:
                self.screenshot('error_dbl_click')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно нажать элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def zoom(self, steps=5, hover_css='ymaps', zoom_in=True):
        with allure.step(f'Зум увеличение карты на {hover_css}'):
            self.hover(hover_css, 'Карта')
            for i in range(steps):
                if zoom_in:
                    self.mouse_wheel(0, -200)
                else:
                    self.mouse_wheel(0, 200)
                self.wait_for_timeout(0.2)
                self.screenshot(f'zoom_{i}')

        return self

    def hover(self, css, el_name=None, force=False):
        mess = f"Навести курсор на элемент, css = {css}" if el_name is None \
            else f"Навести курсор на элемент [{el_name}], css = {css}"
        with allure.step(mess):
            try:
                self.page.hover(css, force=force)
            except Exception as ex:
                self.screenshot('error_hover')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно навести курсор на элемент по селектору = {css}:\n{error_msg}") from ex

        return self

    def run_js(self, js, need_result=False):
        with allure.step('Execute JS'):
            allure.attach(js, 'JS', AttachmentType.TEXT)
            result = self.page.evaluate(js)
            if need_result:
                return result

        return self

    def fill(self, css, value, el_name=None, click=True):
        mess = f"Заполнить [элемент]=[{value}], css = {css}" if el_name is None \
            else f"Заполнить [{el_name}]=[{value}], css = {css}"
        with allure.step(mess):
            try:
                if click:
                    self.page.click(css)
                self.page.fill(css, '')
                self.page.fill(css, value.__str__())
            except Exception as ex:
                self.screenshot('error_fill')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно заполнить элемент по селектору = {css}:\n{error_msg}") from ex

            return self

    def select_option(self, css, element=None, index=None, value=None, label=None, return_selected=False, force=False):
        mess = (f"Выбрать в селекторе css = {css} опции: [element]={element}, [index]={index}, [value]={value}, "
                f"[label]={label}")
        with allure.step(mess):
            try:
                option_values = self.page.select_option(css, element=element, index=index, value=value, label=label,
                                                        force=force)
                if return_selected:
                    return option_values
            except Exception as ex:
                self.screenshot('error_select_option')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно выбрать опции в селекторе = {css}:\n{error_msg}") from ex

            return self

    def set_input_file(self, css, file_name, el_name=None):
        mess = f"Установить файл: {file_name} для элемента, css = {css}" if el_name is None \
            else f"Установить файл: {file_name} для элемента [{el_name}], css = {css}"
        with allure.step(mess):
            try:
                self.page.set_input_files(css, file_name)
            except Exception as ex:
                self.screenshot('error_set_input_file')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f"Невозможно установить файл для элемента по селектору = {css}:\n{error_msg}") from ex

            return self

    def set_checked(self, css, checked=True, el_name=None):
        mess = f"Проставить checked = {checked} для элемента, css = {css}" if el_name is None \
            else f"Проставить checked = {checked} для элемента [{el_name}], css = {css}"
        with allure.step(mess):
            try:
                self.page.set_checked(css, checked)
            except Exception as ex:
                self.screenshot('error_set_checked')
                error_msg = BaseUI2.format_error(ex)
                raise Exception(
                    f"Невозможно проставить checked для элемента по селектору = {css}:\n{error_msg}") from ex

            return self

    def get_value(self, css):
        try:
            value = self.page.get_attribute(css, 'value')
        except Exception as ex:
            self.screenshot('error_get_value')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно прочитать аттрибут value по селектору = {css}:\n{error_msg}") from ex

        return value

    def get_attribute(self, css, attribute):
        try:
            value = self.page.get_attribute(css, attribute)
        except Exception as ex:
            self.screenshot('error_get_attribute')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно прочитать аттрибут {attribute} по селектору = {css}:\n{error_msg}") from ex

        return value

    def get_current_url(self):
        return self.page.url

    def inner_text(self, css, wait=True, timeout=500):
        if wait:
            self.add_text_to_log('wait')
            self.wait_for_selector(css)
        self.add_text_to_log('get_text')
        return self.page.inner_text(css, timeout=timeout)

    def count(self, css):
        return self.page.evaluate(f"() => document.querySelectorAll('{css}').length")

    def input_value(self, css):
        return self.page.evaluate(f"() => document.querySelector('{css}').value")

    def get_client_height(self):
        with allure.step("Получить высоту страницы в пикселях"):
            return self.page.evaluate("() => document.documentElement.clientHeight")

    def get_scroll_top(self):
        with allure.step("Получить количество пикселей, прокрученных от верха страницы"):
            return self.page.evaluate("() => document.documentElement.scrollTop")

    def set_scroll_top(self, value):
        with allure.step(f"Установить {value} пикселей, прокрученных от верха страницы"):
            self.page.evaluate(f"() => document.documentElement.scrollTop = {value}")
        return self

    def reload(self):
        with allure.step("Рефреш страницы"):
            self.page.reload()
        return self

    def get_data(self):
        raise Exception('Функционал get_data не реализован для ' + type(self).__name__)

    def get_data_not_full(self):
        raise Exception('Функционал get_data_ot_full не реализован для ' + type(self).__name__)

    def wait_for_state_updated(self, full=True, wait=30, timeout=1):
        updated = False
        with allure.step("Ждем обновления данных"):
            while wait > 0:
                time.sleep(timeout)
                try:
                    if full:
                        new_data_state = self.get_data()
                    else:
                        new_data_state = self.get_data_not_full()
                    if self.state_field is not None:
                        if self.data_state[self.state_field] != new_data_state[self.state_field]:
                            self.data_state = new_data_state
                            updated = True
                            break
                    elif self.data_state != new_data_state:
                        self.data_state = new_data_state
                        updated = True
                        break
                except Exception:
                    pass
                wait = wait - 1

        self.check_error_banner()
        if updated:
            self.screenshot('data_updated')
            return self

        self.screenshot('error_wait_for_state_updated')
        raise Exception('Не дождались изменений данных')

    def save_state(self):
        with allure.step("Ждем обновления данных"):
            self.data_state = self.get_data()

    def check_error_banner(self):
        with allure.step("Проверка отсутствия баннера с JS ошибкой"):
            js_banner_exist = self.count("nextjs-portal") > 0
            if js_banner_exist:
                self.screenshot('js_banner')
            assert js_banner_exist is False, "Проверка отсутствия баннера с JS ошибкой"

        return self

    def is_hidden(self, css):
        with allure.step(f'Проверить, что элемент {css} не отображается на странице'):
            return self.page.is_hidden(css)

    def is_visible(self, css):
        with allure.step(f'Проверить, что элемент {css} отображается на странице'):
            return self.page.is_visible(css)

    def screenshot(self, name=None, full_page=False, locator=None):
        from slugify import slugify
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        test_name = slugify(test_name)

        if name is None:
            path = f"images/{BaseUI2.img_index.__str__()}_img_{test_name}.png"
        else:
            path = f"images/{BaseUI2.img_index}_img_{test_name}{name}.png"

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
                error_msg = BaseUI2.format_error(ex)
                raise Exception(f'Невозможно создать скриншот элемента с локатором "{locator}":\n{error_msg}') from ex

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
        BaseUI2.img_index = BaseUI2.img_index + 1

        return path

    def add_text_to_log(self, text):
        return
        # use for debug purposes
        from datetime import datetime
        now = datetime.now().time()
        with open("/code/-to-commit/logs/debug.log", "a") as file1:
            file1.write(f"{now}: {text} \n")

    def mouse_click(self, x, y):
        mess = f'Выполнить клик по координатам страницы (x, y): {x, y}'
        try:
            with allure.step(mess):
                self.page.mouse.click(x, y)
        except Exception as ex:
            self.screenshot('error_mouse_click')
            raise Exception(f"Невозможно выполнить клик по координатам страницы (x, y):{ex.args}") from ex

        return self

    def drag_and_drop(self, x1, y1, x2, y2):
        mess = f'Сделать drag & drop ({x1}, {y1}) => ({x2}, {y2})'
        try:
            with allure.step(mess):
                self.page.mouse.move(x1, y1)
                self.page.mouse.down()
                self.page.mouse.move(x2, y2)
                self.page.mouse.up()
                # self.wait_for_timeout(1)
                self.screenshot('dragged')
        except Exception as ex:
            self.screenshot('error_drag_and_drop')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно выполнить drag & drop ({x1}, {y1}) => ({x2}, {y2}):\n{error_msg}") from ex

        return self

    def mouse_double_click(self, x, y):
        mess = f'Выполнить двойной клик по координатам страницы (x, y): {x, y}'
        try:
            with allure.step(mess):
                self.page.mouse.dblclick(x, y)
        except Exception as ex:
            self.screenshot('error_mouse_click')
            error_msg = BaseUI2.format_error(ex)
            raise Exception(f"Невозможно выполнить двойной клик по координатам страницы (x, y):\n{error_msg}") from ex

        return self

    def mouse_hover(self, css):
        with allure.step(f"Навести мышь на элемент {css}"):
            self.page.hover(css)

        return self

    def mouse_wheel(self, x, y):
        with allure.step(f"Прокрутить страницу горизонтально: на {x} пикселей, вертикально: на {y} пикселей"):
            self.page.mouse.wheel(x, y)

        return self

    def key_press(self, key):
        with allure.step(f'Нажать "{key}" на клавиатуре'):
            self.page.keyboard.press(key)
        return self

    def key_down(self, key):
        with allure.step(f'Зажать "{key}" на клавиатуре'):
            self.page.keyboard.down(key)
        return self

    def key_up(self, key):
        with allure.step(f'Отпустить "{key}" на клавиатуре'):
            self.page.keyboard.up(key)
        return self

    def key_press_locator(self, css, key):
        with allure.step(f'Нажать "{key}" на локаторе css={css}'):
            self.page.locator(f"css={css}").press(key)
        return self

    def press_sequentially(self, css, value, delay=0):
        with allure.step(f'Ввести последовательность "{value}" на локаторе css={css}'):
            self.page.locator(f"css={css}").press_sequentially(value, delay=delay)
        return self

    def accept_dialog_on(self):
        with allure.step('Запустить обработчик диалоговых окон'):
            self.page.on("dialog", lambda dialog: dialog.accept())
        return self

    def accept_dialog_once(self):
        with allure.step('Принять диалоговое окно'):
            self.page.once("dialog", lambda dialog: dialog.accept())
        return self

    def dismiss_dialog_once(self):
        with allure.step('Отклонить диалоговое окно'):
            self.page.once("dialog", lambda dialog: dialog.dismiss())
        return self

    def get_browser_name(self):
        with allure.step('Получить название текущего браузера'):
            return self.page.context.browser.browser_type.name

    def get_cookies(self):
        with allure.step('Получить список cookies из текущего контекста браузера'):
            cookies = self.page.context.cookies()
            allure.attach(str(cookies), 'cookies', AttachmentType.TEXT)
        return cookies

    def set_cookies(self, cookies):
        with allure.step('Установить список cookies в текущий контекст браузера'):
            allure.attach(str(cookies), 'cookies_to_set', AttachmentType.TEXT)
            self.page.context.add_cookies(cookies)
        return self

    def clear_cookies(self):
        with allure.step('Очистить список cookies для текущего контекста браузера'):
            self.page.context.clear_cookies()
        return self

    def set_extra_http_headers(self, headers: dict):
        with allure.step('Установить дополнительные заголовки в текущий контекст браузера'):
            allure.attach(str(headers), 'headers_to_set', AttachmentType.JSON)
            self.page.context.set_extra_http_headers(headers)
        return self

    def add_locator_handler(self, css, handler, no_wait_after=None, times=None):
        self.page.add_locator_handler(self.page.locator(f"css={css}"), handler, no_wait_after=no_wait_after,
                                      times=times)

    def remove_locator_handler(self, css):
        self.page.remove_locator_handler(self.page.locator(f"css={css}"))

    def expect_request(self, url_or_predicate):
        return self.page.expect_request(url_or_predicate)

    def expect_request_finished(self, url_or_predicate):
        return self.page.expect_request_finished(url_or_predicate)

    def expect_response(self, url_or_predicate):
        return self.page.expect_response(url_or_predicate)

    def expect_download(self):
        return self.page.expect_download()

    def expect_page(self):
        return self.page.context.expect_page()

    def expect_to_be_visible(self, css, el_name=None, timeout=10):
        step_msg = f'Ожидание, что элемент css = {css} будет отображаться на странице' if el_name is None \
            else f'Ожидание, что [{el_name}], css = {css} будет отображаться на странице'
        with allure.step(step_msg):
            err_msg = f'Невозможно дождаться отображения элемента css = {css}:' if el_name is None \
                else f'Невозможно дождаться отображения [{el_name}], css = {css}:'
            expect(self.page.locator(f"css={css}"), err_msg) \
                .to_be_visible(timeout=timeout * 1000)
        return self

    def expect_to_be_hidden(self, css, el_name=None, timeout=10):
        step_msg = f'Ожидание, что элемент css = {css} будет скрыт на странице' if el_name is None \
            else f'Ожидание, что [{el_name}], css = {css} будет скрыт на странице'
        with allure.step(step_msg):
            err_msg = f'Невозможно дождаться скрытия элемента css = {css}:' if el_name is None \
                else f'Невозможно дождаться скрытия [{el_name}], css = {css}:'
            expect(self.page.locator(f"css={css}"), err_msg) \
                .to_be_hidden(timeout=timeout * 1000)
        return self

    def expect_to_be_checked(self, css, el_name=None, checked=True, timeout=10):
        step_msg = f'Ожидание состояния [checked={checked}] элемента css = {css}' if el_name is None \
            else f'Ожидание состояния [checked={checked}] [{el_name}], css = {css}'
        with allure.step(step_msg):
            err_msg = f'Невозможно дождаться состояния [checked={checked}] элемента css = {css}:' if el_name is None \
                else f'Невозможно дождаться состояния [checked={checked}] [{el_name}], css = {css}:'
            expect(self.page.locator(f"css={css}"), err_msg) \
                .to_be_checked(checked=checked, timeout=timeout * 1000)
        return self

    def expect_to_have_attribute(self, css, attribute, value, el_name=None, ignore_case=False, timeout=10):
        step_msg = f'Ожидание, что аттрибут [{attribute}] будет иметь значение [{value}] у элемента css = {css}' \
            if el_name is None \
            else (f'Ожидание, что аттрибут [{attribute}] будет иметь значение [{value}] у элемента [{el_name}], '
                  f'css = {css}')
        with allure.step(step_msg):
            err_msg = f'Невозможно дождаться значения [{value}] аттрибута [{attribute}] у элемента css = {css}:' \
                if el_name is None \
                else (f'Невозможно дождаться значения [{value}] аттрибута [{attribute}] у элемента [{el_name}]:, '
                      f'css = {css}\n')
            expect(self.page.locator(f"css={css}"), err_msg) \
                .to_have_attribute(attribute, value, ignore_case=ignore_case, timeout=timeout * 1000)
        return self

    def expect_to_have_url(self, url_or_reg_exp, timeout=10):
        with allure.step(f'Ожидание на странице URL или RegExp: [{url_or_reg_exp}]'):
            err_msg = f'Невозможно дождаться на странице URL или RegExp: [{url_or_reg_exp}]:'
            expect(self.page, err_msg).to_have_url(url_or_reg_exp=url_or_reg_exp, timeout=timeout * 1000)
        return self

    def on(self, event, handler):
        return self.page.on(event, handler)

    def clock_fast_forward(self, ticks: int or str):
        if type(ticks) is int:
            step_msg = f'Перевести часы вперед немедленно на {ticks} секунд'
            ticks = ticks * 1000
        else:
            step_msg = f'Перевести часы вперед немедленно на время: {ticks}'
        with allure.step(step_msg):
            self.page.clock.fast_forward(ticks)
        return self

    def clock_run_for(self, ticks: int or str):
        if type(ticks) is int:
            step_msg = f'Перевести часы вперед вручную на {ticks} секунд'
            ticks = ticks * 1000
        else:
            step_msg = f'Перевести часы вперед вручную на время: {ticks}'
        with allure.step(step_msg):
            self.page.clock.run_for(ticks)
        return self

    def frame(self, css):
        with allure.step(f'Обращение к iframe по селектору = {css}'):
            from library.ui.base_frame import BaseFrame
            frame = BaseFrame(frame=self.page.frame_locator(f"css={css}"), page=self.page)
        return frame
