import pytest
import time

base_url = 'https://dev.pbees.party'
user_details = {"email": "psureshkumarece@gmail.com", "password": "password"}

# base_url = 'https://storyweaver.org.in/'

def test_guest_create(setUp):
    browser = setUp
    basePage = browser.base_page()
    homePage = browser.home_page()
    basePage.navigate_to_url(base_url)
    homePage.click_create_link()
    assert homePage.is_login_poup() == True

def test_create_story_without_images(setUp):
    browser = setUp
    basePage = browser.base_page()
    loginPage = browser.login_page()
    homePage = browser.home_page()
    createPage = browser.create_page()
    basePage.navigate_to_url(base_url)
    time.sleep(5)
    loginPage.login_with(user_details)
    basePage.wait_for_page_to_load()
    time.sleep(2)
    homePage.click_create_link()
    time.sleep(2)
    assert createPage.is_create_page() == True
    new_book_data = {'title': 'suresh'}
    createPage.fill_new_book_popup(new_book_data)
    time.sleep(5)
    createPage.click_publish()
    time.sleep(5)
    error_flag = createPage.is_validation_error()
    assert error_flag == True