from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://dev:cvdev321@staging.clearvin.com/en/dealer/"

try:
    #opening stag CV in chrome browser
    browser = webdriver.Chrome()
    browser.get(link)
    #finding full name input and fill it with name
    first_name = browser.find_element(By.ID, "firstName")
    first_name.send_keys("rand")
    # finding business name input and fill it with business name
    first_name = browser.find_element(By.ID, "businessName")
    first_name.send_keys("rand")
    # finding email input and fill it with email
    first_name = browser.find_element(By.ID, "email-input")
    first_name.send_keys("rand@fake.co")
    #clicking register button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    # checking if delaer's logo is presented
    dealer_logo = browser.find_element(By.CLASS_NAME, "logo-extra")
    dealer_logo.is_displayed()




finally:

    time.sleep(10)

    browser.quit()

