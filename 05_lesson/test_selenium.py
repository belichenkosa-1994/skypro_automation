from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")

try:
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.google.com")
    print("Title:", driver.title)
    time.sleep(2)
    driver.quit()
    print("Тест пройден успешно!")
except Exception as e:
    print("Ошибка:", e)
