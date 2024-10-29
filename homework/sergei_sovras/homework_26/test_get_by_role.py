from playwright.sync_api import Page, expect


def test_get_by_role_auth(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('login_test')
    page.get_by_role('textbox', name='password').fill('password_test')
    page.get_by_role('button', name=' Login').click()
