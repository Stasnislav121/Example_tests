import testit
import allure


class TestECommerceFaqPage:
    @testit.workItemIds(12607)
    @testit.externalId('TestECommerce_12607')
    @testit.nameSpace('Интернет-магазинам')
    @testit.className('FAQ')
    @testit.displayName('Страница FAQ - Редирект по гиперссылкам')
    @allure.epic('Site ')
    @allure.feature('UI')
    @allure.story('Интернет-магазинам')
    @allure.title('Страница FAQ - Редирект по гиперссылкам')
    @allure.testcase(url='https://testit..ru/browse/12607')
    def test_ecommerce_faq_hyperlinks_redirect(self, site_ecommerce_faq):
        faq_page = site_ecommerce_faq
        data = faq_page.get_data()

        with allure.step('Проверить наличие на странице хотя бы 1 ссылки'):
            links_found = 0
            for theme in data:
                links = theme['Ссылки']
                links_found += len(links)
            assert links_found > 0, 'На странице не найдены ссылки'

        with allure.step('Перейти по ссылке и проверить страницу'):
            topic = data[0]['Ссылки'][0]
            topic_page = faq_page.goto_faq_link(topic['Ссылка']) \
                .check_page()

            data = topic_page.get_data()
            assert data['Заголовок'] == topic['Название']
            assert topic_page.get_current_url() == f"{topic_page.base_url}{topic['Ссылка']}"
