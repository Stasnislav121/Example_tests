import uuid
import pytest
import os
import allure

from library.common.api import ApiClient
from library.site.ui import *
from settings import PROJECT_ROOT
from allure_commons.types import AttachmentType

config = {
    'viewport': {
        'desktop': {'width': 1920, 'height': 1080},
        'mobile': {'width': 360, 'height': 800}
    },
    'geolocation': {"longitude": 36.8550435, "latitude": 55.7415733},
}


# @pytest.fixture(autouse=True)
# def check_task_available():
#     task = os.environ.get('TASK_ENV')
#     if task is None or task == '' or task == 'master':
#         task = 'predprod'
#
#     is_autotests_task = os.environ.get('AUTOTESTS_SELF_DEPLOY')
#     if is_autotests_task is not None and is_autotests_task.lower() == 'true':
#         base_url = f"https://nsite-{task}-autotests.task..ru"
#     else:
#         base_url = f"https://nsite-{task}.task..ru"
#
#     auto_test_url = os.environ.get('AUTO_TESTS_URL')
#     if auto_test_url is not None and auto_test_url != '':
#         base_url = auto_test_url
#
#     site_task = os.environ.get('SITE_TASK')
#     if site_task is not None and site_task != '':
#         base_url = f"https://nsite-{site_task}.task..ru"
#
#     if base_url is not None and base_url != "":
#         client = ApiClient(base_url)
#         response = client.get('', print_url=False)
#         if response.status_code != 200:
#             pytest.fail(f'Хост {base_url} недоступен, код ответа: {response.status_code}')


@pytest.fixture
def viewport(browser_mode):
    if browser_mode.lower() == 'mobile':
        return config['viewport']['mobile']
    elif browser_mode.lower() == 'desktop':
        return config['viewport']['desktop']
    else:
        return config['viewport']['desktop']


@pytest.fixture(params=[
    'desktop',
    'mobile'
])
def browser_mode(request):
    result = request.param
    if result.lower() == 'mobile':
        os.environ['IS_MOBILE'] = str(True)
    elif result.lower() == 'desktop':
        os.environ['IS_MOBILE'] = str(False)
    else:
        os.environ['IS_MOBILE'] = str(False)

    return result


@pytest.fixture
def site_page(browser, viewport, request, browser_context_args):
    context = browser.new_context(**browser_context_args, viewport=viewport, permissions=["geolocation"],
                                  geolocation=config['geolocation'])
    page = context.new_page()
    yield page
    context.close()
