import pytest
from playwright.sync_api import expect

@pytest.mark.ui
def test_complete_checkout( checkout_page) -> None:
    checkout_page.fill_customer_details("John", "Doe", "12345")
    checkout_page.continue_to_overview()
    checkout_page.finish_checkout()
    expect(checkout_page.complete_header).to_be_visible()
