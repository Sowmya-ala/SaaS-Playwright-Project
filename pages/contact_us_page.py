class ContactUsPage:
    def __init__(self, page):
        self.page = page

    def submit_form(self,name,email,subject,message):
        self.page.locator("input[name='name']").fill(name)
        self.page.locator("input[name='email']").fill(email)
        self.page.locator("input[name='subject']").fill(subject)
        self.page.locator("#message").fill(message)
        self.page.set_input_files("input[type='file']", "test_data/contact_us_form.txt")
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.page.locator("input[name='submit']").click()


    def click_home(self):
        self.page.locator("#contact-page a.btn-success").click()
