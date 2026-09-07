import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@allure.feature("Login")
@allure.story("Valid login")
def test_valid_login(page, login_page) -> None:
    login_page.goto();
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.get_by_text("Products", exact=True)).to_be_visible()



@pytest.mark.ui
@allure.feature("Login")
@allure.story("Invalid login")
def test_invalid_login(login_page) -> None:
    login_page.goto();
    login_page.login("standard_user", "invalid_password")

    expect(login_page.error_message).to_contain_text("Username and password do not match")
