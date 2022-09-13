import requests
import pytest

base_url = "http://127.0.0.1:5000/device/"

@pytest.fixture
def setup():
    print("Inside Setup")

def test_fetching_existing_device(device_id="200"):
    response = requests.get( base_url + device_id)
    assert response.status_code == 200

def test_fetching_nf_profile_which_does_not_exist(device_id="800"):
    response = requests.get( base_url + device_id)
    assert response.status_code == 404

