import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class" )
def init_chrome(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "edge":
        driver = webdriver.Edge(EdgeDriverManager().install())
        driver.close()


def login():
    print("login")