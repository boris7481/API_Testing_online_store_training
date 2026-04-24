import pytest
from routes.Routes import Routes
from utils.ConfigReader import ReadConfig


@pytest.fixture(scope="class")
def setup():
#    base_url = Routes.BASE_URL
#    config_reader = ReadConfig

    yield {"bsae_url":Routes.BASE_URL, "config_reader":ReadConfig}