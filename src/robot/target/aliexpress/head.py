from services.storage import storage
from robot.layout import spider

HEAD = {
    "job_name": "aliexpress",
    "storage_read": storage.read_pandas,
    "storage_save": storage.write_pandas,
    "page_parser": "selenium"
}

run = lambda job_type: spider.start(HEAD, job_type)