
from config.config import Config
from pages.account_created import AccountCreatedPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import Signuppage
from test_data.user_data import UserData
from playwright.sync_api import expect
import time


def test_new_user(page):
    user = UserData()
    user.email = f"test_{int(time.time())}@gmail.com"
    # Home page validation
    page.goto(Config.BASE_URL)
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    home.navigate_to_login()
    # log in page validation
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    # create a new user
    login_page = LoginPage(page)
    login_page.sign_up(user.name,user.email)
    # Signup page validation
    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    # Create a new account
    sign_up_page = Signuppage(page)
    sign_up_page.create_account(user)
    # Account validation
    expect(page.get_by_text("Account Created!")).to_be_visible()
    accountcreatedpage = AccountCreatedPage(page)
    accountcreatedpage.account_created()
    # validate the user login
    expect(page.get_by_text(f"Logged in as {user.name}")).to_be_visible()
    # delete the account
    home.delete_account()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
