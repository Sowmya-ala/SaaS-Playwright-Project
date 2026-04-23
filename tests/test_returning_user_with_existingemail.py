from playwright.sync_api import expect

from config.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.user_data import UserData, ExistingUserData


def test_returning_user_with_existing_email(page):
    user = UserData()
    existing_user_data = ExistingUserData()
    page.goto(Config.BASE_URL)
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    home.navigate_to_login()
    # log in page validation
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    # create a new user
    login_page = LoginPage(page)
    login_page.sign_up(user.name, existing_user_data.email)
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()