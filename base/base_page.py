import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from metaclasses.meta_locators import MetaLocator
class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver


    def open(self):
        with allure.step(f"Open page {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)