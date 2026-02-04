"""
Вспомогательные утилиты для ожиданий.
Демонстрирует документацию методов.
"""
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CustomWaiters:
    """Класс с кастомными ожиданиями."""
    
    @staticmethod
    @allure.step("Ожидать видимости элемента: {locator}")
    def wait_for_element_visible(
        driver: WebDriver, 
        locator: tuple, 
        timeout: int = 10
    ) -> bool:
        """
        Ожидание видимости элемента.
        
        Args:
            driver: Экземпляр веб-драйвера
            locator: Локатор элемента (By, selector)
            timeout: Время ожидания в секундах
            
        Returns:
            bool: True если элемент стал видимым
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False
    
    @staticmethod
    @allure.step("Ожидать кликабельности элемента: {locator}")
    def wait_for_element_clickable(
        driver: WebDriver,
        locator: tuple,
        timeout: int = 10
    ) -> bool:
        """
        Ожидание кликабельности элемента.
        
        Args:
            driver: Экземпляр веб-драйвера
            locator: Локатор элемента
            timeout: Время ожидания в секундах
            
        Returns:
            bool: True если элемент стал кликабельным
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False