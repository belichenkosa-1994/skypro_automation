import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestStore:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Firefox()
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        yield
        self.driver.quit()

    def test_complete_purchase(self):
        # Открываем сайт и авторизуемся
        self.login_page.open()
        self.login_page.login("standard_user", "secret_sauce")

        # Добавляем товары в корзину
        self.main_page.add_product_to_cart("Sauce Labs Backpack")
        self.main_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        self.main_page.add_product_to_cart("Sauce Labs Onesie")

        # Переходим в корзину
        self.main_page.go_to_cart()

        # Переходим к оформлению заказа
        self.cart_page.checkout()

        # Заполняем форму
        self.checkout_page.fill_form("Иван", "Иванов", "123456")

        # Получаем итоговую стоимость
        total_text = self.checkout_page.get_total()
        total_amount = total_text.replace("Total: $", "")

        assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"