import pytest
from PageObjects.LoginPage import LoginPage
from Utilities.customLogger import LogGen
from PageObjects.AddCustomer import AddCustomer
from selenium.webdriver.common.by import By
import string
import random

class TestAddCustomer:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):

        self.logger.info("************* test_addCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Add Customer Test **********")
        self.Customer = AddCustomer(self.driver)
        self.Customer.clickOnCustomersMenu()
        self.Customer.clickOnCustomersMenuItem()
        self.Customer.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.Customer.setFirstName("Hadeel")
        self.Customer.setLastName("FIS")
        self.Customer.setEmail(self.email)
        self.Customer.setPassword("test123")
        self.Customer.setGender("Female")
        self.Customer.setCustomerRoles("Guests")
        self.Customer.setManagerOfVendor("Vendor 2")
        self.Customer.setDob("9/02/1980")  # Format: D / MM / YYY
        self.Customer.setCompanyName("FIS")
        self.Customer.setAdminContent("This form just for testing... ")
        self.Customer.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
