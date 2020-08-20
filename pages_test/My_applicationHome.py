class My_applicationHome:

    def __init__(self, driver):
        self.driver = driver
        self.driver.econnect_link_xpath = "body.ms-backgroundImage:nth-child(2) div.ms-core-overlay:nth-child(23) div.ms-mysite-bodyContainer div.ms-mysite-contentBox:nth-child(1) div.sopra-webpart-mesapps div.sopra-roster-theme-container:nth-child(3) ul:nth-child(2) li:nth-child(4) > a:nth-child(1)"

    def open_econnect(self, driver):

        self.driver.find_element_by_css_selector(self.driver.econnect_link_xpath).click()
