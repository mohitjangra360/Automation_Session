from behave import *

from Pages.Header_Menu import HeaderMenu

use_step_matcher("re")

#
# @then("Click On Digital Download")
# def click_on_digital_header_menu_link(context):
#     hm = HeaderMenu(context.driver)
#     hm.click_on_header_link()


@then('Click On {}')
def click_On_header_link(context, link_text):
    hm = HeaderMenu(context.driver)
    hm.click_on_header_link(link_text)