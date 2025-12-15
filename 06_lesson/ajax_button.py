from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_ajax_button():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/ajax")
    
    # Нажимаем на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    button.click()
    
    # Ждем появления зеленой плашки с текстом
    wait = WebDriverWait(driver, 15)
    success_message = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )
    
    # Получаем и выводим текст
    text = success_message.text
    print(text)
    
    driver.quit()


if __name__ == "__main__":
    test_ajax_button()