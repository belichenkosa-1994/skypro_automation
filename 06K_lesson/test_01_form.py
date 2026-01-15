from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest


def test_form_validation():
    # Автоматическая загрузка и установка правильного драйвера
    service = Service(EdgeChromiumDriverManager().install())

    # Настройка Edge с опциями
    edge_options = Options()

    # Добавляем аргументы для решения проблемы с DevToolsActivePort
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--remote-debugging-port=9222")
    edge_options.add_argument("--start-maximized")

    # Отключаем автоматическое управление расширениями
    edge_options.add_experimental_option('useAutomationExtension', False)
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])

    # Инициализация драйвера Edge
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        # Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        wait = WebDriverWait(driver, 15)

        # Явное ожидание загрузки формы
        form_element = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )

        # Заполнение формы
        fields_to_fill = [
            ("[name='first-name']", "Иван"),
            ("[name='last-name']", "Петров"),
            ("[name='address']", "Ленина, 55-3"),
            ("[name='e-mail']", "test@skypro.com"),
            ("[name='phone']", "+7985899998787"),
            # Zip code пропускаем - оставляем пустым
            ("[name='city']", "Москва"),
            ("[name='country']", "Россия"),
            ("[name='job-position']", "QA"),
            ("[name='company']", "SkyPro")
        ]

        for selector, value in fields_to_fill:
            element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            element.clear()
            element.send_keys(value)

        # Нажатие кнопки Submit
        submit_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

        # Ожидание обновления стилей полей
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[name='zip-code'].is-invalid"))
        )

        # Проверка, что поле Zip code подсвечено красным
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
        zip_code_classes = zip_code_field.get_attribute("class")
        assert "is-invalid" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"

        # Проверка, что остальные поля подсвечены зеленым
        fields_to_validate = [
            ("first-name", "First name"),
            ("last-name", "Last name"),
            ("address", "Address"),
            ("e-mail", "Email"),
            ("phone", "Phone number"),
            ("city", "City"),
            ("country", "Country"),
            ("job-position", "Job position"),
            ("company", "Company")
        ]

        for field_name, field_display in fields_to_validate:
            field = driver.find_element(By.CSS_SELECTOR, f"[name='{field_name}']")
            field_classes = field.get_attribute("class")
            assert "is-valid" in field_classes, f"Поле '{field_display}' должно быть подсвечено зеленым"

        print("Тест успешно пройден!")

    except Exception as e:
        # Делаем скриншот при ошибке
        driver.save_screenshot("form_test_error.png")
        raise e

    finally:
        # Закрытие браузера
        driver.quit()


if __name__ == "__main__":
    test_form_validation()