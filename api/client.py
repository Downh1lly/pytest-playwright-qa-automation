import requests


class BookingApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def auth(self, username: str, password: str) -> str:
        response = self.session.post(
            f"{self.base_url}/auth",
            json={"username": username, "password": password}
        )
        self.token = response.json()["token"]
        return self.token

    def create_booking(self, booking_data: dict) -> requests.Response:
        return self.session.post(f"{self.base_url}/booking", json=booking_data)

    def get_bookings(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/booking")

    
    def get_booking(self, booking_id: int) -> requests.Response:
        return self.session.get(f"{self.base_url}/booking/{booking_id}")

    def update_booking(self, booking_id: int, booking_data: dict) -> requests.Response:
        return self.session.put(
            f"{self.base_url}/booking/{booking_id}",
            json=booking_data,
            cookies={"token": self.token}
        )

    def delete_booking(self, booking_id: int) -> requests.Response:
        return self.session.delete(
            f"{self.base_url}/booking/{booking_id}",
            cookies={"token": self.token}
        )

    def close(self):
        self.session.close()