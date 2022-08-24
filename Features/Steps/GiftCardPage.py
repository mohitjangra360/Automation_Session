from behave import *

from Pages.GiftCardPage import GiftCardPage

use_step_matcher("re")


@then("Click on Add to Cart button of gift card page")
def click_on_add_to_cart_button_gift_card_page(context):
    cart1 = GiftCardPage(context.driver)
    cart1.click_on_add_to_cart_gift_card_page()
