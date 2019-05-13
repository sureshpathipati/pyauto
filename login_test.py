import pytest

def test_login_page(setUp):
	browser = setUp
	basePage = browser.base_page()
	basePage.navigate_to_url("https://dev.pbees.party")
	loginPage = browser.login_page()
	user_details = {"email": "psureshkumarece@gmail.com", "password": "password"}
	loginPage.login_with(user_details)
	
