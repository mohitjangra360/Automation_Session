from selenium.webdriver.common.by import By


class LoginPage:
    username_by_name = "userName"
    password_by_name = "password"
    login_btn_by_class = "loginbtn"


    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME,self.username_by_name).clear()
        self.driver.find_element(By.NAME, self.username_by_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.NAME, self.password_by_name).clear()
        self.driver.find_element(By.NAME, self.password_by_name).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element(By.CLASS_NAME, self.login_btn_by_class).click()
