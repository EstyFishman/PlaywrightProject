import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_update_user():
    response = users_request_generator.update_user(2, {
        "name": "morpheus",
        "job": "zion resident"
    })
    users_request_generator.validate_status_code(response, 200)
    response_json = response.json()
    assert response_json["name"] == "morpheus"
    assert response_json["job"] == "zion resident"
    assert "updatedAt" in response_json
