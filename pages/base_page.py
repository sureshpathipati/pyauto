
class BasePage():

		def __init__(self, browser):
				self.browser = browser

		def navigate_to_url(self, url):
				self.browser.get(url)

		def return_data(self):
				return {
					'error': False,
					'success': True,
					'error_message': "",
					'details': []
				}