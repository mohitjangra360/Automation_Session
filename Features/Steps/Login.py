import time

from behave import *

from Pages.LoginPage import LoginPage
from Utilities.readProperty import ReadConfig

use_step_matcher("re")

username = ReadConfig.getUserName()
password = ReadConfig.getPassword()

@step("User Enter Username")
def user_enter_username(context):
    lp = LoginPage(context.driver)
    lp.enterUsername(username)



@step("Click On Login Link")
def click_on_login_link(context):
    lp = LoginPage(context.driver)
    lp.click_on_login_link()


@then("User Enter Password")
def enter_password(context):
    lp = LoginPage(context.driver)
    lp.enterPassword(password)


@then("click on login button")
def click_on_login(context):
    mohit = LoginPage(context.driver)
    mohit.click_on_login_btn()