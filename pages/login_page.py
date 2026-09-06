from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page, base_url: str) -> None:
        super().__init__(page, base_url=base_url)
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")



    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
