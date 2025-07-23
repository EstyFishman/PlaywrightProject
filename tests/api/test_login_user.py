import pytest
from api_requests.users_request_generator import UsersRequestGenerator
from dotenv import load_dotenv

load_dotenv()

users_request_generator = UsersRequestGenerator()


@pytest.mark.api
def test_login():
    response = users_request_generator.login({
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })

    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"
    users_request_generator.validate_status_code(response, 200)
