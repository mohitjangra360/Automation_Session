from selenium.webdriver.common.by import By


class Salesforce_Loginpage():
    #initialise driver
    def __init__(self, driver):
        self.driver = driver

    def user_ableto_seelogo(self):
        logo= self.driver.find_element(By.XPATH, "//img[@id= 'logo']")
        logo_status = logo.is_displayed()
        if logo_status == True:
            exp_logo = "https://login.salesforce.com/img/logo214.svg"
            actual_logo = logo.get_attribute("src")
            if exp_logo == actual_logo:
                assert True
                print("logo successfully verified")

            else:
                assert False
        else:
            assert False
