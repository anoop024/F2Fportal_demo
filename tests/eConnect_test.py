import pytest
from pages_test.Face2Face_homepage import Face2Face_homepage
from pages_test.My_applicationHome import My_applicationHome
from pages_test.LoginToeConnect import LoginToeConnect
from pages_test.CV_handling import CV_handling
from pages_test.WindowTab_handling import WindowTab_handling
from pages_test.DownloadChecker import DownloadChecking
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TesteConnect():
    def test_eConnect(self):
        driver = self.driver
        Face2face_homepage = Face2Face_homepage(driver)
        My_application = My_applicationHome(driver)
        Sing_in_to_eConnect = LoginToeConnect(driver)
        HandleCV = CV_handling(driver)
        NewWindow = WindowTab_handling(driver)
        Face2face_homepage.myapplication()
        NewWindow.switch_to_current_tab(1)
        My_application.open_econnect(driver)
        NewWindow.switch_to_current_tab(2)
        Sing_in_to_eConnect.Sign_in_using_email(utils.LoginEmailID)
        Sing_in_to_eConnect.Enter_OTP()
        HandleCV.hoverto_SKillSet()
        HandleCV.Navigate_to_UploadCVpage()
        HandleCV.downloadTemplate()
        HandleCV.downloadCV()
        downloadchecking = DownloadChecking(driver)
        downloadchecking.waitUntilDownloadCompleted()




