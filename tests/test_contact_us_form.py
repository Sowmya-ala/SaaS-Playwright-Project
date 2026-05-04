from playwright.sync_api import expect

from config.config import Config
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from test_data.user_data import ExistingUserData


def test_contact_us_form(page):
    existing_user_data = ExistingUserData()
    name = "Test user"
    subject = "Test subject"
    message = "Test message"
    page.goto(Config.BASE_URL)
    # validating the Home page text
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    home = HomePage(page)
    home.contact_us()
    # Contact Us page validation
    expect(page.get_by_text("Get In Touch")).to_be_visible()
    contact_us_page = ContactUsPage(page)
    # Variables for form submission created dynamically to avoid hardcoding and to make the test more robust
    contact_us_page.submit_form(name,existing_user_data.email,subject,message)
    expect(page.locator("#contact-page .alert-success")).to_be_visible()


    # navigating back to Home page
    contact_us_page.click_home()
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()


