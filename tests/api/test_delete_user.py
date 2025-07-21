import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_delete_user():
    response = users_request_generator.delete_user(2)
    users_request_generator.validate_status_code(response, 204)
