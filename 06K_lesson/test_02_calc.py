from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
import time


def test_calculator():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        wait = WebDriverWait(driver, 50)  # 45 секунд + запас

        # Установка задержки 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие кнопок: 7 + 8 =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидание результата (45 секунд)
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверка результата
        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Ожидался результат 15, но получено {result}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()