import time
class DownloadChecking:

    def __init__(self,driver):
        self.driver=driver


    def waitUntilDownloadCompleted(self, maxtime=600):
        self.driver.execute_script("window.open()")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get('chrome://downloads')
        endTime = time.time() + maxtime
        while True:
            try:
                downloadPercentage = self.driver.execute_script(
                    "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                # check if downloadPercentage is 100 (otherwise the script will keep waiting)
                # print(downloadPercentage)
                if downloadPercentage == 100:
                    print("file is downloading")
                    # exit the method once it's completed
                    return downloadPercentage
            except:
                print("file is not downloaded")
                pass
            # wait for 1 second before checking the percentage next time
            time.sleep(2)
            # exit method if the download not completed with in MaxTime.
            if time.time() > endTime:
                print("file can not be downloaded")
                break