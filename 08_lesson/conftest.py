import os
import pytest
from dotenv import load_dotenv
from api_client import YougileAPIClient

# Загрузка переменных окружения из .env файла
load_dotenv()

# Данные для авторизации
YOUGILE_API_KEY = os.getenv('YOUGILE_API_KEY')
YOUGILE_COMPANY_ID = os.getenv('YOUGILE_COMPANY_ID')
BASE_URL = 'https://ru.yougile.com'

# Проверка наличия обязательных переменных окружения
def pytest_configure(config):
    """Проверяем наличие обязательных переменных окружения перед запуском тестов."""
    required_env_vars = ['YOUGILE_API_KEY', 'YOUGILE_COMPANY_ID']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        pytest.exit(
            f"ОТСУТСТВУЮТ ОБЯЗАТЕЛЬНЫЕ ПЕРЕМЕННЫЕ ОКРУЖЕНИЯ: {', '.join(missing_vars)}\n"
            f"Пожалуйста, создайте файл .env в корне проекта со следующими переменными:\n"
            f"YOUGILE_API_KEY=ваш_api_ключ\n"
            f"YOUGILE_COMPANY_ID=ваш_company_id\n"
            f"Пример файла .env:\n"
            f"YOUGILE_API_KEY=your_actual_api_key_here\n"
            f"YOUGILE_COMPANY_ID=your_actual_company_id_here"
        )

@pytest.fixture(scope='session')
def base_url():
    """Фикстура для базового URL."""
    return BASE_URL

@pytest.fixture(scope='session')
def auth_headers():
    """Фикстура для заголовков авторизации."""
    return {
        'Authorization': f'Bearer {YOUGILE_API_KEY}',
        'Content-Type': 'application/json',
        'X-YouGile-Company-Id': YOUGILE_COMPANY_ID
    }

@pytest.fixture(scope='function')
def api_client(base_url, auth_headers):
    """Фикстура для создания клиента API."""
    return YougileAPIClient(base_url, auth_headers)