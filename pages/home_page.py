
class HomePage:
    def __init__ (self,page):
        self.page = page
    def navigate_to_login(self):
        self.page.locator("a[href='/login']").click()