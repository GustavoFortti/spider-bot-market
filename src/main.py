import datetime

from robot import target_manager

def main():
    
    # robo executado
    target = "aliexpress" 
    # provider - busca por fornecedores 
    # product - busca os produtos dos fornecedores
    job_type = "provider"

    # o robo esta atualizado?
    # tempo que leva para mapear

    target_manager.run(target, job_type)


if __name__ == "__main__":
    main()