from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ссылка на «правильную» страницу.
# На registration1.html тест должен пройти,
# на registration2.html — упасть с NoSuchElementException.
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные селекторы: placeholder + required
    first_name = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your first name'][required]"
    )
    first_name.send_keys("Ivan")

    last_name = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your last name'][required]"
    )
    last_name.send_keys("Petrov")

    email = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Input your email'][required]"
    )
    email.send_keys("test@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что регистрация прошла
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
