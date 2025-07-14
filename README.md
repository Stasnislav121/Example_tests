## Примеры тестов на Python: UI - Playwright, API - Requests

## Требования

Python версии 3.8

## Быстрый старт

1. Склонировать git-репозиторий 
2. Перейти в директорию склонированного проекта
3. Создать и активировать виртуальное окружение:
    - `<venv>` заменить на путь до директории с виртуальным окружением
        - **Windows**: `python -m venv <venv> & <venv>\Scripts\activate`
        - **Linux**: `python -m venv <venv> && <venv>/bin/activate`
    - Для Pycharm инструкция доступна по
      ссылке: https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#env-requirements
4. Установить зависимости:
    - `pip install -r requirements.txt`
    - `pip install -r requirements-api.txt`
    - `pip install -r requirements-ui.txt`
5. Установить браузеры (для UI-тестов): `python -m playwright install`
6. Запустить автотесты: `pytest -s -v --headed --alluredir allure-results tests/`
