from selenium import webdriver
import pytest
import os

@pytest.fixture(autouse=True)
def driver(request):
    if os.environ["BROWSER"] == "chrome":
        driver = webdriver.Chrome()
        request.cls.driver = driver
        yield
        driver.quit()
    elif os.environ["BROWSER"] == "firefox":
        driver = webdriver.Firefox()
        request.cls.driver = driver
        yield
        driver.quit()