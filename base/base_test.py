from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.credentials import Credentials

class BaseTest:
    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
