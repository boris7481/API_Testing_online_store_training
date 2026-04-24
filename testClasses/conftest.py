import pytest
from routes.Routes import Routes

@pytest.fixture(scope="class")
def setup():
    base_url = Routes.BASE_URL