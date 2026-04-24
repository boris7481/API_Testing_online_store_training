import pytest
import json
import requests
from routes.Routes import Routes
from payloads.Payload import Payload

class TstProductAPI:
    @pytest.fixture(autouse=True)
    def __init__(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]