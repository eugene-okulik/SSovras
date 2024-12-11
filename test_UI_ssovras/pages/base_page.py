from playwright.sync_api import Page, expect, Locator
from test_UI_ssovras.pages.locators import title_locator


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator) -> Locator:
        return self.page.locator(locator).locator('nth=0')

    def verify_header_text(self, text):
        header_test_text = self.find(title_locator)
        expect(header_test_text).to_have_text(text)
        # assert header_test_text == text, "The text in the header isn't correct"

    # def find_and_scroll_to_element(self, locator):
    #    page_element = self.find(*locator)
    #    self.page.execute_script("arguments[0].scrollIntoView(true);", page_element)
    #    return page_element

    def send_keys(self, locator, keys):
        element = self.find(locator)
        element.fill(keys)
