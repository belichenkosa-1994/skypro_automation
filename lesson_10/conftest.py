"""
Фикстуры Pytest для проекта.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """
    Фикстура для создания экземпляра веб-драйвера.
    
    Yields:
        WebDriver: Экземпляр Chrome WebDriver
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    """
    Фикстура для создания экземпляра страницы логина.
    
    Args:
        driver: Фикстура драйвера
        
    Returns:
        LoginPage: Экземпляр страницы логина
    """
    from pages.login_page import LoginPage
    return LoginPage(driver)


@pytest.fixture
def dashboard_page(driver):
    """
    Фикстура для создания экземпляра страницы дашборда.
    
    Args:
        driver: Фикстура драйвера
        
    Returns:
        DashboardPage: Экземпляр страницы дашборда
    """
    from pages.dashboard_page import DashboardPage
    return DashboardPage(driver)