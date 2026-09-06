"""Saucedemo cart page object."""

from playwright.sync_api import Page

from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.cart_items = page.locator(".cart_item")
        self.continue_shopping_button = page.get_by_role("button", name="Continue Shopping")

    def get_item(self, item_name: str):
        return self.page.locator(".cart_item").filter(has_text=item_name)

    def remove_item(self, item_name: str) -> None:
        item = self.get_item(item_name)
        remove_button = item.get_by_role("button", name="Remove")
        remove_button.click()

    def checkout(self) -> None:
        self.checkout_button.click()
