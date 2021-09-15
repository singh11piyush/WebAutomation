import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage

class LoginTests(unittest.TestCase):

    def test_validlogin(self):
        baseurl = "https://www.flipkart.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        lp = LoginPage(driver)
        lp.login("9532809913", "Ciomme@123")

        driver.implicitly_wait(5)
        profile = driver.find_element(By.XPATH, "//div[@class='exehdJ' and contains(text(),'piyush')]")

        if profile is not None:
            print(r"\nLogin Successfully")
        else:
            print("Login Failed")
