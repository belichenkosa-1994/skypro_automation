"""
Page Object для страницы авторизации.
Демонстрирует документацию методов с типами.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class LoginPage(BasePage):
    """Page Object для страницы входа в систему."""
    
    # Локаторы элементов
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Ввод имени пользователя.
        
        Args:
            username: Имя пользователя для ввода
        """
        element = self.find_element(self.USERNAME_INPUT)
        element.clear()
        element.send_keys(username)
    
    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Ввод пароля.
        
        Args:
            password: Пароль для ввода
        """
        element = self.find_element(self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)
    
    @allure.step("Нажать кнопку входа")
    def click_login_button(self) -> None:
        """Клик по кнопке входа."""
        self.find_element(self.LOGIN_BUTTON).click()
    
    @allure.step("Проверить наличие ошибки")
    def is_error_displayed(self) -> bool:
        """
        Проверка отображения сообщения об ошибке.
        
        Returns:
            bool: True если ошибка отображается, иначе False
        """
        try:
            return self.find_element(self.ERROR_MESSAGE).is_displayed()
        except:
            return False
    
    @allure.step("Выполнить полный вход: {username}")
    def login(self, username: str, password: str) -> None:
        """
        Полный процесс авторизации.
        
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()