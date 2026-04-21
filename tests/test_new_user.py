
from config.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data.user_data import UserData
from playwright.sync_api import expect


def test_new_user(page):
    # Home page validation
    page.goto(Config.BASE_URL)
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    home.navigate_to_login()
    # log in page validation
    assert page.get_by_text("New User Signup!").is_visible()
    # create a new user
    login_page = LoginPage(page)
    login_page.sign_up(UserData.NAME,UserData.EMAIL)