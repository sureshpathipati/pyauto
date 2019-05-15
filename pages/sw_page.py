from pages.base_page import BasePage
from pages.create_page import CreatePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class SwPage:
	def __init__(self, driver):
		self.driver = driver

	def base_page(self):
		return BasePage(self.driver)

	def create_page(self):
		return CreatePage(self.driver)

	def home_page(self):
		return HomePage(self.driver)

	def login_page(self):
		return LoginPage(self.driver)

	def quit_browser(self):
		return self.driver.quit()