import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

#pp_sndbx = "https://www.sandbox.paypal.com/signin/"

try:

    browser = webdriver.Chrome()
    # Setting the window size to 1200 * 800
    #browser.set_window_size(800, 800)
    browser.get(link)
    #finding email input and fill it with hardcoded email
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys("79818059334z+2@gmail.com")
    # finding password input and fill it with hardcoded password
    pass_input = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    pass_input.send_keys("09876Qq!")
    #поставить ассерт, для появления баннера с протухшим паролем
    #clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    #filling in vin input
    vin_input = browser.find_element(By.CSS_SELECTOR, "[name='vin']")
    vin_input.send_keys('1G11C5SL2EF228854')
    #поставить ассерт на срабатывание автопоиска
    #Waiting for payment prepare page to be presented. Needs to implement scroll
    browser.implicitly_wait(30)
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    #scrolling down to payment choise block and choosing PayPal as a payment method
    browser.execute_script("window.scrollTo(0, 600);")
    browser.implicitly_wait(30)
    #chhosing paypal as a payment method
    paypal_radio = browser.find_element(By.ID, "paypal")
    paypal_parent_container = paypal_radio.find_element(By.XPATH, './..');
    paypal_parent_container.click()
    #clicking on the order report button
    order_report_pp_btn = browser.find_element(By.CLASS_NAME, 'cv-paypal-button')
    order_report_pp_btn.click()
    #paypal sandbox filling in email input
    pp_email_input = browser.find_element(By.ID, "email")
    pp_email_input.send_keys('fake@test.io')
    next_btn = browser.find_element(By.ID, 'btnNext')
    next_btn.click()
    pp_pswrd_input = browser.find_element(By.ID, "password")
    pp_pswrd_input.send_keys('q1w2e3R$T%')
    next_btn = browser.find_element(By.ID, 'btnLogin')
    next_btn.click()
    #Closing accept cookies modal window
    cookies_modal = browser.find_element(By.ID, 'acceptAllButton')
    cookies_modal.click()
    #scrolling to the payment submit button
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    pp_continue_btn = browser.find_element(By.ID, 'payment-submit-btn')
    time.sleep(4)
    pp_continue_btn.click()
    #User transferring to the report page after successful payment
    order_print_btn = browser.find_element(By.ID, 'report-print-button')

except Exception as e:
    print(e)

finally:
    browser.quit()
