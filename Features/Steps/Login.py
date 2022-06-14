from behave import *
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig
import time


baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()
username = ReadConfig.getUserName()
password = ReadConfig.getPassword()


use_step_matcher("re")


@given("Launch Browser")
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylog.info("Open Browser")
    context.driver.get(baseUrl)

@step("Close Browser")
def close_browser(context):
    mylog.info('Close Browser')
    context.driver.close()

@then("Verify Login")
def verify_login(context):
    global lpage
    actual_title = context.driver.title
    expected_title = "InnSight"
    if actual_title == expected_title:
        assert True
        mylog.info("Title Is Pass")
        lpage = LoginPage(context.driver)
        lpage.setUsername(username)
        lpage.setPassword(password)
        lpage.clickOnLogin()
        mylog.info("Done")
