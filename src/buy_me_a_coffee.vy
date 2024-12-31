# pragma version 0.4.0
"""
@license MIT
@title Buy Me A Coffee!
@author You!
@notice This contract is for creating a sample funding contract
"""

# We'll learn a new way to do interfaces later...
interface AggregatorV3Interface:
    def decimals() -> uint8: view
    def description() -> String[1000]: view
    def version() -> uint256: view
    def latestAnswer() -> int256: view


# Constants & Immutables
MINIMUM_USD: public(constant(uint256)) = as_wei_value(5, "ether")
PRICE_FEED: public(
    immutable(AggregatorV3Interface)
)  # 0x694AA1769357215DE4FAC081bf1f309aDC325306 sepolia
PRECISION: constant(uint256) = 1 * (10**18)

# Storage
owner: public((address))
funders: public(DynArray[address, 1000])
funder_to_amount_funded: public(HashMap[address, uint256])

# With constants: 262,853
@deploy
def __init__(price_feed: address):
    PRICE_FEED = AggregatorV3Interface(price_feed)
    self.owner = msg.sender


@external
@payable
def fund():
    self._fund()


@internal
@payable
def _fund():
    """Allows users to send $ to this contract
    Have a minimum $ amount to send

    How do we convert the ETH amount to dollars amount?
    """
    usd_value_of_snx: uint256 = self._get_usd_rate(msg.value)
    assert usd_value_of_snx >= MINIMUM_USD, "You must spend more SNX!"
    self.funders.append(msg.sender)
    self.funder_to_amount_funded[msg.sender] += msg.value


@external
def withdraw():
    """Take the money out of the contract, that people sent via the fund function.

    How do we make sure only we can pull the money out?
    """
    assert msg.sender == self.owner, "Not the contract owner!"
    raw_call(self.owner, b"", value=self.balance)
    # send(self.owner, self.balance)
    # resetting
    for funder: address in self.funders:
        self.funder_to_amount_funded[funder] = 0
    self.funders = []


@view
@internal
def _get_usd_rate(amount: uint256) -> uint256:
    """
    Chris sent us 0.01 ETH for us to buy a coffee
    Is that more or less than $5?
    """
    price: int256 = staticcall PRICE_FEED.latestAnswer()
    token_price: uint256 = (convert(price, uint256)) * (10**10)
    token_amount_in_usd: uint256 = (token_price * amount) // PRECISION
    return token_amount_in_usd  # 18 0's, 18 decimal places


@view
@external
def get_usd_rate(amount: uint256) -> uint256:
    return self._get_usd_rate(amount)


@view
@external
def get_balance() -> uint256:
    balance: uint256 = 0
    for funder_address: address in self.funders:
        balance += self.funder_to_amount_funded[funder_address]
    return balance


@external
def change_owner(_new_owner: address):
    assert msg.sender == self.owner, "Not the contract owner!"
    self.owner = _new_owner


@external
@payable
def __default__():
    self._fund()


# @external
# @view
# def get_price() -> int256:
#     price_feed: AggregatorV3Interface = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306)
#     # ABI
#     # Addresss
#     return staticcall price_feed.latestAnswer()

# 4 / 2 = 2
# # 6 / 3 = 2
# # 7 / 3 = 2 (remove all decimals)
# @external
# @view
# def divide_me(number: uint256) -> uint256:
#     return number // 3


