from selenium.webdriver.common.by import By


class ShoppingCart:
    click_on_add_to_Cart_by_xpath = "(//div[@class= 'add-info']//div[@class= 'buttons'])[1]"

    # click_on_add_to_Cart2_by_xpath = "(//div[@class= 'add-info']//div[@class= 'buttons'])[2]"
    # click_on_add_to_Cart3_by_xpath = "(//div[@class= 'add-info']//div[@class= 'buttons'])[5]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_to_cart_home(self):
        btn1 = self.driver.find_element(By.XPATH, self.click_on_add_to_Cart_by_xpath)
        btn_status1 = btn1.is_displayed()
        if btn_status1:
            btn1.click()

        # btn2 = self.driver.find_element(By.XPATH, self.click_on_add_to_Cart2_by_xpath)
        # btn_status2 = btn2.is_displayed()
        # if btn_status2:
        #   btn2.click()
        # btn3 = self.driver.find_element(By.XPATH, self.click_on_add_to_Cart3_by_xpath)
        # btn_status3 = btn3.is_displayed()
        # if btn_status3:
        #   btn3.click()
