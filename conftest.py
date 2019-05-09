import pytest
from config.browser_setup import browser_setup
from pages.sw_page import SwPage

DEFAULT_TIMEOUT = 10

@pytest.fixture(scope='module')
def setUp(request):
	driver = browser_setup()
	driver.implicitly_wait(DEFAULT_TIMEOUT)
	sw = SwPage(driver)
	return sw
