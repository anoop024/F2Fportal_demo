from tkinter import *
from tkinter import simpledialog

class LoginToeConnect:

    def __init__(self, driver):
        self.driver = driver
        self.driver.EnterEmail_textfield_id = "i0116"
        self.driver.Submit_button_id = "idSIButton9"
        self.driver.EnterOTP_textfield_id = "idTxtBx_SAOTCC_OTC"
        self.driver.Continue_button_id = "idSubmit_SAOTCC_Continue"

    def Sign_in_using_email(self, EmailID):
        self.driver.find_element_by_id(self.driver.EnterEmail_textfield_id).send_keys(EmailID)
        self.driver.find_element_by_id(self.driver.Submit_button_id).click()

    def Enter_OTP(self):
        def get_otp():
            global otp
            otp = simpledialog.askstring("input number", "Enter OTP")
            root.destroy()

        root = Tk()
        button = Button(root, text="Click to Enter OTP", command=get_otp)
        # print(button)
        button.pack()
        root.geometry("300x300")
        root.mainloop()
        print(otp)
        # OTP = driver(driver, 10).un
        self.driver.find_element_by_id(self.driver.EnterOTP_textfield_id).send_keys(otp)
        self.driver.find_element_by_id(self.driver.Continue_button_id).click()
        self.driver.implicitly_wait(10)

