from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 5)
    url = 'https://www.demoblaze.com/index.html'
    item_text = 'Samsung galaxy s6'
    driver.get(url)
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Samsung galaxy s6')))
    item = driver.find_element(By.LINK_TEXT, item_text)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(item)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn-success')))
    success_button = driver.find_element(By.CLASS_NAME, 'btn-success')
    success_button.click()
    wait.until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'success')))
    cart_item = driver.find_elements(By.TAG_NAME, 'td')
    assert cart_item[1].text == item_text, 'Check your code, there is an error'


def test_add_to_compare(driver):
    url = 'https://magento.softwaretestingboard.com/gear/bags.html'
    driver.get(url)
    item = driver.find_element(By.CLASS_NAME, 'product-item-link')
    compare_button = driver.find_element(By.CSS_SELECTOR, '[title="Add to Compare"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", item)

    actions = ActionChains(driver)
    actions.move_to_element(item)
    actions.click(compare_button)
    actions.perform()

    compare_section = driver.find_element(By.TAG_NAME, 'h1')
    driver.execute_script("arguments[0].scrollIntoView(true);", compare_section)
    item_text = driver.find_element(By.CLASS_NAME, 'product-item-link')
    item_comparing = driver.find_element(By.CSS_SELECTOR, '.odd > .product-item-name > a')
    assert item_comparing.text == item_text.text, 'Check your code, there is an error'
