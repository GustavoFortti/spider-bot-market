import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from storage import storage
from utils import seed

from head import INFO

def map():
    """
        Maps the site to search for information about providers
    """

    df = storage.read_pandas(table="provider")
    # print(df)
    # ler arquivo com fornecedores

    # iniciar busca por produtos
    # print('flag')
    pages = seed.read(INFO['job_name'])
    
    for page in pages["seed"]:
        try:
            map_seed(page)
        except (RuntimeError, TypeError, NameError):
            pass
        break
    # requests.get(seeds)
    # print(file)

    # encontrar vendedor do produto

    # fazer verificações

    # armazzenar dados do fornecedor

    pass

def map_seed(seed: str):
    url = seed['page']['url']
    index = seed['page']['index']
    max_index = seed['page']['max_index']
    pattern = seed['page']['pattern']
    
    next = True
    while (next):
        resp = get_html(url)
    
        current_index = f"{pattern}{index}"
        index += 1
        next_index = f"{pattern}{index}"
        url = url.replace(current_index, next_index)

        next = is_seed_over(resp, index, max_index)

def get_html(url: str, parser: str) -> bool:
    option = {
        "beautiful_soup": beautiful_soup,
        "selenium": selenium
    }

    return option[parser](url)

def beautiful_soup(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def selenium(url: str):
    driver = webdriver.Chrome()
    return driver.get(url)

def get_products(r):
    pass

def get_provider():
    pass

def is_seed_over(resp: str, index: int, max_index: int = 1) -> bool:
    return False
    if (index == max_index): return False
    return True