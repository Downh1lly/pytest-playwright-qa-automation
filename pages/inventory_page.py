from playwright.sync_api import Page

from .base_page import BasePage

class InventoryPage(BasePage):

    def __init__(self, page) -> None:
        super().__init__(page)
        self.inventory_items = page.locator(".inventory_item");

    def get_item(self, item_name: str):
        return self.inventory_items.filter(has_text=item_name)

    def add_to_cart(self, item_name: str) -> None:
        item = self.get_item(item_name)
        add_to_cart_button = item.get_by_role("button", name="Add to cart")
        add_to_cart_button.click()

    def remove_from_cart(self, item_name: str) -> None:
        item = self.get_item(item_name)
        remove_button = item.get_by_role("button", name="Remove")
        remove_button.click()

    def open_cart(self) -> None:
        cart_button = self.page.locator(".shopping_cart_link")
        cart_button.click()

    def get_cart_item_count(self) -> int:
        cart_badge = self.page.locator(".shopping_cart_badge")
        if cart_badge.count() == 0:
            return 0
        return int(cart_badge.inner_text())