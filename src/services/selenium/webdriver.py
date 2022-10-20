import time
from selenium import webdriver

def start(url: str) -> object:
    """
        start selenium
    """
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = webdriver.Chrome("./src/services/selenium/module/chromedriver", chrome_options=options)
        print(f"log - get {url}")
        driver.get(url)
        status = 200

        html = driver.page_source

        print("log - time 2")
        time.sleep(2)

        driver.close()
        print("log - driver closed")
    except (RuntimeError, TypeError, NameError):
        status = None
        print(f"log - NameError")
    
    return status, html