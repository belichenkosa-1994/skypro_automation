"""
Тесты для страницы дашборда.
Демонстрируют полную Allure разметку.
"""
import allure
import pytest


@allure.epic("Автоматизация тестирования")
@allure.feature("Панель управления")
class TestDashboard:
    """Тесты страницы дашборда."""
    
    @allure.id("DASH-001")
    @allure.story("Загрузка дашборда")
    @allure.title("Проверка элементов дашборда")
    @allure.description("Тест проверяет наличие всех элементов на дашборде")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "dashboard", "ui")
    def test_dashboard_elements(self):
        """Тест проверки элементов дашборда."""
        
        with allure.step("Подготовка списка ожидаемых элементов"):
            expected_elements = [
                "Заголовок",
                "Меню пользователя", 
                "Виджеты статистики",
                "Кнопка выхода"
            ]
            
            allure.attach(
                str(expected_elements),
                name="Ожидаемые элементы",
                attachment_type=allure.attachment_type.JSON
            )
        
        with allure.step("Имитация проверки элементов"):
            # Имитация найденных элементов
            found_elements = [
                "Заголовок",
                "Меню пользователя",
                "Виджеты статистики",
                "Кнопка выхода"
            ]
            
            for element in found_elements:
                allure.attach(
                    element,
                    name=f"Найден элемент: {element}",
                    attachment_type=allure.attachment_type.TEXT
                )
        
        with allure.step("Проверка наличия всех элементов"):
            assert len(found_elements) == len(expected_elements)
            for expected in expected_elements:
                assert expected in found_elements, f"Элемент '{expected}' не найден"
    
    @allure.id("DASH-002")
    @allure.story("Функциональность дашборда")
    @allure.title("Проверка выхода из системы")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_functionality(self):
        """Тест функциональности выхода."""
        
        with allure.step("Имитация нажатия кнопки выхода"):
            logout_clicked = True
            allure.attach(
                "Кнопка выхода нажата",
                name="Действие пользователя",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Проверка перенаправления на страницу логина"):
            redirected_to_login = True
            
            allure.attach(
                "Перенаправление на страницу логина",
                name="Результат действия",
                attachment_type=allure.attachment_type.TEXT
            )
            
            assert logout_clicked, "Кнопка выхода должна быть нажата"
            assert redirected_to_login, "Должен произойти редирект на страницу логина"