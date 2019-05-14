import pytest
from config.browser_setup import browser_setup
from pages.sw_page import SwPage

DEFAULT_TIMEOUT = 10

# @pytest.fixture(scope='module')
@pytest.fixture(scope='session')
def setUp(request):
	driver = browser_setup()
	driver.implicitly_wait(DEFAULT_TIMEOUT)
	driver.set_page_load_timeout(20)
	sw = SwPage(driver)
	return sw

	# def take_screenshot():
	# 	driver.save_screenshot("{}.png".format(request.function.__name__))
	# request.addfinalizer(take_screenshot)
	# return sw


def take_screenshot(request):
	driver.save_screenshot(request.node.name)