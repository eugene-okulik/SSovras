import pytest
from playwright.sync_api import BrowserContext
from test_UI_ssovras.pages.account_creating import AccountCreate
from test_UI_ssovras.pages.eco_friendly import EcoFriendly
from test_UI_ssovras.pages.sale import Sale


@pytest.fixture()
def account_creating(page):
    return AccountCreate(page)


@pytest.fixture()
def eco_friendly(page):
    return EcoFriendly(page)


@pytest.fixture()
def sale(page):
    return Sale(page)


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
