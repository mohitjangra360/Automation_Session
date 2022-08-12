import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from Utilities.CustomLogger import LogGen
from Utilities.readProperty import ReadConfig

baseUrl = ReadConfig.getApplicationURL()
# mylog = LogGen.loggen()
sfUrl = ReadConfig.getSFApplicationURL()


@step("Open Browser")
def launch_browser(context):
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("start-maximized")

    # Pass the argument 1 to allow and 2 to block
    # option.add_experimental_option("prefs", {
    #     "profile.default_content_setting_values.notifications": 1
    # })
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    # mylog.info("Open Browser")
    # context.driver.maximize_window()
    context.driver.get(baseUrl)


@step("Close Browser")
def close_browser(context):
    # mylog.info('Close Browser')
    context.driver.close()


@step("I wait {} seconds")
def wait_on(context, wait_on):
    wait_time = int(wait_on)
    time.sleep(wait_time)


@given("Open Browser With Salesforce")
def open_browser_sf(context):
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("start-maximized")

    # Pass the argument 1 to allow and 2 to block
    # option.add_experimental_option("prefs", {
    #     "profile.default_content_setting_values.notifications": 1
    # })
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
    # mylog.info("Open Browser")
    # context.driver.maximize_window()
    context.driver.get(sfUrl)
