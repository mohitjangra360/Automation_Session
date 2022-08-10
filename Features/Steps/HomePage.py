from behave import *

from Pages.HomePage import HomePage

use_step_matcher("re")


@then("click on Book Link")
def click_on_book_link(context):
    hp = HomePage(context.driver)
    hp.click_on_book_link()