import allure
from requests import Response
from library.mobapp.api.response_handlers import ResponseHandler
from library.mobapp.api.base_api_client import *


class FeedbackApi(BaseApiClient):
    def __init__(self):
        super().__init__(service='feedback')

    def get_feedback_topics(self, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /feedback/topics'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.get('/topics',
                                headers=self.headers,
                                print_url=False)
            if check_error:
                ResponseHandler.check_response_code_is_200(response)
                ResponseHandler.check_response_has_success_is_true(response)

            return response

    def send_feedback_by_topic_id(self, json, token=None, check_error=True, topic_id=3) -> Response:
        with allure.step(f'Отправка запроса через метод /feedback/reports/{topic_id}'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post(f'/reports/{topic_id}',
                                 headers=self.headers,
                                 data=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

            return response

    def send_feedback_about_app(self, json, token=None, check_error=True) -> Response:
        with allure.step('Отправка запроса через метод /feedback/reports/application'):
            if token is not None:
                self.headers['Authorization'] = token
            response = self.post('/reports/application',
                                 headers=self.headers,
                                 json=json)
            if check_error:
                ResponseHandler.check_response_code_is_201(response)
                ResponseHandler.check_response_has_success_is_true(response)

            return response
