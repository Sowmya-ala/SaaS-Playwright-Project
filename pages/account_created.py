


class AccountCreatedPage:
    def __init__(self, page):
        self.page = page
    def account_created(self):
        self.page.get_by_role("link", name = "Continue").click()