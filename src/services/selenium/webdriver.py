import os

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def start():
    """
        start selenium
    """
    try:
        driver = webdriver.Chrome("./src/services/selenium/chromedriver")
    except (RuntimeError, TypeError, NameError):
        print(NameError)
    

    return driver