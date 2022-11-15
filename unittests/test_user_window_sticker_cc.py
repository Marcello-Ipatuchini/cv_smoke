from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

link2 = "https://dev:cvdev321@staging.clearvin.com/en/window-sticker/"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    #finding email input and fill it with hardcoded email
    email_input = browser.find_element(By.ID, "email-input")
    email_input.send_keys("79818059334z+aaa@gmail.com")
    # finding password input and fill it with hardcoded password
    pass_input = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    pass_input.send_keys("XxX111!!!")
    #поставить ассерт, для появления баннера с протухшим паролем
    #clicking submit button
    login_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    login_button.click()
    #transferring to the window sticker page
    browser.get(link2)
    #filling in vin input
    vin_input = browser.find_element(By.CSS_SELECTOR, "[name='vin']")
    vin_input.send_keys('1G11C5SL2EF228854')
    #lookup_ws_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    #lookup_ws_btn.click()
    #поставить ассерт на срабатывание автопоиска
    browser.implicitly_wait(30)
    #Waiting for payment prepare page to be presented. Needs to implement scroll
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    #scrolling down to payment choise block
    #choosing CC as a payment method
    order_btn = browser.find_element(By.XPATH, "//div/form/button")
    browser.execute_script("window.scrollBy(0, 700);")
    order_btn.click()
    #order page is presented
    order_page = browser.find_element(By.CLASS_NAME, "account-content.grid-x")


finally:

    browser.quit()
