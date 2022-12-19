from .base_page import BasePage
from randomizer import randomEmail, randomName
from selenium.webdriver.common.by import By


class MainPageLocators:
    MY_ACCOUNT_BTN = By.CSS_SELECTOR, "[aria-label='My Account']"
    LOGIN_BTN = By.CSS_SELECTOR, "[type='submit']"
    EMAIL_INPUT = By.CSS_SELECTOR, '[name="email"]'
    PASSWORD_INPUT = By.CSS_SELECTOR, "[name='password']"
    VIN_INPUT = By.CSS_SELECTOR, "[name='vin']"
    ORDER_BTN = By.XPATH, "//div/form/button"
    REGISTER_BUTTON = By.CSS_SELECTOR, 'a[href="/en/user/register"]'
    FIRST_NAME = By.ID, "firstName"

class MainPageActions(BasePage):
    def login_btn_click(self):
        login_button = self.find_element(MainPageLocators.LOGIN_BTN)
        login_button.click()

    def order_btn_click(self):
        order_button = self.find_element(MainPageLocators.ORDER_BTN)
        order_button.click()

    def email_input_random(self):
        input_email = self.find_element(MainPageLocators.EMAIL_INPUT)
        input_email.send_keys(randomEmail)

    def email_input_hardcoded(self):
        input_email = self.find_element(MainPageLocators.EMAIL_INPUT)
        input_email.send_keys("79818059334z+2@gmail.com")

    def password_input_hardcoded(self):
        password_input = self.find_element(MainPageLocators.PASSWORD_INPUT)
        password_input.send_keys("010101@@@Aa")

    def register_btn_click(self):
        register_btn = self.find_element(MainPageLocators.REGISTER_BUTTON)
        register_btn.click()

    def first_name_random(self):
        input_email = self.find_element(MainPageLocators.FIRST_NAME)
        input_email.send_keys(randomName)