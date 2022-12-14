import pytest
from pages.base_page import BasePage
from pages.main_page import MainPageActions



class TestUserSmokeTests:
    @pytest.fixture(autouse=True)
    def user_login(self, setup):
        self.user_login = MainPageActions(setup)
    def test_click(self):
        self.user_login.login_btn_click()
