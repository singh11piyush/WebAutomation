import os

from selenium import webdriver

class Driverinitiator():

    def __init__(self, browser):
        self.browser = browser
        """"#set chrome driver ans ie driver based on env and os
        chromedriver = "path od chrome driver"
        os.environ["webdriver.chrome.driver"]=chromedriver
        self.driver=webdriver.chrome(chromedriver)"""

    def getbrowserinstance(self):
        baseurl = "https://www.flipkart.com/"
        if self.browser == "chrome":
            driver= webdriver.Chrome()
            #set chrome driver to env variable
        elif self.browser=="firefox":
            driver = webdriver.Firefox()
        elif self.browser == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseurl)
        return driver
