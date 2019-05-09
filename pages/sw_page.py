from pages.base_page import BasePage
from pages.login_page import LoginPage

class SwPage:
	def __init__(self, driver):
		self.driver = driver

	def login_page(self):
		return LoginPage(self.driver)

	def base_page(self):
		return BasePage(self.driver)

	def quit_browser(self):
		return self.driver.quit()