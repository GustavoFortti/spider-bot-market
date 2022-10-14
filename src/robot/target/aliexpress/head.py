from storage import storage
from robot.layout.page import map_page

HEAD = {
    "job_name": "aliexpress",
    "storage_read": storage.read_pandas,
    "storage_save": storage.write_pandas,
    "page_parser": "beautiful_soup"
}

def run(job_type: str):

    HEAD['table'] = F"{HEAD['job_name']}_{job_type}"
    HEAD['target'] = getattr(__import__(f"{job_type}"), f"get_{job_type}")

    data = map_page(HEAD)

    HEAD['storage_save'](data)