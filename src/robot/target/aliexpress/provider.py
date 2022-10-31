from layout.page import page_reader

def get_provider(head: dict, element: object) -> None:
    urls = get_random_products(element)

    status, resp = page_reader(urls[0], head['page_parser'])

    print(resp)


def get_random_products(element: object) -> None:
    items = element.find_all("a", {"class": "_3t7zg _2f4Ho"}, href=True)
    return [i['href'] for i in items]