import pytest

base_url = 'https://dev.pbees.party'

def test_guest_create(setUp):
    browser = setUp
    basePage = browser.base_page()
    homePage = browser.home_page()
    basePage.navigate_to_url(base_url)
    homePage.click_create_link()
    # assert homePage.is_login_poup() == True