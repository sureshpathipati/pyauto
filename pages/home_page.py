from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = (driver)

    def is_home_page(self):
        path = self.get_current_url_path()
        return path == '/'
    
    def is_guest_user(self):
        title = self.driver.find_element_by_class_name('pb-site-nav-link__title')
        return title == 'Sign Up/Log In'