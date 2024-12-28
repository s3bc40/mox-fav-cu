# from src import favorites
def test_stating_value(favorites_contract):
    assert favorites_contract.retrieve() == 77


def test_can_change_value(favorites_contract):
    # Arrange
    # Act
    favorites_contract.store(99)
    # Assert
    assert favorites_contract.retrieve() == 99


def test_can_add_people(favorites_contract):
    # Arrange
    new_person = "Hector"
    favorite_number = 16

    # Act
    favorites_contract.add_person(new_person, favorite_number)

    # Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)


# def test_stating_value_two():
#     favorites_contract = favorites.deploy()
#     assert favorites_contract.retrieve() == 7
