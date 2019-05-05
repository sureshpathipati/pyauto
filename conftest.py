import pytest
from selenium.webdriver import Chrome
from pages.sw_page import SwPage

@pytest.fixture(scope='module')
def setUp(request):
	driver = Chrome("/Users/suresh/workspace/pyauto/drivers/chromedriver")
	driver.implicitly_wait(5)
	sw = SwPage(driver)
	return sw

@pytest.fixture(autouse=True)
def webdriver(request):
	pass
