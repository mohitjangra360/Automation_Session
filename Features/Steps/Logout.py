from behave import *
from Pages.Logout.LogoutPage import LogoutPage

use_step_matcher("re")


@step("Logout")
def logout_kar(context):
    global logout
    logout = LogoutPage(context.driver)
    logout.logout()

