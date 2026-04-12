from playwright.sync_api import Page


class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def click_admin_menu(self):
        self.page.locator("//span[text()='Admin']").click()

    def enter_username(self, username: str):
        self.page.locator("(//input[@class='oxd-input oxd-input--active'])[2]").fill(username)

    def click_search(self):
        self.page.locator("//button[@type='submit']").click()

    def search_user(self, username: str):
        self.click_admin_menu()
        self.enter_username(username)
        self.click_search()

    def get_search_result(self):
        return self.page.locator("//div[@class='oxd-table-body']")