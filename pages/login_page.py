from playwright.sync_api import Page
from utils.config import Config


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(Config.BASE_URL)

    def enter_username(self, username: str):
        self.page.locator('input[name="username"]').wait_for(state="visible")
        self.page.fill('input[name="username"]', username)

    def enter_password(self, password: str):
        self.page.fill('input[name="password"]', password)

    def click_login(self):
        self.page.click('button[type="submit"]')

    def login(self, username: str, password: str):
        self.load()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.page.locator(".oxd-alert-content-text").text_content()