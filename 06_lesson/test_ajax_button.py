from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.os_manager import ChromeType

def test_ajax_button():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://uitestingplayground.com/ajax")

    sleep (5)
    driver.quit()
#     # Нажимаем на синюю кнопку
#     button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
#     button.click()
#
#     # Ждем появления зеленой плашки с текстом
#     wait = WebDriverWait(driver, 15)
#     success_message = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success"))
#     )
#
#     # Получаем и выводим текст
#     text = success_message.text
#     print(text)
#
#     driver.quit()
#
#
# if __name__ == "__main__":
# test_rename_button()