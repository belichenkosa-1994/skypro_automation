from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(
    By.CSS_SELECTOR, "button[type='submit']"
)
login_button.click()

message = driver.find_element(By.ID, "flash")
print(message.text)

driver.quit()