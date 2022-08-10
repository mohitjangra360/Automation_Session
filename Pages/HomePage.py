from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_book_link(self):
        self.driver.find_element(By.XPATH, "//ul[@class='top-menu']//li//a[contains(text(),'Books')]").click()
