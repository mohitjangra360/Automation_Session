from behave import *

from Pages.HomePage import HomePage

use_step_matcher("re")


@step("click on Book Link")
def click_on_book_link(context):
    hp = HomePage(context.driver)
    hp.click_on_book_link()

