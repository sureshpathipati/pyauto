import pytest

base_url = 'https://dev.pbees.party'

def test_login_page(setUp):
	browser = setUp
	basePage = browser.base_page()
	loginPage = browser.login_page()
	homePage = browser.home_page()
	basePage.navigate_to_url(base_url)
	user_details = {"email": "psuresh@gmail.com", "password": ""}
	loginPage.login_with(user_details)
	notification_message = homePage.notification_text()
	assert loginPage.is_login_successful(notification_message) == True
	assert homePage.is_home_page() == True
	assert homePage.is_guest_user() == False
	
	
	

	
