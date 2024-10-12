from selenium.webdriver.common.by import By


def test_visit_and_fill_text(driver):
    url = 'https://www.qa-practice.com/elements/input/simple'
    input_text = 'Test_input'
    driver.get(url)
    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys(input_text)
    input_field.submit()
    result_field = driver.find_element(By.ID, 'result-text')
    assert result_field.text == input_text, "Input text doesn't match the result"
    print(result_field.text)
