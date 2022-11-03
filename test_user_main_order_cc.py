import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
    # filling in vin input
    vin_input = browser.find_element(By.CSS_SELECTOR, "[name='vin']")
    vin_input.send_keys('1G11C5SL2EF228854')


    # autosearch assert
    def test_autosearch():
        try:
            browser = webdriver.Chrome()
            browser.get(link)
            with pytest.raises(NoSuchElementException):
                browser.find_element(By.XPATH, "//div[contains(@id, 'history-report-page-content')]//div[contains(@class, 'error')]")
                pytest.fail("autosearch is not implemented")
        finally:
            browser.quit()
    # Waiting for payment prepare page to be presented. Needs to implement scroll
    browser.find_element(By.CLASS_NAME, 'what-is-in.cv-paper')
    # scrolling down to payment choise block
    browser.execute_script("window.scrollTo(0, 800)")
    # choosing CC as a payment method
    order_btn = browser.find_element(By.XPATH, "//div/form/button")
    order_btn.click()
    # order page is presented
    order_page = browser.find_element(By.ID, "report-print-button")


finally:

    browser.quit()
