import pytest
import allure
from api.schemas import AuthResponse

@pytest.mark.api
@allure.feature("auth_api")
@allure.story("Valid authentication")
def test_auth_returns_token(api_client):
    api_client.auth(username="admin", password="password123")
    assert api_client.token is not None
    assert len(api_client.token) > 0


@pytest.mark.api
@allure.feature("auth_api")
@allure.story("Valid authentication")
def test_auth_response_schema(api_client):
    response = api_client.session.post(
        f"{api_client.base_url}/auth",
        json={"username": "admin", "password": "password123"}
    )
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON
    )   
    parsed = AuthResponse(**response.json())
    assert parsed.token