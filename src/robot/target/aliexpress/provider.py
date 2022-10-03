from urllib import response
import requests

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
    page = seed['url']['page']
    index = seed['url']['index']
    max_index = seed['url']['max_index']
    pattern = seed['url']['pattern']
    
    next = True
    while (next):
        resp = get_page(page)

        current_index = f"{pattern}{index}"
        index += 1
        next_index = f"{pattern}{index}"
        page = page.replace(current_index, next_index)

        next = lost_seed(resp, index, max_index)

def get_page(url: str) -> bool:
    response = requests.get(url)
    print(response.text)
    return None

def get_products(r):
    pass

def get_provider():
    pass

def lost_seed(resp: str, index: int, max_index: int = 1) -> bool:
    return False
    if (index == max_index): return False
    return True