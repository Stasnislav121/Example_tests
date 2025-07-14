import allure
import testit
from library.mobapp import *


class TestFeedbackReportsTopicId:
    @testit.workItemIds(17730)
    @testit.externalId('TestFeedbackReportsTopicId_17730')
    @testit.displayName('[201] POST /feedback/reports/topic_id'
                        ' - отправка отзыва на определенную тему (без авторизации)')
    @testit.nameSpace('API')
    @testit.className('Feedback')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Feedback')
    @allure.title('[201] POST /feedback/reports/topic_id'
                  ' - отправка отзыва на определенную тему (без авторизации)')
    @allure.testcase(url='https://testit..ru/browse/17730')
    def test_sending_feedback_by_topic_id_without_auth(self, request):
        expect_report = {
            'rating': 4,
            'message': StringHelper().get_random_ru_string(length=40),
            'orderId': '0000000000000'
        }

        with allure.step('Выполнить POST /feedback/topics/3'):
            client = FeedbackApi()
            response = client.send_feedback_by_topic_id(json=expect_report)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_success_schema)

        with allure.step('Проверка параметров ответа'):
            actual_report = FeedbackHelper.get_feedback_from_db_on_param(filter_param='comment',
                                                                         filter_value=expect_report['message'])[0]
            request.addfinalizer(lambda: FeedbackHelper.delete_feedback(filter_param='comment',
                                                                        filter_value=expect_report['message']))
            actual_report_comment = actual_report['comment']
            actual_report_rating = actual_report['rating']
            actual_report_order_id = actual_report['order_id']
            assert expect_report['rating'] == actual_report_rating, (
                f'Ожидалcя "rating": {expect_report["rating"]}, получен {actual_report_rating}')
            assert expect_report['message'] == actual_report_comment, (
                f'Ожидалcя "comment": {expect_report["message"]}, получен {actual_report_comment}')
            assert expect_report['orderId'] == actual_report_order_id, (
                f'Ожидалcя "order_id": {expect_report["orderId"]}, получен {actual_report_order_id}')

    @testit.workItemIds(41011)
    @testit.externalId('TestFeedbackReportsTopicId_41011')
    @testit.displayName('[201] POST /feedback/reports/topic_id - отправка отзыва на определенную тему (с авторизацией)')
    @testit.nameSpace('API')
    @testit.className('Feedback')
    @allure.epic('MobApp ')
    @allure.feature('API')
    @allure.story('API: Feedback')
    @allure.title('[201] POST /feedback/reports/topic_id - отправка отзыва на определенную тему (с авторизацией)')
    @allure.testcase(url='https://testit..ru/browse/41011')
    def test_sending_feedback_by_topic_id_with_auth(self, with_auth, request):
        expect_report = {
            'rating': 4,
            'message': StringHelper().get_random_ru_string(length=40),
            'orderId': '0000000000000'
        }
        user_info = {
            'name': AUTOTEST_USER_LONG_EXPIRATION_TOKEN['name'],
            'phone': AUTOTEST_USER_LONG_EXPIRATION_TOKEN['phone'],
            'email': AUTOTEST_USER_LONG_EXPIRATION_TOKEN['email']
        }

        with allure.step('Выполнить POST /feedback/topics/3'):
            client = FeedbackApi()
            response = client.send_feedback_by_topic_id(token=with_auth, json=expect_report)

        with allure.step('Валидация схемы ответа'):
            ResponseHandler.validate_response(response, common_success_schema)

        with allure.step('Проверка параметров ответа'):
            actual_report = FeedbackHelper.get_feedback_from_db_on_param(filter_param='comment',
                                                                         filter_value=expect_report['message'])[0]
            request.addfinalizer(lambda: FeedbackHelper.delete_feedback(filter_param='comment',
                                                                        filter_value=expect_report['message']))
            actual_report_comment = actual_report['comment']
            actual_report_rating = actual_report['rating']
            actual_report_order_id = actual_report['order_id']
            actual_report_phone = actual_report['phone']
            actual_report_name = actual_report['name']
            actual_report_email = actual_report['email']
            expect_report.update(user_info)

            assert expect_report['rating'] == actual_report_rating, (
                f'Ожидалcя "rating": {expect_report["rating"]}, получен {actual_report_rating}')
            assert expect_report['message'] == actual_report_comment, (
                f'Ожидалcя "comment": {expect_report["message"]}, получен {actual_report_comment}')
            assert expect_report['orderId'] == actual_report_order_id, (
                f'Ожидалcя "order_id": {expect_report["orderId"]}, получен {actual_report_order_id}')
            assert expect_report['phone'] == actual_report_phone, (
                f'Ожидалcя "phone": {expect_report["phone"]}, получен {actual_report_phone}')
            assert expect_report['name'] == actual_report_name, (
                f'Ожидалcя "name": {expect_report["name"]}, получен {actual_report_name}')
            assert expect_report['email'] == actual_report_email, (
                f'Ожидалcя "email": {expect_report["email"]}, получен {actual_report_email}')
