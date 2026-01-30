"""
Базовый класс для всех Page Object.
Содержит общие методы для работы с веб-страницами.
"""
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц."""
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Открыть URL: {url}")
    def open(self, url: str) -> None:
        """
        Открыть указанный URL в браузере.
        
        Args:
            url: URL для открытия
        """
        self.driver.get(url)
    
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator: tuple) -> WebElement:
        """
        Найти элемент на странице.
        
        Args:
            locator: Кортеж (By, selector)
            
        Returns:
            WebElement: Найденный элемент
            
        Raises:
            TimeoutException: Если элемент не найден за время ожидания
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        """
        Получить текущий URL страницы.
        
        Returns:
            str: Текущий URL
        """
        return self.driver.current_url
    
    @allure.step("Получить заголовок страницы")
    def get_title(self) -> str:
        """
        Получить заголовок страницы.
        
        Returns:
            str: Заголовок страницы
        """
        return self.driver.title