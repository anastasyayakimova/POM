from base.base_page import BasePage
import allure
from data.links import Links

class LoginPage(BasePage):

    _PAGE_URL = Links.LOGIN_PAGE
    _LOGIN_FILD_LOCATOR = "//input[@name='username']"
    _PASSWORD_FILD_LOCATOR = "//input[@name='password']"
    _LOGIN_BUTTON_LOCATOR = "//button[text()=' Login ']"

    @allure.step("Input Login")
    def enter_login(self, login):
        login_field = self.driver.find_element(*self._LOGIN_FILD_LOCATOR)
        login_field.send_keys(login)

    @allure.step("Input password")
    def enter_password(self, password):
        password_field = self.driver.find_element(*self._PASSWORD_FILD_LOCATOR)
        password_field.send_keys(password)

    @allure.step("Click button Login")
    def click_login(self):
        button = self.driver.find_element(*self._LOGIN_BUTTON_LOCATOR)
        button.click()

    def login_as(self, login, password):
        self.driver.find_element(*self._LOGIN_FILD_LOCATOR).send_keys(login)
        self.driver.find_element(*self._PASSWORD_FILD_LOCATOR).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON_LOCATOR).click()