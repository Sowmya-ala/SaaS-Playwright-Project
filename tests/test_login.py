from playwright.sync_api import Page
from pages.login_page import LoginPage
from utils.config import Config


def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    page.wait_for_timeout(5000)  # just wait and observe

    page.wait_for_url("**/dashboard/**")
    assert "dashboard" in page.url.lower()
