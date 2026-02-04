# Домашнее задание №10: Документация и Allure отчеты

## Описание проекта
Этот проект содержит автотесты для веб-приложения, реализованные с использованием:
- **Page Object Pattern** для структурирования кода
- **Pytest** как фреймворк для тестирования  
- **Selenium WebDriver** для автоматизации браузера
- **Allure Framework** для создания детальных отчетов
- **pytest-html** для альтернативных HTML отчетов

Проект демонстрирует выполнение всех требований ДЗ №10:
1. Полная документация всех методов Page Object (типы параметров и возвращаемых значений)
2. Allure разметка тестов (декораторы и шаги)
3. Инструкции по запуску и просмотру отчетов
4. Проверка кода на соответствие стандартам PEP8

## 🚀 Быстрый старт

### 1. Установка зависимостей Python
```bash
pip install -r requirements.txt

Файл requirements.txt содержит:
selenium==4.15.0
pytest==7.4.3
allure-pytest==2.13.2
webdriver-manager==4.0.1
pytest-html==4.1.1
flake8==6.1.0

### 2. Запуск тестов с HTML отчетом (рекомендуемый способ)
bash
# Запуск всех тестов
pytest tests/ --html=report.html --self-contained-html -v

# Запуск конкретного тестового файла
pytest tests/test_login.py --html=report.html --self-contained-html -v

### 3. Просмотр HTML отчета
Перейдите в папку lesson_10 в проводнике Windows

Найдите файл report.html

Откройте его двойным кликом

Если не открывается, выберите "Открыть с помощью" и выберите браузер

Альтернативные способы открытия отчета:

bash
# Через PowerShell (если установлен браузер по умолчанию)
Invoke-Item report.html

# Через командную строку
start report.html

# Прямой путь для браузера (скопируйте в адресную строку):
file:///C:/GitHub-копия/skypro_automation/lesson_10/report.html


📊 Работа с Allure отчетом (дополнительно)
Установка Allure CLI на Windows:
Если хотите использовать оригинальный Allure отчет, установите Allure одним из способов:

Способ 1: Через Scoop (рекомендуется)
powershell
# Установите Scoop (менеджер пакетов для Windows)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Invoke-RestMethod get.scoop.sh | Invoke-Expression

# Установите Allure
scoop install allure

# Проверьте установку
allure --version
Способ 2: Через Chocolatey
powershell
# Установите Chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Установите Allure
choco install allure
Способ 3: Ручная установка
Скачайте Allure с официального сайта

Распакуйте архив в C:\allure\

Добавьте C:\allure\bin в переменную окружения PATH

Запуск тестов с Allure:
bash
# Генерация результатов Allure
pytest tests/ --alluredir=allure-results -v

# Просмотр отчета в браузере
allure serve allure-results

# Или создание статического отчета
allure generate allure-results -o allure-report --clean
allure open allure-report


# Структура проекта

lesson_10/
├── __init__.py              # Инициализатор пакета
├── pages/                   # Page Object классы
│   ├── __init__.py          # Инициализатор пакета pages
│   ├── base_page.py         # Базовый класс для всех страниц
│   ├── login_page.py        # Страница авторизации
│   └── dashboard_page.py    # Страница дашборда
├── tests/                   # Тестовые сценарии
│   ├── __init__.py          # Инициализатор пакета tests
│   ├── test_login.py        # Тесты страницы логина
│   └── test_dashboard.py    # Тесты страницы дашборда
├── utils/                   # Вспомогательные утилиты
│   └── waiters.py           # Кастомные ожидания
├── conftest.py              # Фикстуры Pytest
├── pytest.ini               # Конфигурация Pytest
├── requirements.txt         # Зависимости проекта
└── README.md                # Этот файл

# Запуск тестов без отчетов:
bash
pytest tests/ -v
pytest tests/test_login.py -v

# Запуск с подробным выводом:
pytest tests/ -v --tb=long

# Проверка структуры проекта:
# Windows
tree /f
# Или
dir /s /b *.py

Примечание: Из-за проблем с установкой Allure CLI на Windows использован альтернативный способ с pytest-html. Отчет генерируется в файл homework_report.html и открывается через проводник.