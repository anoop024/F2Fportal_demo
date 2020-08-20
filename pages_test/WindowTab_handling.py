class WindowTab_handling:

    def __init__(self,driver):
        self.driver = driver

    def switch_to_current_tab(self, tabno):
        window_after = self.driver.window_handles[tabno]
        self.driver.switch_to.window(window_after)
        self.driver.implicitly_wait(10)
        # print(self.driver.title)





