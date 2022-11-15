from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def login_btn_click(self):
        login_button = self.browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        login_button.click()
