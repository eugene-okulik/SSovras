from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
    wait = WebDriverWait(driver, 10)
    text_locator = ("xpath", "//*[@id='finish']/h4")
    text_object = wait.until(ec.visibility_of_element_located(text_locator))
    assert text_object.text == 'Hello World!'
