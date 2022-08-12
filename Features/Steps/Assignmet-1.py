from behave import *
from Pages.Assignment_One_Page import AssignmentOne
from Utilities.readProperty import ReadConfig


# username = ReadConfig.getSFUserName()
# password = ReadConfig.getSFUserName()


@when('User Enter Username "{}"')
def enter_sf_username(context, username):
    lp = AssignmentOne(context.driver)
    lp.enterSFUsername(username)


@step('User Enter Password "{}"')
def enter_sf_password(context, password):
    lp = AssignmentOne(context.driver)
    lp.enterSFPassword(password)


@step("Click On Login Button")
def click_on_sf_lgnbtn(context):
    lp = AssignmentOne(context.driver)
    lp.click_on_sf_login_btn()


@then("Verify Error Msg Visible")
def error_msg(context):
    lp = AssignmentOne(context.driver)
    lp.error_msg_login_pg()


@then("Switch Salesforce")
def switch_sf(context):
    lp = AssignmentOne(context.driver)
    lp.switch_sf()