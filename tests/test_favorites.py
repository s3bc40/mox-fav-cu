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


def test_stating_name_to_favorite_number(favorites_add_contract):
    # Arrange
    expected_name_at_index_0 = "Finley"
    expected_favorite_number_at_index_0 = 63
    expected_name_at_index_1 = "Marie"
    expected_favorite_number_at_index_1 = 5

    # Act
    person_at_index_0 = favorites_add_contract.list_of_people(0)
    person_at_index_1 = favorites_add_contract.list_of_people(1)

    # Assert
    assert (
        expected_name_at_index_0 == person_at_index_0[1]
        and expected_favorite_number_at_index_0 == person_at_index_0[0]
    )
    assert (
        expected_name_at_index_1 == person_at_index_1[1]
        and expected_favorite_number_at_index_1 == person_at_index_1[0]
    )


# def test_stating_value_two():
#     favorites_contract = favorites.deploy()
#     assert favorites_contract.retrieve() == 7
