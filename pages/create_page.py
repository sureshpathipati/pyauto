from pages.base_page import BasePage
import pdb

create_new_book = 'Create New Book'
create_page_path = '/v0/editor/story/'

class CreatePage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def is_create_page(self):
        self.wait_for_page_to_load()
        create_path = self.get_current_url_path()
        return create_path.startswith(create_page_path)

    def is_new_story_popup(self):
        story_form = self.story_form()
        heading_title = story_form.find_element_by_class_name('heading-title')
        return heading_title.text == create_new_book

    def fill_new_book_popup(self, new_book):
        self.wait_for_page_to_load()
        if not self.is_new_story_popup():
            raise Exception("Create new story popup not found!")
        story_form = self.story_form()
        story_form.find_element_by_id('story_title').send_keys(new_book["title"])
        start_with_words = story_form.find_element_by_xpath('//input[@value="start with words"]')
        start_with_words.click()

    def click_publish(self):
        ele_params = {'attribute_value': '//a[@id="publish"]'}
        publish_button = self.explicit_element(ele_params)
        publish_button.click()

    def story_form(self):
        return self.driver.find_element_by_id('newStoryForm')

    def is_validation_error(self):
        flag = False
        try:
            error_popup = self.driver.find_element_by_css_selector('span#ui-id-5')
            flag = error_popup.text == 'Validation Errors'
        except:
            print("No Validation error popup present")
        return flag