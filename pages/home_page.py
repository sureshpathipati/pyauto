from pages.base_page import BasePage


SIGNINLOGIN = 'Sign Up/Log In'

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = (driver)

    def is_home_page(self):
        path = self.get_current_url_path()
        return path == '/'
    
    def is_guest_user(self):
        title = self.driver.find_element_by_class_name('pb-site-nav-link__title')
        return title == SIGNINLOGIN

    def click_create_link(self):
        main_section = self.main_link_section()
        create_link_button = main_section.find_element_by_xpath("//span[contains(text(),'Create')]")
        create_link_button.click()
        self.wait_for_page_to_load()

    def main_link_section(self):
        return self.driver.find_element_by_class_name('pb-site-header__nav-secondary')

    def is_login_poup(self):
        sign_in_ele = self.driver.find_element_by_css_selector('h1.pb-auth-modal__title')
        name = ""
        try:
            name = self.driver.find_element_by_id('auth-modal-email').get_attribute('name')
        except:
            print("Log In PopUp Not found")
        name_flag = name == 'username'
        sign_in_flag = sign_in_ele.text == SIGNINLOGIN
        return sign_in_flag and name_flag