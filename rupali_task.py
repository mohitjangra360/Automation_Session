import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

optionnew = Options()
optionnew.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=optionnew)
driver.get("http://demowebshop.tricentis.com/")

driver.maximize_window()
time.sleep(2)

link_text_from_ui = driver.find_elements(By.XPATH, "//div[@class='column my-account']//a")

text_link = []

for get_text_link in link_text_from_ui:
    mohit = get_text_link.text
    text_link.append(mohit)
    # print(mohit)
# print(text_link)

for link in text_link:
    aditya = link
    xpath_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{aditya}')]")
    # print(xpath_link)
    xpath_link.click()
    actual_title = driver.title
    assert aditya in actual_title
    assert True

