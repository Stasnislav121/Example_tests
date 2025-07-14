import os
import allure
import pytest
import shutil

from io import BytesIO
from pathlib import Path
from PIL import Image
from allure_commons.types import AttachmentType
from pixelmatch.contrib.PIL import pixelmatch

from library.site.ui.screenshots.settings import SCREENSHOTS_DIR_PATH


class ScreenshotHelper:
    def __init__(self, page, request):
        self.page = page
        self.request = request
        self.img_index = 0

    def create_screenshot(self, locator=None, name=None):
        if locator:
            msg = f'Создать скриншот элемента с локатором [{locator}]'
        else:
            msg = 'Создать скриншот текущей страницы'

        with allure.step(msg):
            try:
                file = self.get_screenshot_file_path(name=name)
                if locator is None:
                    img = self.page.screenshot(full_page=True, type="png")
                else:
                    img = self.page.locator(locator).screenshot(type="png")
                file.write_bytes(img)
            except Exception as ex:
                raise Exception(f"При создании скриншота возникла ошибка: {ex.args}") from ex

    def compare_screenshots(self, locator=None, name=None):
        if locator is None:
            msg = 'Сравнение скриншота текущей страницы с эталоном'
        else:
            msg = f'Сравнение скриншота элемента с локатором [{locator}] с эталоном'

        self.img_index += 1

        with allure.step(msg):
            update_screenshot = self.request.config.option.update_screenshot
            if update_screenshot:
                self.create_screenshot(locator=locator, name=name)
                pytest.fail("--> Эталон отсутствует! Создан новый, необходимо его проверить")
            try:
                standard = self.get_screenshot_file_path(name=name)
                if standard.exists():
                    if locator is None:
                        screenshot = self.page.screenshot(full_page=True, type="png", locator=locator)
                    else:
                        screenshot = self.page.locator(locator).screenshot(type="png")

                    img_actual = Image.open(BytesIO(screenshot))
                    img_expected = Image.open(standard)
                    # if img_actual.size != img_expected.size:
                    #     img_actual, img_expected = self.resize_image(img_actual, img_expected)
                    img_diff = Image.new("RGBA", img_actual.size)
                    mismatch = pixelmatch(img_actual, img_expected, img_diff)
                else:
                    self.create_screenshot(locator=locator, name=name)
                    pytest.fail("--> Эталон отсутствует! Создан новый, необходимо его проверить")

                if mismatch == 0:
                    return
                else:
                    name = f'{self.get_test_name()}.png'
                    test_result_dir = self.get_screenshot_dir_path() / 'test_error'
                    if os.path.exists(test_result_dir):
                        shutil.rmtree(test_result_dir)
                    test_result_dir.mkdir(parents=True, exist_ok=True)
                    diff_file = f'{test_result_dir}/Diff_{name}'
                    actual_file = f'{test_result_dir}/Actual_{name}'
                    expected_file = f'{test_result_dir}/Expected_{name}'
                    img_diff.save(diff_file)
                    img_actual.save(actual_file)
                    img_expected.save(expected_file)

                    with open(diff_file, "rb") as img:
                        diff_img_byte = img.read()
                    with open(actual_file, "rb") as img:
                        actual_img_byte = img.read()
                    with open(expected_file, "rb") as img:
                        expected_img_byte = img.read()

                    allure.attach(diff_img_byte, name='diff', attachment_type=AttachmentType.PNG)
                    allure.attach(actual_img_byte, name='actual', attachment_type=AttachmentType.PNG)
                    allure.attach(expected_img_byte, name='expected', attachment_type=AttachmentType.PNG)
                    pytest.fail("--> Скриншоты не совпадают!")

            except Exception as ex:
                raise Exception(f"При сравнении возникла ошибка: {ex.args}") from ex

    def get_test_name(self):
        test_name = f"{str(Path(self.request.node.name))}"
        return test_name

    def get_screenshot_dir_path(self):
        test_module = self.request.module.__name__
        test_dir = str(Path(self.request.node.name)).split('[', 1)[0]
        test_parent_dir = str(os.path.basename(Path(os.getenv('PYTEST_CURRENT_TEST')).parent))
        filepath = (Path(SCREENSHOTS_DIR_PATH) / test_parent_dir / test_module / test_dir)
        filepath.mkdir(parents=True, exist_ok=True)
        return filepath

    def get_screenshot_file_path(self, name=None):
        filepath = self.get_screenshot_dir_path()
        test_name = self.get_test_name()
        if name is None:
            image_name = f'{self.img_index}_{test_name}.png'
        else:
            image_name = f'{self.img_index}_{test_name}_{name}.png'
        file = filepath / image_name
        return file

    def resize_image(self, img_actual, img_expected):
        width_act, height_act = img_actual.size[0], img_actual.size[1]
        width_exp, height_exp = img_expected.size[0], img_expected.size[1]

        max_width = max(width_act, width_exp)
        max_height = max(height_act, height_exp)

        ratio_act = min(max_width / width_act, max_height / height_act)
        ratio_exp = min(max_width / width_exp, max_height / height_exp)

        actual_thumb_img = (Path(self.get_screenshot_dir_path() / f'{self.get_test_name()}_actual_thumb.png'))
        img_actual.thumbnail(size=(width_act * ratio_act, height_act * ratio_act))
        img_actual.save(actual_thumb_img)
        img_actual_resized = Image.open(actual_thumb_img)

        expected_thumb_img = (Path(self.get_screenshot_dir_path() / f'{self.get_test_name()}_expected_thumb.png'))
        img_expected.thumbnail(size=(width_exp * ratio_exp, height_exp * ratio_exp))
        img_expected.save(expected_thumb_img)
        img_expected_resized = Image.open(expected_thumb_img)

        print(f'ACTUAL_SIZE_RESIZED = {img_actual_resized.size}')
        print(f'EXPECTED_SIZE_RESIZED = {img_expected_resized.size}')

        return img_actual_resized, img_expected_resized


@pytest.fixture
def site_screenshot_helper(request):
    def _site_screenshot_helper(page):
        return ScreenshotHelper(page, request)

    return _site_screenshot_helper


def pytest_addoption(parser) -> None:
    group = parser.getgroup("site-screenshot", "Site screenshot helper")
    group.addoption(
        "--update_screenshot",
        action="store_true",
        default=False,
        help="Обновить скриншоты запущенных тестов",
    )
