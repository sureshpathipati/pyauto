from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from pathlib import Path

parent_dir = Path(__file__).resolve().parent

def browser_setup():
    return firefox_browser()
    # which_browser = resolve_browser()
    # browser = which_browser
    # return browser_instance


def firefox_browser():
    return Firefox(executable_path=parent_dir+'/drivers/geckodriver')

def chrome_browser():
    return Chrome(executable_path=parent_dir+'/drivers/chromedriver')