from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

try:
    #opening stag CV in chrome browser
    browser = webdriver.Chrome()
    browser.get(link)
    #finding email input and fill it with hardcoded email
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys("79818059334z+2@gmail.com")
    # finding password input and fill it with hardcoded password
    pass_input = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    pass_input.send_keys("QQQqqq!1")
    #clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    #checking if myaccount button is presented
    my_account_button = browser.find_element(By.CSS_SELECTOR, "[aria-label='My Account']")
    my_account_button.is_displayed()


finally:

    time.sleep(10)

    browser.quit()

