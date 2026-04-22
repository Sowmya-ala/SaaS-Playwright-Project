from playwright.sync_api import expect

from config.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.user_data import ExistingUserData


def test_returning_user(page):
    existing_user_data = ExistingUserData()
    page.goto(Config.BASE_URL)
    # Home Page validation
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    # Navigating to Login page
    home.navigate_to_login()
    expect(page.get_by_text("Login to your account")).to_be_visible()
    # Logging in with existing user credentials
    login = LoginPage(page)
    login.sign_in(existing_user_data.email, existing_user_data.password)
    # validating the user login
    expect(page.get_by_text("Logged in as Test")).to_be_visible()
    # log out
    home.logout()
    expect(page.get_by_text(" Signup / Login")).to_be_visible()


