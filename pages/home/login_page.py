from selenium.webdriver.common.by import By
from base.actionclass import ActionClass

class LoginPage(ActionClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    #here we are going to add all locators of given Page

    _usernamefield = "//input[@class='_2IX_2- VJZDxU']"
    _password = "//input[@class='_2IX_2- _3mctLh VJZDxU']"
    _submitbtn = "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']"

    def enterusrname(self,usrname):
        self.inputtext(usrname, self._usernamefield, "XPath" )

    def enterpassword(self,password):
        self.inputtext(password, self._password, "XPath")

    def clickonsubmit(self):
        self.Click(self._submitbtn, "Xpath")


    def login(self, Username,Paassword):

        self.enterusrname(Username)
        self.enterpassword(Paassword)
        self.clickonsubmit()