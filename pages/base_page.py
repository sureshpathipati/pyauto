from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        """
        To navigate to respective url passed
        """
        self.driver.get(url)

    def return_data(self):
        return {
            'error': False,
            'success': True,
            'error_message': "",
            'details': []
        }

    def wait_for_ele(self,ele,waitTime=10):
        pass
        # try:
        # 	WebDriverWait(self.driver, waitTime).until( expected_conditions.presence_of_element_located((By.ID, "myDynamicElement")))
        # return True

    def click_ele_by_xpath(self, xpath_attr):
        try:
            ele = self.driver.find_element_by_xpath(xpath_attr)
            if not ele.is_enabled(): print("Element with attribute {} id disabled".format(xpath_attr))
            ele.click()
        except NoSuchElementException:
            print("Element with attribute {} not found".format(xpath_attr))

    def has_css(self, css_value):
        """
        To check page has respective Css
        It doesnot add to webdriver hence chaining with webelement throws error
        returns Boolean
        """
        return has_attribute_checker("css", css_value)

    def has_xpath(self, xpath_value):
        """
        To check page has respective Xpath
        It doesnot add to webdriver hence chaining with webelement throws error
        returns Boolean
        """
        return has_attribute_checker("xpath", xpath_value)

    def has_attribute_checker(self, attribute, value):
        """
        General Method to check attribute is present in the page or not
        returns Boolean
        """
        try:
            function_name = "find_element_by_{}".forrmat(attribute)
            getattr(self.driver, function_name)(value)
        except NoSuchElementException:
            return False
        return True