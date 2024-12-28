from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network, Network
from src import favorites


def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number is {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"Ending number is {ending_number}")

    active_network: Network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()

    return favorites_contract


def moccasin_main() -> VyperContract:
    return deploy_favorites()


if __name__ == "__main__":
    moccasin_main()

# Deploy on sepolia
