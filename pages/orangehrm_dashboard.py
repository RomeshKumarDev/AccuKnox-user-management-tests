from playwright.sync_api import Page,expect
import re

class OrangeHRMDashboardPage:
    def __init__(self,page:Page):
        self.page=page
        self.admin_menu= page.get_by_role("link", name="Admin")
        self.dashboard_header =page.locator("h6:has-text('Dashboard')")
        
    def check_dashboard_header(self):
        expect(self.page).to_have_url(re.compile(r".*/dashboard/index"),timeout=30000)
        expect(self.dashboard_header).to_be_visible(timeout=30000)


    def click_admin_menu(self):
        self.admin_menu.click()    