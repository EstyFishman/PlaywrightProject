import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_get_user_with_generator():
    response = users_request_generator.get_user_by_id(2)
    print(f"GET Status: {response.status_code}")
    users_request_generator.validate_status_code(response, 200)
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["first_name"] == "Janet"
