import pytest
from selenium import webdriver
import time

# THIS FILE IS BASICALLY USED FOR SETTING UP WEBPAGE , DRIVER AND FIXTURE


@pytest.fixture(scope="function")
def browser_setup():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    time.sleep(2)  # Small delay
    yield driver
    driver.quit()  #  Close browser after test execution