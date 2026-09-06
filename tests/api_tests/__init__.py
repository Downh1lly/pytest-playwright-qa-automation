"""Reusable client helpers for the Restful Booker API."""

from __future__ import annotations

from typing import Any, Mapping

import requests


class RestfulBookerClient:
	"""Client for the endpoints documented at /apidoc/."""

	def __init__(self, base_url: str = "https://restful-booker.herokuapp.com") -> None:
		self.base_url = base_url.rstrip("/")
		self.session = requests.Session()
		self.session.headers.update({"Accept": "application/json"})

	def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
		response = self.session.request(
			method, f"{self.base_url}/{path.lstrip('/')}", **kwargs
		)
		response.raise_for_status()
		return response

	def authenticate(self, username: str = "admin", password: str = "password123") -> str:
		token = self.request(
			"POST", "/auth", json={"username": username, "password": password}
		).json()["token"]
		self.session.cookies.set("token", token)
		return token

	def list_bookings(self, **filters: Any) -> requests.Response:
		return self.request("GET", "/booking", params=filters)

	def get_booking(self, booking_id: int) -> requests.Response:
		return self.request("GET", f"/booking/{booking_id}")

	def create_booking(self, booking: Mapping[str, Any]) -> requests.Response:
		return self.request("POST", "/booking", json=dict(booking))

	def update_booking(self, booking_id: int, booking: Mapping[str, Any]) -> requests.Response:
		return self.request("PUT", f"/booking/{booking_id}", json=dict(booking))

	def patch_booking(self, booking_id: int, fields: Mapping[str, Any]) -> requests.Response:
		return self.request("PATCH", f"/booking/{booking_id}", json=dict(fields))

	def delete_booking(self, booking_id: int) -> requests.Response:
		return self.request("DELETE", f"/booking/{booking_id}")
