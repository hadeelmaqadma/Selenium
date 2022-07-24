from selenium.webdriver.common.by import By
from Locators import LoginLocators
from PageObjects.BasePage import BasePage


class LoginPage(BasePage):
    testbox_username_id = "Email"
    testbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"


    def setUserName(self, username):
        user_name_element = self.driver.find_element(By.ID, self.testbox_username_id)
        user_name_element.clear()
        user_name_element.send_keys(username)

    def setPassword(self, password):
        password_element = self.driver.find_element(By.ID, self.testbox_password_id)
        password_element.clear()
        password_element.send_keys(password)

    def clickLogin(self):
        button = self.driver.find_element(By.XPATH, self.button_login_xpath)
        button.click()

    def clickLogout(self):
        button = self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext)
        button.click()
