import pytest
from playwright.sync_api import Page, expect

@pytest.mark.ui
def test_add_item_to_cart(inventory_page, cart_page) -> None:

    inventory_page.add_to_cart("Sauce Labs Backpack")
    assert inventory_page.get_cart_item_count() == 1
    inventory_page.open_cart()
    expect(cart_page.cart_items).to_have_count(1)
    expect(cart_page.get_item("Sauce Labs Backpack")).to_be_visible()

@pytest.mark.ui
def test_remove_item_from_cart(inventory_page, cart_page) -> None:
   
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.remove_item("Sauce Labs Backpack")
    expect(cart_page.cart_items).to_have_count(0)
