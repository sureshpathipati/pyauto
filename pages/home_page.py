from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = (driver)

    def is_home_page(self):
        path = self.get_current_url_path
        return path == '/'
    