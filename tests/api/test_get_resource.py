import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_get_resource():
    response = users_request_generator.get_user_by_id(23)
    users_request_generator.validate_status_code(response, 404)
