import pytest
import requests
from api_requests.users_request_generator import UsersRequestGenerator
import os
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_create_user():
    response = users_request_generator.create_user({
        "name": "morpheus",
        "job": "leader"
    })
    users_request_generator.validate_status_code(response, 201)
    response_json = response.json()
    assert response_json["name"] == "morpheus"
    assert response_json["job"] == "leader"
    assert "id" in response_json
    assert "createdAt" in response_json
