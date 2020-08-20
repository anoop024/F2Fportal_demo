import pytest
import time
from selenium import webdriver
from utils import utils as utils

@pytest.fixture(scope='class')
def test_setup(request):
    driver = webdriver.Chrome(executable_path=utils.driver_path)
    # driver.maximize_window()
    driver.get(utils.URL)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()
    driver.quit()
    print("testing completed")