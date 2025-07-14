import allure
import testit
from library.mobapp import *


class TestFeedbackTopics:
    @testit.workItemIds(17732)
    @testit.externalId('TestFeedbackTopics_17732')
    @testit.displayName('[200] GET /feedback/topics - получение списка тем для отзыва')
    @testit.nameSpace('API')
    @testit.className('Feedback')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Feedback')
    @allure.title('[200] GET /feedback/topics - получение списка тем для отзыва')
    @allure.testcase(url='https://testit..ru/browse/17732')
    def test_get_feedback_topics(self):
        expect_topics = FeedbackHelper.get_feedback_topics_with_show_on_list()

        with allure.step('Выполнить GET /feedback/topics'):
            client = FeedbackApi()
            response = client.get_feedback_topics()

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, feedback_topic_schema)

        with allure.step('Проверка параметров ответа'):
            actual_topics_resp = response.json()['data']['items']
            assert expect_topics == actual_topics_resp, f'Ожидалось равенство с {expect_topics}, \
             получен {actual_topics_resp}'
