from webbrowser import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver):
        #self.browser = Chrome()
        #self.url = 'https://dev:cvdev321@staging.clearvin.com/en/user/login/'
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                  message=f"Can't find element by locator {locator}")


    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                  message=f"Can't find elements by locator {locator}")


    def go_to_site(self):
        return self.driver.get(self.url)