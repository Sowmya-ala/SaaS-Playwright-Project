from test_data.user_data import UserData

class LoginPage:
    def __init__(self, page):
        self.page = page
    def sign_up(self,name,email):
        self.page.locator("input[data-qa='signup-name']").fill(name)
        self.page.locator("input[data-qa='signup-email']").fill(email)
        self.page.get_by_role("button", name= "Signup").click()