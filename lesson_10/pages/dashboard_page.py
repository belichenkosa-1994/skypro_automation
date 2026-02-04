"""
Page Object для страницы дашборда.
Демонстрирует документацию методов с типами.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page Object для страницы дашборда (панели управления)."""
    
    # Локаторы элементов
    HEADER = (By.TAG_NAME, "h1")
    USER_MENU = (By.ID, "user-menu")
    LOGOUT_BUTTON = (By.ID, "logout")
    WIDGETS = (By.CLASS_NAME, "widget")
    
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы дашборда.
        
        Args:
            driver: Экземпляр веб-драйвера
        """
        super().__init__(driver)
    
    @allure.step("Получить заголовок дашборда")
    def get_header_text(self) -> str:
        """
        Получение текста заголовка.
        
        Returns:
            str: Текст заголовка
        """
        return self.find_element(self.HEADER).text
    
    @allure.step("Проверить наличие виджетов")
    def are_widgets_present(self) -> bool:
        """
        Проверка наличия виджетов.
        
        Returns:
            bool: True если есть хотя бы один виджет
        """
        widgets = self.driver.find_elements(*self.WIDGETS)
        return len(widgets) > 0
    
    @allure.step("Нажать кнопку выхода")
    def click_logout(self) -> None:
        """Клик по кнопке выхода."""
        self.find_element(self.LOGOUT_BUTTON).click()
    
    @allure.step("Проверить отображение меню пользователя")
    def is_user_menu_visible(self) -> bool:
        """
        Проверка видимости меню пользователя.
        
        Returns:
            bool: True если меню отображается
        """
        try:
            return self.find_element(self.USER_MENU).is_displayed()
        except:
            return False