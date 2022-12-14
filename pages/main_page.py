from .base_page import BasePage
from randomizer import randomEmail
from selenium.webdriver.common.by import By

class MainPageLocators:

        MY_ACCOUNT_BTN = By.CSS_SELECTOR, "[aria-label='My Account']"
        LOGIN_BTN = By.CSS_SELECTOR, "[type='submit']"
        EMAIL_INPUT = By.ID, "email-input"
        PASSWORD_INPUT = By.CSS_SELECTOR, "[name='password']"
        VIN_INPUT = By.CSS_SELECTOR, "[name='vin']"
        ORDER_BTN = By.XPATH, "//div/form/button"


class MainPageActions(BasePage):
    def login_btn_click(self):
        login_button = self.find_element(MainPageLocators.LOGIN_BTN)
        login_button.click()
    def email_input_random(self):
        input_email = self.find_element(MainPageLocators.EMAIL_INPUT)
        input_email.send_keys(randomEmail)
    def order_btn_click(self):
        order_button = self.find_element(MainPageLocators.ORDER_BTN)
        order_button.click()
