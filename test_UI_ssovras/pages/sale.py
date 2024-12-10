from playwright.sync_api import expect

from test_UI_ssovras.pages.base_page import BasePage
from test_UI_ssovras.pages.locators import compare_products, whats_new


class Sale(BasePage):
    page_url = '/sale.html'

    def verify_comparing(self, text):
        compare_title = self.find(compare_products)
        expect(compare_title).to_have_text(text)

    def verify_whats_new(self, text):
        compare_title = self.find(whats_new)
        expect(compare_title).to_have_text(text)
