import time
import allure
import pytest
from base.base_test import BaseTest


@allure.epic("Users")
@allure.feature("Travel accounts")
@allure.story("New accounts")
class TestLoginPage(BaseTest):

    @allure.title("Login in new account. Имеративный подход")
    def test_login_in_account(self):
        self.login_page.open()
        time.sleep(3)
        self.login_page.enter_login(self.credentials.LOGIN)
        self.login_page.enter_password(self.credentials.PASSWORD)
        self.login_page.click_login()
        time.sleep(3)
        self.dashboard_page.click_help_button()
        time.sleep(3)

    @allure.title("Декларативный подход")
    def test_successful_login(self):
        self.login_page.open()
        time.sleep(3)
        self.login_page.login_as("Admin", "admin123")