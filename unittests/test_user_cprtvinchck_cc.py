import time
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
    # TODO auto search assert
    #finding email input and fill it with random email
    email_input = browser.find_element(By.XPATH, "//div[contains(@id,'newCardForm')]//input[contains(@id,'new-user-email')]")
    email_input.send_keys(" 12hyu3@qw.er")
    # finding cc input and fill it with valid credit card number
    # TODO input mask + selenium how to work with it. card input looks awful
    cc_input = browser.find_element(By.ID, "card-number")
    cc_input.click()
    time.sleep(2)
    cc_input.send_keys("4111")
    cc_input.send_keys("1111")
    cc_input.send_keys("1111")
    cc_input.send_keys("1111")
    # finding date input and fill it with valid exp date
    exp_date = browser.find_element(By.ID, "exp-date-input")
    time.sleep(1)
    exp_date.send_keys("09")
    exp_date.send_keys("29")
    # finding ccv input and fill it with valid ccv
    exp_date = browser.find_element(By.ID, "ccv-input")
    exp_date.send_keys("918")
    #поставить ассерт, для появления баннера с протухшим паролем
    #clicking submit button
    order_rprt_button = browser.find_element(By.XPATH, "//form[contains(@id,'payment-card-form')]//button[contains(@id,'order_report_now_button')]")
    order_rprt_button.click()
    #successful page is presented
    success_page = browser.find_element(By.CLASS_NAME, "text-center.thanks__title-buttons")


finally:

    browser.quit()
