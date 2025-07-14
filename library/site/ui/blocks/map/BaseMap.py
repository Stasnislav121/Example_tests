import allure

from library.site.ui.pages.BasePage import BasePage


class BaseMap(BasePage):
    css_cluster_icon = '.ymaps-2-1-79-svg-icon'
    css_point_icon = '.ymaps-2-1-79-image'
    css_address_input = '.ymaps-2-1-79-searchbox-input__input'
    css_search = '.ymaps-2-1-79-searchbox-button-text'
    css_close_address = '.ymaps-2-1-79-balloon__close'
    css_address_card = '.ymaps-2-1-79-islets_card'
    css_address_block = '.ymaps-2-1-79-balloon'
    css_calc_map_locator = '.calculator-map-content'

    def search_point(self, address='микрорайон Пронина, 8, Звенигород'):
        with allure.step(f'Поиск отделения по адресу: {address}'):
            self.set_search_address(address)
            self.click_search()
            self.wait_for_selector('.ymaps-2-1-79-islets_card')
            self.remove_address_card()
        return self

    def click_search(self):
        with allure.step('Кликнуть на кнопку "Найти"'):
            self.click(self.css_search, force=False)
        return self

    def click_close_address_card(self):
        with allure.step('Кликнуть на иконку закрытия карточки адреса'):
            self.click(self.css_close_address, force=False)
            self.wait_for_selector('.ymaps-2-1-79-islets_card', state='detached')
        return self

    def click_first_suggestion(self, value):
        with allure.step(f'Кликнуть в дропдауне поля "Введите ваш адрес" на начальное предложенное значение: {value}'):
            self.click(f".ymaps-2-1-79-search__suggest [id] > ymaps > ymaps:has-text('{value}')")
        return self

    def click_second_suggestion(self, value):
        with allure.step(f'Кликнуть в дропдауне поля "Введите ваш адрес" на значение после выбора адреса: {value}'):
            self.click(f".ymaps-2-1-79-islets_serp-popup [id] > ymaps > ymaps:has-text('{value}')")
        return self

    def set_search_address(self, address):
        with allure.step(f'Установить в поле "Введите ваш адрес" значение: {address}'):
            if self.is_mobile:
                with allure.step('Раскрыть поисковую строку, если она скрыта'):
                    for _ in range(10):
                        search_open_btn_visible = self.is_visible('.ymaps-2-1-79-float-button-text')
                        if search_open_btn_visible:
                            self.click('.ymaps-2-1-79-float-button-text', force=False)  # раскрыть поисковую строку
                            break
                        self.wait_for_timeout(0.1)
                self.fill(self.css_address_input, address)
            else:
                self.fill(self.css_address_input, address)
                # self.wait_for_selector('.ymaps-2-1-79-search__suggest')
        return self

    def get_first_search_suggestions(self):
        with allure.step('Считать начальные предложенные значения из дропдауна поля "Введите ваш адрес"'):
            suggestions = []
            cnt = self.count('.ymaps-2-1-79-suggest-item')
            for i in range(cnt):
                sug = self.inner_text(
                    f'.ymaps-2-1-79-search__suggest [id] .ymaps-2-1-79-suggest-item:nth-child({i + 1})')
                suggestions.append(sug)
            allure.attach(str(sug), 'Дропдаун поля "Введите ваш адрес"', allure.attachment_type.JSON)

        return suggestions

    def get_second_search_suggestions(self):
        with allure.step('Считать предложенные значения после выбора адреса из дропдауна поля "Введите ваш адрес"'):
            suggestions = []
            cnt = self.count('.ymaps-2-1-79-islets_serp-item')
            for i in range(cnt):
                sug = self.inner_text(f'.ymaps-2-1-79-islets_serp-popup [id] > ymaps > ymaps:nth-child({i + 1})')
                suggestions.append(sug)
            allure.attach(str(sug), 'Дропдаун поля "Введите ваш адрес"', allure.attachment_type.JSON)

        return suggestions

    def get_points_cnt(self):
        with allure.step('Считать данные на карте'):
            points = self.count(f"{self.css_point_icon}")

            points_in_clusters = self.run_js("clusters = document.querySelectorAll('.ymaps-2-1-79-svg-icon-content');"
                                             "cnt = 0;"
                                             "clusters.forEach(element => cnt += Number(element.textContent));"
                                             "cnt;",
                                             need_result=True)
            cnt = int(points) + int(points_in_clusters)

        return cnt

    def get_points_in_calc_cnt(self):
        with allure.step('Считать данные на карте в калькуляторе'):
            points = self.count(f"{self.css_calc_map_locator} {self.css_point_icon}")
            points_in_clusters = self.run_js(f"clusters = document.querySelectorAll('{self.css_calc_map_locator} "
                                             f"{self.css_cluster_icon}');"
                                             "cnt = 0;"
                                             "clusters.forEach(element => cnt += Number(element.textContent));"
                                             "cnt;",
                                             need_result=True)
            cnt = int(points) + int(points_in_clusters)

        return cnt

    def remove_address_card(self):
        with allure.step('Удалить карточку адреса через JS'):
            self.wait_for_selector(self.css_address_block)
            self.run_js(f'document.querySelector("{self.css_address_block}").remove()')
            self.wait_for_selector('.ymaps-2-1-79-islets_card', state='detached')
        return self
