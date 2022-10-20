import importlib

def run(target: str, job_type: str):
    job = importlib.import_module(f"robot.target.{target}.head")
    
    print(f"log - target - {target}")
    print(f"log - type - {job_type}")
    job.run(job_type)