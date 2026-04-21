class Signuppage:
    def __init__(self,page):
        self.page = page

    def account_info(self,user):
        self.page.locator("#id_gender2").check()
        self.page.locator("#name").fill(user.name)
        self.page.locator("#password").fill(user.password)
        self.page.locator("#days").select_option(user.day)
        self.page.locator("#months").select_option(user.month)
        self.page.locator("#years").select_option(user.year)
        self.page.locator("#newsletter").check()
        self.page.locator("#optin").check()

    def address_info(self,user):
        self.page.locator("#first_name").fill(user.first_name)
        self.page.locator("#last_name").fill(user.last_name)
        self.page.locator("#company").fill(user.company)
        self.page.locator("#address1").fill(user.address1)
        self.page.locator("#address2").fill(user.address2)
        self.page.locator("#country").select_option(user.country)
        self.page.locator("#state").fill(user.state)
        self.page.locator("#city").fill(user.city)
        self.page.locator("#zipcode").fill(user.zipcode)
        self.page.locator("#mobile_number").fill(user.mobile)

    def create_account(self,user):
        self.account_info(user)
        self.address_info(user)
        self.page.get_by_role("button", name= "Create Account").click()

