from behave import *

from Pages.ClickOnShoppingCart import ClickOnShoppingCart

use_step_matcher("re")


@then("Click on shopping cart button")
def click_on_cart(context):
    cart3 = ClickOnShoppingCart(context.driver)
    cart3.click_on_cart_btn()


@then("Click on remove checkbox")
def click_remove_btn(context):
    checkbox = ClickOnShoppingCart(context.driver)
    checkbox.click_on_remove_btn()


@then("Click on update cart button")
def click_update_cart(context):
    update = ClickOnShoppingCart(context.driver)
    update.click_on_update_shopping_cart_btn()


@then("Click on multiple checkbox of product")
def click_on_multiple_checkbox(context):
    multiple = ClickOnShoppingCart(context.driver)
    multiple.click_on_multi_checkbox()
