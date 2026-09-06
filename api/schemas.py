from pydantic import BaseModel
from typing import Optional


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None


class CreateBookingResponse(BaseModel):
    bookingid: int
    booking: Booking


class AuthResponse(BaseModel):
    token: str


class GetBookingIdsResponse(BaseModel):
    bookingid: int