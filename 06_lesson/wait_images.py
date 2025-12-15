from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_images():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем загрузки всех картинок
    wait = WebDriverWait(driver, 20)
    
    # Ждем, пока пропадет индикатор загрузки
    wait.until(
        EC.invisibility_of_element_located((By.ID, "loading"))
    )
    
    # Ждем, пока все изображения загрузятся (атрибут complete у всех img)
    wait.until(
        lambda d: all(
            d.execute_script(
                "return arguments[0].complete && "
                "typeof arguments[0].naturalWidth != 'undefined' && "
                "arguments[0].naturalWidth > 0",
                img
            )
            for img in d.find_elements(By.TAG_NAME, "img")
        )
    )
    
    # Получаем 3-ю картинку (индекс 2)
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)
    
    driver.quit()


if __name__ == "__main__":
    test_wait_images()