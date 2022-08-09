from selenium.webdriver.common.by import By


class Salesforce_Login_Page:

    def __init__(self, driver):
        self.driver = driver

    def user_able_to_see_logo(self):
        logo = self.driver.find_element(By.XPATH, "//img[@class='standard_logo']")
        logo_status = logo.is_displayed()
        if logo_status == True:
            exp_logo = "https://login.salesforce.com/img/logo214.svg"
            actual_logo = logo.get_attribute('src')
            if exp_logo == actual_logo:
                assert True
                print("logo successfully verified")
            else:
                assert False
        else:
            assert False

    def user_able_to_see_login_btn(self):
        login_btn = self.driver.find_element(By.XPATH, "//input[@id='Login']")
        logo_status = login_btn.is_displayed()
        if logo_status == True:
                login_btn.click()
        else:
            assert False

