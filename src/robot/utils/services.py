import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def beautiful_soup(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def selenium(url: str):
    driver = webdriver.Chrome()
    return driver.get(url)
