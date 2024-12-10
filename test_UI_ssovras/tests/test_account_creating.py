import random


login_page_url = 'https://magento.softwaretestingboard.com/customer/account/'

def test_title_is_presented(account_creating):
    account_creating.open_page()
    account_creating.verify_header_text('Create New Customer Account')


def test_valid_form(account_creating):
    account_creating.open_page()
    account_creating.fill_form('first', 'last', f'123456{random.randint(1, 100)}@123.tt', 'Qwe123!@#')
    account_creating.submit_form()
    account_creating.verify_valid_form(login_page_url)


def test_invalid_form(account_creating):
    account_creating.open_page()
    account_creating.submit_form()
    account_creating.verify_invalid_form('This is a required field.')
