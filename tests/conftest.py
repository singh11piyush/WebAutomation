import pytest
from selenium import webdriver
from base.driverinitiator import Driverinitiator
from pages.home.login_page import LoginPage
@pytest.fixture()
def setUp(request, browser):
    print("Running conftest demo method setup ")
    Driverini = Driverinitiator(browser)
    driver = Driverini.getbrowserinstance()
    lp = LoginPage(driver)
    lp.login()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("Running conftest demo method teardown")
    driver.quit()


@pytest.fixture(scope='class')
def OneTimeSetUp():
    print("Running One Time SetUP")
    yield
    print("Running One Time teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--ostype", help='Type of operating system')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

