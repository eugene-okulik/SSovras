from playwright.sync_api import expect

from test_UI_ssovras.pages.base_page import BasePage
from test_UI_ssovras.pages.locators import (
    first_name_locator, last_name_locator, email_locator, password_locator, password_confirmation_locator,
    submit_button_locator, error_first_name_locator)


class AccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def fill_form(self, first_name, last_name, email_address, password):
        self.send_keys(first_name_locator, first_name)
        self.send_keys(last_name_locator, last_name)
        self.send_keys(email_locator, email_address)
        self.send_keys(password_locator, password)
        self.send_keys(password_confirmation_locator, password)

    def submit_form(self):
        submit_button = self.find(submit_button_locator)
        submit_button.click()

    def verify_valid_form(self, page_url_1):
        expect(self.page).to_have_url(page_url_1)

    def verify_invalid_form(self, text):
        first_name_error = self.find(error_first_name_locator)
        expect(first_name_error).to_have_text(text)
