from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_language_select(driver):
    selected_text = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_field = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select_field)
    dropdown.select_by_visible_text(selected_text)
    button = driver.find_element(By.ID, 'submit-id-submit')
    button.click()
    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == selected_text
