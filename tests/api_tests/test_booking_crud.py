from urllib import response

import allure
import pytest
from api.schemas import CreateBookingResponse, GetBookingIdsResponse


@pytest.fixture
def booking_payload():
    return {
        "firstname": "Ivan",
        "lastname": "Petrov",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-10",
            "checkout": "2026-09-15"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture
def existing_booking_id(api_client):
    response = api_client.get_bookings();
    booking_ids = response.json()
    return booking_ids[0]["bookingid"]

@pytest.mark.api
@allure.feature("booking_api")
@allure.story("Get bookings")
def test_get_bookings(api_client):
    response = api_client.get_bookings();
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON
    )
    assert response.status_code == 200;
    booking_ids = response.json();
    assert isinstance(booking_ids, list);
    if booking_ids:
        parsed = [GetBookingIdsResponse(**booking) for booking in booking_ids];
        assert all(isinstance(booking.bookingid, int) for booking in parsed);


@pytest.mark.api
@allure.feature("booking_api")
@allure.story("Create booking")
def test_create_booking(api_client, booking_payload):
    response = api_client.create_booking(booking_payload);
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON
    )
    parsed = CreateBookingResponse(**response.json());
    assert response.status_code == 200;
    assert parsed.booking.firstname == booking_payload["firstname"];
    assert parsed.booking.lastname == booking_payload["lastname"]; 
    assert parsed.booking.totalprice == booking_payload["totalprice"];

@pytest.mark.api
@allure.feature("booking_api")
@allure.story("Get booking by ID")
def test_get_booking(api_client, existing_booking_id):
    response = api_client.get_booking(existing_booking_id);
    allure.attach(
        response.text,
        name="Response body",
        attachment_type=allure.attachment_type.JSON
    )
    assert response.status_code == 200;

@pytest.mark.api
@allure.feature("booking_api")
@allure.story("Update booking")
def test_update_booking(api_client,booking_payload):
    response = api_client.create_booking(booking_payload)
    created = response.json()
    allure.attach(
            response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
    booking_id = created["bookingid"]
    api_client.auth(username="admin", password="password123")
    updated_payload = {**booking_payload,
                       "firstname": "UpdatedName",
                       "lastname": "UpdatedLastName",
                       "depositpaid": False,
                       "bookingdates": {
                           "checkin": "2026-09-18",
                           "checkout": "2026-09-27"
                       },
                       "totalprice": 250, "additionalneeds": "Lunch"}
    response = api_client.update_booking(booking_id, updated_payload)
    assert response.status_code == 200
    assert response.json() == updated_payload

@pytest.mark.api
@allure.feature("booking_api")
@allure.story("Delete booking")
def test_delete_booking(api_client, booking_payload):
    response = api_client.create_booking(booking_payload)
    created = response.json()
    allure.attach(
            response.text,
            name="Response body",
            attachment_type=allure.attachment_type.JSON
        )
    booking_id = created["bookingid"]
    api_client.auth(username="admin", password="password123")
    response = api_client.delete_booking(booking_id)
    assert response.status_code == 201
    # Проверка того, что запись удалена
    get_response = api_client.get_booking(booking_id)
    
    assert get_response.status_code == 404