from services.storage import storage
from robot.layout import page_manager

HEAD = {
    "job_name": "aliexpress",
    "storage_read": storage.read_pandas,
    "storage_save": storage.write_pandas,
    "page_parser": "beautiful_soup"
}

run = lambda job_type: page_manager.run(HEAD, job_type)