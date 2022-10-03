from robot.target.aliexpress import provider

def run():
    # log information
    target = "aliexpress"
    type_job = "map_provider"

    print(f"target - {target}")
    print(f"type - {type_job}")

    # running

    print("running...\n")
    provider.map()