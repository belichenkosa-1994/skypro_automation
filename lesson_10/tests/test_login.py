"""
Тесты для страницы авторизации.
Демонстрируют полную Allure разметку.
"""
import allure
import pytest


@allure.epic("Автоматизация тестирования")
@allure.feature("Авторизация пользователей")
class TestLogin:
    """Тесты страницы входа в систему."""
    
    @allure.id("LOGIN-001")
    @allure.story("Успешный вход")
    @allure.title("Проверка успешной авторизации")
    @allure.description("Тест проверяет вход в систему с валидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "regression", "login")
    def test_successful_login(self):
        """Тест успешной авторизации."""
        
        with allure.step("Подготовка тестовых данных"):
            username = "test_user"
            password = "secure_password123"
            
            allure.attach(
                f"Username: {username}\nPassword: {password}",
                name="Тестовые данные",
                attachment_type=allure.attachment_type.TEXT
            )
        
        with allure.step("Выполнение проверок логики"):
            # Имитация проверок
            assert len(username) > 0, "Имя пользователя не должно быть пустым"
            assert len(password) >= 8, "Пароль должен быть не менее 8 символов"
            assert any(c.isdigit() for c in password), "Пароль должен содержать цифры"
        
        with allure.step("Проверка окончательного результата"):
            login_successful = True  # Имитация успешного входа
            assert login_successful, "Вход должен быть успешным"
            
            allure.attach(
                "Авторизация прошла успешно!",
                name="Результат теста",
                attachment_type=allure.attachment_type.TEXT
            )
    
    @allure.id("LOGIN-002")
    @allure.story("Неуспешный вход")
    @allure.title("Проверка входа с неверными данными")
    @allure.description("Тест проверяет обработку невалидных учетных данных")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("username,password,expected_error", [
        ("", "password", "Пустое имя пользователя"),
        ("user", "", "Пустой пароль"),
        ("wrong", "wrong", "Неверные учетные данные")
    ])
    def test_failed_login(self, username: str, password: str, expected_error: str):
        """Тест неудачных попыток входа."""
        
        with allure.step(f"Попытка входа с данными: {username}"):
            allure.attach(
                f"Username: {username}\nPassword: {password}",
                name="Введенные данные",
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Имитация проверки
            has_error = True
            error_message = f"Ошибка: {expected_error}"
            
            allure.attach(
                error_message,
                name="Сообщение об ошибке",
                attachment_type=allure.attachment_type.TEXT
            )
            
            assert has_error, "Должна отображаться ошибка"