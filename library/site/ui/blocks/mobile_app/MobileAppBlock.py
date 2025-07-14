import allure

from library.site.ui.pages.BasePage import BasePage


class MobileAppBlock(BasePage):
    page_element = '.mobile-app-links'
    css_title = ('.mobile-app-links__title:text("Отслеживайте доставку и оформляйте посылки в новом мобильном '
                 'приложении ")')
    css_image = '.mobile-app-stores__image-hand'
    css_link_google_play = '.mobile-app-links__item__link_google'
    css_link_app_store = '.mobile-app-links__item__link_store'
    css_link_app_gallery = '.mobile-app-links__item__link_gallery'
    css_qr_code = '.mobile-app-links__qr-code'
    url_image_iphone = 'https://storage.img.net/site-public/mobile_app'

    def check_element(self, screen=False):
        with allure.step("Проверить блок мобильного приложения"):
            super().check_element(screen=screen)
            with allure.step("Проверить, что блок загрузился"):
                self.wait_for_selector(self.page_element)
                self.screenshot('MobileAppBlock_loaded', locator=self.page_element)
        return self

    def check_mobile_app_block(self):
        with allure.step('Проверить блок раздела "мобильном приложении "'):
            with allure.step('Наличие заголовка'):
                self.wait_for_selector(self.css_title)
            with allure.step('Наличие ссылки на "Google Play"'):
                self.wait_for_selector(self.css_link_google_play)
            with allure.step('Наличие ссылки на "App Store"'):
                self.wait_for_selector(self.css_link_app_store)
            with allure.step('Наличие ссылки на "App Gallery"'):
                self.wait_for_selector(self.css_link_app_gallery)
            with allure.step('Наличие изображения'):
                img = self.get_phone_image_link()
                if self.is_mobile:
                    expected_img = f'{self.url_image_iphone}/iphone-sm.png'
                else:
                    expected_img = f'{self.url_image_iphone}/iphone.png'
                assert img == expected_img, f'Ожидалась ссылка на изображение: {expected_img}, получена: {img}'
            if not self.is_mobile:
                with allure.step('Наличие QR кода'):
                    self.wait_for_selector(self.css_qr_code)

        return self

    def goto_app_store(self):
        with allure.step('Кликнуть по ссылке на App Store и перейти на страницу сайта Apple Store'):
            with self.expect_page() as page_info:
                self.click(self.css_link_app_store)
            new_page = page_info.value
        return BasePage(new_page)

    def goto_app_gallery(self):
        with allure.step('Кликнуть по ссылке на AppGallery и перейти на страницу сайта AppGallery'):
            with self.expect_page() as page_info:
                self.click(self.css_link_app_gallery)
            new_page = page_info.value
        return BasePage(new_page)

    def click_qr_code(self):
        with allure.step('Кликнуть на QR код и обратиться к модальному окну с QR кодом'):
            self.click(self.css_qr_code)
            self.screenshot('qr_code_clicked', locator=self.page_element)
        from library.site.ui.modals.mobile_app.QRCodeModal import QRCodeModal
        return QRCodeModal(self.page).check_element()

    def get_google_play_link(self):
        with allure.step('Считать значение ссылки на Google Play'):
            return self.get_attribute(self.css_link_google_play, 'href')

    def get_app_store_link(self):
        with allure.step('Считать значение ссылки на App Store'):
            return self.get_attribute(self.css_link_app_store, 'href')

    def get_app_gallery_link(self):
        with allure.step('Считать значение ссылки на AppGallery'):
            return self.get_attribute(self.css_link_app_gallery, 'href')

    def get_phone_image_link(self):
        with allure.step('Считать ссылку на изображение телефона'):
            link = self.run_js(
                f'window.getComputedStyle(document.querySelector("{self.page_element}"), "::after")'
                f'.getPropertyValue("background-image"); ', need_result=True)
            link = link.replace('url("', '').replace('")', '')
        return link

    def get_qr_code_image(self):
        with allure.step('Считать и сохранить QR код'):
            path = self.screenshot('qr_code', locator=self.css_qr_code)
        return path
