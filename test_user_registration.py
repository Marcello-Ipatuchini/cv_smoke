from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://dev:cvdev321@staging.clearvin.com/en/user/register/"

try:
    #opening stag CV in chrome browser
    browser = webdriver.Chrome()
    browser.get(link)
    #finding first name input and fill it with name
    first_name = browser.find_element(By.ID, "firstName")
    first_name.send_keys("rand")
    # finding email input and fill it with email
    first_name = browser.find_element(By.ID, "email-input")
    first_name.send_keys("rand@fake.co")
    #clicking register button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    #checking if myaccount button is presented
    my_account_button = browser.find_element(By.CSS_SELECTOR, "[aria-label='My Account']")
    my_account_button.is_displayed()




finally:

    time.sleep(10)

    browser.quit()

