from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse
import time

class BasePage():
    
    PAGE_LOAD_WAIT_INTERVAL = 2
    PAGE_LOAD_COUNTER = 5

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        """
        To navigate to respective url passed
        """
        self.driver.get(url)
        self.wait_for_page_to_load()

    def get_current_url_path(self):
        """
        Returns the current url path the page
        Input : N/A
        Output : String
        """
        url = self.driver.current_url
        url = urlparse(url)
        return url.path

    def wait_for_page_to_load(self):
        """
        Waits for the page to Load completely
        if Page takes more than Counter*Interval, it raises an Expection 
        """
        counter = self.PAGE_LOAD_COUNTER
        while(counter > 0):
            page_state = self.driver.execute_script('return document.readyState;' ) 
            if(page_state == 'complete'): return True
            time.sleep(self.PAGE_LOAD_WAIT_INTERVAL)
            counter-=1
        raise Exception("Timeout! Page taking long time to load")

    def return_data(self):
        return {
            'error': False,
            'success': True,
            'error_message': "",
            'details': []
        }

    def is_slim_notification(self):
        self.has_css('pb-slim-notification')

    def wait_until_for(self,ele,waitTime=10):
        pass
        # return WebDriverWait(self.driver, waitTime).until()

    def click_ele_by_xpath(self, xpath_attr):
        try:
            ele = self.driver.find_element_by_xpath(xpath_attr)
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