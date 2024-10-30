from playwright.sync_api import Page


def test_fill_form(page: Page):
    url = 'https://demoqa.com/automation-practice-form'
    page.goto(url)

    page.get_by_placeholder('First Name').fill('First name test')
    page.get_by_placeholder('Last Name').fill('Last name test')
    page.get_by_placeholder('name@example.com').fill('test@email.com')
    page.locator('[for="gender-radio-1"]').check()
    page.get_by_placeholder('Mobile Number').fill('1231231231')

    dob_field = page.locator('#dateOfBirthInput')
    dob_field.fill('2,01,12')
    dob_field.press('Enter')

    subject = page.locator('#subjectsInput')
    subject.fill('Math')
    subject.press('Enter')

    page.locator('[for="hobbies-checkbox-1"]').check()
    page.get_by_placeholder('Current Address').fill('Test address')

    state = page.locator('[id="state"]')
    state.click()
    state.press('Enter')

    city = page.locator('[id="city"]')
    city.click()
    city.press('Enter')

    page.locator('[id="submit"]').click()
