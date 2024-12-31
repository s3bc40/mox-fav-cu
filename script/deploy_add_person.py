from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import Network, get_active_network


def deploy_favs_add() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    favorites_contract.add_person("Finley", 63)
    print(f"Person added: {favorites_contract.list_of_people(0)}")

    new_person: favorites.Person = favorites_contract.add_person("Marie", 5)
    print(f"New person: {favorites_contract.list_of_people(1)}")

    active_network: Network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()

    return favorites_contract


def moccasin_main() -> VyperContract:
    return deploy_favs_add()


if __name__ == "__main__":
    moccasin_main()
