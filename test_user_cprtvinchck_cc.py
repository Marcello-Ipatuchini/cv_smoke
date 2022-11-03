import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://dev:cvdev321@staging.clearvin.com/en/copart-vin-check/"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
    # filling in vin input
    vin_input = browser.find_element(By.CSS_SELECTOR, "[name='vinLot']")
    vin_input.send_keys('1G11C5SL2EF228854')
    submit_vin_btn = browser.find_element(By.CLASS_NAME, 'cv-button.cv-primary-button.cv-large.vin-lot-submit.upcase')
    submit_vin_btn.click()
    # autosearch assert
    #finding email input and fill it with random email
    email_input = browser.find_element(By.XPATH, "//div[contains(@id,'newCardForm')]//input[contains(@id,'new-user-email')]")
    email_input.send_keys(" 123@qw.er")
    # finding cc input and fill it with valid credit card number
    cc_input = browser.find_element(By.ID, "card-number")
    cc_input.send_keys("4111 1111 1111 1111")

    # finding date input and fill it with valid exp date
    exp_date = browser.find_element(By.ID, "exp-date-input")
    exp_date.send_keys("09 29")
    # finding ccv input and fill it with valid ccv
    exp_date = browser.find_element(By.ID, "ccv-input")
    exp_date.send_keys("918")
    #поставить ассерт, для появления баннера с протухшим паролем
    #clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()


    #Waiting for payment prepare page to be presented. Needs to implement scroll
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    #scrolling down to payment choise block
    browser.execute_script("window.scrollTo(0, 800)")
    #choosing CC as a payment method
    order_btn = browser.find_element(By.XPATH, "//div/form/button")
    order_btn.click()
    #order page is presented
    order_page = browser.find_element(By.ID, "report-print-button")


finally:

    browser.quit()
