
from selenium.webdriver.common.action_chains import ActionChains

class CV_handling:

    def __init__(self, driver):
        self.driver = driver
        self.driver.SkillSet_link_xpath = "//a[contains(text(),'Skill Set & CV')]"
        self.driver.UploadCV_link_xpath = "//a[@id='ecMainNav_LMenu625']"
        self.driver.CVpageHeading_text_xpath = "//span[@id='lblHeading']"
        self.driver.TemplateDownload_link_id = "ContentPlaceHolder1_btnTemplate"
        self.driver.CVdownload_link_xpath = "//a[@id='ContentPlaceHolder1_GvCVDetail11_lnkDownload_0']"

    def hoverto_SKillSet(self):
        self.driver.find_element_by_xpath(self.driver.SkillSet_link_xpath).click()

        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.driver.SkillSet_link_xpath)).perform()

    def Navigate_to_UploadCVpage(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.driver.SkillSet_link_xpath)).perform()
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.driver.UploadCV_link_xpath)).perform()
        self.driver.find_element_by_xpath(self.driver.UploadCV_link_xpath).click()
        print(self.driver.find_element_by_xpath(self.driver.CVpageHeading_text_xpath).text)

    def downloadTemplate(self):
        self.driver.find_element_by_id(self.driver.TemplateDownload_link_id).click()

    def downloadCV(self):
        self.driver.find_element_by_xpath(self.driver.CVdownload_link_xpath).click()




