from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        # Находим кнопку добавления товара по названию товара
        product_container = self.driver.find_element(By.XPATH,
                                                     f"//div[contains(text(), '{product_name}')]/ancestor::div[@class='inventory_item']")
        add_button = product_container.find_element(By.CLASS_NAME, "btn_inventory")
        add_button.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()