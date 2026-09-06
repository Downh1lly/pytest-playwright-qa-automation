import pytest
from api.schemas import AuthResponse

@pytest.mark.api
def test_auth_returns_token(api_client):
    api_client.auth(username="admin", password="password123")
    assert api_client.token is not None
    assert len(api_client.token) > 0


@pytest.mark.api
def test_auth_response_schema(api_client):
    response = api_client.session.post(
        f"{api_client.base_url}/auth",
        json={"username": "admin", "password": "password123"}
    )
    parsed = AuthResponse(**response.json())
    assert parsed.token