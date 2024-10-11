from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_fill_full_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    form_title = driver.find_element(By.CLASS_NAME, 'text-center')
    driver.execute_script("arguments[0].scrollIntoView(true);", form_title)

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Test first name')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Test last name')

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('Test@email.com')

    gender = driver.find_element(By.ID, 'gender-radio-1')
    driver.execute_script("arguments[0].click();", gender)

    phone_number = driver.find_element(By.ID, 'userNumber')
    phone_number.send_keys('1234567890')

    dof = driver.find_element(By.ID, 'dateOfBirthInput')
    for _ in range(len(dof.get_attribute('value')) - 1):
        dof.send_keys(Keys.BACKSPACE)
    # Если удалить все символы, страница падает (BUG)
    dof.send_keys('1.12.2020')
    dof.send_keys(Keys.ENTER)

    subject_select = driver.find_element(By.ID, 'subjectsInput')
    subject_select.send_keys('Math')
    subject_select.send_keys(Keys.ENTER)

    hobby_checkbox = driver.find_element(By.ID, 'hobbies-checkbox-1')
    driver.execute_script("arguments[0].click();", hobby_checkbox)

    current_address = driver.find_element(By.ID, 'currentAddress')
    current_address.send_keys('Test address')

    select_state = driver.find_element(By.ID, 'react-select-3-input')
    select_state.send_keys('NCR')
    select_state.send_keys(Keys.ENTER)

    select_city = driver.find_element(By.ID, 'react-select-4-input')
    select_city.send_keys('Noida')
    select_city.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.ID, 'submit')
    submit_button.click()

    header_title = driver.find_element(By.ID, 'example-modal-sizes-title-lg')
    print(header_title.text)

    str_head_table = driver.find_element(By.XPATH, '//thead/tr')
    table_record = str_head_table.find_elements(By.TAG_NAME, 'th')
    for string in table_record:
        print(string.text, end=' ')
    print('\n')

    str_body_table = driver.find_elements(By.XPATH, '//tbody/tr')
    for string_body in str_body_table:
        string_ttt = string_body.find_elements(By.TAG_NAME, 'td')
        for string in string_ttt:
            print(string.text, end=' ')
        print('\n')
