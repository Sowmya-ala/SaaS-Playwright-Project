from playwright.sync_api import expect

from config.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.user_data import ExistingUserData


def invalid_user(page):
    existing_user_data = ExistingUserData()
    page.goto(Config.BASE_URL)
    # Home Page validation
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    home.navigate_to_login()
    # validating Login page
    expect(page.get_by_text("Login to your account")).to_be_visible()
    invalid_password = "wrong123"
    # logging in with invalid password and valid email
    login_page = LoginPage(page)
    login_page.sign_in(existing_user_data.email, invalid_password)
    # validating the error message for invalid login
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

