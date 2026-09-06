"""Shared Playwright page object helpers."""

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, base_url: str | None = None) -> None:
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = ""):
        self.page.goto(f"{self.base_url}/{path}")

    def get_title(self) -> str:
        return self.page.title()
