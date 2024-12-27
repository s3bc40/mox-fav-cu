import pytest
from script.deploy import deploy_favorites

@pytest.fixture(scope="session")
def favorites_contract():
    return deploy_favorites()