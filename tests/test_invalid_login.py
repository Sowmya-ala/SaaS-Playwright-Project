from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.config import Config

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "wrongpassword")

    page.wait_for_timeout(2000)

    error = login_page.get_error_message()
    assert "invalid" in error.lower()
    assert "login" in page.url.lower()
