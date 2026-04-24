# Sprint_6

Автотесты для учебного сервиса Яндекс.Самокат.

## Технологии

- Python
- Selenium WebDriver
- Pytest
- Allure Report

## Структура проекта

- `conftest.py` — фикстура браузера
- `data.py` — тестовые данные
- `locators.py` — локаторы
- `pages/` — page object классы
- `test/` — тесты

## Что проверяется

### FAQ
- Открытие каждого вопроса
- Проверка текста ответа

### Заказ самоката
- Заказ через верхнюю кнопку
- Заказ через нижнюю кнопку

### Логотипы
- Переход по логотипу Самоката
- Открытие новой вкладки по логотипу Яндекса

## Установка

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Запуск всех тестов:

```bash
pytest -v
```

Запуск с сохранением результатов Allure:

```bash
pytest -v --alluredir=allure_results
```

## Отчёт Allure

Чтобы после запуска тестов отчёт открылся в браузере, выполни:

```bash
allure serve allure_results
```

Эта команда генерирует отчёт и автоматически открывает его в браузере. [web:711]

Если нужно сначала сохранить html-отчёт в папку, а потом открыть:

```bash
allure generate allure_results -o allure-report --clean
allure open allure-report
```

`allure generate` сохраняет HTML-отчёт в директорию, а `allure open` открывает его в браузере. [web:759]