"""Saucedemo checkout page object."""

from playwright.sync_api import Page

from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_header = page.get_by_text("Thank you for your order!")

    def fill_customer_details(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self) -> None:
        self.continue_button.click()

    def finish_checkout(self) -> None:
        self.finish_button.click()
