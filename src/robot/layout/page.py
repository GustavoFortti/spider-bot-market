
import requests
import pandas as pd

from utils import seed
from services.selenium import webdriver
from bs4 import BeautifulSoup

def map_page(head: dict) -> object:
    """
        Maps the site to search for information about providers
    """
    df = head['storage_read'](table=head['table'])
    pages = seed.read(head['job_name'])


    for page in pages["seed"]:
        try:
            data_page = map_seed(page, head, df.columns)
            df = pd.concat([df, data_page])
            break
        except (RuntimeError, TypeError, NameError):
            print(f"log - NameError")
        break

def map_seed(seed: str, head: dict, columns: list) -> object:
    url = seed['page']['url']
    index = seed['page']['index']
    max_index = seed['page']['max_index']
    pattern = seed['page']['pattern']

    df = pd.DataFrame(columns=columns)

    next = True
    while (next):
        status, resp = page_reader(url, head['page_parser'])
    
        data_provider = head['target'](head, resp)
        df = pd.concat([df, data_provider])

        current_index = f"{pattern}{index}"
        index += 1
        next_index = f"{pattern}{index}"
        url = url.replace(current_index, next_index)

        next = is_seed_over(status, index, max_index)
        break

def page_reader(url: str, parser: str) -> list:
    option = {
        "beautiful_soup": beautiful_soup,
        "selenium": selenium
    }

    try:
        url = parse_url(url)
        status, resp = option[parser](url)
    except (RuntimeError, TypeError, NameError):
        print(f"log - {TypeError}")

    return status, resp

def beautiful_soup(url: str) -> object:
    response = requests.get(url)
    return response.status_code, BeautifulSoup(response.text, 'html.parser')

def selenium(url: str) -> object:
    status, html = webdriver.start(url)
    element = BeautifulSoup(html, 'html.parser')
    return status, element

def parse_url(url: str):
    ref = "https:"
    if (not (url[:6] == ref)):
        return f"{ref}{url}"

def is_seed_over(status: str, index: int, max_index: int = 1) -> bool:
    if ((index == max_index) | (status != 200)): return False
    return True