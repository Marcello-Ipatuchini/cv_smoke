import self as self
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "https://dev:cvdev321@staging.clearvin.com/en/user/login/"

def scroll_to_click(driver, element):
    i = 0
    condition = True
    try:
        element.click()
    except (ElementClickInterceptedException, ElementNotInteractableException):
        condition = False

    while not condition and i < 1000:
        i += 1
        height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {height+10})")
        # try:
        try:
            element.click()
            time.sleep(.1)
            condition = True
        except (ElementClickInterceptedException, ElementNotInteractableException):
            condition = False
        # except
    if i > 1000:
        raise TimeoutException

try:
    #opening stag CV in chrome browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
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
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    #scrolling down to payment choise block
    browser.execute_script("window.scrollTo(0, 800)")
    #choosing CC as a payment method
    #credit_card = browser.find_elements(By.CLASS_NAME, "payment-method")[1]
    #credit_card = browser.execute_script("document.querySelectorAll('.payment-method')[1].click()")
    #credit_card = browser.find_element(By.ID, "card")
    #scroll_to_click(browser, credit_card)
    #assert self.is_element_present('credit_card', timeout=30), "payment choise block is not presented"
    #credit_card.click()
    #choosing New card feature from the drop-down
    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_index(1)
    #filling in cc number date and cvv
    #card_number = browser.find_element(By.ID, "card-number")
    #card_number.send_keys('4111111111111111')
    #card_date = browser.find_element(By.ID, "exp-date-input")
    #card_date.send_keys('11/27')
    #cvv = browser.find_element(By.ID, "ccv-input")
    #cvv.send_keys('103')
    #address = browser.find_element(By.ID, "address")
    #address.send_keys('111')
    #zip = browser.find_element(By.ID, "zip")
    #zip.send_keys('111')
    order_btn = browser.find_element(By.XPATH, "// div / form / button")
    order_btn.click()


finally:

    browser.quit()
