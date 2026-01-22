from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()

driver.quit()