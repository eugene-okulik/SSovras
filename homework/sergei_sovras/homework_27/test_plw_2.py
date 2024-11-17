from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_alert_submit(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    def accepting_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accepting_alert)
    page.get_by_role('link', name='Click').click()
    result_text = page.locator('#result-text')
    expect(result_text).to_have_text('Ok')


def test_tabs_testing(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.locator('#new-page-button')

    with context.expect_page() as new_tab_event:
        click_button.click()

    new_tab = new_tab_event.value
    text_tab = new_tab.locator('#result-text')
    expect(text_tab).to_have_text('I am a new page in a new tab')
    expect(click_button).to_be_enabled()


def test_color_changing(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_button = page.locator('#colorChange')
    expecting_button = page.locator('#visibleAfter')
    expect(expecting_button).to_be_visible()
    color_button.click()
