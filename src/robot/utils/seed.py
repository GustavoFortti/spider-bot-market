import json

def read(target: str) -> dict:
    """
        Reads the provider search start file
    """

    file = open(f"./src/robot/target/{target}/seed.json").read()
    return json.loads(file)