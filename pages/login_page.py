from pages.base_page import BasePage

class LoginPage(BasePage):
	
	def __init__(self, driver):
			self.driver = (driver)

	def login_with(self, data):
		return_hash = BasePage.return_data()
		self.driver.find_element_by_link_text("Sign Up/Log In").click()
		self.enter_email(data['email'])
		self.click_next()
		self.enter_password(data['password'])
		return return_hash

	def enter_email(self, email):
		self.enter_field("auth-modal-email", email)

	def enter_password(self, password):
		self.enter_field("auth-modal-password", password)

	def enter_field(self, id_attr, data):
		id_ele = self.driver.find_element_by_id(id_attr)
		id_ele.clear()
		id_ele.send_keys(data)

	def click_next(self):
		self.driver.find_element_by_xpath('//button[text()="Next"]').click()

	def login_error():
		pass

	def password_error():
		pass





