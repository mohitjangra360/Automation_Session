from behave import *

from Pages.ShoppingCart import ShoppingCart

use_step_matcher("re")


@then("Click on Add to Cart")
def click_on_add_to_cart_btn(context):
    cart = ShoppingCart(context.driver)
    cart.click_on_add_to_cart_home()
