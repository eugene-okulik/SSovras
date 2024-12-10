from playwright.sync_api import expect

from test_UI_ssovras.pages.base_page import BasePage
from test_UI_ssovras.pages.locators import *


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def verify_sorting(self, text):
        filter_title = self.find(sorting_title)
        expect(filter_title).to_have_text(text)

    def verify_item_is_presented(self, text):
        item = self.find(product_item)
        expect(item).to_have_text(text)
