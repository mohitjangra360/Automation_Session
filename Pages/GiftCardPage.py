from selenium.webdriver.common.by import By


class GiftCardPage:
    click_on_add_to_cart_gift_page_by_ID = "add-to-cart-button-2"
    enter_recipient_name_by_ID = "giftcard_2_RecipientName"
    enter_recipient_email_by_ID = "giftcard_2_RecipientEmail"

    def __init__(self, driver):
        self.driver = driver

    # verify after clicking on add to cart btn error msg displays or not
    def click_on_add_to_cart_gift_card_page(self):
        self.driver.find_element(By.ID, self.enter_recipient_name_by_ID).send_keys("Test User")
        self.driver.find_element(By.ID, self.enter_recipient_email_by_ID).send_keys("abcd@gmail.com")
        btn1 = self.driver.find_element(By.ID, self.click_on_add_to_cart_gift_page_by_ID)
        btn1_status = btn1.is_displayed()
        if btn1_status:
            btn1.click()
        else:
            print("button is not displayed")

