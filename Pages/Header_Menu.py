from selenium.webdriver.common.by import By


class HeaderMenu:
    # header_link_by_xpath = "(//div[@class='header-menu']//ul//li//a[contains(text(),'Book')])[1]"

    def __init__(self, driver):
        self.driver = driver

    # def click_on_header_link(self):
    #     header_link = self.driver.find_element(By.XPATH, self.header_link_by_xpath)
    #     header_link_status = header_link.is_displayed()
    #     if header_link_status == True:
    #         header_link.click()
    #         assert True

    def click_on_header_link(self, link_text):
        header_link_by_xpath = f"(//div[@class='header-menu']//ul//li//a[contains(text(),'{link_text}')])[1]"

        header_link = self.driver.find_element(By.XPATH, self.header_link_by_xpath)
        header_link_status = header_link.is_displayed()
        if header_link_status == True:
            header_link.click()
            assert True