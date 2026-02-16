from playwright.sync_api import Page,expect
import re


class OrangeHrmAddUserPage:
    def __init__(self,page:Page):
        self.page=page
        self.userpage_header=page.locator("h6:has-text('Add User')")
        self.username_roleclick=page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow")
        self.username_roleselect=page.get_by_role("option", name="ESS")
        self.employee_name_input=page.get_by_role("textbox", name="Type for hints...")
        self.status_click=page.get_by_text("-- Select --")
        self.status_select=  page.get_by_role("option", name="Enabled")
        self.username_input=page.get_by_role("textbox").nth(2)
        self.password_input=page.get_by_role("textbox").nth(3)
        self.confirmpassword_input=page.get_by_role("textbox").nth(4)
        self.click_savebutton= page.get_by_role("button", name="Save")


    def check_userpage_header(self):
        expect(self.userpage_header).to_be_visible()

    def userrole_roleselect(self):
        self.username_roleclick.first.click()
        self.username_roleselect.click()

    def  enteremployee_name(self):
        self.employee_name_input.click()
        self.employee_name_input.fill("")
        self.employee_name_input.type("R",delay=400)
        first_option = self.page.locator("//div[contains(@class,'oxd-autocomplete-option')]")
        self.page.wait_for_timeout(500)
        max_attempts = 3
        for attempt in range(max_attempts):
            count=first_option.count()
            if count>=2:
                break
            self.page.wait_for_timeout(1000)
            self.employee_name_input.fill("")
            self.employee_name_input.type("R", delay=400)
        first_option.first.wait_for(state="visible", timeout=20000)
        first_option.first.click()    
      

 
    def  staus_select_(self):
        self.status_click.click()
        self.status_select.click()

    def enterusername(self,username):
        self.username_input.fill(username) 

    def enterpassword(self,password):
         self.password_input.fill(password)  
    def enterconfirmpassword(self,confirmpassword):
        self.confirmpassword_input.fill(confirmpassword) 

    def clickonSave(self):
        self.click_savebutton.click()      
        expect(self.page).to_have_url(re.compile(r".*/admin/viewSystemUsers"),timeout=30000)
    def adduser(self,username,password):
        self.userrole_roleselect()
        self.enteremployee_name()
        self.staus_select_()
        self.enterusername(username)
        self.enterpassword(password)
        self.enterconfirmpassword(password)
        self.clickonSave()

