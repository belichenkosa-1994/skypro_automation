from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_rename_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    
    # Вводим текст в поле
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")
    
    # Нажимаем на кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()
    
    # Ждем обновления текста кнопки
    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )
    
    # Получаем и выводим текст кнопки
    updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    print(updated_button.text)
    
    driver.quit()


if __name__ == "__main__":
    test_rename_button()