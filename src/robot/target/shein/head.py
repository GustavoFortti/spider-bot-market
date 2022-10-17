from storage import storage
from robot.layout.page_manager import map_page

HEAD = {
    "job_name": "shein",
    "storage": storage.read_pandas,
    "page_parser": "beautiful_soup"
}

def run(job_type: str):

    HEAD['table'] = F"{HEAD['job_name']}_{job_type}"
    HEAD['target'] = getattr(__import__(f"{job_type}"), f"get_{job_type}")

    map_page(HEAD)