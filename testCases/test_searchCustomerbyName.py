import time
import pytest
from PageObjects.AddCustomer import AddCustomer
from PageObjects.LoginPage import LoginPage
from PageObjects.SearchCustomerPage import SearchCustomer
from Utilities.customLogger import LogGen


class Test_SearchCustomerByName:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("************* test_searchCustomerByName **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Customer By Name **********")
        self.Customer = AddCustomer(self.driver)
        self.Customer.clickOnCustomersMenu()
        self.Customer.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by Name **********")
        searchCustomer = SearchCustomer(self.driver)
        searchCustomer.setFirstName("Brenda")
        searchCustomer.clickSearch()
        time.sleep(5)
        status = searchCustomer.searchCustomerByName("Brenda Lindgren")
        self.driver.close()
        assert True == status
        self.logger.info("***************  test_searchCustomerByName Finished  ***********")
