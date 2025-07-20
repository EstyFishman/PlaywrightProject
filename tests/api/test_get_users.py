import pytest
import requests
import pytest_check as check
from api_requests.users_request_generator import UsersRequestGenerator
import os
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


# Without Generator
@pytest.mark.api
def test_get_user():
    headers = {"x-api-key": os.getenv("X_API_KEY")}
    response = requests.get("https://reqres.in/api/users/2", headers=headers)

    # Soft Validation
    # check.equal(response.status_code, 200)
    # check.equal(response.json()["data"]["id"], 3)
    # check.equal(response.json()["data"]["first_name"], "Janetttttt")

    # Hard Validation
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["first_name"] == "Janet"


# With Generator
@pytest.mark.api
def test_get_user_with_generator():
    response = users_request_generator.get_user(2)

    # Soft Validation
    # check.equal(response.status_code, 200)
    # check.equal(response.json()["data"]["id"], 3)
    # check.equal(response.json()["data"]["first_name"], "Janetttttt")

    # Hard Validation
    users_request_generator.validate_status_code(response, 200)
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["first_name"] == "Janet"
