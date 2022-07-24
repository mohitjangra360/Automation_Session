from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login.LoginPage import LoginPage
from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig

baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()


@step("Open Browser")
def launch_browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylog.info("Open Browser")
    context.driver.get(baseUrl)


@step("Close Browser")
def close_browser(context):
    mylog.info('Close Browser')
    context.driver.close()


@step("User On Login Page")
def user_on_login_page(context):
    global logopage
    actual_title = context.driver.title
    expected_title = "InnSight"
    if actual_title == expected_title:
        assert True
        logopage = LoginPage(context.driver)
        logopage.verify_logo()
    else:
        assert False
