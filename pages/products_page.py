class ProductsPage():
    def __init__(self, page):
        self.page = page
    def go_to_products(self):
        self.page.locator(".product-image-wrapper").first.get_by_text("View Product").click()

