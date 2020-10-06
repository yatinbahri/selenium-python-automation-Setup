from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("----Launching Test On Chrome Browser----")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("----Launching Test On Firefox Browser----")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return browser value to setup method
    return request.config.getoption("--browser")