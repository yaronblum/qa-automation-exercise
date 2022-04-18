import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def chrome_web_driver_base(request):
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    chrome_driver.delete_all_cookies()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.close()
