import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"


try:

    browser = webdriver.Chrome()
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
    vin_input.send_keys('WAUFFAFLXAN056349')
    #поставить ассерт на срабатывание автопоиска
    #Waiting for payment prepare page to be presented. Needs to implement scroll
    browser.implicitly_wait(30)
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    #scrolling down to payment choise block and choosing PayPal as a payment method
    browser.execute_script("window.scrollTo(0, 600);")
    browser.implicitly_wait(30)
    #chhosing paypal as a payment method
    googlepay_radio = browser.find_element(By.ID, "googlepay")
    googlepay_parent_container = googlepay_radio.find_element(By.XPATH, './..');
    googlepay_parent_container.click()
    #clicking on the order report button
    order_report_gp_btn = browser.find_element(By.XPATH, "//button[contains(@data-cv, 'googlepay')]")
    order_report_gp_btn.click()
    #paypal sandbox filling in email input
    browser.implicitly_wait(30)
    gp_email_input = browser.find_element(By.ID, "identifierId")
    gp_email_input.send_keys('fakietopsoul@gmail.com')
    next_btn = browser.find_element(By.XPATH, '//span[contains(text(),"Next")]')
    next_btn.click()
    gp_pswrd_input = browser.find_element(By.XPATH, '//input[contains(@name, "Passwd")]')
    gp_pswrd_input.send_keys('SuBZer0016%$%')
    next_btn = browser.find_element(By.XPATH, '//span[contains(text(), "Next")]')
    next_btn.click()
    #Clicking Continue button to close googlepay modal window
    gp_continue_btn = browser.find_element(By.XPATH, '//div[contains(@role, "button")]')
    gp_continue_btn.click()
    #User transferring to the report page after successful payment
    order_print_btn = browser.find_element(By.ID, 'report-print-button')

except Exception as e:
    print(e)

finally:
    browser.quit()
