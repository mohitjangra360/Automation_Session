from behave import *

from Pages.Salesforce_Login_Page import Salesforce_Login_Page

use_step_matcher("re")


@then("logo is visible")
def user_able_to_see_logo(context):
    mohit = Salesforce_Login_Page(context.driver)
    mohit.user_able_to_see_logo()


@then("click on login")
def click_on_login_btn(context):
    ibran = Salesforce_Login_Page(context.driver)
    ibran.user_able_to_see_login_btn()
