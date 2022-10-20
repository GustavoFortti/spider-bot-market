import json

SEED_PATH = "./src/robot/target/__SUBPATH__/seed.json"

def read(target: str) -> dict:
    """
        Reads the provider search start file
    """

    file = open(target.replace("__SUBPATH__", f"{target}")).read()
    return json.loads(file)

def save_page(html: object) -> None:
    pass

def load_page(html: object) -> None:
    pass