from playwright.sync_api import expect

from config.config import Config
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_all_products_and_product_details_page(page):
    page.goto(Config.BASE_URL)
    expect(page.get_by_text("Full-Fledged practice website for Automation Engineers").first).to_be_visible()
    homepage = HomePage(page)
    # navigating to the Products page
    homepage.navigate_to_products()
    # validating the user is navigated to the products page
    expect(page).to_have_url("https://automationexercise.com/products")
    # To validate all the products are visible
    products = page.locator(".product-image-wrapper")
    assert products.count() > 0
    products_page = ProductsPage(page)
    # clicking the first product
    products_page.go_to_products()
    expect(page).to_have_url("https://automationexercise.com/product_details/1")
    expect(page.locator(".product-information")).to_be_visible()
    # validating the name of the product
    expect(page.locator(".product-information h2")).to_be_visible()  # name
    expect(page.get_by_text("Category:")).to_be_visible()
    expect(page.get_by_text("Rs.")).to_be_visible()  # price
    expect(page.get_by_text("Availability:")).to_be_visible()
    expect(page.get_by_text("Condition:")).to_be_visible()
    expect(page.get_by_text("Brand:")).to_be_visible()
