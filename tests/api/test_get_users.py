import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
@pytest.mark.parametrize("page, expected", [
    (1, 200),
    (2, 200),
])
def test_get_users_list(page, expected):
    response = users_request_generator.get_users(page=page)
    print(f"GET Users Status: {response.status_code}")
    users_request_generator.validate_status_code(response, expected)
    assert len(response.json()["data"]) > 0

