from playwright.sync_api import Page,expect
import re

class OrangeHRMaddeduserCheckPage:
    def __init__(self,page:Page):
        self.page=page
        self.added_user_header = page.get_by_role("heading", name="System Users")
        self.username_search_input=page.locator("input.oxd-input.oxd-input--active").nth(1)
        self.search_button=page.get_by_role("button", name="Search")
        self.delete_button=page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3)
        
        
        

    def check_added_user_header(self):
        expect(self.added_user_header).to_be_visible()


    def added_user_search(self,username):
        return self.page.get_by_role("cell", name=username).first
    
    def enter_username_search(self,username):
        
        self.username_search_input.fill(username)

    def click_search_button(self):
        self.search_button.click()

    def user_role_search(self,userrole):
        return self.page.get_by_role("cell", name=userrole).first   
    
    def click_delete(self):
        self.delete_button.click()
        modal=self.page.get_by_role("button", name=" Yes, Delete")
        modal.click()

    def verify_added_user(self,username):
        self.enter_username_search(username)
        self.click_search_button()
        expect(self.added_user_search(username)).to_be_visible()      

    def validatingupdates(self,username,userrole):
        self.enter_username_search(username)
        self.click_search_button()
        expect(self.added_user_search(username)).to_be_visible()      
        expect(self.user_role_search(userrole)).to_be_visible()

    def click_delete_button(self,username):
        self.enter_username_search(username)
        self.click_search_button()
        expect(self.added_user_search(username)).to_be_visible()    
        self.click_delete()  
        
    def verify_deleted_user(self,username):
        self.enter_username_search(username)
        self.click_search_button()
        expect( self.page.locator("span").filter(has_text="No Records Found")).to_be_visible()