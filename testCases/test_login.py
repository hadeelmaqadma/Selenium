import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperities import ReadConfig


class TestLogin:
    # baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUsername()
    # password = ReadConfig.getPassword()
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********## starting test_homePageTitle ##********")
        self.logger.info("********## Verifying the home page title ##********")  # self.logger.error
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.save_screenshot('.//Screenshots/test_login1.png')  # ==> check the path
        assert act_title in "Your store. Login"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setPassword(self.password)
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
