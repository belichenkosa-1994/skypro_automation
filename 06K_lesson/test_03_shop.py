from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
import time


def test_shopping_cart():
    driver = webdriver.Firefox()

    try:
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        wait = WebDriverWait(driver, 10)

        # Авторизация
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Добавление товаров в корзину:
        # 1) Sauce Labs Backpack
        backpack_button = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        backpack_button.click()

        # 2) Sauce Labs Bolt T-Shirt
        tshirt_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_button.click()

        # 3) Sauce Labs Onesie
        onesie_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_button.click()

        # Переход в корзину
        cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_button.click()

        # Нажатие Checkout
        checkout_button = wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Заполнение формы
        first_name_field = wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Иван")

        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        #  Нажатие кнопки Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        # Чтение итоговой стоимости
        total_element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text

        # Проверка суммы
        assert total_text == "Total: $58.29", f"Ожидалась сумма $58.29, но получено {total_text}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_shopping_cart()