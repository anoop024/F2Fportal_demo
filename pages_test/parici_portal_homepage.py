class parici_portal_homepage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.pariciheader_text_class_name = "cssSmall"
        self.driver.face2face_link_xpath = "//b[contains(text(),'Face2Face')]"

    def face2face_link(self):
        print(self.driver.find_element_by_class_name(self.driver.pariciheader_text_class_name).text)
        self.driver.find_element_by_xpath(self.driver.face2face_link_xpath).click()
