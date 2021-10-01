import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage

@pytest.mark.usefixtures("OneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.lp = LoginPage(self.driver)

    def test_validlogin(self):
        self.lp.login("9532809913", "Ciomme@123")


