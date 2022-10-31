from page import map_page

def start(head: dict, job_type: str):
    """
    """
    head['table'] = F"{head['job_name']}_{job_type}"
    head['target'] = getattr(__import__(f"{job_type}"), f"get_{job_type}")

    data = map_page(head)

    head['storage_save'](data)
