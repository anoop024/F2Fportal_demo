from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import time
class portal_login:
    def __init__(self, driver):
        self.driver = driver
        self.driver.header1_text_xpath = "//b[contains(text(),'Welcome to the')]"
        self.driver.header2_text_xpath = "//b[contains(text(),'Sopra Steria Parici portal')]"
        self.driver.username_text_id = "username"
        self.driver.password_text_id = "password"
        self.driver.submit_button_id = "btnSubmit_6"
        self.driver.forgotpassword_link_xpath = "//a[contains(text(),'Forgot password ?')]"

    def enter_details(self, username, password):
        self.driver.find_element_by_id(self.driver.username_text_id).send_keys(username)
        self.driver.find_element_by_id(self.driver.password_text_id).send_keys(password)

    def submit(self):
        self.driver.find_element_by_id(self.driver.submit_button_id).click()
