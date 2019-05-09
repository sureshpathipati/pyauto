from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

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

    def wait_until_for(self,ele,waitTime=10):
        pass
        # return WebDriverWait(self.driver, waitTime).until()

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
        It doesnot add to webdriver hence chaining with web-element throws error
        returns Boolean
        """
        return self.has_attribute_checker("css", css_value)

    def has_xpath(self, xpath_value):
        """
        To check page has respective Xpath
        It doesnot add to webdriver hence chaining with web-element throws error
        returns Boolean
        """
        return self.has_attribute_checker("xpath", xpath_value)
    
    def has_id(self, id_value):
        """
        To check page has respective ID
        It doesnot add to webdriver hence chaining with web-element throws error
        returns Boolean
        """
        return self.has_attribute_checker("id", id_value)

    def has_attribute_checker(self, attribute, value):
        """
        General Method to check attribute is present in the page or not
        returns Boolean
        """
        try:
            ele_dict = { "id": By.ID, "xpath": By.XPATH, "css": By.CSS_SELECTOR }
            WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((ele_dict[attribute], value)) )
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True