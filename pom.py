# Page Object Model
# Author Radovan Mitrovic
# Date 2019-May-25

from selenium import webdriver

class TestFlow(object):
# Initate driver
    def __init__(self, driver):
        self.driver = driver
# Prepare Name control
    def testName(self, test_name):
        self.driver.find_element_by_id("et_pb_contact_name_1").clear()
        self.driver.find_element_by_id("et_pb_contact_name_1").send_keys(test_name)
# Prepare Message control
    def testMessage(self, test_message):
        self.driver.find_element_by_id("et_pb_contact_message_1").clear()
        self.driver.find_element_by_id("et_pb_contact_message_1").send_keys(test_message)
# Prepare captcha
    def setCaptcha(self, test_captcha):
        self.driver.find_element_by_id("userName").clear()
        self.driver.find_element_by_id("userName").send_keys(test_captcha)
# Click Submit button
    def submit(self):
        self.driver.find_element_by_class_name("et_contact_submit et_pb_button").click()
# Check is alert displayed
    def testAlert(self):
        alert = self.driver.find_element_by_class_name("et-pb-contact-message")
        if alert.is_displayed():
            print('Alert displayed in order.')
        else:
            print('Error - Alert not displayed!')

# Collect attribute by class name, extract values, slice string, reverse string
# convert to int steps and calculate
    def calval(calvalue):
        d = webdriver.find_element_by_class_name("et_pb_contact_captcha_question", ).getattribute()
        a = str[:d.index("+")]
        a_val = int(a)
        b_inv = d[::-1]
        b = str[:b_inv("+")]
        b_val = int(b)
        c = (a_val+b_val)
        return c
