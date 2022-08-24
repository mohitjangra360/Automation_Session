import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class AssignmentOne:
    username_by_id = "username"
    password_by_id = "password"
    lgn_btn_by_id = "Login"
    error_mg_by_xpath = "(//div[@class='loginError'])[2]"
    profile_icon_by_xpath = "//button[contains(@class,'branding-userProfile-button')]"
    switch_ltn_to_classic_by_xpath = "//a[contains(@class,'switch-to-aloha')]"
    switch_classic_to_lgtn_by_xpath = "//a[@class='switch-to-lightning']"

    def __init__(self, driver):
        self.driver = driver

    def enterSFUsername(self, username):
        self.driver.find_element(By.ID, self.username_by_id).clear()
        self.driver.find_element(By.ID, self.username_by_id).send_keys(username)

    def enterSFPassword(self, password):
        self.driver.find_element(By.ID, self.password_by_id).clear()
        self.driver.find_element(By.ID, self.password_by_id).send_keys(password)

    def click_on_sf_login_btn(self):
        self.driver.find_element(By.ID, self.lgn_btn_by_id).click()

    def error_msg_login_pg(self):
        eror = self.driver.find_element(By.XPATH, self.error_mg_by_xpath).is_displayed()
        if eror:
            time.sleep(2)
            errormsg = self.driver.find_element(By.XPATH, self.error_mg_by_xpath).text
            actual_errormsg = "Please check your username and password. If you still can't log in, contact your Salesforce administrator."
            time.sleep(2)
            if errormsg == actual_errormsg:
                assert True

    def switch_sf(self):
        classic_link = self.driver.find_element(By.XPATH, self.switch_classic_to_lgtn_by_xpath).is_displayed()
        # if classic_link:
        #     print("already in classic")
        #     self.driver.find_element(By.XPATH, self.switch_classic_to_lgtn_by_xpath).click()
        #     print("successfully switch to lightening")
        #     time.sleep(2)
        # else:
        #     lgt_org = self.driver.find_element(By.XPATH, self.profile_icon_by_xpath).is_displayed()
        #     if lgt_org:
        #         self.driver.find_element(By.XPATH, self.profile_icon_by_xpath).click()
        #         time.sleep(2)
        #         self.driver.find_element(By.XPATH, self.switch_ltn_to_classic_by_xpath).click()
        #         time.sleep(10)
        #         self.driver.find_element(By.XPATH, self.switch_classic_to_lgtn_by_xpath).is_displayed()
        #         print("successfully switch to classic")
