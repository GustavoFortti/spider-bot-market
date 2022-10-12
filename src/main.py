import datetime

from robot.target_manager import run

def main():

    # robo executado
    target = "aliexpress" 
    # provider - busca por fornecedores 
    # product - busca os produtos dos fornecedores
    job_type = "provider"

    # o robo esta atualizado?
    # tempo que leva para mapear

    run(target, job_type)


if __name__ == "__main__":
    main()