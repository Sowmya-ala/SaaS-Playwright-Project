from playwright.sync_api import expect

from config.config import Config
from pages.home_page import HomePage


def test_validate_testcases(page):

    page.goto(Config.BASE_URL)
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    homepage = HomePage(page)
    homepage.navigate_to_testcases()
    expect(page).to_have_url("https://automationexercise.com/test_cases")
