from behave import *
import allure
from allure_commons.types import AttachmentType
from Pages.Login.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig

baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()



@step("I should see sliding image")
def check_login_slide_image(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "InnSight"
    if actual_title == expected_title:
        assert True
        logopage = LoginPage(context.driver)
        logopage.verify_logo_slide_img()
    else:
        assert False


@step("Verify Login")
def verify_login(context):
    global lpage
    actual_title = context.driver.title
    expected_title = "InnSight"
    if actual_title == expected_title:
        assert True
        allure.attach(context.driver.get_screenshot_as_png(), name="Login Page 2",
                      attachment_type=AttachmentType.PNG)
        mylog.info("Title Is Pass")
        lpage = LoginPage(context.driver)
        lpage.setUsername(username)
        lpage.setPassword(password)
        lpage.clickOnLogin()
        mylog.info("Login Success")
        expected_title = ":: INNSIGHT ::"
        actual_title = context.driver.title
        if expected_title == actual_title:
            mylog.info("Login Success And User On Home Page")
            allure.attach(context.driver.get_screenshot_as_png(),name="Login Page",
            attachment_type=AttachmentType.PNG)