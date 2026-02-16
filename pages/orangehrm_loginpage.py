from playwright.sync_api import Page

class OrangeHRMLoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input= page.locator("input[name='username']")
        self.password_input= page.locator("input[name='password']")
        self.login_button=page.locator("button[type='submit']")

    def enter_username(self,username):
        self.username_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self,username,password):
        self.page.wait_for_selector("input[name='username']", timeout=60000)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()        