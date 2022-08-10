from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_link(self):
        self.driver.find_element(By.XPATH, "//a[text()='Log in']").click()

    def enterUsername(self, username):
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys(password)

    def click_on_login_btn(self):
        self.driver.find_element(By.XPATH, "//input[contains(@class,'login-button')]").click()