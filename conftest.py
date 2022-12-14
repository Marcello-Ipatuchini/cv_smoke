import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"
@pytest.fixture(scope="class")
def setup():
    print("\nstart chrome browser for test")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("\nstart ")
    # driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(URL)
    # request.cls.driver = driver
    yield driver

    driver.quit()