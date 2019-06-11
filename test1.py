# Test 1 Use Case 1 - Negative value test
# Author Radovan Mitrovic
# Date 2019-May-25


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from pom import TestFlow


class TestNegative(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.base_url = "https://www.ultimateqa.com/filling-out-forms/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
# Fill in test data
    def test_negative_value(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        addnegative = TestFlow(driver)

        addnegative.testName('Testname')
        addnegative.testMessage('Testmessage')
        addnegative.setCaptcha('-1')
        addnegative.submit()
        print(driver.find_element_by_class_name('et-pb-contact-message').get_attribute("You entered the wrong number in captcha."))
        driver.close()
# Element is missing - throw excpt
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
# Alert is missing - throw excpt
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True
# Close
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class Login():

    def AddNegativeValue(self, user_name):
        print("Enter test_name to Testname field on Form.")
