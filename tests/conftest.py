import pytest
from script.deploy import deploy_favorites
from script.deploy_add_person import deploy_favs_add


@pytest.fixture(scope="session")
def favorites_contract():
    return deploy_favorites()


@pytest.fixture(scope="session")
def favorites_add_contract():
    return deploy_favs_add()
