import pytest
import requests
from test_data import new_pet_data

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def create_pet():
    response = requests.post(f"{BASE_URL}/pet", json=new_pet_data)
    assert response.status_code == 200, f"Не удалось создать питомца: {response.text}"
    pet = response.json()
    yield pet
    requests.delete(f"{BASE_URL}/pet/{pet['id']}")
