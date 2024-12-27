from src import favorites
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contact: VyperContract = favorites.deploy()
    starting_number: int = favorites_contact.retrieve()
    print(f"Starting number is {starting_number}")

    favorites_contact.store(77)
    ending_number: int = favorites_contact.retrieve()
    print(f"Ending number is {ending_number}")
    return favorites_contact

def moccasin_main() -> VyperContract:
    return deploy_favorites()

if __name__ == "__main__":
    moccasin_main()
