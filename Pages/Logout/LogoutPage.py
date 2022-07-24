import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    profile_icon_by_xpath = "//span[@id='divlogout']"
    popup_yes_btn_by_xpath = "(//button[@id='spnYes'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(By.XPATH, self.profile_icon_by_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.popup_yes_btn_by_xpath).click()


