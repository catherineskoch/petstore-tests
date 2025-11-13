import requests
import pytest
from test_data import new_pet_data, updated_pet_data
import time

def test_get_pets_by_status(base_url):
    status = "available"
    response = requests.get(f"{base_url}/pet/findByStatus", params={"status": status})
    assert response.status_code == 200
    pets = response.json()
    assert isinstance(pets, list)
    if pets:
        for pet in pets:
            assert "id" in pet
            assert pet["status"] == status

def test_create_pet(base_url):
    response = requests.post(f"{base_url}/pet", json=new_pet_data)
    assert response.status_code == 200
    pet = response.json()
    assert pet["id"] == new_pet_data["id"]
    assert pet["name"] == new_pet_data["name"]
    assert pet["status"] == new_pet_data["status"]
    requests.delete(f"{base_url}/pet/{new_pet_data['id']}")

def test_update_pet(base_url, create_pet):
    updated_pet_data["id"] = create_pet["id"]
    response = requests.put(f"{base_url}/pet", json=updated_pet_data)
    assert response.status_code == 200
    pet = response.json()
    assert pet["id"] == updated_pet_data["id"]
    assert pet["name"] == updated_pet_data["name"]
    assert pet["status"] == updated_pet_data["status"]

def test_delete_pet(base_url):
    response_create = requests.post(f"{base_url}/pet", json=new_pet_data)
    pet = response_create.json()
    time.sleep(10)
    response_delete = requests.delete(f"{base_url}/pet/{pet['id']}")
    assert response_delete.status_code == 200
    response_get = requests.get(f"{base_url}/pet/{pet['id']}")
    assert response_get.status_code == 404

