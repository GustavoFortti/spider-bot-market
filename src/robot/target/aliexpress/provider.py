

def get_provider(driver: str) -> None:
    # print(driver)
    html = driver.find_all(class_ = "right-menu")
    print(html)