import allure

from library.site.ui.pages.BasePage import BasePage


class BaseBannerBlock(BasePage):
    css_slider_desktop = '.slider-desktop'
    css_slider_mobile = '.slider-mobile'
    css_slider_active = '.slider__item_active'
    css_slider_title_desktop = '.slider__itemTitle'
    css_slider_title_mobile = '.slider__itemTextWrp'
    css_navigation = '.slider__nav'
    css_point = '.slider__point'
    css_point_active = '.slider__point_active'

    def __init__(self, page):
        super().__init__(page)
        if self.is_mobile:
            self.wait_for_selector(self.css_slider_mobile)
        else:
            self.wait_for_selector(self.css_slider_desktop)

    def get_active_banner_number(self):
        with allure.step('Получить номер текущего активного баннера'):
            if self.is_mobile:
                point_locator = f"{self.css_slider_mobile} {self.css_point}"
            else:
                point_locator = f"{self.css_slider_desktop} {self.css_point}"

            number = None
            point_cnt = self.count(point_locator)
            for i in range(point_cnt):
                is_active_visible = self.is_visible(f"{point_locator}:nth-child({i + 1}){self.css_point_active}")
                if is_active_visible:
                    number = i + 1
                    return number
            allure.attach(str(number), 'Номер текущего активного баннера', allure.attachment_type.TEXT)
            if self.is_mobile:
                self.screenshot('banner', locator=self.css_slider_mobile)
            else:
                self.screenshot('banner', locator=self.css_slider_desktop)
            assert number is not None, 'Не удалось определить номер текущего активного баннера'

        return number

    def get_active_banner_title(self):
        with allure.step('Получить заголовок текущего баннера'):
            if self.is_mobile:
                css_slider_title_active = f"{self.css_slider_mobile} {self.css_slider_active} " \
                                          f" {self.css_slider_title_mobile}"
            else:
                css_slider_title_active = f"{self.css_slider_desktop} {self.css_slider_active} " \
                                          f" {self.css_slider_title_desktop}"
            slider_title_active = self.inner_text(css_slider_title_active)
            allure.attach(str(slider_title_active), 'Заголовок текущего баннера', allure.attachment_type.TEXT)
        return slider_title_active

    def click_while_change_blocked(self, number):
        with allure.step(f'Кликнуть по переключателю банера {number}'):
            if self.is_mobile:
                point = f"{self.css_slider_mobile} {self.css_point}:nth-child({number})"
                active_point = f"{self.css_slider_mobile} {self.css_point}:nth-child({number}){self.css_point_active}"
            else:
                point = f"{self.css_slider_desktop} {self.css_point}:nth-child({number})"
                active_point = f"{self.css_slider_desktop} {self.css_point}:nth-child({number}){self.css_point_active}"
            for _ in range(100):
                self.click(point, force=False)
                click_success = self.is_visible(active_point)
                if click_success:
                    break
        return self

    def get_banner_count(self):
        with allure.step('Получить количество баннеров'):
            if self.is_mobile:
                point_locator = f"{self.css_slider_mobile} {self.css_point}"
            else:
                point_locator = f"{self.css_slider_desktop} {self.css_point}"

        return self.count(point_locator)

    def click_change_button(self, number=None):
        if number is None:
            number = self.get_banner_count()  # последняя кнопка

        with allure.step(f'Нажать на {number}-ю кнопку переключения баннера'):
            if self.is_mobile:
                self.click(f"{self.css_slider_mobile} {self.css_point}:nth-child({number})", force=False)
                self.screenshot(locator=self.css_slider_mobile, name='change_button_clicked')
            else:
                self.click(f"{self.css_slider_desktop} {self.css_point}:nth-child({number})", force=False)
                self.screenshot(locator=self.css_slider_desktop, name='change_button_clicked')

        return self
