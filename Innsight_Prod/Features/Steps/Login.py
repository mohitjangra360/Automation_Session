from behave import *
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Innsight_Prod.Pages.LoginPage import LoginPage
from Innsight_Prod.Utilities.CustomLogger import LogGen
from Innsight_Prod.Utilities.readProperty import ReadConfig
import time

baseUrl = ReadConfig.getApplicationURL()
mylog = LogGen.loggen()


# use_step_matcher("re")


@given("Launch Browser")
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylog.info("Open Browser")
    context.driver.get(baseUrl)


@then("Verify Title")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Verify Title')


@step("Close Browser")
def step_impl(context):
    context.driver.close()
