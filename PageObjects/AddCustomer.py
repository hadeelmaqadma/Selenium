from selenium.webdriver.support.ui import Select
from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class AddCustomer(BasePage):
    lnkCustomers_menu_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    lnkCustomers_menuitem_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"
    btnAddnew_xpath = "//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    btnAddnew_link = "Add new"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    checkIsTaxExempt_id = "IsTaxExempt"

    lstitemRegistered_xpath = "//span[contains(text(),'Registered')]"   # xpath=//ul[@id='SelectedCustomerRoleIds_taglist']/li

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    checkActive_xpath = "//input[@id='Active']"

    txtAdminContent_xpath = "//textarea[@id='AdminComment']"

    txtcustomerRoles_xpath = "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    btnSave_xpath = "//button[@name='save']"

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.LINK_TEXT, self.btnAddnew_link).click()
        # self.driver.find_element(By.XPATH, self.btnAddnew_xpath)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, name):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(name)

    def setLastName(self, name):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(name)

    def setCustomerRoles(self, role):
        ##############################################
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).clear()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li").click() # //*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        # elif role == 'Registered':
        #     self.listitem = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setGender(self, gender):
        if gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_xpath).click()

    def setCompanyName(self, companyName):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(companyName)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

