import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


class TestCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.calculator_page = CalculatorPage(self.driver)
        yield
        self.driver.quit()

    def test_calculator_with_delay(self):
        self.calculator_page.open()
        self.calculator_page.set_delay(45)

        self.calculator_page.click_button("7")
        self.calculator_page.click_button("+")
        self.calculator_page.click_button("8")
        self.calculator_page.click_button("=")

        result = self.calculator_page.get_result()
        assert result == "15", f"Expected 15, but got {result}"