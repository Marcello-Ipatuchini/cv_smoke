import pytest
from pages.base_page import BasePage
from pages.main_page import MainPageActions


class TestUserSmokeTests:
    @pytest.fixture(autouse=True)
    def browser_setup(self, setup):
        self.browser_setup = MainPageActions(setup)

    def test_user_login(self):
        self.browser_setup.email_input_hardcoded()
        self.browser_setup.password_input_hardcoded()
        self.browser_setup.login_btn_click()


    def test_user_registration(self):
        self.browser_setup.email_input_random()
        self.browser_setup.login_btn_click()
        self.browser_setup.register_btn_click()
        self.browser_setup.first_name_random()
        self.browser_setup.email_input_random()
