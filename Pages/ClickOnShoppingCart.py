from selenium.webdriver.common.by import By


class ClickOnShoppingCart:
    shopping_Cart_by_xpath = "//span[text() = 'Shopping cart']"
    remove_checkbox_by_xpath = "//input[@name = 'removefromcart']"
    update_btn_by_xpath = "//input[@class = 'button-2 update-cart-button']"
    multi_checkbox_xpath = "//div[@class='order-summary-content']//tr[@class='cart-item-row']//td[@class='remove-from-cart']//input"

    def __init__(self, driver):
        self.driver = driver

    def click_on_cart_btn(self):
        cart_btn = self.driver.find_element(By.XPATH, self.shopping_Cart_by_xpath)
        cart_btn_status = cart_btn.is_displayed()
        if cart_btn_status:
            cart_btn.click()
        else:
            print("No cart button displayed")

    def click_on_remove_btn(self):
        remv_btn = self.driver.find_element(By.XPATH, self.remove_checkbox_by_xpath)
        remv_btn_status = remv_btn.is_displayed()
        if remv_btn_status:
            remv_btn.click()
        else:
            print("No checkbox present")

    def click_on_update_shopping_cart_btn(self):
        update_btn = self.driver.find_element(By.XPATH, self.update_btn_by_xpath)
        update_btn_status = update_btn.is_displayed()
        if update_btn_status:
            update_btn.click()
        else:
            print("No update btn present")

    def click_on_cart(self):
        cart_btn = self.driver.find_element(By.XPATH, self.shopping_Cart_by_xpath)
        cart_btn_status = cart_btn.is_displayed()
        if cart_btn_status:
            cart_btn.click()
        else:
            print("No cart button displayed")

    def click_on_multi_checkbox(self):
        multi_checkbox_from_ui = self.driver.find_elements(By.XPATH, self.multi_checkbox_xpath)
        # multi_checkbox_from_ui_status = multi_checkbox_from_ui.is_displayed()
        multi_checkbox = []

        for get_checkbox in multi_checkbox_from_ui:
            test = get_checkbox.get_attribute('value')
            multi_checkbox.append(test)

        for box in multi_checkbox:
            tester = box
            xpath_link = self.driver.find_element(By.XPATH, f"//input[contains(@value,'{tester}')]")
            xpath_link_status = xpath_link.is_displayed()
            if xpath_link_status:
                xpath_link.click()
            else:
                print("No checkbox found")
