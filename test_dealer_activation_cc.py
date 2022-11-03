import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get(link)
    #finding email input and fill it with hardcoded email
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys("79818059334z+11@gmail.com")
    # finding password input and fill it with hardcoded password
    pass_input = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    pass_input.send_keys("XxX111!!!!")
    #поставить ассерт, для появления баннера с протухшим паролем
    #clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    browser.implicitly_wait(20)
    #clicking on activation button
    activation_btn = browser.find_element(By.ID, "subs_activate_button-2")
    activation_btn.click()
    #Activationg subscription with previouscly added card
    subscription_activation_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    subscription_activation_btn.click()
    #Checking that payment was successful
    browser.find_element(By.XPATH, "//a[contains(@href, '/en/dealer/account/subscription/#cancel-subscription')]")

finally:

    browser.quit()
