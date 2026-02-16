from playwright.sync_api import Page,expect
import re

class OrangeaHRMEditUserPage:
    def __init__(self,page:Page):
        self.page=page
        self.editbutton=page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(4)
        self.edituser_header=page.get_by_role("heading", name="Edit User")
        self.userrole_dropdown= page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow")
       
        self.employee_name_input=page.get_by_role("textbox", name="Type for hints...")
        self.status_dropdown_click=page.locator("div.oxd-select-text--after").nth(1)
        self.status_dropdown=page.get_by_role("option", name="Disabled")
        self.password_checkbox=page.locator(".oxd-icon.bi-check")
        self.username_input=page.get_by_role("textbox").nth(2)
        self.password_input=page.get_by_role("textbox").nth(3)
        self.confirmpassword_input=page.get_by_role("textbox").nth(4)
        self.save_button=page.get_by_role("button", name="Save")

    def click_edit_button(self):
        self.editbutton.click()

    def check_edituser_header(self):
        expect(self.edituser_header).to_be_visible()        

    def select_userrole(self,userrole):
        self.userrole_dropdown.first.click()
        self.userrole_option= self.page.get_by_role("option", name=userrole)
        self.userrole_option.click()

    def enter_employee_name(self):  
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
        first_option.nth(1).click()         
    
    def select_status(self):
        self.status_dropdown_click.click()
        self.status_dropdown.click()
    def click_password_checkbox(self):
        self.password_checkbox.click()
    def enter_username(self,username):
        self.username_input.fill("")
        self.username_input.fill(username)

    def enter_password(self,password):
        self.password_input.fill("")
        self.password_input.fill(password)

    def enter_confirmpassword(self,confirmpassword):
        self.confirmpassword_input.fill("")
        self.confirmpassword_input.fill(confirmpassword)

    def click_save_button(self):
        self.save_button.click()
        expect(self.page).to_have_url(re.compile(r".*/admin/viewSystemUsers"),timeout=30000)

    def edit_user(self,username,password,userrole):
        self.click_edit_button()
        self.check_edituser_header()
        self.select_userrole(userrole=userrole)
        self.enter_employee_name()
        self.select_status()
        self.enter_username(username)
        self.click_password_checkbox()
        self.enter_password(password)
        self.enter_confirmpassword(password)
        self.click_save_button()    
            
