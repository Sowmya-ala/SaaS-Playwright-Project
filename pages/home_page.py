
class HomePage:
    def __init__ (self,page):
        self.page = page
    def navigate_to_login(self):
        self.page.locator("a[href='/login']").click()

    def delete_account(self):
        self.page.get_by_role("link", name = "Delete Account").click()

    def logout(self):
        self.page.get_by_role("link", name = "Logout").click()

    def contact_us(self):
        self.page.get_by_role("link", name = "Contact Us").click()

    def navigate_to_testcases(self):
        self.page.locator("ul.nav a[href='/test_cases']").click()

    def navigate_to_products(self):
        self.page.locator("ul.nav a[href='/products']").click()