from playwright.sync_api import Page,expect

class OrangeHRMAdminPage:
    def __init__(self,page:Page):
        self.page=page
        self.Admin_header=page.locator("h6:has-text('Admin')")
        self.Add_user_button=page.get_by_role("button", name="Add")


    def check_admin_header(self):
        expect(self.Admin_header).to_be_visible(timeout=30000)

    def click_add_user(self):
        self.Add_user_button.click()      