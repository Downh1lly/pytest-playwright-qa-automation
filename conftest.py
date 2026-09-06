"""Shared pytest fixtures."""

from config import API_BASE_URL, UI_BASE_URL
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
import pytest
from playwright.sync_api import Page

from api.client import BookingApiClient


@pytest.fixture
def api_client():
    client = BookingApiClient(base_url=API_BASE_URL) 
    yield client
    client.close()


@pytest.fixture
def Base_page(page: Page) -> BasePage:
    return BasePage(page)


@pytest.fixture
def login_page(page):
    return LoginPage(page, base_url=UI_BASE_URL);

@pytest.fixture
def logged_in_page(login_page, page):
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return page

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page);

@pytest.fixture
def cart_page(page):
    return CartPage(page);

@pytest.fixture
def on_checkout_page(inventory_page, cart_page, page):

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    return page

@pytest.fixture
def checkout_page(on_checkout_page):
    return CheckoutPage(on_checkout_page);  