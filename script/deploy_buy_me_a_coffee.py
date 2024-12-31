from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network, Network
from src import buy_me_a_coffee
import boa

# Constants
SNX_USD_PRICE_FEED_ADDRESS = "0xc0F82A46033b8BdBA4Bb0B0e28Bc2006F64355bC"
SNX_WEI_AMOUNT = 5 * (10**18)


def deploy_buy_me_a_coffee() -> VyperContract:
    print("Deploying buy_me_a_coffee contract with SNX/USD...")
    contract = buy_me_a_coffee.deploy(SNX_USD_PRICE_FEED_ADDRESS)

    # Get SNX/USD rate
    snx_to_usd_rate = contract.get_usd_rate(SNX_WEI_AMOUNT)
    print(f"{SNX_WEI_AMOUNT} SNX to USD rate: {snx_to_usd_rate}")

    # Fund the contract
    old_balance: uint256 = contract.get_balance()
    print(f"Current contract balance: {old_balance}")
    contract.fund(value=SNX_WEI_AMOUNT)
    contract.fund(value=SNX_WEI_AMOUNT)
    new_balance: uint256 = contract.get_balance()
    print(f"New contract balance: {new_balance}")

    # Change ownership
    print(f"Current contract owner: {contract.owner()}")
    new_owner = boa.env.generate_address()
    contract.change_owner(new_owner)
    print(f"New contract owner: {contract.owner()}")

    # Select network
    active_network: Network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(contract)
        result.wait_for_verification()

    return contract


def moccasin_main() -> VyperContract:
    return deploy_buy_me_a_coffee()


if __name__ == "__main__":
    moccasin_main()
