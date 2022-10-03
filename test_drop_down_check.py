from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get(link)
    # finding email input and fill it with hardcoded email
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys("79818059334z+2@gmail.com")
    # finding password input and fill it with hardcoded password
    pass_input = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    pass_input.send_keys("09876Qq!")
    # поставить ассерт, для появления баннера с протухшим паролем
    # clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    # go to settings page
    browser.get('https://staging.clearvin.com/en/user/account/settings/')
    # find countries drop-down
    browser.find_element(By.CSS_SELECTOR, '[name="input-country"]')
    # find any country
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("Austria")

finally:

    browser.quit()
