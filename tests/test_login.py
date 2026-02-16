import pytest
from pages.orangehrm_loginpage import OrangeHRMLoginPage
from pages.orangehrm_dashboard import OrangeHRMDashboardPage
from pages.orangehrm_adminpage import OrangeHRMAdminPage
from pages.orangehrm_adduser_page import OrangeHrmAddUserPage
from pages.orangehrm_searchnewuser_added import OrangeHRMaddeduserCheckPage
from pages.orangehrm_edituser import OrangeaHRMEditUserPage

USERNAME = "Rajsingh128900456"
UPDATED_USERNAME = "Rajsingh7787670"
PASSWORD = "babul@12345Aj"
UPDATED_PASSWORD = "Rajsingh@390"
ROLE = "Admin"

@pytest.mark.order(1)
def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = OrangeHRMLoginPage(page)
    dashboard_page = OrangeHRMDashboardPage(page)
    login_page.login("Admin", "admin123")
    dashboard_page.check_dashboard_header()

@pytest.mark.order(2)
def test_navigate_to_admin(page):
    dashboard_page = OrangeHRMDashboardPage(page)
    admin_page = OrangeHRMAdminPage(page)
    dashboard_page.click_admin_menu()
    admin_page.check_admin_header()

@pytest.mark.order(3)
def test_add_user(page):
    admin_page = OrangeHRMAdminPage(page)
    add_user_page = OrangeHrmAddUserPage(page)
    added_user_check_page = OrangeHRMaddeduserCheckPage(page)
    admin_page.click_add_user()
    add_user_page.check_userpage_header()
    add_user_page.adduser(USERNAME, PASSWORD)
    added_user_check_page.check_added_user_header()
    added_user_check_page.verify_added_user(USERNAME)

@pytest.mark.order(4)
def test_edit_user(page):
    edit_user_page = OrangeaHRMEditUserPage(page)
    added_user_check_page = OrangeHRMaddeduserCheckPage(page)
    edit_user_page.edit_user(UPDATED_USERNAME, UPDATED_PASSWORD, ROLE)
    added_user_check_page.validatingupdates(UPDATED_USERNAME, ROLE)

@pytest.mark.order(5)
def test_delete_user(page):
    added_user_check_page = OrangeHRMaddeduserCheckPage(page)
    added_user_check_page.click_delete_button(UPDATED_USERNAME)
    added_user_check_page.verify_deleted_user(UPDATED_USERNAME)
