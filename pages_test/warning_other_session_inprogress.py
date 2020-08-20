class warning_other_session_inprogress:
    def __init__(self, driver):
        self.driver = driver
        self.driver.header_text_xpath = "//b[contains(text(),'There are already other user sessions in progress:')]"
        self.driver.warning_text_xpath = "//b[contains(text(),'Continue will result in termination of the other s')]"
        self.driver.continue_button_id = "btnContinue"
        self.driver.cancle_button_id = "btnCancel"

    def continue_session(self):
        print(self.driver.find_element_by_xpath(self.driver.header_text_xpath).text)
        # print(self.driver.find_element_by_xpath(self.driver.warning_text_xpath).text)
        self.driver.find_element_by_id(self.driver.continue_button_id).click()
