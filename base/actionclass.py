from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ActionClass():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=5, pollFrequency=0.5):
        element = None
        try:
            #self.driver.implicitly_wait(0)
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            print("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                              ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        self.driver.implicitly_wait(2)
        return element


    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            element = self.waitForElement(locator,locatorType)
            if element is not None:
                print("Element Found")
        except:
            print("Element not found")
        return element

    def Click(self, locator, locatortype="id"):
        element = None
        try:
            element = self.waitForElement(locator, locatortype)
            element.click()
            print(f"User Click on element with locator as {locator} and locatortype as {locatortype}")
        except:
            print_stack()
            print(f"Cannot click on element with locator as {locator} and locatortype as {locatortype}")

    def inputtext(self, text, locator, locatortype="id"):
        element = None
        try:
            element = self.waitForElement(locator, locatortype)
            element.send_keys(text)
            print(f"User entered text {text} on locator {locator} and locatortype as {locatortype}")
        except:
            print_stack()
            print(f"User cannot entered text {text} on locator {locator} and locatortype as {locatortype}")

