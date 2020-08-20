from selenium.webdriver.common.action_chains import ActionChains
import time

class Face2Face_homepage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.applauncher_dropdown_xpath = "//img[@class='AppLauncher-img-Menu']"
        self.driver.myapplication_link_css_selector = "body.sopra-colortype-red.ms-backgroundImage:nth-child(2) div.ms-core-overlay:nth-child(26) div.ms-dialogHidden:nth-child(1) div.sopra-contneur div.AppLauncher-dropdown div.AppLauncher-dropdown-content table:nth-child(1) tbody:nth-child(1) tr:nth-child(1) td:nth-child(1) > div.AppLauncher-div-item"



    def myapplication(self):

        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.driver.applauncher_dropdown_xpath)).perform()
        print(self.driver.find_element_by_xpath(self.driver.applauncher_dropdown_xpath).text)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(self.driver.myapplication_link_css_selector)).perform()
        print(self.driver.find_element_by_css_selector(self.driver.myapplication_link_css_selector).text)
        self.driver.find_element_by_css_selector(self.driver.myapplication_link_css_selector).click()
